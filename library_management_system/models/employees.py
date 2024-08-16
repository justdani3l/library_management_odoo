from odoo import fields, models, api


class Employees(models.Model):
    _name = 'library.employees'
    _description = 'Library Employees'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    email = fields.Char(string='Email', required=True, tracking=True)
    phone = fields.Char(string='Phone Number', required=True, tracking=True)
    job_title = fields.Char(string='Job Title', required=True, tracking=True)
    hire_date = fields.Date(string='Hire Date', required=True, tracking=True)
    image = fields.Image(string='Image', tracking=True)

