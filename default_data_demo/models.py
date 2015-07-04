# -*- coding: utf-8 -*-

from openerp import models, fields, api

class default_data_demo(models.Model):
    _name = 'demo.default.data'
    _description = 'Demo default data'
    name = fields.Char('Name', required=True)
    description = fields.Html('Description')
