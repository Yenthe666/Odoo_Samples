# -*- coding: utf-8 -*-

from openerp import models, fields, api

class on_change_function(models.Model):
    #Inhertis the model product.template
    _inherit = 'product.template'
    #Creates two new fields (CostPrice and ShippingCost) in the model product.template
    CostPrice = fields.Float('Buy price')
    ShippingCost = fields.Float('Shipping Cost')
    FieldAfterGroup = fields.Char(string='Field After Group')
    FieldNewPage = fields.Char(string='Field New Page')

    #This method will be called when either the field CostPrice or the field ShippingCost changes.
    def on_change_price(self,cr,user,ids,CostPrice,ShippingCost,context=None):
	#Calculate the total
	total = CostPrice + ShippingCost
        res = {
            'value': {
		#This sets the total price on the field standard_price.
                'standard_price': total
	      }
	}
	#Return the values to update it in the view.
	return res
