"""
Este modelo recogerá los datos necesarios de cada modelo de Odoo y los MODELARÁ en cada caso para poder trabajar con ellos.
    Es la INFRAESTRUCTURA de los datos

Ejemplo: 
    class PartnerPortalMixin(models.AbstractModel):
    _name = 'partner.portal.mixin'

    portal_token = fields.Char()

    def _get_portal_url(self):
        return f"/my/record/{self.id}?access_token={self.portal_token}"
"""

from odoo import models, fields


