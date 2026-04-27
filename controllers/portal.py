from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class PisterraPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'delivery_count' in counters:
            partner = request.env.user.partner_id
            #dominio de seguridad 
            delivery_count = request.env['stock.picking'].sudo().search_count([
                ('partner_id', '=', partner.id),
                ('picking_type_id.code', '=', 'incoming') # Solo recepciones
            ])
            values['delivery_count'] = delivery_count
        return values

    # 2. La ruta principal del listado
    @http.route(['/mis-entregas'], type='http', auth="user", website=True)
    def portal_mis_entregas(self, **kw):
        partner = request.env.user.partner_id
        
        #Si se quita esto, filtras datos de todos los clientes.
        domain = [
            ('partner_id', '=', partner.id),
            ('picking_type_id.code', '=', 'incoming')
        ]
        
        pickings = request.env['stock.picking'].sudo().search(domain)
        
        # Preparamos los valores para enviarlos al Frontend (QWeb)
        values = {
            'pickings': pickings,
            'page_name': 'entregas',
        }
        
        return request.render("pisterra_partner_portal.entrega_list_template", values)
    # 3. La ruta de detalle de una entrega específica
    @http.route(['/mis-entregas/<int:picking_id>'], type='http', auth="user", website=True)
    def portal_entrega_detalle(self, picking_id, **kw):
        partner = request.env.user.partner_id
        
        # Buscamos el albarán solicitado usando sudo() para saltar las reglas de empleado
        picking = request.env['stock.picking'].sudo().browse(picking_id)
        
        # FILTRO DE SEGURIDAD
        # Si el albarán no existe, o si el dueño del albarán NO es el usuario actual, lo expulsamos.
        if not picking.exists() or picking.partner_id.id != partner.id:
            return request.redirect('/mis-entregas')
            
        values = {
            'picking': picking,
            'page_name': 'entrega_detalle',
        }
        
        return request.render("pisterra_partner_portal.entrega_detail_template", values)