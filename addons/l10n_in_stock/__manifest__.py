# -*- coding: utf-8 -*-


{
    'name': 'Indian - Stock Report(GST)',
    'icon': '/l10n_in/static/description/icon.png',
    'version': '1.0',
    'description': """GST Stock Report""",
    'category': 'Accounting/Localizations',
    'depends': [
        'l10n_in',
        'stock',
    ],
    'data': [
        'views/report_stockpicking_operations.xml',
    ],
    'demo': [
        'data/product_demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'LGPL-3',
}
