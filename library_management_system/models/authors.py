from odoo import fields, models, api


class Authors(models.Model):
    _name = 'library.authors'
    _description = 'Library Authors'

    name = fields.Char(string='Name', required=True)
    biography = fields.Text(string='Biography', required=True)
    nationality = fields.Char(string='Nationality', required=True)
    image = fields.Binary(string='Image')

