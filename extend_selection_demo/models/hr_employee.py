# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    gender = fields.Selection(selection_add=[('transgender', 'Transgender')])