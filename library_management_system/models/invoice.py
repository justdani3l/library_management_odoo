from datetime import timedelta

from odoo import fields, models, api


class Invoice(models.Model):
    _name = 'library.invoice'
    _description = 'Library Invoice'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'member_id'

    member_id = fields.Many2one(comodel_name='library.member', string='Member', required=True, tracking=True)
    book_id = fields.Many2one(comodel_name='library.books', string='Book Name', required=True, tracking=True)
    issue_date = fields.Date(string='Issue Date', default=fields.Date.context_today, tracking=True)
    return_date = fields.Date(string='Return Date', required=False, compute="_compute_return_date",
                              inverse="_inverse_return_date", tracking=True)
    duration = fields.Integer(string='Duration', default=1, tracking=True)
    employee_id = fields.Many2one(comodel_name='library.employees', string='Handled by Employee', tracking=True)
    payment_status = fields.Selection([('Paid', 'Paid'), ('Progress', 'Progress'), ('Unpaid', 'Unpaid')],
                                      string='Payment Status', default='Unpaid', tracking=True)

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
