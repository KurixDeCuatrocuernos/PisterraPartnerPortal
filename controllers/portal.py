from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class PisterraPortal(CustomerPortal):

    @http.route(['/mis-entregas'], type='http', auth="user", website=True)
    def portal_mis_entregas(self, **kw):
        partner = request.env.user.partner_id
        
        # Filtro innegociable de seguridad
        domain = [
            ('partner_id', '=', partner.id),
            ('picking_type_id.code', '=', 'incoming')
        ]
        
        pickings = request.env['stock.picking'].sudo().search(domain)
        
        values = {
            'pickings': pickings,
            'page_name': 'entregas',
        }
        return request.render("pisterra_partner_portal.entrega_list_template", values)

    @http.route(['/mis-entregas/<int:picking_id>'], type='http', auth="user", website=True)
    def portal_entrega_detalle(self, picking_id, **kw):
        partner = request.env.user.partner_id
        picking = request.env['stock.picking'].sudo().browse(picking_id)
        
        # Validación de seguridad contra intrusiones (IDOR)
        if not picking.exists() or picking.partner_id.id != partner.id:
            return request.redirect('/mis-entregas')
            
        values = {
            'picking': picking,
            'page_name': 'entrega_detalle',
        }
        return request.render("pisterra_partner_portal.entrega_detail_template", values)