# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class PisterraRegistro(http.Controller):

    # 1. Ruta para mostrar la página web
    @http.route('/registro', type='http', auth="public", website=True)
    def pagina_registro(self, **kwargs):
        # Odoo buscará la plantilla HTML
        return request.render('pisterra_partner_portal.formulario_registro_template')

    # 2. Ruta para procesar el botón de "Enviar" del formulario
    @http.route('/registro/enviar', type='http', auth="public", website=True, csrf=False)
    def procesar_registro(self, **post):
        # Si llegan datos del formulario web...
        if post:
            # Creamos el contacto. 
            # Usamos sudo() porque un usuario público de internet no tiene permisos de administrador
            request.env['res.partner'].sudo().create({
                'name': post.get('nombre'),
                'email': post.get('correo'),
                # El archivo res_partner.py ya le pondrá 'pendiente' por defecto
            })
            
            # Llamamos a la plantilla de "registro completado"
            return request.render('pisterra_partner_portal.registro_completado_template')