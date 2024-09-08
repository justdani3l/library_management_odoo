from odoo import models, fields


class PharmacyStockMovement(models.Model):
    _name = 'pharmacy.stock.movement'
    _description = 'Pharmacy Stock Movement'

    medicine_id = fields.Many2one('pharmacy.medicine', string='Medicine', required=True)
    quantity = fields.Integer(string='Quantity', required=True)
    movement_type = fields.Selection([('in', 'In'), ('out', 'Out')], string='Movement Type', required=True)
    date = fields.Datetime(string='Date', default=fields.Datetime.now)
