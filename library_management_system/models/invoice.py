from odoo import fields, models, api


class Invoice(models.Model):
    _name = 'library.invoice'
    _description = 'Library Invoice'

    invoice_id = fields.Integer(required=True)
    member_id = fields.Integer(required=True)
    issue_id = fields.Integer
    invoice_date = fields.Date(string='Invoice Date', required=True)
    total_amount = fields.Text(string='Total Amount', required=True)
    payment_status = fields.Selection[('Paid', 'Paid'), ('Progress', 'Progress'), ('Unpaid', 'Unpaid')]

