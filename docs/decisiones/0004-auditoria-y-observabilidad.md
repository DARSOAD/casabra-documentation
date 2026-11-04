# ADR 0004 Auditoría y observabilidad

- Estado: Propuesto.
- Fecha: 2026-11-03.
- Responsable: líder técnico y responsable de operación por asignar.
- Relacionado: todas las historias del módulo; BE-FI-14, OPS-FI-02 y BASE-05.
- Evidencia de aceptación: pendiente.

## Contexto y alternativas

El proyecto necesita conservar decisiones técnicas, cambios de expedientes y diagnósticos de errores. Utilizar CloudWatch como único historial de negocio dificulta asegurar atomicidad y aplicar la conservación adecuada. Guardar cada error técnico en las tablas del expediente tampoco ofrece observabilidad suficiente.

## Propuesta

ADR en Git para decisiones; auditoría RDS para acciones de negocio en la misma transacción del cambio; logs JSON en CloudWatch para operación. CloudTrail complementa con acciones AWS y eventos S3 seleccionados, sin sustituir al actor de negocio registrado por la app.

API, frontend servidor y worker envían logs mediante ECS awslogs. Correlacionar `request_id`, `trace_id`, release y códigos de error; instrumentar con OpenTelemetry/ADOT y exportar a AWS. Proponer retención de logs de 14/30/90 días para desarrollo/staging/producción, muestreo inicial de trazas del 10 % en producción y alarmas calibradas con carga. No incluir datos personales, tokens, URLs firmadas, payloads o parámetros SQL sensibles.

La aplicación solo añade auditoría; no tiene permisos de actualización o borrado sobre sus eventos. La retención documental y de auditoría debe acordarse por separado antes de producción. No se promete inmutabilidad frente a administradores privilegiados.

## Consecuencias y verificación

Logs, consultas, métricas, trazas y data events tienen costo recurrente. Evitar dimensiones de métricas por usuario o expediente. El responsable de operación y el canal SNS deben definirse para que las alarmas sean atendibles.

Probar rollback si falla auditoría, ausencia de datos sensibles, correlación API/worker, recepción de una alarma controlada y búsqueda de una solicitud por identificador. Cada incidente corregido aporta una prueba de regresión y, cuando corresponde, una actualización de la guía operativa o ADR.

Fuentes: [ECS awslogs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html), [Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html), [instrumentación Python en AWS](https://docs.aws.amazon.com/xray/latest/devguide/xray-python.html), [CloudTrail para S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.html).

## Historial

| Fecha | Cambio | Evidencia |
|---|---|---|
| 2026-11-03 | Propuesta inicial para estimación | Aceptación pendiente |
| 2026-11-03 | Referencias alineadas al nuevo desglose de tareas | Aceptación técnica pendiente |
