# Épica de adquisición de inmuebles

Desglose técnico del módulo 2 para cotización inicial, con la misma estructura de tareas, tecnologías y horas de la [épica del login](login-epica.md). Cubre HU-04 a HU-08 y el flujo de adquisición acordado. Se conserva el nombre del archivo para mantener sus enlaces.

**Referencia funcional:** [criterios mínimos de aceptación en Gherkin](adquisicion-inmuebles-criterios-aceptacion.md). Las tareas implementan esos criterios; las horas son estimaciones iniciales de esfuerzo por persona, no tiempos medidos ni un precio cerrado.

## Resumen de horas

| Capa | Estimación anterior | Rango revisado |
|---|---:|---:|
| Definición y requisitos | 8 h | 4–8 h |
| Backend | 194 h | 135–292 h |
| Frontend | 94 h | 69–132 h |
| Infraestructura incremental y observabilidad | 24 h | 21–44 h |
| Validación transversal | 28 h | 24–56 h |
| Entrega y documentación | 8 h | 6–16 h |
| **Módulo sobre base funcional** | **356 h** | **259–548 h** |
| Base compartida, solo si está pendiente | 100 h | 78–176 h |
| **Módulo más toda la base pendiente** | **456 h** | **337–724 h** |

Las cifras anteriores se conservan como antecedente, no como esfuerzo medido. Los rangos incluyen implementación, TDD, revisión y pruebas propias. Setup compartido y pruebas transversales tienen partidas separadas para evitar doble cobro. Consumo AWS y esperas de accesos/decisiones no son horas de desarrollo.

### Método de reestimación

Se aplica la fase B de **estimate-reddo-task**, adaptada a **estimate-task** para Codex. Ya existe un desglose aprobado: se conservan los 28 IDs y su alcance, sin escribir en la página Helper de Reddo. El cálculo reproducible está en [los datos de estimación](../docs/estimaciones/modulo-2-estimacion.json).

**Unidad:** 1 día productivo = 8 horas-persona, convención de esta estimación. No se verificó la duración de las jornadas originales de Reddo. Los días expresan esfuerzo, no fechas de entrega. La modalidad asistida por IA no supone un descuento fijo.

| Referencia | Base de comparación | Evidencia disponible |
|---|---|---|
| A1 — S9.2 / RED-3596 | 0,5 d para conectar UI a un endpoint existente, errores y pruebas básicas | Referencia importada del archivo anchors.md de la skill de Claude |
| A2 — RED-765 / PR 766 | Aproximadamente 1 d para consultas sobre modelo nuevo y generación de documento con patrones existentes | Referencia importada; analogía parcial para consultas de ficha/seguimiento |
| H — hipótesis técnica | 1 d como unidad para dimensionar entregables y su verificación | Juicio técnico; **no es una tarea histórica ni un ancla medida** |

El archivo de origen declara tareas cerradas con esfuerzo observado, pero aquí no se consultaron tickets ni registros de tiempo para corroborarlo. No existen tiempos reales de Casabra disponibles. El framework externo de modos referenciado por la skill no se encontró; se usa la definición resumida que contiene su SKILL.md. **Confianza baja**, especialmente en infraestructura y procesamiento documental.

- **M0:** análisis y decisiones sin implementación; aplica a AN-FI-01.
- **M1:** dinero, autenticación/permisos, información personal, migraciones, acciones sensibles o ausencia de patrón implementado comprobable. Aplica al resto de esta revisión.
- **M2:** patrón existente comprobado y sin las condiciones de M1; no se asigna por tener una épica escrita.
- **M3:** automatización repetible con controles probados; una integración nueva de escaneo no cumple esa condición.

**Fórmula:** mínimo = base de referencia × unidades mínimas × factor mínimo; máximo = base × unidades máximas × factor máximo. M1 usa ×1,5–2; M0 usa ×1. Se convierte a horas y se redondea hacia arriba por tarea. Las unidades comparables son juicio técnico explícito, no datos observados. Para H, esas unidades describen el trabajo de análisis, implementación e integración antes de la verificación reforzada.

El factor M1 incorpora diseño, revisión detallada y comprobación de casos positivos/negativos, no solo escritura de código. Se reconstruyó la base de cada tarea: **no se multiplicaron las horas anteriores**, que ya incluían TDD. No volver a aplicar M1 al total ni sumar las mismas pruebas otra vez. Las reutilizaciones entre tareas se identifican en su motivo, sin eliminar la verificación de permisos o datos sensibles.

