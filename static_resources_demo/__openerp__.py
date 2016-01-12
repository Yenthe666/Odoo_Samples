# -*- coding: utf-8 -*-
{
    'name': "static_resources_demo",

    'summary': """
        Demo showing you how to add JS, CSS and images to an Odoo module!""",

    'description': """
         Demo showing you how to add JS, CSS and images to an Odoo module!
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
        'views/resources.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
