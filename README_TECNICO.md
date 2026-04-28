=====================================================
# **ALEJANDRO** 
=====================================================

## *controllers/portal.py*

### `🏷️ class` Portal():
La clase que contiene las redirecciones del módulo 

#### `🔧 def` dashboard(): 
Función que establece la ruta para ir a la página dashboard.

#### `🔧 def` mis_facturas():
Función que establece las rutas para ir a la página de facturas.

#### `🔧 def` factura_en_detalle():
Función que establece las rutas para ir al página para ver una factura en detalle.

#### `🔧 def` descargar_factura_pdf():
Función que establece la ruta (y el proceso) para descargar la factura en un documento pdf.

## *models/dash_model.py*

### `🏷️ class` DashModel(models.Model):
Clase que recoge los datos del módulo de facturación para mostrarlos cuando sea oportuno (concretamente en las funciones mis_facturas() factura_en_detalle()). Se la invoca mediante: *pisterra.dash.model*

### `🏷️ class` FacturaModel(models.AbstractModel):
Clase que recoge los datos del módulo de facturación para mostrarlos cuando sea oportuno (concretamente en las funciones mis_facturas() factura_en_detalle()).
Se la invoca mediante el id: *pisterra.factura.model*

## *views/*

### `📄 template` menus.xml:
Esta plantilla en lenguaje XML es la que define los botones y las redirecciones que se utilizarán en el navbar.

### `📄 template` dash_main_template.xml:
Esta plantilla en lenguaje XML es la que define la página de inicio (dashboard).
Se la invoca mediante el id: *dash_main_template*, concretamente en la función *dashboard()* ya mencionada.

### `📄 template` dash_navbar.xml:
Esta plantilla en lenguaje XML es la que define la visualización del navbar (navegación) de nuestro módulo, para ello hereda la plantilla *portal.frontend_layout* y la modifica. 
Se la invoca mediante el id: *pisterra_portal_navbar*, en todas las plantillas de páginas (que acaban en template).

### `📄 template` factura_simple_template.xml:
Esta plantilla en lenguaje XML es la que define la página que muestra las facturas de un usuario si es un cliente o un productor (o todas si es administrador).
Se la invoca mediante el id: *factura_simple_template*

### `📄 template` factura_detallada_template.xml:
Esta plantilla en lenguaje XML es la que define la página que muestra los datos de una factura en detalle.
Se la invoca mediante el id: *factura_simple_template*

