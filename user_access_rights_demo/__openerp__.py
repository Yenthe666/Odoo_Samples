# -*- coding: utf-8 -*-
{
    'name': "user_access_rights_demo",

    'summary': """
        This demo module shows you how to create user access rights for a module (under Settings > Users)""",

    'description': """
        This demo module shows you how to create user access rights for a module (under Settings > Users)
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
        'security/user_groups.xml',
	'security/ir.model.access.csv',
	'views/user_access_views.xml'
    ],
}
