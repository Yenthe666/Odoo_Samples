# -*- coding: utf-8 -*-
{
    'name': "website_snippet_demo",

    'summary': """
        Demo module that shows how to create new building blocks""",

    'description': """
        Demo module that shows how to create new building blocks
    """,

    'author': "Yenthe Van Ginneken",
    'website': "http://www.odoo.yenthevg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/snippets.xml',
    ]
}