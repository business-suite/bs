# -*- coding: utf-8 -*-

{
    'name': 'K.S.A. - Point of Sale',
    'author': 'Odoo S.A',
    'category': 'Accounting/Localizations/Point of Sale',
    'description': """
K.S.A. POS Localization
=======================================================
    """,
    'license': 'LGPL-3',
    'depends': ['l10n_gcc_pos', 'l10n_sa_invoice'],
    'data': [
    ],
    'assets': {
        'web.assets_qweb': [
            'l10n_sa_pos/static/src/xml/OrderReceipt.xml',
        ],
        'point_of_sale.assets': [
            'web/static/lib/zxing-library/zxing-library.js',
            'l10n_sa_pos/static/src/js/models.js',
        ]
    },
    'auto_install': True,
}
