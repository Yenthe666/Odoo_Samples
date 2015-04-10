# -*- coding: utf-8 -*-
from openerp import http

# class OnChangeFunction(http.Controller):
#     @http.route('/on_change_function/on_change_function/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/on_change_function/on_change_function/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('on_change_function.listing', {
#             'root': '/on_change_function/on_change_function',
#             'objects': http.request.env['on_change_function.on_change_function'].search([]),
#         })

#     @http.route('/on_change_function/on_change_function/objects/<model("on_change_function.on_change_function"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('on_change_function.object', {
#             'object': obj
#         })