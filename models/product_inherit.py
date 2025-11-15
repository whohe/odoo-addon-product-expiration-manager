from odoo import models, fields

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    pos_note = fields.Char(string="Nota para el POS")