## Alcance para la estimación

| Historia | Resultado |
|---|---|
| HU-04 | Cargar, conservar y reutilizar documentos propios; identificar requisitos pendientes |
| HU-05 | Consultar la ficha con datos, fotos y documentos autorizados |
| HU-06 | Registrar estudio de títulos, conclusión y alertas jurídicas |
| HU-07 | Confirmar adquisición y asignar arriendo o venta, indicando si requiere adecuaciones |
| HU-08 | Consultar avance, pendientes y fecha estimada; consultar y responder la oferta |

Se incluyen las acciones acordadas durante el análisis: el asesor envía una oferta o rechaza el inmueble, el propietario responde y una persona autorizada confirma la compra. Confirmar la compra en la app no sustituye la formalización jurídica.

### Máquina de estados aprobada

| Estado actual | Acción | Responsable | Nuevo estado |
|---|---|---|---|
| Documentación faltante | Completar los requisitos configurados | Propietario | En estudio |
| En estudio | Enviar oferta económica | Asesor | Propuesta enviada |
| En estudio | Rechazar el inmueble con motivo | Asesor | Rechazado |
| Propuesta enviada | Aceptar oferta | Propietario | En proceso de compra |
| Propuesta enviada | Rechazar oferta | Propietario | Rechazado |
| En proceso de compra | Confirmar que se completó la compra | Abogado o persona con permiso explícito | Adquirido |

El inmueble inicia en **Documentación faltante**. La validación técnica del archivo permite usarlo; no constituye aprobación jurídica del inmueble. Al quedar **Adquirido**, el gerente asigna **Arriendo** o **Venta** y registra **requiere adecuaciones: sí/no**. La ruta es independiente del estado de adquisición.

### Supuestos de cotización

- Aplicación web Next.js adaptable a celular, con componentes visuales y login reutilizables. Una empresa y un propietario principal por inmueble.
- FastAPI para el API, S3 privado para documentos/fotos y base relacional RDS. PostgreSQL es la propuesta para estimar; no se cotiza soporte simultáneo de PostgreSQL y MySQL.
- La lista exacta de datos y documentos obligatorios sigue pendiente. Se configura mediante catálogo versionado, sin construir una consola administrativa de reglas.
- Tipos/tamaños de archivo, retención, región, capacidad AWS y volumen esperado se cierran antes de implementar. Se estima carga de PDF e imágenes habituales, sin video, OCR ni conversión de formatos especiales.
- La oferta contiene valor y moneda; el propietario la consulta y responde en la app. Se estima una oferta enviada por solicitud, sin contraofertas, vencimiento automático ni renegociación.
- La fecha estimada de respuesta la registra el asesor; si no existe, se muestra **Por confirmar**. No se incluye un motor de SLA/calendarios.
- La confirmación registra una compra completada por fuera de este flujo técnico. Contratos, firma, pagos y trámites notariales corresponden a otras épicas.
- No se incluyen aplicaciones nativas, migración masiva, reapertura de rechazos, reclasificación de ruta, operación de arriendos/ventas ni notificaciones externas al propietario. HU-07 deja la ruta disponible para esos módulos.

## 0 Definición y requisitos

**Subtotal: 4–8 h.**

### AN-FI-01 Definición de campos y requisitos configurables — 4–8 h

**Estimación:** 0,5–1 d · M0 · H (1 d) × 0,5–1 unidades × factor 1 · Alcance y catálogo pendientes; decisiones, sin implementación.

- Mapear los criterios aprobados a formularios, permisos y contrato API.
- Definir un catálogo configurable de requisitos por tipo de documento/dato, con identificación de pendientes.
- Cerrar formatos, límites, fecha de respuesta y acceso a expedientes; registrar pendientes y cambios de alcance.
- La ausencia de una lista definitiva no impide esta cotización inicial.

**Tecnologías:** Markdown, OpenAPI y configuración versionada en Git.

## 1 Backend con FastAPI SQLAlchemy y Pydantic

**Subtotal: 135–292 h.** Todas las rutas usan el prefijo `/api/v1`; los endpoints son el contrato técnico propuesto.

### BE-FI-01 Modelos de base de datos y migraciones — 12–24 h

**Estimación:** 1,5–3 d · M1 · H (1 d) × 1–1,5 unidades × factor 1,5–2 · Esquema nuevo, relaciones, migraciones y verificación sobre datos.

