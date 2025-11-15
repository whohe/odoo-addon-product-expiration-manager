# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class date-expiration-product(models.Model):
#     _name = 'date-expiration-product.date-expiration-product'
#     _description = 'date-expiration-product.date-expiration-product'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

