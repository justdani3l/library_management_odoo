from odoo import fields, models, api


class IssueBooks(models.Model):
    _name = 'library.issue'
    _description = 'Issue Books'

    issue_id = fields.Integer()
    book_id = fields.Integer()
    member_id = fields.Integer()
    issue_date = fields.Date(string='Issue Date', required=True)
    due_date = fields.Date(string='Due Date', required=True)
    return_date = fields.Date(string='Return Date', required=True)
    fine_amount = fields.Text(string='Fine Amount', required=True)
    employee_id = fields.Integer()