- Crear modelos de inmueble, solicitud, documentos/versiones, requisitos, fotos, estudio, alertas, oferta, adquisición, ruta e historial.
- Relacionar documentos con su titular o inmueble y permitir vínculos autorizados a expedientes.
- Agregar claves foráneas, restricciones e índices por propietario, estado e inmueble.
- Versionar y probar migraciones, incluida su aplicación sobre datos anteriores.

**Tecnologías:** SQLAlchemy 2 asíncrono, PostgreSQL en RDS y Alembic.

### BE-FI-02 Esquemas de validación y requisitos — 6–12 h

**Estimación:** 0,75–1,5 d · M1 · H (1 d) × 0,5–0,75 unidades × factor 1,5–2 · Validación de documentos, importe y DTO sin patrón probado.

- Crear DTO de entrada y salida separados para impedir cambios de campos internos.
- Validar datos, monto/moneda de la propuesta, ruta y necesidad de adecuaciones.
- Evaluar completitud contra el catálogo configurado y devolver los requisitos pendientes.
- Contar como entregados solo los archivos disponibles después de su validación técnica.

**Tecnologías:** Pydantic v2, FastAPI y pytest.

### BE-FI-03 Autorización por rol y expediente — 9–20 h

**Estimación:** 1,12–2,5 d · M1 · H (1 d) × 0,75–1,25 unidades × factor 1,5–2 · Autorización por rol/expediente y accesos ajenos.

- Reutilizar autenticación del login y validar permisos en consultas, cambios y descargas.
- Restringir al propietario a sus solicitudes/documentos; aplicar al equipo el acceso autorizado al expediente.
- Reservar estudio al abogado, envío/rechazo al asesor, respuesta al propietario y ruta al gerente.
- Implementar el permiso explícito para confirmar adquisición; administrar la plataforma no concede por sí solo ese permiso.

**Tecnologías:** dependencias FastAPI, autenticación existente y pytest/HTTPX.

### BE-FI-04 Datos del inmueble y consulta de la ficha — 9–16 h

**Estimación:** 1,12–2 d · M1 · A2 (1 d) × 0,75–1 unidades × factor 1,5–2 · Ficha nueva con datos personales, filtros y persistencia.

**Endpoints:** `POST /properties`, `GET /properties`, `GET/PATCH /properties/{id}` y `/properties/{id}/photos`.

- Registrar inmueble y solicitud inicial en Documentación faltante; conservar datos parciales.
- Listar con paginación y filtros según acceso del usuario.
- Componer la ficha con datos, fotos, documentos y requisitos pendientes.
- Registrar/ordenar fotos y elegir una principal; su carga usa el servicio común de archivos.

**Tecnologías:** FastAPI, SQLAlchemy y Pydantic.

### BE-FI-05 Carga y descarga privada de archivos — 18–40 h

**Estimación:** 2,25–5 d · M1 · H (1 d) × 1,5–2,5 unidades × factor 1,5–2 · S3 privado, versiones, expiración y confirmación idempotente.

**Endpoints:** `POST /applications/{id}/upload-intents`, `POST /upload-intents/{id}/confirm` y `GET /documents/{id}/versions/{version}/download`.

- Crear intención autorizada y POST firmado con duración limitada, clave opaca y restricciones de tamaño/tipo.
- Confirmar existencia, tamaño y versión S3; tolerar reintentos sin duplicar documentos.
- Mantener el archivo en procesamiento hasta terminar su validación; comprobar tipo real del contenido.
- Emitir descargas temporales únicamente para versiones disponibles y usuarios autorizados.

**Tecnologías:** Boto3, S3 privado con versionado, KMS y FastAPI.

### BE-FI-06 Análisis de archivos y procesamiento asíncrono — 18–48 h

**Estimación:** 2,25–6 d · M1 · H (1 d) × 1,5–3 unidades × factor 1,5–2 · Escaneo nuevo, cuarentena, eventos fuera de orden y recuperación.

- Integrar GuardDuty Malware Protection for S3 y resultados mediante EventBridge/SQS.
- Procesar por clave y versión, tolerando eventos duplicados y fuera de orden.
- Habilitar archivos solo con resultado sin amenazas y validaciones técnicas exitosas; bloquear errores y resultados pendientes.
- Implementar reintentos, cola de errores y conciliación de cargas huérfanas/atascadas.
- Permitir lectura en cuarentena al servicio de análisis y worker validador; bloquear al rol que firma descargas.

**Tecnologías:** GuardDuty, EventBridge, SQS y worker Python en ECS. Los recursos específicos se configuran en OPS-FI-01.

