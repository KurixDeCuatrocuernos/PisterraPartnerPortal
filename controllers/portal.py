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

class Portal(http.Controller):
    @http.route('/my/bookings', auth='user')
    def my_bookings(self):
        bookings = request.env['pisterra.unload.booking'].search([])
        return request.render('pisterra_partner_portal.portal_bookings_template', {
            'bookings': bookings
        })
