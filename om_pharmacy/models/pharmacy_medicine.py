from odoo import models, fields


class PharmacyMedicine(models.Model):
    _name = 'pharmacy.medicine'
    _description = 'Pharmacy Medicine'

    name = fields.Char(string='Medicine Name', required=True)
    code = fields.Char(string='Medicine Code', required=True)
    category_id = fields.Many2one('pharmacy.medicine.category', string='Category')
    manufacturer = fields.Char(string='Manufacturer')
    expiry_date = fields.Date(string='Expiry Date')
    stock_quantity = fields.Integer(string='Stock Quantity', default=0)
    price = fields.Float(string='Price')
    prescription_required = fields.Boolean(string='Prescription Required', default=False)
