from odoo import models, fields, api
from odoo.exceptions import AccessError

class FacturaModel(models.AbstractModel):
    """Modelo abstracto para la gestión de facturas del portal"""
    _name = 'pisterra.factura.model' # id del modelo que se usa en menu.xml
    _description = 'Modelo de Factura' # Descripción breve

    @api.model
    def get_facturas_usuario(self):
        """Obtiene las facturas del usuario actual según sus privilegios"""
        user = self.env.user
        
        # Verificamos si es admin o manager
        is_admin = user.has_group('base.group_system')
        is_manager = user.has_group('sales_team.group_sale_manager')
        has_privileged = is_admin or is_manager
        
        domain = [
            ('move_type', '=', 'out_invoice'),
            ('state', '=', 'posted')
        ]
        
        # Si no tiene privilegios, filtramos por su partner
        if not has_privileged:
            domain.append(('partner_id', '=', user.partner_id.id))
        
        facturas = self.env['account.move'].sudo().search(domain)
        
        return {
            'facturas': facturas,
            'is_admin': has_privileged,
            'admin_label': self._get_admin_label(is_admin, is_manager)
        }
    
    @api.model
    def _get_admin_label(self, is_admin, is_manager):
        """Devuelve la etiqueta del rol del usuario"""
        if is_admin:
            return 'Administrador'
        elif is_manager:
            return 'Manager'
        return 'Usuario'
    
    @api.model
    def get_factura_detalle(self, invoice_id):
        """Obtiene una factura específica verificando permisos"""
        factura = self.env['account.move'].sudo().browse(invoice_id)
        
        if not factura.exists():
            return None
        
        # Verificamos permisos
        user = self.env.user
        is_admin = user.has_group('base.group_system')
        is_manager = user.has_group('sales_team.group_sale_manager')
        has_privileged = is_admin or is_manager
        
        if not has_privileged and factura.partner_id.id != user.partner_id.id:
            raise AccessError("No tiene permiso para ver esta factura")
        
        return factura
    
    @api.model
    def descargar_factura_pdf(self, invoice_id):
        """Genera el PDF de una factura verificando permisos"""
        factura = self.get_factura_detalle(invoice_id)
        
        if not factura:
            return None
        
        # Generamos PDF usando el reporte estándar de Odoo
        pdf = self.env['ir.actions.report'].sudo()._render_qweb_pdf(
            'account.account_invoices', 
            factura.ids
        )[0]
        
        return {
            'pdf': pdf,
            'nombre': f'Factura_{factura.name}.pdf'
        }
    