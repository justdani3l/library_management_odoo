from odoo import fields, models, api


class Configuration(models.Model):
    _name = 'library.configuration'
    _description = 'Library Configuration'
    _rec_name = 'config_name'

    config_name = fields.Char(string='Configuration Name', required=True)
    config_value = fields.Char(string='Configuration Value')

