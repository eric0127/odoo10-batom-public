# -*- coding: utf-8 -*-
{
    'name': "batom_settings",

    'summary': "Batom customized settings modules",

    'description': """
        Long description of module's purpose
    """,

    'author': "Batom Co., Ltd.",
    'website': "http://www.greattaiwangear.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}