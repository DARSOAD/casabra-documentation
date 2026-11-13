# Épica del módulo 7. Contratos y firma electrónica

Cotización inicial de **HU-20 a HU-22** de las [historias del proyecto](../historias_de_usuario_plan_del_proyecto.md), según el [contexto del negocio](../contexto.md). Mantiene la estructura por capas de la [épica del login](login-epica.md). Cubre generación, revisión, firma mediante proveedor y archivo de contratos para adquisición, arriendo y venta.

**Referencia funcional:** [criterios Gherkin propuestos](contratos-firma-criterios-aceptacion.md). No se encontraron criterios aprobados específicos de este módulo. Los escenarios y límites de proveedor/plantillas son supuestos de cotización pendientes de validación; se preservan las reglas de los [criterios aprobados de adquisición](adquisicion-inmuebles-criterios-aceptacion.md).

## Resumen de horas

| Capa | Rango |
|---|---:|
| Definición | 12–24 h |
| Backend | 147–312 h |
| Frontend | 51–108 h |
| Infraestructura incremental y observabilidad | 21–44 h |
| Validación transversal | 27–56 h |
| Entrega | 9–20 h |
| **Módulo sobre base funcional** | **267–564 h** |
| Base compartida, solo si está pendiente | 78–176 h |
| **Módulo con toda la base pendiente** | **345–740 h** |

**Unidad:** horas-persona; 1 d = 8 h como convención, no calendario. TDD, pruebas propias y revisión están incluidos en cada tarea funcional; QA cubre recorridos y fallos entre componentes en staging. Consumo AWS, licencias, transacciones del proveedor y esperas se separan. No se identificó estimación anterior del módulo 7.

## Método y evidencia

Se aplica [estimate-task local](../skills/estimate-task/SKILL.md) y sus [referencias de calibración](../skills/estimate-task/references/calibration.md). [Datos y cálculo reproducible](../docs/estimaciones/modulo-7-estimacion.json) y [generador](../docs/estimaciones/generar_modulo_7.py): `python docs/estimaciones/generar_modulo_7.py`.

**Confianza baja:** proveedor, plantillas, identidad y retención pendientes; no existen tiempos reales Casabra disponibles ni base implementada comprobada. A1 (S9.2 / RED-3596, 0,5 d) representa conexión UI a endpoint con errores/pruebas; A2 (RED-765 / PR 766, aproximadamente 1 d), consultas y generación documental con servicios existentes. Son referencias importadas no verificadas, usadas como analogías parciales, no mediciones de este proyecto. H (1 d) es unidad de hipótesis técnica por entregables, no un antecedente real. Las horas de módulos anteriores no son anclas medidas.

**Fórmula por extremo:** `ceil(8 × días_referencia × unidades_base × factor_riesgo)`. ×ref indica unidades antes del riesgo. M0 aplica ×1 a definición; M1 aplica ×1,5–2 una sola vez por permisos, datos personales, documentos sensibles, migraciones o patrón no comprobado. No multiplicar el total de nuevo ni duplicar TDD/revisión. No se presume descuento fijo por IA. Recalibrar con tiempos reales después del primer contrato completo; los rangos no son percentiles estadísticos.

## Alcance confirmado y límites de cotización

| Historia | Resultado incluido |
|---|---|
| HU-20 | Abogado maneja plantillas para adquirir, arrendar y vender |
| HU-21 | Contraparte revisa y firma desde celular |
| HU-22 | Administrador consulta documentos firmados y trazabilidad archivados |

**Confirmado por contexto:** adquisición tiene como contraparte al propietario original. Arriendo y venta se realizan sobre activos adquiridos de la compañía, con arrendatario y comprador respectivamente. Firma de contrato no cambia por sí sola el inmueble a Adquirido, no confirma pago, no entrega el activo y no cierra la operación. Cada módulo conserva sus decisiones y permisos de negocio.

**Supuestos de cotización:**

