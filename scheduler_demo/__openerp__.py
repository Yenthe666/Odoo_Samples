# -*- coding: utf-8 -*-
{
    'name': "scheduler_demo",

    'summary': """
        This demo will show you how to create a new scheduler that automatically runs
	and will update all records in the current model.""",

    'description': """
        This demo will show you how to create a new scheduler that automatically runs
	and will update all records in the current model. Every time the scheduler is run it will 	  update all records on this model and will update the 'Number of updates' as demo.
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
	'data/default_data.xml',
	'data/scheduler_data.xml',
	'views/scheduler_view.xml'
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
