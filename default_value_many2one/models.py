# -*- coding: utf-8 -*-

from openerp import models, fields, api

class default_value_many2one(models.Model):
    def _set_default_currency(self, cr, uid, context=None):
	#I've chosen to simply hardcode a currency. You could also get the currency that is set on the company
	#by getting the data from the account.config.settings model.
        res = self.pool.get('res.company').search(cr, uid, [('currency_id','=','EUR')], context=context)
        return res and res[0] or False

    #Lets inherit an already existing model.
    _inherit= "product.template"
    #Create a new many2one field
    purchaseCurrency = fields.Many2one('res.currency', string="Currency bought in")

    #Default values that need to be set
    defaults = {
	'purchaseCurrency':_set_default_currency,
    }