- Una compañía; tres plantillas iniciales, una por tipo de operación, en español y diseño fijo con textos/cláusulas y variables editables mediante esquema acotado. Abogado entrega y aprueba contenido; versionar/publicar/retirar plantillas forma parte de este módulo. Versiones adicionales usan el mismo esquema, sin formatos arbitrarios.
- Un PDF por contrato, sin paquete de anexos a firmar; dos firmantes secuenciales: contraparte y representante designado de la compañía. Ambos deben completar su firma. Copropietarios, codeudores, garantes, testigos, múltiples representantes, anexos firmados y rutas condicionales requieren revisar alcance.
- Un proveedor contratado con API/sandbox, firma alojada adaptable a móvil, invitaciones, verificación de identidad, consulta autoritativa de estados, webhook verificable, expiración/cancelación y descarga de PDF firmado más evidencias. Es un requisito para sostener esta estimación, no una capacidad comprobada de un proveedor seleccionado.
- El proveedor permite idempotencia o consulta por referencia de envío. Si una respuesta es incierta, se concilia antes de reintentar; si la consulta no resuelve, se conserva estado de atención operativa sin emitir otro contrato. La app no implementa criptografía de firma, emisión de certificados ni un sistema propio de OTP/biometría.
- Invitaciones enviadas mediante el proveedor. La contraparte con cuenta existente puede revisar desde la app y abrir su sesión; quien no tenga cuenta usa el enlace personal y verificación del proveedor. No se incluye nuevo onboarding para compradores/arrendatarios ni acceso anónimo al repositorio contractual interno.
- Abogado prepara/aprueba/envía; representante firma la invitación asignada; contraparte firma solo lo asignado; administrador consulta archivo/trazabilidad. La matriz definitiva, reemplazos de representante y facultades para cancelar quedan pendientes. Se adapta identidad existente, sin nueva consola de permisos.
- PDF generado con snapshot de datos, plantilla y participantes. La aprobación se refiere a una revisión exacta. Cambiar datos antes de envío obliga a nueva revisión/aprobación; después de envío, el documento no se edita. Corregirlo exige cancelación confirmada cuando sea posible y un contrato nuevo vinculado; no se elimina la evidencia anterior.
- Archivo automático del PDF firmado y evidencia descargada del proveedor en S3 privado, con versión y hashes propios; eventos/auditoría en RDS. Conservar original enviado y resultado firmado por separado. La firma modifica bytes: sus hashes no tienen que coincidir. Un hash local detecta cambios, no reemplaza la comprobación de identidad o suficiencia de la evidencia.
- FastAPI, Next.js adaptable a celular, AWS, S3 y RDS PostgreSQL propuesto. Acceso conectado; sin app nativa ni firma offline. El tipo de firma y el mecanismo de identidad que requiera cada documento deben ser aprobados por negocio/abogado y soportados por el proveedor.

### Estados propuestos y recuperación

| Dimensión | Estados / regla |
|---|---|
| Preparación y firma | Borrador → Listo para firma → En firma → Firma completa; alternativas Rechazado, Expirado o Cancelado confirmadas por proveedor |
| Envío o cancelación inciertos | Conciliación pendiente; no repetir envío ni afirmar cancelación por un timeout |
| Archivo | Pendiente → Archivado o Error de archivo, independiente de firma |
| Firma parcial | Mantener En firma y estado por participante; no dar contrato por completo |

El retorno del navegador no confirma firma. Los eventos se autentican y deduplican; una consulta al proveedor resuelve estados ambiguos o desordenados. Firma completa exige todos los participantes requeridos; Archivado exige PDF firmado y evidencias persistidos. Reintentar archivo no vuelve a firmar ni enviar. Una carrera entre cancelación y firma se concilia contra el proveedor y conserva historial.

**Pendientes que afectan el rango:** proveedor/API y límites, método de identidad/firma, número/orden de firmantes, formatos y longitud real de plantillas, campos por operación, capacidad de invitar externos, política de expiración/reenvío, retención, volumen mensual, residencia de datos y responsables de aprobación. La suficiencia jurídica de cada documento y mecanismo es una decisión de la empresa y su abogado; estas horas no incluyen redacción ni dictamen legal.