### BE-FI-07 Reutilización y versiones documentales — 6–16 h

**Estimación:** 0,75–2 d · M1 · H (1 d) × 0,5–1 unidades × factor 1,5–2 · Reutilización de documentos personales y aislamiento entre titulares.

**Endpoints:** `GET /me/documents` y `GET/POST /applications/{id}/documents`.

- Listar documentos propios utilizables y vincularlos a un expediente autorizado sin recarga.
- Conservar versiones anteriores y registrar la versión vinculada al expediente y al estudio.
- Impedir acceso/reutilización de documentos de otro titular sin autorización.
- Para esta estimación, restringir las cargas que alteran requisitos a Documentación faltante; reemplazos durante etapas posteriores requieren definir reglas adicionales.

**Tecnologías:** SQLAlchemy, S3 VersionId y FastAPI.

### BE-FI-08 Máquina de estados del inmueble — 12–24 h

**Estimación:** 1,5–3 d · M1 · H (1 d) × 1–1,5 unidades × factor 1,5–2 · Transiciones, permisos y concurrencia; sin máquina implementada.

- Implementar exclusivamente los seis estados y transiciones aprobados.
- Pasar automáticamente a En estudio al completar los requisitos configurados.
- Centralizar transiciones para impedir saltos por edición directa de campos.
- Comprobar estado, actor y versión; resolver respuestas simultáneas y reintentos sin efectos duplicados.
- Rechazar operaciones inválidas conservando datos/estado; registrar cambios mediante BE-FI-14.

**Tecnologías:** servicios de dominio Python, transacciones SQLAlchemy y pytest.

### BE-FI-09 Estudio de títulos y alertas jurídicas — 9–16 h

**Estimación:** 1,12–2 d · M1 · H (1 d) × 0,75–1 unidades × factor 1,5–2 · Estudio jurídico sensible, alertas y visibilidad por audiencia.

**Endpoints:** `POST/GET /applications/{id}/title-studies` y `POST /title-studies/{id}/alerts`.

- Exigir estado En estudio y permiso de abogado para registrar el estudio y sus alertas.
- Registrar estudio, conclusión y alertas de gravámenes, embargos o falta de licencias cuando correspondan.
- Guardar fecha, abogado y documentos considerados en la evaluación.
- Permitir al asesor autorizado consultar el resultado para decidir si propone o rechaza.
- Separar observaciones internas de información visible al propietario; el estudio no crea un estado adicional.

**Tecnologías:** FastAPI, Pydantic y SQLAlchemy.

### BE-FI-10 Oferta económica y decisiones de las partes — 12–24 h

**Estimación:** 1,5–3 d · M1 · H (1 d) × 1–1,5 unidades × factor 1,5–2 · Dinero, respuesta única, oferta exacta y decisiones simultáneas.

**Endpoints:** `POST/GET /applications/{id}/proposal`, `POST /proposals/{id}/response` y `POST /applications/{id}/reject`.

- Permitir al asesor enviar valor/moneda desde En estudio y pasar a Propuesta enviada.
- Permitir al asesor rechazar desde En estudio con motivo y registrar el origen del rechazo.
- Permitir solo al propietario responder: aceptar inicia En proceso de compra; rechazar produce Rechazado.
- Vincular cada respuesta a la oferta exacta y su importe; impedir modificar una oferta enviada o contestarla dos veces con decisiones distintas.

**Tecnologías:** FastAPI, Pydantic, SQLAlchemy y control de concurrencia/idempotencia.

### BE-FI-11 Confirmación de compra y alta como activo — 6–16 h

**Estimación:** 0,75–2 d · M1 · H (1 d) × 0,5–1 unidades × factor 1,5–2 · Confirmación de compra y alta atómica sin duplicados.

**Endpoint:** `POST /applications/{id}/acquisition`.

- Exigir En proceso de compra y permiso explícito para confirmar adquisición.
- Registrar confirmación, fecha y responsable; pasar a Adquirido y marcar el activo de la compañía en una sola transacción.
- Evitar altas duplicadas ante reintentos; conservar al propietario original como participante de la solicitud.

**Tecnologías:** FastAPI y transacciones SQLAlchemy.

### BE-FI-12 Asignación de ruta y adecuaciones — 3–8 h

**Estimación:** 0,38–1 d · M1 · H (1 d) × 0,25–0,5 unidades × factor 1,5–2 · Incremento acotado que reutiliza estados/permisos de BE-FI-03/08.

