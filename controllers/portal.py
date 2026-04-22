"""
Este es el módulo de orquestación que consume los modelos de /models para que funcione como un módulo de Odoo 
    (y unifica su comportamiento)

Ejemplo:
    class Portal(http.Controller):

    @http.route('/my/invoices', type='http', auth='user')
    def portal_invoices(self):
        invoices = request.env['account.move'].search([
            ('partner_id', '=', request.env.user.partner_id.id)
        ])
        return request.render('mi_template', {
            'invoices': invoices
        })
"""
from odoo import http
from odoo.http import request

# Enrutamiento al módulo principal 
class Portal(http.Controller):
    
# Ruta para ir a la página de inicio
    @http.route(['/', '/pisterra/dashboard', '/pisterra/dashboard/'], type="http", auth='public', website=True)
    def dashboard(self):
        dashboard = request.env['pisterra.dash.model'].sudo().search([]) # Recogemos los datos del modelo
        return request.render('pisterra_partner_portal.dash_main_template', {
            'breadcrumb_pages': [], 
            'page_active': 'Inicio', # Añadimos la referencia para el breadcrumb
            'dash': dashboard
        }) # Devolvemos el modelo a dash_template.xml
    
# Ruta para ir a la página para ver los envíos
    @http.route(['/pisterra/bookings', '/pisterra/bookings/'], auth='user', website=True)
    def my_bookings(self):
        bookings = request.env['pisterra.unload.booking'].search([])
        return request.render('pisterra_partner_portal.booking_template', {
            'breadcrumb_pages': [
                {'name': 'Mis Envíos', 'url': '/pisterra/bookings'}
            ],
            'page_active': 'Mis Envíos', # Añadimos la referencia para el breadcrumb
            'bookings': bookings,
        })
    
# Ruta para ir a la página que muestra las facturas
    @http.route(['/pisterra/invoices', '/pisterra/invoices/'], auth='user', website=True)
    def mis_facturas(self):
        is_admin = request.env.user.has_group('base.group_system') # Verificamos si el usuario es admin
        is_manager = request.env.user.has_group('sales_team.group_sale_manager')
        has_privileged = is_admin or is_manager

        if has_privileged:
            # Recogemos todas las facturas si tiene privilegios
            facturas = request.env['account.move'].search([
                ('move_type', '=', 'out_invoice'),
                ('state', '=', 'posted')
            ])
            
        else: 
            # Recogemos las facturas del usuario que sean enviadas y no estén canceladas
            facturas = request.env['account.move'].sudo().search([
                ('partner_id', '=', request.env.user.partner_id.id),
                ('move_type', '=', 'out_invoice'),
                ('state', '=', 'posted')
            ])
            
        # Mostramos cada role
        if is_admin:
            admin_label = 'Administrador'
        elif is_manager:
            admin_label = 'Manager'
        else: 
            admin_label = 'Usuario'
        
        return request.render('pisterra_partner_portal.factura_simple_template', {
            'breadcrumb_pages': [
                {'name': 'Mis Facturas', 'url': '/pisterra/invoices'}
            ],
            'page_active': 'Mis Facturas', # Añadimos la referencia para el breadcrumb
            'facturas': facturas,
            'is_admin': has_privileged,
            'admin_label': admin_label
        }) # Devolvemos las facturas a facturas_template.xml
   
# Ruta para ir a la página que muestra una factura en detalle   
    @http.route('/pisterra/invoices/<int:invoice_id>', auth='user', website=True)
    def factura_en_detalle(self, invoice_id):
        factura = request.env['account.move'].sudo().browse(invoice_id) # Recogemos la factura por su id
        return request.render('pisterra_partner_portal.factura_detallada_template', {
            'breadcrumb_pages': [
                {'name': 'Mis Facturas', 'url': '/pisterra/invoices'},
                {'name': factura.name, 'url': f'/pisterra/invoices/{invoice_id}'}
            ],
            'page_active': factura.name, # Añadimos la referencia para el breadcrumb
            'f': factura
        }) # Devolvemos la factura a factura_detallada_template.xml

# Ruta para descargar una factura en pdf inmodificable
    @http.route(['/pisterra/invoices/download/<int:invoice_id>'], auth='user', website=True)
    def descargar_factura_pdf(self, invoice_id):
        factura = request.env['account.move'].sudo().browse(invoice_id)
        
        # Revisamos que exista la factura
        if not factura:
            return request.redirect('/pisterra/invoices')
        
        # Verificamos privilegios
        is_admin = request.env.user.has_group('base.group_system')
        is_manager = request.env.user.has_group('sales_team.group_sale_manager')
        has_privileged = is_admin or is_manager
        # Redirigimos si no tiene privilegios
        if not has_privileged and factura.partner_id.id != request.env.user.partner_id.id:
            return request.redirect('/pisterra/invoices')
        
        # Usamos el método estándar de Odoo para generar el pdf inmodificable
        pdf = request.env['ir.actions.report'].sudo()._render_qweb_pdf('account.account_invoices', factura.ids)[0]

        return request.make_response(
            pdf,
            headers=[
                ('Content-Type', 'application/pdf'),
                ('Content-Disposition', f'inline; filename="Factura_{factura.name}.pdf"') # cambiar inline por attachment  hará que se descargue directamente
            ]
        )
