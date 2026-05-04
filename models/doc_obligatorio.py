from odoo import models, fields, api

class DocObligatorio(models.Model):
    _name = 'pisterra.doc.obligatorio'
    _description = 'Documento Obligatorio del Productor'

    name = fields.Char(string='Nombre del Documento', required=True, help="Ej: DNI, Certificado Ecológico, Contrato...")
    
    partner_id = fields.Many2one('res.partner', string='Productor', required=True, ondelete='cascade')
    
    doc_type = fields.Selection([
        ('upload', 'Subir archivo'),
        ('accept', 'Aceptar términos')
    ], string='Tipo de requerimiento', required=True, default='upload')
    
    state = fields.Selection([
        ('pending', 'Pendiente'),
        ('submitted', 'En revisión (Subido)'),
        ('approved', 'Aprobado'),
        ('rejected', 'Rechazado')
    ], string='Estado', default='pending', tracking=True)

    doc_file = fields.Binary(string='Archivo adjunto', attachment=True)
    doc_filename = fields.Char(string='Nombre del archivo')

    is_accepted = fields.Boolean(string='Aceptado por el productor', default=False)

    admin_notes = fields.Text(string='Notas del Administrador')