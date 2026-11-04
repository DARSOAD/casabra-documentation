# ADR 0002 Documentos privados y versiones

- Estado: Propuesto.
- Fecha: 2026-11-03.
- Responsable: líder técnico y responsable de negocio por asignar.
- Relacionado: HU-04, HU-05, HU-06; BE-FI-05/06/07, FE-FI-03 y OPS-FI-01.
- Evidencia de aceptación: pendiente.

## Contexto y alternativas

El propietario debe cargar documentos y evitar entregarlos repetidamente. Guardar binarios en RDS dificulta separar almacenamiento y transferencias; canalizar todos los bytes a través de la API aumenta su carga. Se propone carga directa a S3 con autorización temporal emitida por FastAPI. Publicar archivos o confiar solamente en su extensión no satisface el control requerido.

## Propuesta

S3 privado con versionado, SSE-KMS y claves opacas. RDS conserva metadatos, titular, permisos, versiones y vínculos a expedientes. La cédula puede reutilizarse únicamente en expedientes autorizados de su titular. El sistema no deduplica ni comparte entre propietarios.

Una intención autorizada produce un POST firmado corto con clave y tamaño limitados. La confirmación fija una versión. El análisis administrado de GuardDuty, los eventos EventBridge/SQS y el worker validan esa versión; solo un resultado sin amenazas y un contenido válido habilitan descarga. Ausencia de resultado, error o formato no soportado bloquean acceso. Se procesan eventos duplicados o fuera de orden sin duplicar efectos.

Las descargas requieren nueva autorización y GET temporal de la versión aprobada. Una URL firmada no es de un solo uso ni una prueba de descarga completada. Se conserva la versión documental vinculada al expediente y al estudio. El alcance inicial limita cambios de requisitos documentales a Documentación faltante; reemplazos posteriores, reapertura e invalidación automática del estudio quedan pendientes de definición y fuera de esta estimación. GuardDuty y el worker tienen permiso mínimo de lectura en cuarentena para poder analizar; usuarios y firmante de descargas permanecen bloqueados hasta la aprobación técnica del archivo.

## Consecuencias y verificación

GuardDuty, versiones S3, KMS y mensajería agregan consumo y trabajo de integración, incluido explícitamente en BE-FI-06 y OPS-FI-01. La conservación y eliminación requieren política de negocio antes de producción. No se implementa OCR ni se valida automáticamente autenticidad o suficiencia jurídica.

Probar cargas ajenas, tamaño/tipo falso, malware, errores, caducidad, reintentos, versiones sobreescritas, eventos tardíos, cuarentena y conciliación de huérfanos. Los dobles de AWS se complementan con pruebas reales en staging.

Fuentes: [Políticas POST de S3](https://docs.aws.amazon.com/AmazonS3/latest/developerguide/sigv4-HTTPPOSTConstructPolicy.html), [flujo GuardDuty para S3](https://docs.aws.amazon.com/guardduty/latest/ug/how-malware-protection-for-s3-gdu-works.html).

## Historial

| Fecha | Cambio | Evidencia |
|---|---|---|
| 2026-11-03 | Propuesta inicial para estimación | Aceptación pendiente |
| 2026-11-03 | Referencias actualizadas; se retiró la invalidación automática propuesta anteriormente al no formar parte del flujo aprobado | Alcance inicial reflejado en la épica; diseño técnico propuesto |
