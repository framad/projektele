# -*- coding: utf-8 -*-
{
    'name': "ProjekTele",

    'summary': """
        Module Projek Tele""",

    'description': """
        Manajemen Projek Tele
    """,

    'author': "Febry",
    'website': "framad.github.io/framadhan",

    'category': 'Uncategorized',
    'version': '0.1',

		# Depencicy
    'depends': ['base','sale'],

		# Include ALL XML Code in Here be mindful of order
    'data': [
        'security/ir.model.access.csv',
        'views/menuitems.views.xml',
        'views/sale_order_views.xml'
        # 'views/rekapsol.views.xml'
    ],

    'installable': True,
    'application': True,
    'auto_install': False

}