from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'
    expiration_date = fields.Date(string="Fecha de expiracion del lote")

    @api.constrains('expiration_date')
    def _check_future_date(self):
        for record in self:
            if record.future_date and record.future_date <= date.today():
                raise ValidationError("La fecha debe ser posterior a hoy.")

    #pos_note = fields.Char(string="Nota para el POS")

