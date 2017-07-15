# -*- coding: utf-8 -*-
{
    'name': "create_webpage_demo",

    'summary': """
        This demo shows you how to create controllers and webpages in Odoo.""",

    'description': """
        This demo will show you how make a controller that links to a webpage and how to create a new
	webpage from the XML code. You can view the page under http://yourOdooUrl.com/example
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
        'views/example_webpage.xml',
    ],
}
