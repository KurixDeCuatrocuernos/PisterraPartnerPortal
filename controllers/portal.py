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
    @http.route(['/', '/pisterra/dashboard', '/pisterra/dashboard/'], type="http", auth='user', website=True)
    def dashboard(self):
        dashboard = request.env['pisterra.dash.model'].search([]) # Recogemos los datos del modelo
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
        # Recogemos las facturas del usuario que sean enviadas y no estén canceladas
        facturas = request.env['account.move'].search([
            ('partner_id', '=', request.env.user.partner_id.id),
            ('move_type', '=', 'out_invoice'),
            ('state', '=', 'posted')
        ])
        return request.render('pisterra_partner_portal.factura_simple_template', {
            'breadcrumb_pages': [
                {'name': 'Mis Facturas', 'url': '/pisterra/invoices'}
            ],
            'page_active': 'Mis Facturas', # Añadimos la referencia para el breadcrumb
            'facturas': facturas,
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