**Fuera de alcance:** trámites notariales/registrales, confirmación de pagos/adquisición, operación de arriendo/venta, KYC propio, múltiples proveedores, firma criptográfica propia, validación especializada a largo plazo, sellado de tiempo independiente, almacenamiento WORM, OCR, Word colaborativo/redlining, múltiples idiomas, importación masiva y conservación de documentos históricos externos. Si alguno es requerido, se cotiza antes de implementar.

## Tabla de estimación por tarea

| ID | h | d | Modo | Referencia × unidades; riesgo | Motivo / verificación |
|---|---:|---:|---|---|---|
| AN-CT-01 | 12–24 | 1,5–3 | M0 | H × 1,5–3; ×1–1 | Definiciones documentales e integración externa aún desconocidas. |
| BE-CT-01 | 15–32 | 1,875–4 | M1 | H × 1,25–2; ×1,5–2 | Datos personales, versiones y consistencia de estados distribuidos. |
| BE-CT-02 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Tres formatos acotados con contenido controlado y publicación trazable. |
| BE-CT-03 | 24–48 | 3–6 | M1 | A2 × 2–3; ×1,5–2 | Analogía parcial A2: tres documentos con snapshot y revisión de renderizado. |
| BE-CT-04 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Aprobación del documento exacto, permisos y cambios sensibles. |
| BE-CT-05 | 24–56 | 3–7 | M1 | H × 2–3,5; ×1,5–2 | Proveedor sin seleccionar, enlaces sensibles y envío con resultado incierto. |
| BE-CT-06 | 24–48 | 3–6 | M1 | H × 2–3; ×1,5–2 | Webhooks desordenados, firmas parciales y recuperación de eventos perdidos. |
| BE-CT-07 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Descarga recuperable e integridad de artefactos sensibles. |
| BE-CT-08 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Tres mapeos de datos y separación de contrato frente al negocio. |
| FE-CT-01 | 12–28 | 1,5–3,5 | M1 | A1 × 2–3,5; ×1,5–2 | Analogía parcial A1: catálogo, edición limitada y versiones. |
| FE-CT-02 | 15–32 | 1,875–4 | M1 | A1 × 2,5–4; ×1,5–2 | Formulario por operación y confirmación de PDF/firmantes. |
| FE-CT-03 | 12–24 | 1,5–3 | M1 | A1 × 2–3; ×1,5–2 | Documento asignado, navegación al proveedor y retorno no confiable. |
| FE-CT-04 | 12–24 | 1,5–3 | M1 | A1 × 2–3; ×1,5–2 | Lista, detalle y descarga sensible con dos estados separados. |
| OPS-CT-01 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Credenciales, endpoint público y ejecución recuperable. |
| OPS-CT-02 | 9–20 | 1,125–2,5 | M1 | H × 0,75–1,25; ×1,5–2 | Conservación operativa y detección de fallos sin filtrar PII. |
| QA-CT-01 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Recorridos entre capas, roles, móvil y documentos reales de prueba. |
| QA-CT-02 | 15–32 | 1,875–4 | M1 | H × 1,25–2; ×1,5–2 | Contrato externo y consistencia RDS/proveedor/S3 bajo fallos. |
| REL-CT-01 | 9–20 | 1,125–2,5 | M1 | H × 0,75–1,25; ×1,5–2 | Cambio de ambiente, revisión de plantillas y operación recuperable. |

## 0 Definición — 12–24 h

### AN-CT-01 Acordar plantillas, firmantes y contrato del proveedor — 12–24 h

**Fuente:** HU-20, HU-21, HU-22. **Estimación:** M0 · H × 1,5–3; luego ×1–1. Definiciones documentales e integración externa aún desconocidas.

