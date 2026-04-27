{
    'name': 'Pisterra Partner Portal',
    'version': '0.1',
    'summary': 'Portal de Facturas para Clientes y Productores',
    # Módulos necesarios para funcionar
    'depends': ['base', 'web', 'portal', 'sale', 'stock', 'account'],
    'data': [ 
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/dash_navbar.xml',
        'views/dash_main_template.xml',
        'views/factura_simple_template.xml',
        'views/factura_detallada_template.xml',
    ],
    'installable': True,
    'application': True,
}