**Endpoint:** `POST/GET /properties/{id}/route`.

- Exigir inmueble Adquirido y permiso de gerente.
- Registrar una ruta, Arriendo o Venta, y un indicador independiente de adecuaciones sí/no.
- Habilitar consulta/selección del activo por el módulo correspondiente; la operación posterior se desarrolla en su propia épica.

**Tecnologías:** FastAPI, Pydantic y PostgreSQL.

### BE-FI-13 Seguimiento del propietario y fecha estimada — 6–12 h

**Estimación:** 0,75–1,5 d · M1 · A2 (1 d) × 0,5–0,75 unidades × factor 1,5–2 · Consulta privada y fecha manual; reutiliza ficha/autorización.

**Endpoints:** `GET /applications/{id}/tracking` y `PATCH /applications/{id}/response-estimate`.

- Devolver estado, requisitos pendientes y fecha estimada con acceso limitado al titular.
- Permitir al asesor registrar/actualizar la fecha; devolver ausencia explícita para mostrar Por confirmar.
- Exponer solo información autorizada, sin notas jurídicas internas.

**Tecnologías:** FastAPI, Pydantic y SQLAlchemy.

### BE-FI-14 Auditoría e historial del expediente — 9–16 h

**Estimación:** 1,12–2 d · M1 · H (1 d) × 0,75–1 unidades × factor 1,5–2 · Auditoría atómica, rollback y restricciones de edición.

**Endpoint de consulta:** `GET /applications/{id}/audit`.

- Guardar estado anterior/nuevo, fecha UTC y responsable en cada transición.
- Registrar oferta, respuesta, confirmación, ruta y cambios documentales sin copiar contenido de documentos.
- Guardar mutación y auditoría en la misma transacción; revertir ambas si falla el registro.
- Proveer consulta interna autorizada; impedir edición/borrado del historial desde la aplicación.

**Tecnologías:** PostgreSQL, SQLAlchemy y pruebas de transacciones con pytest.

## 2 Frontend con Next.js App Router

**Subtotal: 69–132 h.** Interfaz adaptable a celular sobre los componentes y la sesión existentes.

### FE-FI-01 Cliente HTTP y permisos de interfaz — 6–12 h

**Estimación:** 0,75–1,5 d · M1 · A1 (0,5 d) × 1–1,5 unidades × factor 1,5–2 · Sesión, permisos y errores de concurrencia.

- Integrar endpoints con la sesión existente.
- Gestionar errores de validación, acceso y conflictos de versión; evitar dobles envíos.
- Mostrar acciones por rol/estado, manteniendo al backend como autoridad de permisos.

**Tecnologías:** Next.js, TypeScript y Fetch o el cliente HTTP del login.

### FE-FI-02 Registro y ficha del inmueble — 12–24 h

**Estimación:** 1,5–3 d · M1 · A1 (0,5 d) × 2–3 unidades × factor 1,5–2 · Varias vistas, datos personales y guardado parcial.

- Crear formulario con guardado parcial, listado y ficha de consulta.
- Mostrar datos, galería, documentos, pendientes y estado actual.
- Gestionar fotos, orden y principal mediante el componente compartido de archivos.
- Mostrar estados de carga, vacío y error.

**Tecnologías:** React, React Hook Form, Zod y componentes/Tailwind existentes.

### FE-FI-03 Documentos y reutilización — 12–24 h

**Estimación:** 1,5–3 d · M1 · A1 (0,5 d) × 2–3 unidades × factor 1,5–2 · Carga asíncrona, fallos, documentos personales y reutilización.

- Crear carga con progreso, reintento y estados de procesamiento/archivo rechazado.
- Mostrar requisitos pendientes y documentos ya entregados.
- Permitir seleccionar documentos propios existentes y descargar versiones autorizadas.
- Actualizar la vista cuando la validación complete requisitos y el inmueble pase a En estudio.

**Tecnologías:** Next.js, cliente HTTP y carga directa firmada a S3.

### FE-FI-04 Estudio de títulos y alertas — 9–16 h

**Estimación:** 1,12–2 d · M1 · A1 (0,5 d) × 1,5–2 unidades × factor 1,5–2 · Formulario jurídico sensible sobre componentes de FE-FI-02.

- Crear formulario del abogado para estudio, conclusión y alertas; habilitar registro únicamente en En estudio.
- Mostrar documentos relacionados, fecha y responsable.
- Presentar al asesor autorizado el resultado registrado.

