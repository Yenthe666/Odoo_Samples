# -*- coding: utf-8 -*-
from openerp import http

# class DefaultDataDemo(http.Controller):
#     @http.route('/default_data_demo/default_data_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/default_data_demo/default_data_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('default_data_demo.listing', {
#             'root': '/default_data_demo/default_data_demo',
#             'objects': http.request.env['default_data_demo.default_data_demo'].search([]),
#         })

#     @http.route('/default_data_demo/default_data_demo/objects/<model("default_data_demo.default_data_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('default_data_demo.object', {
#             'object': obj
#         })