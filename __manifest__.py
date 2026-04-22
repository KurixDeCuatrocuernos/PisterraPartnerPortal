{
    'name': 'Portal Productor - Catuven',
    'version': '1.0',
    'author': 'Daniel',
    'depends': ['base', 'contacts', 'mail', 'portal', 'website'],
    'data': [
        #'security/ir.model.access.csv',
        #'security/security.xml',
        #'views/menus.xml',
        #'views/portal_templates.xml',
        #'views/unload_booking_views.xml',
        'views/res_partner_views.xml',
        'data/mail_template_data.xml',
        'views/registro_web_template.xml'
    ],
    'installable': True,
    'application': True,
}