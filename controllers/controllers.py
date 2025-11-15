# -*- coding: utf-8 -*-
# from odoo import http


# class Date-expiration-product(http.Controller):
#     @http.route('/date-expiration-product/date-expiration-product', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/date-expiration-product/date-expiration-product/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('date-expiration-product.listing', {
#             'root': '/date-expiration-product/date-expiration-product',
#             'objects': http.request.env['date-expiration-product.date-expiration-product'].search([]),
#         })

#     @http.route('/date-expiration-product/date-expiration-product/objects/<model("date-expiration-product.date-expiration-product"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('date-expiration-product.object', {
#             'object': obj
#         })

