from odoo import fields, models, api


class Categories(models.Model):
    _name = 'library.categories'
    _description = 'Library Categories'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description', required=True)

