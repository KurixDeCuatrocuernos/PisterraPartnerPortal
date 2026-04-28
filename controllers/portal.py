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
    @http.route(['/pisterra', '/pisterra/' '/pisterra/dashboard', '/pisterra/dashboard/'], type="http", auth='public', website=True)
    def dashboard(self):
        dashboard = request.env['pisterra.dash.model'].sudo().search([]) # Recogemos los datos del modelo
        return request.render('pisterra_partner_portal.dash_main_template', {
            'breadcrumb_pages': [], 
            'page_active': 'Inicio', # Añadimos la referencia para el breadcrumb
            'dash': dashboard
        }) # Devolvemos el modelo a dash_template.xml
    
# Ruta para ir a la página que muestra las facturas
    @http.route(['/pisterra/invoices', '/pisterra/invoices/'], auth='user', website=True)
    def mis_facturas(self):
         # Usamos el modelo para obtener las facturas
        factura_model = request.env['pisterra.factura.model']
        data = factura_model.get_facturas_usuario()
        
        return request.render('pisterra_partner_portal.factura_simple_template', {
            'breadcrumb_pages': [
                {'name': 'Mis Facturas', 'url': '/pisterra/invoices'}
            ],
            'page_active': 'Mis Facturas',
            'facturas': data['facturas'],
            'is_admin': data['is_admin'],
            'admin_label': data['admin_label']
        })# Devolvemos las facturas a facturas_template.xml
   
# Ruta para ir a la página que muestra una factura en detalle   
    @http.route('/pisterra/invoices/<int:invoice_id>', auth='user', website=True)
    def factura_en_detalle(self, invoice_id):
        try:
            factura = request.env['pisterra.factura.model'].get_factura_detalle(invoice_id)
            if not factura:
                return request.redirect('/pisterra/invoices')
            
            return request.render('pisterra_partner_portal.factura_detallada_template', {
                'breadcrumb_pages': [
                    {'name': 'Mis Facturas', 'url': '/pisterra/invoices'},
                    {'name': factura.name, 'url': f'/pisterra/invoices/{invoice_id}'}
                ],
                'page_active': factura.name,
                'f': factura
            })
        except Exception:
            return request.redirect('/pisterra/invoices') # Devolvemos la factura a factura_detallada_template.xml

# Ruta para descargar una factura en pdf inmodificable
    @http.route(['/pisterra/invoices/download/<int:invoice_id>'], auth='user', website=True)
    def descargar_factura_pdf(self, invoice_id):
        try:
            data = request.env['pisterra.factura.model'].descargar_factura_pdf(invoice_id)
            if not data:
                return request.redirect('/pisterra/invoices')
            
            return request.make_response(
                data['pdf'],
                headers=[
                    ('Content-Type', 'application/pdf'),
                    ('Content-Disposition', f'inline; filename="{data["nombre"]}"')
                ]
            )
        except Exception:
            return request.redirect('/pisterra/invoices')
