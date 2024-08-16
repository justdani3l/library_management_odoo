from odoo import fields, models, api


class Authors(models.Model):
    _name = 'library.authors'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Library Authors'

    name = fields.Char(string='Name', required=True, tracking=True)
    biography = fields.Text(string='Biography', required=True, tracking=True)
    nationality = fields.Char(string='Nationality', required=True, tracking=True)
    image = fields.Binary(string='Image', tracking=True)
    book_ids = fields.One2many('library.books', 'author_id', string='Books', tracking=True)

