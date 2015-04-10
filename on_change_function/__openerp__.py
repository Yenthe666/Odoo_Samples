# -*- coding: utf-8 -*-
{
    'name': "on_change_function",

    'summary': """
        Automatically calculates total price from two other fields.""",

    'description': """
        This module will calculate the sale price by automatically calculating
	the total of two other fields (CostPrice and ShippingCosts).
	You can see this in action under Sales > Products when you create a new product or edit one.
    """,

    'author': "Yenthe Van Ginneken",
    'website': "http://www.odoo.yenthevg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
