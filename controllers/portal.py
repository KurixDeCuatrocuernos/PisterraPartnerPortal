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
    
    # Ruta para ver los envíos
    @http.route('/pisterra/bookings', auth='user')
    def my_bookings(self):
        bookings = request.env['pisterra.unload.booking'].search([])
        return request.render('pisterra_partner_portal.portal_bookings_template', {
            'bookings': bookings
        })
    
    # Ruta para ver las facturas
    @http.route(['/pisterra/invoices', '/pisterra/invoices/'], auth='user', website=True)
    def mis_facturas(self):
        # Recogemos las facturas del usuario que sean enviadas y no estén canceladas
        facturas = request.env['account.move'].search([
            ('partner_id', '=', request.env.user.partner_id.id),
            ('move_type', '=', 'out_invoice'),
            ('state', '=', 'posted')
        ])
        return request.render('pisterra_partner_portal.factura_simple_template', {
            'facturas': facturas,
        })
        # Devolvemos las facturas a facturas_template.xml
   
    # Ruta para ver una factura en detalle   
    @http.route('/pisterra/invoices/<int:invoice_id>', auth='user', website=True)
    def factura_en_detalle(self, invoice_id):
        factura = request.env['account.move'].sudo().browse(invoice_id)
        return request.render('pisterra_partner_portal.factura_detallada_template', {
            'f': factura
        })
