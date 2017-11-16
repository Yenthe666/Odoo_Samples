# -*- coding: utf-8 -*-
from odoo import http

class Example(http.Controller):
    @http.route('/example', type='http', auth='public', website=True)
    def render_example_page(self):
        return http.request.render('create_webpage_demo.example_page', {})

    @http.route('/example/detail', type='http', auth='public', website=True)
    def navigate_to_detail_page(self):
        # This will get all company details (in case of multicompany this are multiple records)
        companies = http.request.env['res.company'].sudo().search([])
        return http.request.render('create_webpage_demo.detail_page', {
          # pass company details to the webpage in a variable
          'companies': companies})
