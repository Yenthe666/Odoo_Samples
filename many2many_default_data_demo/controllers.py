# -*- coding: utf-8 -*-
from openerp import http

# class Many2manyDefaultDataDemo(http.Controller):
#     @http.route('/many2many_default_data_demo/many2many_default_data_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/many2many_default_data_demo/many2many_default_data_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('many2many_default_data_demo.listing', {
#             'root': '/many2many_default_data_demo/many2many_default_data_demo',
#             'objects': http.request.env['many2many_default_data_demo.many2many_default_data_demo'].search([]),
#         })

#     @http.route('/many2many_default_data_demo/many2many_default_data_demo/objects/<model("many2many_default_data_demo.many2many_default_data_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('many2many_default_data_demo.object', {
#             'object': obj
#         })