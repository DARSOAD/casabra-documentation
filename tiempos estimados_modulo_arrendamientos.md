# Tiempos estimados de desarrollo

Este documento consolida levantamientos y estimaciones de esfuerzo por módulo para calcular posteriormente un precio de desarrollo aplicando las tarifas acordadas por perfil.

> Las horas son estimaciones de esfuerzo-persona, no tiempos calendario ni compromisos. El detalle se conserva en épicas y su cálculo reproducible.

## Módulo 8. Arriendo de inmuebles adquiridos

**Estado:** estimación preliminar desglosada con `estimate-task`; confianza baja.
**Alcance:** operación de inmuebles adquiridos, autoservicio del arrendatario, pago digital del canon, recordatorios, comprobantes internos y control de cartera/mora.

| Capa | Estimación (horas-persona) |
|---|---:|
| Análisis funcional | 8–16 |
| Diseño UX/UI adaptable | 20–32 |
| Backend | 195–336 |
| Frontend | 114–204 |
| Infraestructura incremental y observabilidad | 24–48 |
| Validación transversal | 24–40 |
| Entrega y documentación | 6–16 |
| **Módulo sobre base funcional existente** | **391–692** |
| Base compartida, solo si aún no existe | 48–96 |
| **Módulo más base compartida pendiente** | **439–788** |

La estimación preliminar anterior de **360–570 h** se conserva solo como antecedente; no es tiempo real ni ancla de productividad y no se suma al nuevo rango. La reestimación desglosada refleja incertidumbre sobre reutilización real, estados financieros e integración de pasarela.

### Método y referencias

- 1 día productivo = 8 horas-persona, como convención de cálculo; no fija plazo calendario ni horas facturables.
- Las referencias A1/A2 de la skill son importadas y no verificadas; no se consideran comparables para cuantificar este módulo. Se usa H, hipótesis técnica por entregable, porque no hay tareas cerradas ni código inspeccionado de Casabra.
- M0 cubre análisis/diseño sin implementación. M1 cubre dinero, contratos, permisos, datos personales o patrones no comprobados. El factor M1 (×1,5–2) se aplica una sola vez.
- TDD, pruebas propias y revisión están incluidos en cada tarea; la capa QA es solo transversal para integración, regresión y flujos completos.
- No se añade contingencia porcentual genérica: el riesgo M1 ya está incorporado. La base compartida solo se agrega si se confirma que falta.

### Supuestos y exclusiones principales

- Se estima web adaptable a móvil, no aplicación nativa. Los anuncios y enlaces se gestionan manualmente; no se sincronizan portales externos.
- Se contempla una pasarela por seleccionar, pagos externos registrados manualmente y comprobantes internos. No incluye facturación electrónica DIAN ni conciliación bancaria automática.
- Login, inmuebles, contratos/firma, permisos, AWS, base de datos, pipeline y monitoreo son capacidades por verificar; no se descuentan como reutilización confirmada.
- No incluye tarifas de pasarela, mensajes/SMS, consumo AWS ni tiempos de espera de terceros.
- Reglas de vencimientos, pagos parciales/reversos, mora y criterios Gherkin del módulo deben confirmarse antes de cerrar cotización.

El desglose por tarea, modos, fórmula, exclusiones y condiciones de la base están en la [épica de arriendo](epicas%20y%20tiempos/arriendo-inmuebles-epica.md) y el [cálculo reproducible](docs/estimaciones/modulo-8-estimacion.json).

### Notas para la estimación económica

- Desglosar horas por perfil (análisis, diseño, backend, frontend, QA y DevOps) y aplicar la tarifa acordada; no multiplicar el rango por una tarifa única si las tarifas varían por perfil.
- No convertir el esfuerzo-persona a calendario dividiendo por cantidad de desarrolladores sin considerar dependencias, capacidad y tiempos de terceros.
- Registrar horas reales al terminar para recalibrar estimaciones futuras.
