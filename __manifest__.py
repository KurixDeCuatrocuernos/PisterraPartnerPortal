{
    'name': 'Pisterra Partner Portal',
    'version': '0.1',
    'summary': 'Portal de bookings y clientes',
    # Módulos necesarios para funcionar
    'depends': ['base', 'web', 'portal', 'sale', 'stock', 'account'],
    'data': [ 
            'security/ir.model.access.csv',
            'views/unload_booking_views.xml',
            'views/menus.xml',
            'views/portal_templates.xml',
        ],
        'installable': True,
        'application': True,
}