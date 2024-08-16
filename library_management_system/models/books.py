from odoo import fields, models, api


class Books(models.Model):
    _name = 'library.books'
    _description = 'Library Books'
    _rec_name = 'book'

    book = fields.Char(string='Book Title', required=True)
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
    categories_id = fields.Many2one(comodel_name='library.categories', string='Categories', required=True)
    nr_copies = fields.Integer(string='Number of Copies')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')
    ], string='Priority')
