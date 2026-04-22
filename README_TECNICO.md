### Rol: Daniel - Registro de Agricultores y Validaciones

**1. Modelos Modificados (`models/res_partner.py`)**
* `res.partner`: Se ha añadido el campo `registro_estado` (Selection: 'pendiente', 'aprobado', 'rechazado') con valor por defecto 'pendiente'.
* Se ha sobrescrito el método `write` para interceptar el cambio de estado a 'aprobado' y disparar automáticamente el envío de correo.

**2. Vistas y Menús Internos (`views/res_partner_views.xml`)**
* **Vista heredada:** `registro_view_partner_form_inherit` (Añade el campo `registro_estado` debajo de `category_id` en el formulario de contactos).
* **Acción:** `registro_action_agricultores_pendientes` (Filtra res.partner con domain `[('registro_estado', '=', 'pendiente')]`).
* **Menús:** * `registro_menu_root` (Pisterra Portal)
  * `registro_menu_validaciones` (Validaciones)
  * `registro_menu_pendientes` (Agricultores Pendientes)

**3. Automatización de Correos (`data/mail_template_data.xml`)**
* **Plantilla:** `email_template_agricultor_aprobado` (Envía notificación de bienvenida al cambiar el estado a aprobado).

**4. Controladores Web (`controllers/main.py`)**
* `PisterraRegistro.pagina_registro`: Ruta `/registro` (Renderiza el formulario web).
* `PisterraRegistro.procesar_registro`: Ruta `/registro/enviar` (Procesa el POST, crea el `res.partner` por sudo y renderiza la pantalla de éxito).

**5. Plantillas QWeb Web (`views/registro_web_template.xml`)**
* `formulario_registro_template`: Formulario de captura de datos integrado en `website.layout`.
* `registro_completado_template`: Mensaje visual de éxito tras solicitar el registro.