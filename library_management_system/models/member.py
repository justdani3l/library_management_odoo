from odoo import fields, models, api


class Members(models.Model):
    _name = 'library.member'
    _description = 'Library Member'

    name = fields.Char(String='Name', required=True)
    invoice_ids = fields.One2many('library.invoice', 'member_id', string='Invoice')
    email = fields.Char(string='Email', required=True)
    address = fields.Char(string='Address', required=True)
    phone = fields.Char(string='Phone', required=True)
    city = fields.Char(string='City', required=True)
    gender = fields.Selection(string='Gender', selection=[('Male', 'Male'), ('Female', 'Female')])
    image = fields.Image(string='Image')
    membership_date = fields.Date(string='Membership Date', required=True)

