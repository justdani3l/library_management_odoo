from odoo import fields, models, api


class Books(models.Model):
    _name = 'library.books'
    _description = 'Library Books'

    book_title = fields.Char(string='Book Title', required=True)
    isbn = fields.Char(string='ISBN', required=True)
    publisher_name = fields.Char(string='Publisher Name', required=True)
    production_year = fields.Text(string='Production Year', required=True)
    pages = fields.Integer(string='Pages', required=True)
    availability = fields.Boolean(string='Availability ', default=True)
    language = fields.Char(string='Language', required=True)
    rating = fields.Text(string='Rating', required=True)
    book_price = fields.Text(string='Book Price', required=True)
    image = fields.Image(string='Image')
    author_id = fields.Many2one(comodel_name='library.authors', string='Author', required=True)
    categories = fields.Many2one(comodel_name='library.categories', string='Categories', required=True)

