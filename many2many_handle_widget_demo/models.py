# -*- coding: utf-8 -*-

from openerp import models, fields, api

class many2many_default_data_demo(models.Model):
    _name = 'sale.order.handle'
    _description = 'Model for many2many (handle)'
    _order = 'sequence'
    name = fields.Char('Naam')
    sequence = fields.Integer('sequence', help="Sequence for the handle.",default=10)

class print_order_sample(models.Model):
    def _get_default_print_order_ids(self):
        return self.pool.get('sale.order.handle').search(self.env.cr, self.env.uid, [])

    _inherit = 'sale.order'
    print_handle_ids = fields.Many2many('sale.order.handle','sale_handle','order_id','order_handle_id','Many2many order',help='This could be used to create a print order for your report, for example.This is a drag an drop (handle) widget.',default=_get_default_print_order_ids)

