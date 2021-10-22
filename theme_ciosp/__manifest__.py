{
    'name': 'CIOSP theme',
    'description': 'A description for your theme.',
    'version': '14.0.1.0.0',
    'author': "Lymtech",
    'website': "http://www.lymtech.com.br",
    'category': 'Theme/Creative',

    'depends': ['base', 'website', 'website_form', 'event', 'website_event'],
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        # 'views/layout.xml',
        # 'views/pages.xml'
        'views/index.xml',
        'views/snippets/s_banner.xml',
        'views/snippets/s_carousel.xml',
        'views/snippets/s_nav.xml'
    ],
}