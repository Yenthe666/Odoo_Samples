# -*- coding: utf-8 -*-
{
    'name': "send_mail_template_demo",

    'summary': """
        Demo module to show how you can send e-mail templates to people by clicking on a button""",

    'description': """
        Demo module to show how you can send e-mail templates to people by clicking on a button
    """,

    'author': "Yenthe Van Ginneken",
    'website': "http://www.odoo.yenthevg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts','mail', 'mail_template_demo'],

    # always loaded
    'data': [
        'views/contact_view.xml',
    ],
}