# Resultados de verificación

17 de noviembre de 2026. La revisión automatizada se ejecutó en Windows con Chrome sin interfaz y Playwright, abriendo `index.html` mediante `file://`. La inspección visual de escritorio y móvil se hizo en Edge. [Validación visual](../validacion-visual.md)

| Verificación | Resultado |
| --- | --- |
| Pruebas de Node.js | 3 aprobadas, 0 fallidas |
| Sintaxis de `app.js` | Código de salida 0 |
| Auditoría de flujos en Chrome | 126 comprobaciones aprobadas, 0 fallidas |
| Diseño adaptable | Ambas pestañas y cinco paneles de muestra en anchos de 375, 768, 1024 y 1440 px. Sin desbordamiento horizontal de la página ni de los paneles medidos. |
| Recursos | 0 errores JavaScript, 0 recursos fallidos y 0 solicitudes HTTP o HTTPS en la página durante las pruebas. |

## Recorridos comprobados

- Pestañas con flechas, Inicio y Fin. Apertura de diálogo con Enter, foco inicial en el título, 25 pulsaciones de Tab y 15 de Mayús+Tab dentro del panel. Escape devolvió el foco y conservó el desplazamiento de origen. También se probó el botón **Cerrar**.
- Registro de Laura Méndez con autorización y verificación simulada. Continuidad de Laura y CAS-024 en CRM, con actividad y compromiso. Cambiar la etapa comercial conservó el estado del inmueble.
- Adquisición desde **Documentación faltante** hasta **Adquirido**, pasando por **En estudio**, **Propuesta enviada** y **En proceso de compra**. Se verificaron restricciones por rol, confirmación de compra, asignación de Venta con adecuaciones tras la compra e historial. También se comprobó **Rechazado** por la propietaria y por la compañía, con motivo y responsable en este último caso.
- LeanCore con cuatro respuestas de muestra, incluida indisponibilidad seguida de reintento. El intercambio conservó el estado de adquisición. Los siete módulos opcionales abrieron su detalle y pudieron añadirse al escenario sin cambiar las horas publicadas. Se verificó la opción de retirar un módulo.
- Se contrastaron horas, hitos de pago y cargos de referencia presentados con el inventario de fuentes. La anualización corresponde al mínimo del proveedor. Las condiciones del cargo por crédito y los costos del core propio quedan por definir. [Inventario de fuentes](../fuentes-propuesta.md)

La evidencia reproducible del repositorio está en `qa/flujos-resultados.json`, `qa/probe-resultados.json` y `qa/capturas/`. Las pruebas cubren Chromium en Windows y los tamaños y recorridos indicados. La revisión de teclado es funcional y el alcance excluye lectores de pantalla, una auditoría formal de accesibilidad y pruebas en otros motores.
