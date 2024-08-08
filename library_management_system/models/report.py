from odoo import fields, models, api


class Report(models.Model):
    _name = 'library.report'
    _description = 'Library Report'

    report_id = fields.Integer()
    employee_id = fields.Integer()
    report_date = fields.Date(string='Report Date', required=True)
    description = fields.Text(string='Description', required=True)
