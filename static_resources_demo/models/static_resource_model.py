# -*- coding: utf-8 -*-

from openerp import models, fields, api

class static_resource_model(models.Model):
    _name = 'static.resource.demo'
    _description = 'Demo adding resources'
    name = fields.Char('Name', required=True)
