from odoo import models, api, exceptions

class UnloadBookingDocValidation(models.Model):
    ##### Usamos _inherit para acoplarnos al modelo de Roberto sin sobreescribirlo #####
    _inherit = 'pisterra.unload.booking'

    @api.constrains('partner_id')
    def _check_mandatory_docs(self):
        for booking in self:
            pending_docs = self.env['pisterra.doc.obligatorio'].search([
                ('partner_id', '=', booking.partner_id.id),
                ('state', '!=', 'approved')
            ])
            
            if pending_docs:
                raise exceptions.ValidationError(
                    "No puedes realizar una reserva hasta que todos tus documentos obligatorios "
                    "estén subidos y aprobados por la administración."
                )