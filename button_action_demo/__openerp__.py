# -*- coding: utf-8 -*-
{
    'name': "button_action_demo",

    'summary': """
        This demo shows you how to create buttons in a form view and how to trigger actions from them.""",

    'description': """
        This demo shows you how to create buttons in a form view and how to trigger actions from them.
    """,

    'author': "Yenthe Van Ginneken",
    'website': "http://www.odoo.yenthevg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/button_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
}
