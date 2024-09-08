from odoo import models, fields, api


class PharmacyPrescription(models.Model):
    _name = 'pharmacy.prescription'
    _description = 'Pharmacy Prescription'

    prescription_code = fields.Char(string='Prescription Code', required=True)
    medicine_id = fields.Many2one('pharmacy.medicine', string='Medicine', required=True)
    date_prescribed = fields.Date(string='Date Prescribed', default=fields.Date.today())
    quantity = fields.Integer(string='Quantity')
    price = fields.Float(string='Price')