**Tecnologías:** React Hook Form, Zod y componentes existentes.

### FE-FI-05 Envío y respuesta de propuestas — 9–20 h

**Estimación:** 1,12–2,5 d · M1 · A1 (0,5 d) × 1,5–2,5 unidades × factor 1,5–2 · Valor económico, acciones por actor y respuesta única.

- Crear formulario del asesor con valor/moneda y envío de propuesta.
- Crear acción de rechazo del inmueble con motivo para el asesor.
- Mostrar al propietario el importe exacto con acciones de aceptar/rechazar y confirmación de su decisión.
- Actualizar estado y evitar respuestas repetidas sobre una oferta contestada.

**Tecnologías:** Next.js, TypeScript, React Hook Form y Zod.

### FE-FI-06 Confirmación de adquisición — 6–12 h

**Estimación:** 0,75–1,5 d · M1 · A1 (0,5 d) × 1–1,5 unidades × factor 1,5–2 · Confirmación sensible y prevención de doble envío.

- Mostrar la acción al abogado o usuario con permiso únicamente en En proceso de compra.
- Solicitar confirmación de compra completada y mostrar el resultado Adquirido.
- Presentar errores/conflictos sin duplicar operaciones.

**Tecnologías:** Next.js y componentes existentes.

### FE-FI-07 Ruta y necesidad de adecuaciones — 6–8 h

**Estimación:** 0,75–1 d · M1 · A1 (0,5 d) × 1–1 unidades × factor 1,5–2 · Formulario pequeño que reutiliza FE-FI-01/02; mantiene control por rol.

- Crear formulario del gerente para Arriendo/Venta y adecuaciones sí/no.
- Habilitarlo únicamente para inmuebles Adquiridos.
- Mostrar la ruta guardada y su disponibilidad para la siguiente etapa.

**Tecnologías:** React Hook Form, Zod y Next.js.

### FE-FI-08 Seguimiento y fecha de respuesta — 9–16 h

**Estimación:** 1,12–2 d · M1 · A1 (0,5 d) × 1,5–2 unidades × factor 1,5–2 · Dos audiencias, fecha y consulta de historial.

- Mostrar al propietario etapa, pendientes y fecha estimada o Por confirmar.
- Proveer al asesor el control para registrar/actualizar la fecha estimada.
- Mostrar al personal autorizado el historial con fecha y responsable.

**Tecnologías:** Next.js, TypeScript y componentes existentes.

## 3 Infraestructura incremental y observabilidad

**Subtotal: 21–44 h.** Se extiende la plataforma existente; la creación inicial se estima en BASE-01 a BASE-05.

### OPS-FI-01 Recursos y permisos AWS del módulo — 12–24 h

**Estimación:** 1,5–3 d · M1 · H (1 d) × 1–1,5 unidades × factor 1,5–2 · Políticas sensibles y flujo AWS que no tienen ancla comparable.

- Configurar almacenamiento privado, versionado, cifrado, CORS y roles mínimos de carga/análisis/descarga.
- Configurar GuardDuty, reglas EventBridge, SQS/DLQ y ejecución del worker de BE-FI-06.
- Versionar parámetros por ambiente: límites, caducidad de firmas y requisitos. Secretos en Secrets Manager; parámetros no secretos en Parameter Store/configuración versionada.
- Probar políticas, recursos sintetizados y flujo básico en staging.

**Tecnologías:** CDK Python, CloudFormation, IAM, S3, KMS, GuardDuty, SQS, EventBridge y ECS.

### OPS-FI-02 Logs correlacionados y alertas en CloudWatch — 9–20 h

**Estimación:** 1,12–2,5 d · M1 · H (1 d) × 0,75–1,25 unidades × factor 1,5–2 · Redacción de PII, trazas y prueba de alarmas.

- Emitir JSON desde API/worker con servicio, ambiente, release, request_id/trace_id, ruta, duración y código de error.
- Enviar a CloudWatch, propagar correlación e instrumentar trazas con OpenTelemetry/ADOT.
- Crear consultas, panel y alarmas de errores, latencia, procesamiento atascado y DLQ; probar el aviso al canal operativo.
- Configurar retención por ambiente y excluir tokens, URLs firmadas, documentos, cédulas y cuerpos sensibles.

**Tecnologías:** logging Python, CloudWatch Logs/Logs Insights, métricas/alarmas, SNS y OpenTelemetry/ADOT.

## 4 Pruebas y calidad