- Inventariar una plantilla inicial por adquisición, arriendo y venta; acordar campos, cláusulas editables, variables y quién aprueba el documento.
- Revisar documentación y sandbox del proveedor elegido: creación idempotente o consulta por referencia, autenticación de eventos, estados por firmante, cancelación, expiración, descarga de PDF firmado y evidencias.
- Definir dos firmantes en secuencia, identidad exigida, invitación, retención, roles y aceptación Gherkin; registrar ADR. El abogado aporta y aprueba contenido y suficiencia jurídica; no se redactan contratos legales en estas horas.

**Tecnologías:** Markdown, OpenAPI, documentación/sandbox del proveedor por seleccionar, ADR.


## 1 Backend — 147–312 h

### BE-CT-01 Modelo contractual y migraciones — 15–32 h

**Fuente:** HU-20, HU-21, HU-22. **Estimación:** M1 · H × 1,25–2; luego ×1,5–2. Datos personales, versiones y consistencia de estados distribuidos.

- Modelar plantilla/versiones, contrato/revisión, operación de origen, firmantes, solicitud al proveedor, eventos recibidos, artefactos y auditoría.
- Guardar snapshot de datos y referencias de documento, hashes separados del PDF enviado y firmado, IDs externos únicos e índices de consulta.
- TDD de integridad y migración sobre datos previos, contrato/revisión únicos y pertenencia a operación. No duplicar personas, inmuebles o movimientos de pago.

**Tecnologías:** SQLAlchemy 2, Alembic, PostgreSQL en RDS, pytest y Testcontainers.

### BE-CT-02 Plantillas versionadas para las tres operaciones — 18–40 h

**Fuente:** HU-20. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Tres formatos acotados con contenido controlado y publicación trazable.

- Proponer GET/POST /api/v1/plantillas-contrato y publicación/retiro de versiones; configurar una plantilla de adquisición, una de arriendo y una de venta.
- Permitir al abogado editar textos/cláusulas y variables de un esquema limitado sobre diseño fijo; escapar contenido y rechazar expresiones/código arbitrario.
- Congelar versiones publicadas, crear nueva versión al corregir y mantener anteriores para contratos emitidos. TDD de variable desconocida, permisos y retiro sin modificar contratos existentes.
- Sin editor Word colaborativo, carga arbitraria DOCX, variantes ilimitadas, comparación legal de cláusulas ni maquetación libre.

**Tecnologías:** FastAPI, Pydantic, esquema de campos permitido, plantillas HTML controladas, pytest.

### BE-CT-03 Completar datos y generar PDF de contrato — 24–48 h

**Fuente:** HU-20, HU-21. **Estimación:** M1 · A2 × 2–3; luego ×1,5–2. Analogía parcial A2: tres documentos con snapshot y revisión de renderizado.

- Proponer POST /api/v1/contratos y generación de revisión PDF a partir de plantilla publicada y datos validados; validar campos obligatorios antes de enviar.
- Guardar snapshot de plantilla, datos, participantes y versión del documento; generar PDF reproducible en contenido y conservar hash del archivo concreto aprobado.
- Preparar saltos de página, cabeceras, tablas y campos de firma para tres formatos iniciales. Inspeccionar renderizado con nombres/direcciones largos, acentos y distintas cantidades de texto.
- TDD de importes/fechas, datos faltantes, inyección de contenido, fuentes y nueva revisión sin alterar PDF ya enviado. No permitir lectura de red/archivos arbitrarios desde el renderizador.

**Tecnologías:** FastAPI, motor HTML a PDF propuesto WeasyPrint, almacenamiento S3, pytest y comparación visual de muestras.

### BE-CT-04 Revisión, autorización y ciclo contractual — 12–24 h

**Fuente:** HU-20, HU-21, HU-22, HU-33 (dependencia transversal). **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Aprobación del documento exacto, permisos y cambios sensibles.

- Implementar política: abogado prepara/aprueba/envía; contraparte revisa/firma lo asignado; administrador consulta archivo y trazabilidad. Representante de compañía firma mediante invitación asignada, no por tener un rol genérico.
- Validar Borrador → Listo para firma → En firma; correcciones antes del envío generan revisión e invalidan aprobación previa. Bloquear edición del documento enviado.
- Registrar solicitud de cancelación y confirmarla solo desde proveedor; una carrera con firma completada queda en conciliación. Proponer reemplazo como nuevo contrato vinculado, sin borrar el anterior.
- TDD de ID ajeno, rol no autorizado, aprobación de versión antigua y rechazo de transiciones; no construir login ni consola general de roles.

