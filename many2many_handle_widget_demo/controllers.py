# -*- coding: utf-8 -*-
from openerp import http

# class Many2manyHandleWidgetDemo(http.Controller):
#     @http.route('/many2many_handle_widget_demo/many2many_handle_widget_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/many2many_handle_widget_demo/many2many_handle_widget_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('many2many_handle_widget_demo.listing', {
#             'root': '/many2many_handle_widget_demo/many2many_handle_widget_demo',
#             'objects': http.request.env['many2many_handle_widget_demo.many2many_handle_widget_demo'].search([]),
#         })

#     @http.route('/many2many_handle_widget_demo/many2many_handle_widget_demo/objects/<model("many2many_handle_widget_demo.many2many_handle_widget_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('many2many_handle_widget_demo.object', {
#             'object': obj
#         })