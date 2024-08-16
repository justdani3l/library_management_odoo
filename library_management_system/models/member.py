from odoo import fields, models, api


class Members(models.Model):
    _name = 'library.member'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Library Member'

    name = fields.Char(String='Name', required=True, tracking=True)
    invoice_ids = fields.One2many('library.invoice', 'member_id', string='Invoice', tracking=True)
    email = fields.Char(string='Email', required=True, tracking=True)
    address = fields.Char(string='Address', required=True, tracking=True)
    phone = fields.Char(string='Phone', required=True, tracking=True)
    city = fields.Char(string='City', required=True, tracking=True)
    gender = fields.Selection(string='Gender', selection=[('Male', 'Male'), ('Female', 'Female')], tracking=True)
    image = fields.Image(string='Image', tracking=True)
    membership_date = fields.Date(string='Membership Date', required=True, tracking=True)
    invoice_count = fields.Integer(string='Invoice Count', compute='_compute_invoice_count')

    @api.depends('invoice_ids')
    def _compute_invoice_count(self):
        for member in self:
            member.invoice_count = len(member.invoice_ids)