**Tecnologías:** Dependencias FastAPI, PostgreSQL, pytest y HTTPX.

### BE-CT-05 Integración de envío y sesión de firma — 24–56 h

**Fuente:** HU-21. **Estimación:** M1 · H × 2–3,5; luego ×1,5–2. Proveedor sin seleccionar, enlaces sensibles y envío con resultado incierto.

- Integrar un adaptador de proveedor para crear solicitud con PDF aprobado, dos firmantes en secuencia y referencia interna única; usar invitaciones y verificación de identidad alojadas por el proveedor.
- Proponer POST /api/v1/contratos/{id}/envio y /sesion-firma; verificar participante, vigencia y documento antes de emitir acceso temporal al flujo móvil del proveedor.
- Persistir intento antes de llamar; ante timeout consultar por referencia antes de repetir. Si no puede resolverse la ambigüedad, mantener envío en conciliación sin crear otra solicitud.
- Implementar expiración, reenvío de invitación y solicitud de cancelación según API acordada. TDD de timeout, duplicado, destinatario incorrecto y sesión vencida. Sin motor propio de firma, OTP, biometría o integración con varios proveedores.

**Tecnologías:** FastAPI, HTTPX, API/sandbox del proveedor, worker Python, pytest.

### BE-CT-06 Eventos verificados y conciliación de firmas — 24–48 h

**Fuente:** HU-21, HU-22. **Estimación:** M1 · H × 2–3; luego ×1,5–2. Webhooks desordenados, firmas parciales y recuperación de eventos perdidos.

- Proponer POST /api/v1/integraciones/firma/eventos; verificar autenticidad conforme al proveedor, persistir recepción y procesar idempotentemente con correlación por solicitud/contrato.
- Actualizar estados por firmante y contrato consultando fuente autoritativa cuando el evento sea ambiguo o anterior al estado actual; no aceptar una redirección del navegador como firma confirmada.
- Implementar conciliación periódica de envíos inciertos/pendientes y reintentos con registro de fallos; preservar estados terminales frente a eventos viejos y conciliar conflictos cancelación/completado.
- TDD de evento falsificado, duplicado, fuera de orden, parcial, perdido y finalización repetida; confirmado completo solo cuando todos los firmantes requeridos consten en el proveedor.

**Tecnologías:** FastAPI, PostgreSQL, worker Python, HTTPX, pytest.

### BE-CT-07 Archivo de firmados y evidencias — 18–40 h

**Fuente:** HU-22. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Descarga recuperable e integridad de artefactos sensibles.

- Tras confirmación completa, obtener PDF firmado y evidencia/certificado del proveedor; verificar correlación con solicitud y revisión enviada, tamaño/tipo y completitud del paquete.
- Guardar artefactos en S3 privado con referencias de versión y hashes propios; no exigir igualdad de hash entre PDF original y firmado, pues la firma modifica el archivo.
- Separar Firma completa de Archivo pendiente/Archivado/Error de archivo. Reintentar descarga sin repetir firma y marcar Archivado solo con documento y evidencias persistidos.
- Proponer GET /api/v1/contratos/{id}/archivo y /trazabilidad con descargas autorizadas temporales, original preservado y auditoría de acceso; TDD de artefacto ausente, fallo S3 y recuperación. Hash/versionado técnico no equivalen a dictamen jurídico ni validación criptográfica de largo plazo.

**Tecnologías:** FastAPI, boto3, S3, hashlib, PostgreSQL, pytest.

### BE-CT-08 Vínculos con adquisición, arriendo y venta — 12–24 h

**Fuente:** HU-20, HU-21, HU-22, HU-38/HU-48/HU-49 (dependencias, sin implementar sus flujos). **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Tres mapeos de datos y separación de contrato frente al negocio.

