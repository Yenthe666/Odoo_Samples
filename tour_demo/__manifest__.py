# -*- coding: utf-8 -*-
{
    'name': "Tour demo",

    'summary': """
        An example module showing you how to create a tour in Odoo""",

    'description': """
        An example module showing you how to create a tour in Odoo
    """,

    'author': "Yenthe Van Ginneken",
    'website': "http://www.odoo.yenthevg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/assets.xml',
    ]
}