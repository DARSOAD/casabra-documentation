# Tiempos estimados de desarrollo

Este documento consolida los levantamientos y estimaciones de esfuerzo por módulo. Servirá como base para calcular posteriormente un precio estimado del desarrollo, aplicando las tarifas acordadas por perfil o por hora.

> Las cifras son estimaciones iniciales en horas de trabajo, no compromisos de entrega. Se ajustarán cuando se definan arquitectura, integraciones, plataformas y criterios de aceptación.

## Módulo 8. Arriendo de inmuebles adquiridos

**Estado:** estimación preliminar  
**Alcance considerado:** gestión del ciclo de arriendo de inmuebles adquiridos por la compañía, autoservicio del arrendatario, pago digital del canon, notificaciones, comprobantes y control administrativo de cartera y mora.

| Componente | Esfuerzo estimado (horas) |
|---|---:|
| Refinamiento de requisitos y diseño UX/UI | 40–64 |
| Alistamiento, publicación e interesados | 40–60 |
| Contrato, entrega e inventario | 24–40 |
| Portal del arrendatario | 32–48 |
| Integración de pagos y confirmaciones | 40–70 |
| Conciliación, mora y comprobantes | 32–48 |
| Recordatorios y notificaciones | 16–24 |
| Tablero de cartera y ocupación | 24–36 |
| Permisos, auditoría y seguridad | 16–24 |
| Pruebas, ajustes y salida a producción | 52–80 |
| **Subtotal estimado** | **316–494** |
| Margen de riesgo aproximado (15 %) | 47–74 |
| **Total estimado con margen** | **360–570** |

### Supuestos de esta estimación

- Ya existen autenticación, gestión básica de inmuebles y funcionalidades de contratos y firma electrónica que se puedan reutilizar.
- El MVP permite administrar anuncios manualmente, sin integración automática con portales inmobiliarios.
- Se integra inicialmente un solo proveedor de pagos y el pago queda confirmado con la respuesta verificable del proveedor.
- Los recordatorios son básicos y se envían por los canales de notificación disponibles en la plataforma.
- Se generan comprobantes internos de pago; no se incluye facturación electrónica DIAN.
- Los pagos recibidos por medios externos se pueden registrar manualmente con su soporte para mantener conciliada la cartera.

### Fuera del alcance estimado

- Integración automática con portales inmobiliarios o publicación multicanal sincronizada.
- Integración con varios proveedores de pago, bancos o pasarelas.
- Facturación electrónica DIAN y desarrollo contable o tributario especializado.
- Consulta de centrales de riesgo, validaciones externas de candidatos o automatización avanzada de la selección de arrendatarios.
- Desarrollo de una aplicación móvil nativa independiente, si la plataforma actual no ofrece una experiencia móvil reutilizable.

### Notas para la estimación económica

- El total representa esfuerzo de trabajo; no equivale directamente a semanas calendario. La duración depende del tamaño del equipo, la disponibilidad de perfiles y los tiempos de terceros.
- Para calcular el precio, se deberá desglosar el esfuerzo por perfil (por ejemplo, análisis, diseño, desarrollo backend/frontend, QA y DevOps) y multiplicarlo por la tarifa correspondiente.
- La estimación deberá revisarse después de validar las capacidades reutilizables del producto y seleccionar el proveedor de pagos.