- Definir contrato de datos de entrada y salida con operación/inmueble/partes/condiciones para tres tipos; mapear fuentes disponibles y permitir completar campos faltantes autorizados antes de aprobación.
- Exponer consulta de estado/referencias de archivo para módulos consumidores; impedir vincular contrato a operación ajena o tipo incompatible.
- TDD de adquisición con propietario original, arriendo con arrendatario y venta con comprador. Firma completa no confirma compra, pago, entrega ni cierre de inventario.
- Sin construir módulos 8/9, sus pantallas, sincronización automática de sus estados ni recolección duplicada de sus condiciones comerciales.

**Tecnologías:** FastAPI, Pydantic, OpenAPI, pytest y fixtures de contratos de integración.


## 2 Frontend — 51–108 h

### FE-CT-01 Administración acotada de plantillas — 12–28 h

**Fuente:** HU-20. **Estimación:** M1 · A1 × 2–3,5; luego ×1,5–2. Analogía parcial A1: catálogo, edición limitada y versiones.

- Crear listado y editor de campos/textos de las tres plantillas con vista previa, publicación y retiro por abogado.
- Mostrar versión y campos permitidos; nuevas ediciones no alteran documentos existentes.
- TDD de variable inválida, pérdida de sesión, conflicto de versión y acceso denegado; sin editor de documentos libre.

**Tecnologías:** Next.js, TypeScript, React Hook Form, Zod, Vitest y Testing Library.

### FE-CT-02 Preparación, revisión y envío del contrato — 15–32 h

**Fuente:** HU-20, HU-21. **Estimación:** M1 · A1 × 2,5–4; luego ×1,5–2. Formulario por operación y confirmación de PDF/firmantes.

- Integrar selección de plantilla/operación, datos y participantes; visualizar PDF generado y aprobar la revisión exacta antes de enviar.
- Mostrar estados de envío/conciliación, progreso por firmante y acciones autorizadas de reenvío/cancelación; evitar doble clic sin suplantar idempotencia backend.
- TDD de campos faltantes, cambio posterior a aprobación, error externo y cancelación no confirmada; sin automatizar aceptación jurídica.

**Tecnologías:** Next.js, TypeScript, visor PDF del navegador, Testing Library.

### FE-CT-03 Revisión y acceso a firma desde celular — 12–24 h

**Fuente:** HU-21. **Estimación:** M1 · A1 × 2–3; luego ×1,5–2. Documento asignado, navegación al proveedor y retorno no confiable.

- Presentar contrato asignado en web móvil con acceso al PDF y botón hacia sesión alojada por proveedor; usar enlace personal de invitación del proveedor para contrapartes sin cuenta interna.
- Al regresar consultar estado backend; mostrar Pendiente de confirmación hasta evidencia verificada, permitir retomar sesión vigente y tratar rechazo/expiración.
- TDD de participante equivocado, enlace vencido, retorno manipulado y accesibilidad de la pantalla local; no construir interfaz de captura de firma del proveedor.

**Tecnologías:** Next.js, TypeScript, redirección HTTPS al proveedor, Testing Library.

### FE-CT-04 Archivo contractual y trazabilidad — 12–24 h

**Fuente:** HU-22. **Estimación:** M1 · A1 × 2–3; luego ×1,5–2. Lista, detalle y descarga sensible con dos estados separados.

- Crear bandeja administrativa filtrada por operación/estado/fecha y detalle con historial, firmantes, revisión y acceso a PDF/evidencias.
- Distinguir Firma completa y Archivo pendiente; mostrar descarga disponible solo cuando los artefactos estén habilitados y el usuario autorizado.
- TDD de vacío/error, descarga expirada y datos de contrato ajeno; no incluir exportación masiva ni portal general del cliente.

**Tecnologías:** Next.js, TypeScript, componentes accesibles, Testing Library.


## 3 Infraestructura incremental y observabilidad — 21–44 h

### OPS-CT-01 Conectividad, secretos y procesamiento externo — 12–24 h

**Fuente:** HU-21, HU-22. **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Credenciales, endpoint público y ejecución recuperable.

