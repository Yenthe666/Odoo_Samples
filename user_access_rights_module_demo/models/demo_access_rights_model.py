# -*- coding: utf-8 -*-
from openerp import models, fields, api

class demo_access_rights(models.Model):
    _name = 'demo.access.rights'
    _rec_name = 'name'
    name = fields.Char('Name',required=True)
