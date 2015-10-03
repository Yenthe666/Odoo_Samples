# -*- coding: utf-8 -*-
from openerp import http

# class InheritReportDemo(http.Controller):
#     @http.route('/inherit_report_demo/inherit_report_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inherit_report_demo/inherit_report_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inherit_report_demo.listing', {
#             'root': '/inherit_report_demo/inherit_report_demo',
#             'objects': http.request.env['inherit_report_demo.inherit_report_demo'].search([]),
#         })

#     @http.route('/inherit_report_demo/inherit_report_demo/objects/<model("inherit_report_demo.inherit_report_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inherit_report_demo.object', {
#             'object': obj
#         })