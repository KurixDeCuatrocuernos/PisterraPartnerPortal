# Este modelo es para crear lo necesario para la página Dashboard
from odoo import models, fields

class DashModel(models.Model):
    _name = 'pisterra.dash.model' # id del modelo que se usa en menu.xml
    _description = 'Dashboard Model' # Descripción breve
    
    name = fields.Char(string='Nombre', required=True) 
    description = fields.Text(string='Descripción')
    active = fields.Boolean(string='Activo', default=True)