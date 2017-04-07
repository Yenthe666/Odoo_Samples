# -*- coding: utf-8 -*-

from odoo import models, fields, api

class res_partner(models.Model):
    _inherit = 'res.partner'
    passed_override_write_function = fields.Boolean(string='Has passed our super method')

    @api.model
    def create(self, values):
        # Override the original create function for the res.partner model
        record = super(res_partner, self).create(values)

        # Change the values of a variable in this super function
        record['passed_override_write_function'] = True
        print 'Passed this function. passed_override_write_function value: ' + str(record['passed_override_write_function'])

        # Return the record so that the changes are applied and everything is stored.
	return record

