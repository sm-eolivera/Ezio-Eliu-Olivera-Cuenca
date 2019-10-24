# -*- coding: utf-8 -*-
{
    'name':        "Library Management",

    'summary':
                   """
                   Library management
                   """,

    'description': """
        Manage a Library: customers, books, etc.... 
    """,

    'author':      "Odoo",
    'website':     "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category':    'Library',
    'version':     '0.3',

    # any module necessary for this one to work correctly
    'depends':     ['base','mail'],

    # always loaded
    'data':[
        "security/user_groups.xml",
        "security/ir.model.access.csv",        
        "views/book_views.xml",
        "views/partner_views.xml",
        "views/rental_views.xml",
        "views/dashboard_views.xml",
        "views/price_views.xml",
        "views/menu_views.xml",
        "wizard/select_views_books.xml",
        "report/report.xml",
        "data/library_data.xml",
        "data/cron.xml",
        "data/mail.xml",
         ],
    # only loaded in demonstration mode
    'demo':        [],
    'license': 'AGPL-3',
}
