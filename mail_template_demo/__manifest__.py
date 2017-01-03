# -*- coding: utf-8 -*-
{
    'name': "mail_template_demo",

    'summary': """
        A demo module that shows you how to create your own e-mail templates""",

    'description': """
        A demo module that shows you how to create your own e-mail templates
    """,

    'author': "Yenthe Van Ginneken",
    'website': "http://www.odoo.yenthevg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail','contacts'],

    # always loaded
    'data': [
        'views/mail_template.xml',
    ],
}
