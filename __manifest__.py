# -*- coding: utf-8 -*-
{
    'name': "Projektai",

    'summary': """Projektų valdymo programa""",

    'description': """
        Projektų valdymo programa leidžia:
            - sukurti projektus
            - priskirti projektams darbus
            - priskirti klientams projektus
            - išrašyti sąskaitas
    """,

    'author': "Donatas Noreika",
    'website': "http://programosverslui.lt/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],
    # 'depends': ['base', 'res.partner', 'hr.employee'],

    # always loaded
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        # 'templates.xml',
        'views/projektas_view.xml',
        'views/darbas_view.xml',
        'views/saskaita_view.xml',
        'mail_templates.xml',
        'reports/projektas_report.xml',
        'views/partner_inherited.xml',
        # 'views/session_board.xml',
        # 'reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}