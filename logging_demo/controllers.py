# -*- coding: utf-8 -*-
from openerp import http

# class LoggingDemo(http.Controller):
#     @http.route('/logging_demo/logging_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/logging_demo/logging_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('logging_demo.listing', {
#             'root': '/logging_demo/logging_demo',
#             'objects': http.request.env['logging_demo.logging_demo'].search([]),
#         })

#     @http.route('/logging_demo/logging_demo/objects/<model("logging_demo.logging_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('logging_demo.object', {
#             'object': obj
#         })