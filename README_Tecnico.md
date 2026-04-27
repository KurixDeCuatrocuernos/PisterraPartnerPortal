# Módulo: Entregas (Portal Cliente)
**Responsable:** Jean

### 1. Modelos Técnicos
* `stock.picking`: Acceso en modo lectura para mostrar el historial de descargas.

### 2. Campos de Base de Datos
* `name`: Referencia del albarán.
* `scheduled_date`: Fecha de recepción.
* `state`: Estado del movimiento.
* `partner_id`: **CRÍTICO**. Campo utilizado para filtrar y aislar los registros por usuario.

### 3. IDs de Vistas y Menús (Prefijo estricto: entrega_)
* `entrega_portal_menu`: ID del menú lateral del portal.
* `entrega_list_template`: Plantilla QWeb del listado de entregas.
* `entrega_detail_template`: Plantilla QWeb del detalle del albarán.

### 4. Rutas de Controladores
* `/mis-entregas`: Listado general.
* `/mis-entregas/<int:picking_id>`: Detalle de una entrega específica.
