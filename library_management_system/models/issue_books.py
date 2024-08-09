from odoo import fields, models, api


class IssueBooks(models.Model):
    _name = 'library.issue'
    _description = 'Issue Books'

    book_id = fields.Many2one(comodel_name='library.books', string='Book Name', required=True)
    member_id = fields.Many2one(comodel_name='library.member', string='Responsible Member', required=True)
    issue_date = fields.Date(string='Issue Date', default=fields.Date.context_today)
    due_date = fields.Date(string='Due Date', required=True)
    return_date = fields.Date(string='Return Date')
    fine_amount = fields.Text(string='Fine Amount', required=True)
    employee_id = fields.Many2one(comodel_name='library.employees', string='Handled by Employee')
