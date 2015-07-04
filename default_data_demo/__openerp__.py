# -*- coding: utf-8 -*-
{
    'name': "default_data_demo",

    'summary': """
        A demo that shows how default data is created in code and how it is inserted in the Odoo db.""",

    'description': """
        A demo that shows how default data is created in code and how it is inserted in the Odoo db.
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
	'templates.xml',
	'data/defaultdata.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
