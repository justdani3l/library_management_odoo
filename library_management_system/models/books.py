from odoo import fields, models, api


class Books(models.Model):
    _name = 'library.books'
    _description = 'Library Books'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'book'

    book = fields.Char(string='Book Title', required=True, tracking=True)
    isbn = fields.Char(string='ISBN', required=True, tracking=True)
    publisher_name = fields.Char(string='Publisher Name', required=True, tracking=True)
    production_year = fields.Text(string='Production Year', required=True, tracking=True)
    pages = fields.Integer(string='Pages', required=True, tracking=True)
    availability = fields.Boolean(string='Availability ', default=True, tracking=True)
    language = fields.Char(string='Language', required=True, tracking=True)
    rating = fields.Text(string='Rating', required=True, tracking=True)
    book_price = fields.Text(string='Book Price', required=True, tracking=True)
    image = fields.Image(string='Image', tracking=True)
    author_id = fields.Many2one(comodel_name='library.authors', string='Author', required=True, tracking=True)
    categories_id = fields.Many2one(comodel_name='library.categories', string='Categories', required=True, tracking=True)
    nr_copies = fields.Integer(string='Number of Copies', tracking=True)
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')
    ], string='Priority')
