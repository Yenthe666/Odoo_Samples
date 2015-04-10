# -*- coding: utf-8 -*-
from openerp import http

# class DefaultValueMany2one(http.Controller):
#     @http.route('/default_value_many2one/default_value_many2one/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/default_value_many2one/default_value_many2one/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('default_value_many2one.listing', {
#             'root': '/default_value_many2one/default_value_many2one',
#             'objects': http.request.env['default_value_many2one.default_value_many2one'].search([]),
#         })

#     @http.route('/default_value_many2one/default_value_many2one/objects/<model("default_value_many2one.default_value_many2one"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('default_value_many2one.object', {
#             'object': obj
#         })