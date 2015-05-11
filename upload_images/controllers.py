# -*- coding: utf-8 -*-
from openerp import http

# class UploadImages(http.Controller):
#     @http.route('/upload_images/upload_images/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upload_images/upload_images/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('upload_images.listing', {
#             'root': '/upload_images/upload_images',
#             'objects': http.request.env['upload_images.upload_images'].search([]),
#         })

#     @http.route('/upload_images/upload_images/objects/<model("upload_images.upload_images"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upload_images.object', {
#             'object': obj
#         })