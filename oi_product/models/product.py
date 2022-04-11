from odoo import api, fields, models
from odoo.exceptions import UserError


class Product(models.Model):
    _inherit = 'product.template'

    manufacture_name = fields.Char("Manufacturer Name")
    manufacture_part = fields.Char("Manufacturer Part / SKU Number")
    manufacture_catalog = fields.Char("Manufacturers Catalog Description")
    drawing_number = fields.Char("Our Internal Drawing Number")
    internal_desc = fields.Char("Our Internal Description")