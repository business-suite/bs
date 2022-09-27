# -*- coding: utf-8 -*-


{
    'name': 'Discuss',
    'category': 'Productivity',
    'summary': 'Discuss',
    'description': "Discuss",
    'depends': ['base', 'mail'],
    'data': [
        'views/contact_views.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
    'data': [
        'views/discuss_views.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'mail_discuss/static/src/components/*/*.js',
            'mail_discuss/static/src/components/*/*.scss',
            'mail_discuss/static/src/widgets/*/*.js',
            'mail_discuss/static/src/widgets/*/*.scss',
            'mail_discuss/static/src/js/**/*.js',
        ],
        'web.assets_qweb': [
            'mail_discuss/static/src/xml/*.xml',
            'mail_discuss/static/src/components/*/*.xml',
            'mail_discuss/static/src/widgets/*/*.xml',
        ],
    }
}
