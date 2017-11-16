# -*- coding: utf-8 -*-
{
    'name': "override_method_demo",

    'summary': """
        This demo shows you how to override existing Python functions in Odoo.""",

    'description': """
        This demo shows you how to override existing Python functions in Odoo. In this example we 
        will override the create function of the res.partner (contact) model and set a boolean
        to true in the proces.
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
}
