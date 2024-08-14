from odoo import fields, models, api


class Invoice(models.Model):
    _name = 'library.invoice'
    _description = 'Library Invoice'

    member_id = fields.Many2one(comodel_name='library.member', string='Member', required=True)
    book_id = fields.Many2one(comodel_name='library.books', string='Book Name', required=True)
    issue_date = fields.Date(string='Issue Date', default=fields.Date.context_today)
    return_date = fields.Date(string='Return Date', required=True)
    employee_id = fields.Many2one(comodel_name='library.employees', string='Handled by Employee')
    payment_status = fields.Selection([('Paid', 'Paid'), ('Progress', 'Progress'), ('Unpaid', 'Unpaid')],
                                      string='Payment Status', default='Unpaid')
