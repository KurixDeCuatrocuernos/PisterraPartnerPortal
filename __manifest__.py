{
    'name': 'Pisterra Partner Portal',
    'version': '1.0',
    'category': 'Website/Portal',
    'summary': 'Portal Cliente / Productor para Pisterra',
    'description': """
        Módulo para la gestión del portal de productores:
        - Reserva de turnos (Roberto)
        - Entregas y Documentos Obligatorios (Jaime)
        - Facturas y Dashboard (Alejandro)
        - Registro y Autenticación (Daniel)
        - Historial de Entregas (Jean)
    """,
    'author': 'DAM Equipo 1 - Catuven Innovación',
    'depends': ['portal', 'contacts', 'account', 'mail', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/doc_views.xml',              # jaime
        'views/unload_booking_views.xml',
        'views/menus.xml',
        'views/portal_templates.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}