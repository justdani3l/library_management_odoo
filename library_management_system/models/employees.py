from odoo import fields, models, api


class Employees(models.Model):
    _name = 'library.employees'
    _description = 'Library Employees'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone Number', required=True)
    job_title = fields.Char(string='Job Title', required=True)
    hire_date = fields.Date(string='Hire Date', required=True)