**Subtotal: 24–56 h.** Las pruebas de cada tarea funcional ya están incluidas en sus horas.

### QA-FI-01 Recorridos completos y permisos — 12–24 h

**Estimación:** 1,5–3 d · M1 · H (1 d) × 1–1,5 unidades × factor 1,5–2 · Diseño y validación E2E de varios roles y caminos de rechazo; sin ancla equivalente.

- Automatizar el recorrido propietario → asesor → abogado → propuesta → respuesta → compra → gerente.
- Cubrir rechazo del asesor/propietario, documentación pendiente y acciones inválidas por estado/rol.
- Verificar criterios Gherkin en navegador, incluida vista móvil, acceso a expediente ajeno y errores de formularios.

**Tecnologías:** Playwright Test, TypeScript y staging.

### QA-FI-02 Integración AWS rendimiento y recuperación — 12–32 h

**Estimación:** 1,5–4 d · M1 · H (1 d) × 1–2 unidades × factor 1,5–2 · AWS real, restauración y fallos; sin referencia equivalente.

- Probar carga/descarga real, expiración, cuarentena, reintentos y eventos repetidos con datos sintéticos.
- Ejecutar un ensayo acotado de concurrencia con volumen acordado en AN-FI-01; registrar resultados y límites.
- Restaurar RDS en un entorno aislado y comprobar referencias S3; verificar recuperación del despliegue.

**Tecnologías:** pytest, Boto3, Locust, RDS y S3.

### Herramientas para TDD

| Nivel | Tecnología | Qué verifica |
|---|---|---|
| Unitarias backend | pytest, parametrización y botocore Stubber | Requisitos, permisos, estados, propuestas y errores simulados |
| API e integración | HTTPX/ASGITransport y AnyIO | Validaciones, respuestas, autorización e idempotencia |
| Base de datos | Testcontainers PostgreSQL, Docker y Alembic | Migraciones, relaciones, concurrencia y transacciones |
| Interfaz | Vitest, React Testing Library y MSW | Formularios, cargas y comportamiento de componentes |
| Recorridos web | Playwright Test | Criterios entre actores/pantallas; componentes de servidor asíncronos |
| Infraestructura/AWS | assertions CDK y pruebas reales en staging | Recursos, IAM, S3/KMS y eventos |

El pipeline ejecuta formato/tipos, pruebas y cobertura antes de integrar; despliega a staging y verifica el artefacto antes de promoverlo. La configuración base queda en BASE-02/04. Cada defecto corregido agrega una regresión. La cobertura es un indicador, no reemplaza probar cada transición y permiso.

## 5 Entrega y documentación

**Subtotal: 6–16 h.**

### REL-FI-01 Despliegue aceptación y registro de decisiones — 6–16 h

**Estimación:** 0,75–2 d · M1 · H (1 d) × 0,5–1 unidades × factor 1,5–2 · Despliegue/migración, aceptación y evidencia de recuperación.

- Ejecutar despliegue incremental y migraciones mediante el pipeline, con una ronda de aceptación.
- Entregar contrato API, evidencias de pruebas y guía breve de diagnóstico/recuperación.
- Actualizar [ADR y registro de decisiones](../docs/decisiones/README.md) con contexto, alternativas, decisión, fecha y responsable.
- Relacionar versiones con commit, imagen y revisión de migración. No guardar secretos en Git.

**Tecnologías:** Git, Markdown, OpenAPI y pipeline AWS existente.

El historial de decisiones técnicas vive en Git/ADR; los cambios de expedientes, en auditoría RDS; los errores, en CloudWatch. CloudTrail complementa las acciones AWS; los eventos de objetos S3 se habilitan explícitamente según necesidad y costo.

## 6 Base compartida si aún no está implementada

**Subtotal con todas las partidas pendientes: 78–176 h.** Se requiere evidencia de entrega para descontar partidas. Este escenario también supone un login funcional que adaptar; construirlo desde cero se cotiza en su propia épica.

| ID | Trabajo compartido | Tecnologías | Rango revisado |
|---|---|---|---:|
| BASE-01 | Infraestructura inicial y ambientes: red, servicios API/web/worker, base de datos, almacenamiento y secretos | CDK/CloudFormation, ECS Fargate, ECR, ALB, ACM, RDS, S3/KMS | 36–80 h |
| BASE-02 | Construcción, pipeline, migraciones y recuperación del despliegue | CodeBuild, CodePipeline y conexión al repositorio | 12–32 h |
| BASE-03 | Adaptación del login a roles Casabra y provisión de usuarios/permisos; sin consola administrativa completa | FastAPI, autenticación existente y RDS | 12–24 h |
| BASE-04 | Base de pruebas, fixtures, contenedores y reportes | pytest, Testcontainers, Vitest y Playwright | 12–24 h |
| BASE-05 | Grupos de logs, exportación de trazas, retención y canal operativo compartidos | CloudWatch, ADOT, SNS y CloudTrail | 6–16 h |
| **Total** | | | **78–176 h** |

