# -*- coding: utf-8 -*-

from openerp import models, fields, api

class many2many_default_data_demo(models.Model):
    _name = 'sale.order.printorder'
    _description = 'Model for many2many'
    name = fields.Char('Name')

class print_order_sample(models.Model):
    def _get_default_print_order_ids(self):
        return self.pool.get('sale.order.printorder').search(self.env.cr, self.env.uid, [])

    _inherit = 'sale.order'
    print_order_ids = fields.Many2many('sale.order.printorder','sale_order_print','print_id','order_print_id','Print order',help='This could be used to create a print order for your report, for example.',default=_get_default_print_order_ids)

