from odoo import fields, models, api


class Report(models.Model):
    _name = 'library.report'
    _description = 'Library Report'

    employee_id = fields.Many2one(comodel_name='library.employees', string='Employee', required=True)
    report_date = fields.Date(string='Report Date', default=fields.Date.context_today)
    description = fields.Text(string='Description', required=True)
