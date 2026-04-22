# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    registro_estado = fields.Selection([
        ('pendiente', 'Pendiente de Validación'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado')
    ], string='Estado de Registro', default='pendiente')

    def write(self, vals):
        # 1. Dejamos que Odoo guarde los datos en la base de datos normalmente
        res = super(ResPartner, self).write(vals)
        
        # 2. Comprobamos si en este guardado se ha cambiado el estado a 'aprobado'
        if 'registro_estado' in vals and vals['registro_estado'] == 'aprobado':
            for record in self:
                # 3. Buscamos nuestra plantilla de correo
                template = self.env.ref('pisterra_partner_portal.email_template_agricultor_aprobado', raise_if_not_found=False)
                
                # 4. Si la encuentra y el contacto tiene correo, se manda el correo
                if template and record.email:
                    template.send_mail(record.id, force_send=True)
                    
        return res