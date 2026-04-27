{
    'name': 'Pisterra Partner Portal',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Portal de cliente y productor - Entregas y Reservas',
    'description': """
        Módulo base para el portal de Catuven/Pisterra.
        Incluye la gestión de entregas en modo lectura.
    """,
    # Dependencias críticas para que tu código funcione
    'depends': ['base', 'portal', 'stock', 'account', 'mail', 'contacts'],
    
    # Archivos que Odoo debe cargar (el orden importa)
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/portal_templates.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': False,
}