- Configurar secretos por ambiente, conectividad saliente, webhook HTTPS autenticado, permisos mínimos de worker/colas y programación de conciliación.
- Configurar reintentos, DLQ o equivalente y procedimientos de reproceso; comprobar recepción sandbox y disparo periódico real.
- Reutilizar servicios API/web/worker de base compartida; no crear otra plataforma AWS por módulo.

**Tecnologías:** Secrets Manager, IAM, ECS, SQS, EventBridge Scheduler, CDK/CloudFormation.

### OPS-CT-02 Archivo protegido, métricas y alarmas — 9–20 h

**Fuente:** HU-22. **Estimación:** M1 · H × 0,75–1,25; luego ×1,5–2. Conservación operativa y detección de fallos sin filtrar PII.

- Configurar S3 privado/versionado, cifrado, permisos que impidan sobrescritura/borrado desde la app y retención según decisión aprobada; conservar auditoría de negocio en RDS.
- Agregar métricas de eventos rechazados, envíos inciertos, archivo pendiente y retraso de conciliación; probar alarmas y redactar PII, secretos y enlaces de firma en logs.
- Sin prometer almacenamiento WORM, sellado de tiempo independiente o conservación probatoria especializada; si se exigen, reestimar configuración y validación.

**Tecnologías:** S3/KMS, IAM, CloudWatch, SNS, logs estructurados.


## 4 Validación transversal — 27–56 h

### QA-CT-01 Tres recorridos contractuales y permisos — 12–24 h

**Fuente:** HU-20, HU-21, HU-22. **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Recorridos entre capas, roles, móvil y documentos reales de prueba.

- Ejecutar adquisición/arriendo/venta en staging: preparar → aprobar → enviar → dos firmas sandbox → archivo y descarga autorizada.
- Revisar visualmente PDFs de tres plantillas, navegación móvil local/proveedor y permisos de abogado, contraparte y administrador con datos sintéticos.
- Verificar que no cambien automáticamente pagos o estados de negocio; no duplicar unitarias de cada componente.

**Tecnologías:** Playwright, sandbox del proveedor, revisión de PDF renderizado, fixtures sintéticas.

### QA-CT-02 Fallos del proveedor y recuperación de evidencias — 15–32 h

**Fuente:** HU-21, HU-22. **Estimación:** M1 · H × 1,25–2; luego ×1,5–2. Contrato externo y consistencia RDS/proveedor/S3 bajo fallos.

- Ensayar timeout al enviar, evento duplicado/desordenado, firma parcial, enlace vencido y carrera cancelación/firma completa contra sandbox o simulación documentada si no permite inyección.
- Interrumpir descarga/archivo, recuperar sin nueva solicitud de firma y verificar asociación de artefactos, hashes y trazabilidad; ensayar migración/recuperación con evidencia.
- Separar casos comprobados con proveedor real de los simulados; no afirmar validez jurídica, certificación criptográfica ni pruebas de proveedor que no puedan ejecutarse.

**Tecnologías:** pytest/HTTPX, sandbox, staging AWS, S3 y PostgreSQL.


## 5 Entrega — 9–20 h

### REL-CT-01 Activación del proveedor y aceptación — 9–20 h

**Fuente:** HU-20, HU-21, HU-22. **Estimación:** M1 · H × 0,75–1,25; luego ×1,5–2. Cambio de ambiente, revisión de plantillas y operación recuperable.

- Preparar configuración productiva, migraciones, comprobación de callbacks/archivo y checklist de activación usando pipeline existente.
- Entregar guía de abogado/administrador, ADR, OpenAPI, matriz de evidencia y runbook de incidentes/reconciliación; acordar aceptación con responsables de negocio.
- Separar aprobación legal, compra del proveedor, verificación de cuenta, credenciales y tiempos de firma de las horas-persona. No enviar contratos reales como parte de esta cotización.

**Tecnologías:** Git, OpenAPI, pipeline AWS, documentación del proveedor y Markdown.

## 6 Dependencias y base compartida