No se repiten la integración del análisis documental, las políticas del módulo ni la instrumentación funcional: corresponden a BE-FI-06 y OPS-FI-01/02.

### Calibración de la base compartida

| ID | Rango en días | Modo | ×ref antes del factor M1 | Motivo |
|---|---:|---|---|---|
| BASE-01 | 4,5–10 d | M1 | H × 3–5; luego ×1,5–2 | Ambientes, red, RDS, contenedores y secretos desde una base pendiente. |
| BASE-02 | 1,5–4 d | M1 | H × 1–2; luego ×1,5–2 | Pipeline, migraciones y rollback no acreditados. |
| BASE-03 | 1,5–3 d | M1 | H × 1–1,5; luego ×1,5–2 | Adaptar autenticación existente y roles; no reconstruir login. |
| BASE-04 | 1,5–3 d | M1 | H × 1–1,5; luego ×1,5–2 | Crear infraestructura de pruebas sin patrón comprobado. |
| BASE-05 | 0,75–2 d | M1 | H × 0,5–1; luego ×1,5–2 | Base de logs/trazas/retención sin configuración acreditada. |

## 7 Estimación de complejidad

| Grupo | Complejidad | Motivo |
|---|---|---|
| Modelos, validación y ficha | M | Relaciones, documentos y acceso por expediente |
| Carga, análisis y reutilización | L | S3, versiones, asincronía y recuperación de fallos |
| Estados, ofertas y compra | L | Permisos distintos, concurrencia e historial consistente |
| Estudio de títulos | M | Registro estructurado, alertas y visibilidad por rol |
| Ruta y adecuaciones | S | Dos rutas y un indicador, condicionados a compra completada |
| Formularios y seguimiento | M | Integración por rol y manejo de errores |
| Observabilidad y validación transversal | M | Correlación, alarmas y comprobación entre servicios |

S/M/L expresan complejidad relativa, no una conversión automática a horas.

## 8 Condiciones de la cotización

| Escenario | Trabajo, sin contingencia | Contingencia condicionada | Rango total con contingencia de 0–8 h |
|---|---:|---:|---:|
| Módulo sobre base funcional | 259–548 h | 0–8 h | 259–556 h |
| Módulo más toda la base pendiente | 337–724 h | 0–8 h | 337–732 h |

La contingencia se suma **una vez**, no por tarea ni otra vez sobre la base compartida:
- **+0,5 d (4 h)** si el contrato del login entregado difiere del acordado y exige una adaptación acotada para integrar el módulo. Responsable de revisión: quien integre backend y autenticación.
- **+0,5 d (4 h)** si la integración real revela una discrepancia acotada entre el contrato de carga/eventos pactado y el servicio disponible. Responsable de revisión: quien integre archivos y AWS.

Los reintentos, eventos duplicados, pruebas y revisión ya incluidos en las tareas no consumen otra reserva. Si hay que reconstruir el login, cambiar arquitectura o ampliar alcance, corresponde reestimar, no asumir que 4 h lo cubren. Se retira la reserva genérica del 15–20 % de la versión anterior para no sumar el mismo riesgo encima de M1 y del rango.

Las referencias importadas no permiten elegir un punto central como si fuera una predicción validada. Las 356 h previas quedan dentro del nuevo intervalo; esto no demuestra ahorro ni que esa cifra sea un compromiso viable. Las mayores incertidumbres están en documentos privados/escaneo, plataforma compartida y requisitos pendientes.

El precio se calcula con horas por perfil × tarifa y los conceptos comerciales acordados. Consumo AWS y soporte posterior se cotizan aparte. Para calendario deben considerarse capacidad efectiva, dependencias y esperas, sin convertir estos días-persona en una fecha prometida.

La revisión conserva el alcance funcional y cambia el método de estimación. Recalibrar tras el primer flujo completo de documentos/propuesta con horas reales de implementación, validación y espera separadas. El intervalo no representa un percentil estadístico ni acredita que el software o la infraestructura ya estén implementados.
