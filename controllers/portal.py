from odoo import http
from odoo.http import request

class PisterraPortalDocs(http.Controller):

    @http.route(['/mis-documentos'], type='http', auth="user", website=True)
    def mis_documentos(self, **kw):
        partner = request.env.user.partner_id
        
        documentos = request.env['pisterra.doc.obligatorio'].search([
            ('partner_id', '=', partner.id)
        ])
        
        return request.render('pisterra_partner_portal.doc_portal_list_template', {
            'documentos': documentos
        })
    @http.route(['/mis-documentos/<int:doc_id>'], type='http', auth="user", website=True)
    def gestionar_documento(self, doc_id, **kw):
        partner = request.env.user.partner_id
        documento = request.env['pisterra.doc.obligatorio'].search([
            ('id', '=', doc_id),
            ('partner_id', '=', partner.id)
        ], limit=1)

        if not documento:
            return request.redirect('/mis-documentos')

        return request.render('pisterra_partner_portal.doc_portal_detail_template', {
            'documento': documento
        })

    @http.route(['/mis-documentos/procesar'], type='http', auth="user", methods=['POST'], website=True)
    def procesar_documento(self, **post):
        doc_id = int(post.get('doc_id'))
        partner = request.env.user.partner_id
        
        documento = request.env['pisterra.doc.obligatorio'].search([
            ('id', '=', doc_id),
            ('partner_id', '=', partner.id)
        ], limit=1)

        if documento:
            if documento.doc_type == 'upload' and post.get('upload_file'):
                import base64
                file_content = post.get('upload_file').read()
                documento.write({
                    'doc_file': base64.b64encode(file_content),
                    'doc_filename': post.get('upload_file').filename,
                    'state': 'submitted' # Cambiamos el estado para que el admin lo revise
                })
            elif documento.doc_type == 'accept' and post.get('accept_terms') == 'on':
                documento.write({
                    'is_accepted': True,
                    'state': 'submitted'
                })

        return request.redirect('/mis-documentos')