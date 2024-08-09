from odoo import fields, models, api


class Invoice(models.Model):
    _name = 'library.invoice'
    _description = 'Library Invoice'

    member_id = fields.Many2one(comodel_name='library.member', string='Member', required=True)
    issue_id = fields.Many2one(comodel_name='library.issue', string='Issued Book')
    invoice_date = fields.Date(string='Invoice Date', default=fields.Date.context_today)
    return_date = fields.Date(string='Return Date', required=True)
    total_amount = fields.Text(string='Total Amount', required=True)
    payment_status = fields.Selection([('Paid', 'Paid'), ('Progress', 'Progress'), ('Unpaid', 'Unpaid')],
                                      string='Payment Status', default='Unpaid')
