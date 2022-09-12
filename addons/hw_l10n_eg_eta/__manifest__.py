# -*- coding: utf-8 -*-


{
    'name': 'Egypt ETA Hardware Driver',
    'category': 'Accounting/Accounting',
    'website': 'https://www.odoo.com',
    'summary': 'Egypt ETA Hardware Driver',
    'description': """
Egypt ETA Hardware Driver
=======================

This module allows Odoo to digitally sign invoices using an USB key approved by the egyptian government

Special thanks to Plementus <info@plementus.com> for their help in developing this module.

Requirements per system
-----------------------

Windows:
    - eps2003csp11.dll
    
Linux/macOS:
    - OpenSC

""",
    'external_dependencies': {
        'python': ['PyKCS11'],
    },
    'installable': False,
    'license': 'LGPL-3',
}
