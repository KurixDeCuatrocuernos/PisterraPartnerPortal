{
    'name': 'Pisterra Partner Portal',
    'version': '0.1',
    'summary': 'Portal de bookings y clientes',
'depends': ['base', 'web', 'portal', 'website', 'crm'],
'data': [ 
        'security/ir.model.access.csv',
        'views/unload_booking_views.xml',
        'views/menus.xml',
        'views/portal_templates.xml',
    ],
    'installable': True,
    'application': True,
}