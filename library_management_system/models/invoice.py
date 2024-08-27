from datetime import timedelta
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Invoice(models.Model):
    _name = 'library.invoice'
    _description = 'Library Invoice'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'member_id'
    _order = 'id desc'

    member_id = fields.Many2one(comodel_name='library.member', string='Member', required=True, tracking=True)
    book_id = fields.Many2one(comodel_name='library.books', string='Book Name', required=True, tracking=True)
    issue_date = fields.Date(string='Issue Date', default=fields.Date.context_today, tracking=True)
    return_date = fields.Date(string='Return Date', required=False, compute="_compute_return_date",
                              inverse="_inverse_return_date", tracking=True)
    duration = fields.Integer(string='Duration', default=1, tracking=True)
    employee_id = fields.Many2one(comodel_name='library.employees', string='Handled by Employee', tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('running', 'Running'), ('delayed', 'Delayed'), ('ended', 'Ended')],
                             string='Status', default='draft', tracking=True)
    ref = fields.Char(string='Reference', tracking=True)
    progress = fields.Integer(string='Progress', compute="_compute_progress")

    @api.constrains('issue_date')
    def _check_issue_date(self):
        for rec in self:
            if rec.issue_date and rec.issue_date > fields.Date.today():
                raise ValidationError("The entered date of issue date isn't acceptable")

    @api.model
    def create(self, vals):
        # Automatically generates a unique reference for new invoices
        vals['ref'] = self.env['ir.sequence'].next_by_code('library.invoice')
        invoice = super(Invoice, self).create(vals)
        invoice._update_book_copies(-1)  # Decrease book copies when creating an invoice
        return invoice

    def unlink(self):
        if self.state != 'draft':
            raise ValidationError('You can delete Invoice only in draft status!!')
        self._update_book_copies(1)  # Restore book copies if invoice is deleted
        return super(Invoice, self).unlink()

    def write(self, vals):
        old_book_id = self.book_id.id
        result = super(Invoice, self).write(vals)
        if 'book_id' in vals:
            # Restore the old book's copies
            self.env['library.books'].browse(old_book_id)._update_nr_copies(1)
            # Decrease the new book's copies
            self._update_book_copies(-1)
        return result

    @api.depends('issue_date', 'duration')
    def _compute_return_date(self):
        for rec in self:
            if rec.issue_date and rec.duration:
                duration = timedelta(days=rec.duration - 1)
                rec.return_date = fields.Date.to_string(fields.Date.from_string(rec.issue_date) + duration)
            else:
                rec.return_date = False

    def _inverse_return_date(self):
        for rec in self:
            if rec.issue_date and rec.return_date:
                rec.duration = (fields.Date.from_string(rec.return_date) - fields.Date.from_string(
                    rec.issue_date)).days + 1
            else:
                rec.duration = 1

    @api.onchange('issue_date', 'duration')
    def _onchange_issue_date_or_duration(self):
        if self.issue_date and self.duration:
            duration = timedelta(days=self.duration - 1)
            self.return_date = fields.Date.to_string(fields.Date.from_string(self.issue_date) + duration)
        else:
            self.return_date = False

    def action_running(self):
        for rec in self:
            rec.state = 'running'

    def action_delayed(self):
        for rec in self:
            if rec.return_date and fields.Date.today() < rec.return_date:
                raise ValidationError("You cannot delay the book because the return date has not passed yet!")
            rec.state = 'delayed'

    def action_ended(self):
        for rec in self:
            rec.state = 'ended'
            rec.member_id._compute_invoice_count()

    def _return_book(self):
        """Handles the return of the borrowed book."""
        self.ensure_one()
        book = self.book_id
        if book:
            book.nr_copies += 1
            book.availability = book.nr_copies > 0

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def _update_book_copies(self, quantity):
        """Update the number of copies available for the book."""
        if self.book_id:
            self.book_id.sudo()._update_nr_copies(quantity)

    @api.depends("state")
    def _compute_progress(self):
        for rec in self:
            if rec.state == 'draft':
                progress = 25
            elif rec.state == 'running':
                progress = 50
            elif rec.state == 'ended':
                progress = 100
            else:
                progress = 0
            rec.progress = progress
