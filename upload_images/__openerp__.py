# -*- coding: utf-8 -*-
{
    'name': "upload_images",

    'summary': """
        Demo for uploading images & automatically resizing them.""",

    'description': """
        This module will create a new menu item 'Images' under the sale module.
	It will give you the ability to upload images and resize them automatically in multiple formats.
    """,

    'author': "Yenthe Van Ginneken",
    'website': "http://www.odoo.yenthevg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
	'upload_images_report.xml',
	'views/report_images.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