Se presupone login funcional, roles, API/web/worker, RDS/S3, pipeline y herramientas de pruebas. La documentación no acredita que estén entregados. Si falta toda la base, agregar una sola vez [BASE-01 a BASE-05 del módulo 2](ficha-inmueble-epica.md#6-base-compartida-si-aún-no-está-implementada): **78–176 h**. El JSON conserva el desglose. BASE-03 adapta un login existente: si se debe construir desde cero, reestimar autenticación aparte sin sumar ambas variantes.

BE-CT-08 incluye mapeos acotados con contratos de entrada disponibles o acordados, y consulta de estado/archivo para consumidores. Los módulos 2, 8 y 9 suministran operación, partes y condiciones; sus flujos operativos y adaptación de sus pantallas no se construyen aquí. Si faltan, validar con fixtures y completar datos autorizados para preparar documentos, pero no declarar integrada una operación inexistente. Las épicas de arriendo/venta deben reutilizar este motor contractual sin cobrar otro.

El archivo adapta los componentes de almacenamiento/autorización existentes; no cotiza de nuevo carga general de documentos de adquisición u obra. La base compartida y los servicios de cola/worker se pagan una sola vez. La configuración incremental del proveedor, renderizado y evidencia contractual sí pertenece a este módulo. Verificar reutilización real antes de consolidar costos.

Secuencia: definir proveedor/plantillas → modelo y permisos → generación/aprobación → envío/eventos → archivo → tres recorridos de aceptación → activación. Frontend puede avanzar sobre contratos API acordados. Sin documentación/sandbox útil, integración y QA externo quedan condicionados; la incertidumbre no se resuelve con una reserva pequeña.

## 7 Complejidad

| Grupo | S/M/L | Motivo |
|---|---|---|
| Plantillas y PDF | L | Tres formatos, versiones y revisión exacta del contenido |
| Envío y firma móvil | L | Identidad delegada, enlaces sensibles y timeout ambiguo |
| Eventos y conciliación | L | Estados distribuidos, duplicados y concurrencia |
| Archivo y trazabilidad | L | Artefactos y evidencias recuperables sin alterar originales |
| Pantallas internas | M | Formularios, permisos y estados diferenciados |
| Operación y validación | M | Credenciales, ambientes y pruebas de fallos reales |

S/M/L es complejidad relativa, sin equivalencia automática a horas.

## 8 Contingencias, servicios y entrega

- **Reserva condicionada:** 0–4 h, fuera del total base, solo ante un ajuste acotado de campos/IDs de un contrato de origen ya entregado. Dueño: responsable de integración con módulos de origen. Totales bajo esa condición: **267–568 h** sobre base funcional o **345–744 h** con toda la base pendiente. No cubre cambio de proveedor, falta de API, otros firmantes/formatos ni requisitos legales nuevos; se reestiman. No duplicar el riesgo tratado con M1.
- **Consumo AWS fuera de horas:** cómputo de renderizado/API/worker, S3/versiones/transferencia, RDS, SQS, EventBridge Scheduler, KMS, Secrets Manager y CloudWatch. Dimensionar con región, tamaño de PDF/evidencia, retención, concurrencia y volumen de contratos.
- **Proveedor fuera de horas:** suscripción, solicitudes de firma, firmantes, identificación/OTP, mensajes, almacenamiento/descargas o funcionalidades adicionales según contrato elegido. Sin proveedor y volumen no se fija precio ni se afirma disponibilidad comercial de una función.
- **Esperas separadas:** selección/contratación, revisión legal, plantillas aprobadas, alta de cuenta, credenciales, validación de identidad y tiempos de firma de terceros. El calendario depende de estas condiciones y capacidad, no de dividir horas entre personas sin más.
- **Aceptación:** validar los Gherkin y supuestos; conservar ADR, evidencias sandbox y limitaciones de simulaciones; registrar horas reales y recalibrar después de la primera plantilla firmada/archivada. Esta entrega es una cotización documentada, no una integración ejecutada ni envío de contratos reales.
