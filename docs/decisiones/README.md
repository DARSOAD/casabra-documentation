# Registro de decisiones técnicas

Este registro conserva el contexto de las decisiones del proyecto y su relación con las historias y la cotización. La [épica del módulo 2](../../epicas%20y%20tiempos/ficha-inmueble-epica.md) contiene el alcance y la estimación que sustentan las propuestas iniciales.

| ADR | Tema | Estado | Fecha |
|---|---|---|---|
| [0001](0001-arquitectura-modulo-2.md) | FastAPI, PostgreSQL y ejecución AWS | Propuesto | 2026-11-03 |
| [0002](0002-documentos-privados-y-versiones.md) | Documentos privados, versiones y procesamiento | Propuesto | 2026-11-03 |
| [0003](0003-tdd-y-calidad.md) | TDD, pruebas y controles de entrega | Propuesto | 2026-11-03 |
| [0004](0004-auditoria-y-observabilidad.md) | Auditoría de negocio, logs y trazas | Propuesto | 2026-11-03 |

## Forma de trabajo

1. Crear un archivo con número consecutivo usando la [plantilla](plantilla.md), antes de implementar una decisión importante.
2. Relacionar historias, tickets, alternativas e impacto en horas o costo recurrente. Cambios menores de parámetros pueden documentarse en la PR; si alteran una decisión, requieren ADR.
3. Registrar responsable y evidencia de aceptación del equipo en PR o acta. No marcar una propuesta como aceptada por haberla escrito.
4. Estados: Propuesto, Aceptado, Rechazado y Sustituido. Registrar fecha de cada cambio.
5. Una decisión aceptada que cambia se conserva como Sustituida y enlaza al nuevo ADR. No borrar la justificación anterior.
6. Vincular el ADR con PR, commit y versión de despliegue cuando existan. No introducir secretos, documentos personales ni URLs firmadas.

Este historial responde por qué se diseñó el sistema de cierta forma. Los cambios de expedientes se guardan en auditoría de negocio y los errores de ejecución en CloudWatch; no se registran como ADR.

Referencia: [Proceso de registros de decisiones de arquitectura de AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html).
