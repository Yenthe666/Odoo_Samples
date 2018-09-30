# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DefaultDataDemo(models.Model):
    _name = 'demo.default.data'
    _description = 'Demo default data'

    # Field definitions
    name = fields.Char('Name', required=True)
    description = fields.Html('Description')
