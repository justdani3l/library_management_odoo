from odoo import fields, models, api


class Configuration(models.Model):
    _name = 'library.configuration'
    _description = 'Library Configuration'

    config_id = fields.Integer()
    config_name = fields.Char()
    config_value = fields.Char()

