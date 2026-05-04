from odoo import models, fields, api

class DocObligatorio(models.Model):
    # Nombre técnico en la base de datos de Odoo
    _name = 'pisterra.doc.obligatorio'
    _description = 'Documento Obligatorio del Productor'

    # Campos de la base de datos
    name = fields.Char(string='Nombre del Documento', required=True, help="Ej: DNI, Certificado Ecológico, Contrato...")
    
    # Relación con el agricultor (res.partner)
    partner_id = fields.Many2one('res.partner', string='Productor', required=True, ondelete='cascade')
    
    # Según tus instrucciones: "documentos que tiene que aceptar o subir"
    doc_type = fields.Selection([
        ('upload', 'Subir archivo'),
        ('accept', 'Aceptar términos')
    ], string='Tipo de requerimiento', required=True, default='upload')
    
    # Estados para que el administrador los revise
    state = fields.Selection([
        ('pending', 'Pendiente'),
        ('submitted', 'En revisión (Subido)'),
        ('approved', 'Aprobado'),
        ('rejected', 'Rechazado')
    ], string='Estado', default='pending', tracking=True)

    # Campos si el tipo es 'upload' (Subir archivo)
    doc_file = fields.Binary(string='Archivo adjunto', attachment=True)
    doc_filename = fields.Char(string='Nombre del archivo')

    # Campo si el tipo es 'accept' (Aceptar términos)
    is_accepted = fields.Boolean(string='Aceptado por el productor', default=False)

    # Notas por si el administrador rechaza el documento y quiere decirle al agricultor por qué
    admin_notes = fields.Text(string='Notas del Administrador')