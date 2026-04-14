"""
Este modelo recogerá los datos de negocio como una clase 
    y los almacenará en la BASE DE DATOS

Ejemplo:
    class UnloadBooking(models.Model):
        _name = 'pisterra.unload.booking'
        _inherit = ['partner.portal.mixin']

        partner_id = fields.Many2one('res.partner')

"""
from odoo import models, fields # Importamos modelos y campos


class UnloadBooking(models.Model):
    _name = 'pisterra.unload.booking' # Id del modelo
    _description = 'Unload Booking' # Descripción del modelo
    partner_id = fields.Many2one('res.partner') # Id del Cliente/Productor
    date = fields.Date() # Fecha del pedido/envío
    slot = fields.Char() # Puesto del Cliente/Productor
    estimated_kg = fields.Float() # Peso estimado del pedido/envío
    status = fields.Selection([ # Estado del pedido/envío
        ('draft', 'Draft'), # Borrador
        ('confirmed', 'Confirmed'), # Confirmado
        ('done', 'Done'), # Hecho/Completado
    ], default = 'draft') # Por defecto se usa borrador


