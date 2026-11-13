# Épica del módulo 5. CRM

Cotización inicial de **HU-12 a HU-15**, según las [historias del proyecto](../historias_de_usuario_plan_del_proyecto.md) y el [contexto del negocio](../contexto.md). Cubre seguimiento de propietarios y oportunidades de adquisición. El CRM de venta de activos de la compañía (HU-43 a HU-45 y HU-50) se estima en el módulo 9.

**Referencia funcional:** [criterios Gherkin propuestos](crm-criterios-aceptacion.md). No se encontraron criterios aprobados específicos para CRM: los escenarios y supuestos aquí documentados están pendientes de validación.

## Resumen de horas

| Capa | Rango |
|---|---:|
| Definición | 8–12 h |
| Backend | 96–208 h |
| Frontend | 45–100 h |
| Infraestructura incremental y observabilidad | 15–40 h |
| Validación transversal | 21–44 h |
| Entrega | 6–16 h |
| **Módulo sobre base funcional** | **191–420 h** |
| Base compartida, solo si está pendiente | 78–176 h |
| **Módulo con toda la base pendiente** | **269–596 h** |

Horas-persona; **1 d = 8 h** como convención, no plazo de calendario. TDD, pruebas propias y revisión están dentro de cada tarea funcional. QA cubre recorridos entre capas y operación real, sin repetir esas pruebas. Consumo AWS, esperas y módulos dependientes se separan.

## Método y evidencia

Se aplica la [skill local estimate-task](../skills/estimate-task/SKILL.md) y sus [referencias de calibración](../skills/estimate-task/references/calibration.md). [Datos y cálculo reproducible](../docs/estimaciones/modulo-5-estimacion.json); [generador](../docs/estimaciones/generar_modulo_5.py). Ejecutar `python docs/estimaciones/generar_modulo_5.py` desde el repositorio.

**Confianza baja:** no hay horas reales de Casabra ni implementación comprobada de la base. A1 (S9.2 / RED-3596, 0,5 d) es una referencia importada no verificada para conectar una UI a un endpoint, con errores y pruebas. Su uso es una analogía parcial: aquí hay varias vistas y datos personales. H (1 d) es únicamente una unidad de hipótesis técnica por entregables; no es un tiempo medido. No se identificó una estimación anterior del módulo 5 que comparar.

**Fórmula por extremo:** `ceil(8 × días_referencia × unidades_base × factor_riesgo)`. Las unidades ×ref se expresan antes del riesgo. M0 usa ×1; M1 usa ×1,5–2 una sola vez por permisos, datos personales, migraciones o falta de patrón comprobado. No aplicar el factor de nuevo al total ni agregar un descuento fijo por IA. Recalibrar tras el primer recorrido completo con horas reales; los rangos no son percentiles estadísticos.

## Alcance, supuestos y pendientes

- **Confirmado por HU-12 a HU-15:** ficha del cliente con etapa, llamadas/visitas/compromisos compartidos, recordatorios de seguimiento y tablero de clientes por etapa e inmuebles captados para gerente.
- **Supuesto de cotización:** una compañía y equipo comercial autorizado con historial compartido; asesor consulta y registra, gerente consulta tablero. Propietario original y arrendatario no acceden a notas internas. Segmentación por sucursal/cartera y administración completa de permisos quedan pendientes, no incluidas.
- **Supuesto:** clientes existentes del onboarding, sin nueva captación, importación masiva ni deduplicación avanzada. Vínculos a inmuebles/solicitudes del módulo 2, sin copiar documentos o crear otro expediente. Una ficha de cliente puede vincular varias solicitudes.
- **Etapas propuestas:** Contactado, En evaluación y Contrato firmado, tomadas de HU-12; catálogo fijo y registro manual trazable para cotizar. Falta definir etapa inicial, transiciones, significado del contrato y quién puede registrarlo. Contrato firmado no significa Adquirido ni cambia estados del inmueble. Firma y sincronización automática pertenecen al módulo 7 y no están incluidas.
- **Supuesto HU-14:** tareas con responsable, vencimiento y estados Pendiente, Completada o Cancelada; recordatorio dentro de la app al vencimiento, bandeja persistente y marca de leído. Frecuencia técnica propuesta de revisión de cinco minutos, sin SLA contratado; sin correo, WhatsApp, SMS, push ni calendarios externos. Reprogramación invalida el recordatorio anterior y permite uno por nueva versión del vencimiento.
- **Supuesto HU-15:** clientes distintos por etapa actual y captados = inmuebles distintos presentados a evaluación en el período, no comprados. Clientes se filtran por fecha de alta; captados por fecha de primera presentación. No hay histórico de embudo, conversiones o rendimiento individual. Esta definición de captado requiere confirmación del gerente; adquiridos sigue siendo otra métrica.
- **Pendientes antes de implementar:** visibilidad y permisos definitivos, responsable inicial, campos obligatorios, edición/corrección de notas, zona horaria de negocio (propuesta America/Bogota), tolerancia de recordatorios, período/filtros de indicadores, volumen, retención y significado de etapas. Se cotiza historial append-only y correcciones mediante nueva entrada; sin borrado de notas.
- **Tecnologías:** FastAPI, SQLAlchemy, Pydantic, RDS PostgreSQL propuesto y Next.js adaptable a celular. No se necesitan adjuntos propios del CRM: documentos/imágenes siguen en S3 bajo el módulo 2. No se cotiza app nativa, grabación de llamadas, BI externo ni integración con CRM de terceros.

## Tabla de estimación por tarea

| ID | h | d | Modo | Referencia × unidades; riesgo | Motivo / verificación |
|---|---:|---:|---|---|---|
| AN-CRM-01 | 8–12 | 1–1,5 | M0 | H × 1–1,5; ×1–1 | Decisiones y contrato funcional; sin implementación. |
| BE-CRM-01 | 15–32 | 1,875–4 | M1 | H × 1,25–2; ×1,5–2 | Esquema nuevo con datos personales, integridad y migraciones. |
| BE-CRM-02 | 15–32 | 1,875–4 | M1 | H × 1,25–2; ×1,5–2 | Consulta y actualización de PII con control de concurrencia. |
| BE-CRM-03 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Información personal compartida y registro atribuible. |
| BE-CRM-04 | 15–32 | 1,875–4 | M1 | H × 1,25–2; ×1,5–2 | Responsables, fechas y cambios concurrentes afectan recordatorios. |
| BE-CRM-05 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Proceso nuevo con reintentos, deduplicación y carreras. |
| BE-CRM-06 | 12–28 | 1,5–3,5 | M1 | H × 1–1,75; ×1,5–2 | Conteos y filtros sobre relaciones múltiples requieren conciliación. |
| BE-CRM-07 | 9–20 | 1,125–2,5 | M1 | H × 0,75–1,25; ×1,5–2 | Adaptar autorización compartida y auditar acciones sensibles. |
| FE-CRM-01 | 12–28 | 1,5–3,5 | M1 | A1 × 2–3,5; ×1,5–2 | Analogía parcial A1: lista y detalle con PII y edición de etapa. |
| FE-CRM-02 | 9–20 | 1,125–2,5 | M1 | A1 × 1,5–2,5; ×1,5–2 | Formulario y timeline con autoría y errores de envío. |
| FE-CRM-03 | 15–32 | 1,875–4 | M1 | A1 × 2,5–4; ×1,5–2 | Vistas y formularios relacionados con responsable y vencimiento. |
| FE-CRM-04 | 9–20 | 1,125–2,5 | M1 | A1 × 1,5–2,5; ×1,5–2 | Indicadores restringidos y explicación del universo contado. |
| OPS-CRM-01 | 9–24 | 1,125–3 | M1 | H × 0,75–1,5; ×1,5–2 | Disparo AWS e identidad del worker aún sin patrón comprobado. |
| OPS-CRM-02 | 6–16 | 0,75–2 | M1 | H × 0,5–1; ×1,5–2 | Detección de fallos y rezago sin filtrar datos personales. |
| QA-CRM-01 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Validación transversal de roles, persistencia y móvil. |
| QA-CRM-02 | 9–20 | 1,125–2,5 | M1 | H × 0,75–1,25; ×1,5–2 | Validar scheduler real, consultas y migración entre componentes. |
| REL-CRM-01 | 6–16 | 0,75–2 | M1 | H × 0,5–1; ×1,5–2 | Activación coordinada del esquema y trabajo programado. |

## 0 Definición — 8–12 h

### AN-CRM-01 Acordar etapas, permisos e indicadores — 8–12 h

**Fuente:** HU-12, HU-13, HU-14, HU-15. **Estimación:** M0 · H × 1–1,5; luego ×1–1. Decisiones y contrato funcional; sin implementación.

- Mapear campos, etapas y relaciones cliente/solicitud/inmueble; cerrar captados y filtros sin confundir adquisición con contrato firmado.
- Definir responsables, visibilidad, política de recordatorios y criterios Gherkin; registrar pendientes y ADR, sin motor configurable de procesos.

**Tecnologías:** Markdown, Gherkin, OpenAPI y ADR en Git.


## 1 Backend — 96–208 h

### BE-CRM-01 Modelos, relaciones y migraciones — 15–32 h

**Fuente:** HU-12, HU-13, HU-14, HU-15. **Estimación:** M1 · H × 1,25–2; luego ×1,5–2. Esquema nuevo con datos personales, integridad y migraciones.

- Modelar ficha CRM vinculada a cliente existente, historial de etapas, actividades, compromisos y recordatorios con claves e índices.
- Mantener referencias a solicitudes/inmuebles existentes, sin duplicar expediente ni el estado de adquisición.
- Probar migración con datos previos, unicidad de ficha, integridad referencial y restricciones de vencimiento/versión; sin migración masiva de un CRM externo.

**Tecnologías:** SQLAlchemy 2, Alembic, RDS PostgreSQL, pytest y Testcontainers.

### BE-CRM-02 Ficha, búsqueda y etapas del cliente — 15–32 h

**Fuente:** HU-12. **Estimación:** M1 · H × 1,25–2; luego ×1,5–2. Consulta y actualización de PII con control de concurrencia.

- Proponer GET /api/v1/crm/clientes y /clientes/{id}, con paginación, búsqueda, etapa y próximos seguimientos; PATCH /clientes/{id}/etapa con versión esperada.
- Vincular clientes del onboarding e inmuebles del módulo 2; registrar estado anterior/nuevo, fecha y actor sin modificar adquisición.
- TDD de cliente inexistente, búsqueda sin resultados, actualización simultánea y cambio de etapa trazable. No crear un CRUD alternativo de propietarios.

**Tecnologías:** FastAPI, Pydantic, SQLAlchemy, pytest y HTTPX.

### BE-CRM-03 Historial de llamadas, visitas y notas — 12–24 h

**Fuente:** HU-13. **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Información personal compartida y registro atribuible.

- Proponer GET/POST /api/v1/crm/clientes/{id}/actividades para llamadas, visitas y notas, con fecha del contacto, resultado y autor.
- Ordenar y paginar el historial; registrar correcciones como nueva entrada vinculada, sin borrado ni grabaciones/adjuntos.
- Reutilizar vínculos de BE-CRM-01; TDD de orden estable, contenido inválido, autor no falsificable y reenvío idempotente.

**Tecnologías:** FastAPI, Pydantic, PostgreSQL, pytest.

### BE-CRM-04 Compromisos y agenda de seguimiento — 15–32 h

**Fuente:** HU-13, HU-14. **Estimación:** M1 · H × 1,25–2; luego ×1,5–2. Responsables, fechas y cambios concurrentes afectan recordatorios.

- Proponer GET/POST /api/v1/crm/tareas y PATCH /tareas/{id}; asignar a miembro autorizado, completar, cancelar y reprogramar con historial.
- Consultar pendientes de hoy, próximos y vencidos; guardar UTC y presentar zona acordada, distinguiendo fecha vencida de completada.
- TDD de responsable inválido, conversión horaria, tarea completada/cancelada y conflicto de versión. Sin recurrencia ni sincronización de calendario.

**Tecnologías:** FastAPI, SQLAlchemy, datetime/zoneinfo, pytest.

### BE-CRM-05 Generación y bandeja de recordatorios — 18–40 h

**Fuente:** HU-14. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Proceso nuevo con reintentos, deduplicación y carreras.

- Implementar trabajo periódico que persista recordatorios por tarea/versión del vencimiento y destinatario; procesar lotes recuperables con restricción única.
- Revalidar responsable y estado al generar; invalidar avisos al cancelar/completar/reprogramar, incluyendo carreras con el worker.
- Proponer GET /api/v1/crm/recordatorios y PATCH /recordatorios/{id}/lectura; TDD de corrida duplicada, recuperación tras interrupción y acceso ajeno. Solo bandeja in-app; sin entrega externa.

**Tecnologías:** Worker Python, PostgreSQL, FastAPI, pytest; disparo AWS en OPS-CRM-01.

### BE-CRM-06 Indicadores gerenciales — 12–28 h

**Fuente:** HU-15. **Estimación:** M1 · H × 1–1,75; luego ×1,5–2. Conteos y filtros sobre relaciones múltiples requieren conciliación.

- Proponer GET /api/v1/crm/indicadores con clientes por etapa actual y conteo distinto de inmuebles presentados en período.
- Aplicar definiciones de fechas y captados acordadas; evitar multiplicar conteos por contactos, tareas o propietarios vinculados.
- TDD de un cliente con varios inmuebles, múltiples actividades, extremos del período y cero resultados; sin series históricas ni reportes financieros.

**Tecnologías:** SQLAlchemy, PostgreSQL, FastAPI, pytest.

### BE-CRM-07 Permisos y auditoría del módulo — 9–20 h

**Fuente:** HU-12, HU-13, HU-14, HU-15, HU-33 (dependencia transversal). **Estimación:** M1 · H × 0,75–1,25; luego ×1,5–2. Adaptar autorización compartida y auditar acciones sensibles.

- Integrar identidad/roles existentes: equipo autorizado para ficha e historial, gerente para indicadores y destinatario para avisos.
- Añadir política común por recurso y eventos auditables de cambios, excluyendo notas/PII de logs; proteger consultas y mutaciones frente a IDs ajenos.
- Verificar matriz de autorización y transacción atómica dato/auditoría con pruebas de política; las unitarias funcionales quedan en BE-CRM-02 a 06. Sin construir login o consola de permisos.

**Tecnologías:** Dependencias FastAPI, RDS, pytest.


## 2 Frontend — 45–100 h

### FE-CRM-01 Listado y ficha comercial adaptable — 12–28 h

**Fuente:** HU-12. **Estimación:** M1 · A1 × 2–3,5; luego ×1,5–2. Analogía parcial A1: lista y detalle con PII y edición de etapa.

- Construir listado con búsqueda, filtro de etapa, paginación y ficha enlazada a solicitudes/inmuebles autorizados.
- Mostrar etapa comercial separada de adquisición; permitir cambio autorizado con respuesta a conflicto de versión.
- TDD de carga, vacío, error, sesión vencida y navegación móvil/teclado; integrar API BE-CRM-02 sin rehacer expediente.

**Tecnologías:** Next.js, TypeScript, componentes accesibles, Vitest y Testing Library.

### FE-CRM-02 Historial y registro de interacciones — 9–20 h

**Fuente:** HU-13. **Estimación:** M1 · A1 × 1,5–2,5; luego ×1,5–2. Formulario y timeline con autoría y errores de envío.

- Integrar historial paginado de BE-CRM-03 en la ficha FE-CRM-01; formulario de llamada/visita/nota y corrección vinculada.
- Mostrar fecha y autor; conservar borrador ante error sin persistencia sensible en almacenamiento local.
- TDD de validación, doble clic, error y corrección visible; sin edición silenciosa de entradas previas.

**Tecnologías:** Next.js, React Hook Form, Zod, Testing Library.

### FE-CRM-03 Agenda, compromisos y avisos — 15–32 h

**Fuente:** HU-13, HU-14. **Estimación:** M1 · A1 × 2,5–4; luego ×1,5–2. Vistas y formularios relacionados con responsable y vencimiento.

- Crear lista de pendientes/hoy/vencidos y formularios de asignación, reprogramación, cierre y cancelación, reutilizando la ficha y cliente HTTP.
- Añadir bandeja de avisos persistente con indicador de no leídos y actualización periódica mientras la app esté abierta; no WebSocket ni push.
- TDD de presentación horaria, filtros, aviso invalidado y conflicto al completar; mantener autoridad del backend.

**Tecnologías:** Next.js, TypeScript, Zod, Testing Library.

### FE-CRM-04 Tablero gerencial — 9–20 h

**Fuente:** HU-15. **Estimación:** M1 · A1 × 1,5–2,5; luego ×1,5–2. Indicadores restringidos y explicación del universo contado.

- Mostrar clientes por etapa e inmuebles captados, selector de período y definición visible de cada indicador, consumiendo BE-CRM-06.
- Presentar tabla/gráfico accesible, vacío y error sin mostrarlos como cero; ocultar acceso según permiso sin depender solo del frontend.
- TDD de actualización de filtros y datos, acceso denegado y vista móvil; sin exportación Excel/PDF ni constructor de reportes.

**Tecnologías:** Next.js, TypeScript, componentes gráficos accesibles, Testing Library.


## 3 Infraestructura incremental y observabilidad — 15–40 h

### OPS-CRM-01 Ejecución programada de seguimientos — 9–24 h

**Fuente:** HU-14. **Estimación:** M1 · H × 0,75–1,5; luego ×1,5–2. Disparo AWS e identidad del worker aún sin patrón comprobado.

- Configurar disparo periódico con EventBridge Scheduler hacia tarea ECS, IAM mínimo y parámetros por ambiente, reutilizando base compartida.
- Configurar reintentos de invocación y manejo de fallos; probar invocación autorizada y recuperación en staging. La idempotencia de negocio está en BE-CRM-05.
- Sin crear una plataforma genérica de automatizaciones; cuantificar después el consumo según frecuencia y volumen.

**Tecnologías:** AWS EventBridge Scheduler, ECS, IAM, CDK/CloudFormation.

### OPS-CRM-02 Trazas y alertas operativas — 6–16 h

**Fuente:** HU-14, HU-15. **Estimación:** M1 · H × 0,5–1; luego ×1,5–2. Detección de fallos y rezago sin filtrar datos personales.

- Añadir métricas de última corrida exitosa, tareas pendientes de avisar, fallos y latencia de indicadores sobre base de observabilidad existente.
- Crear alarmas operativas y comprobar disparo de prueba; redactar PII y notas en logs. Auditoría de negocio se conserva en RDS.

**Tecnologías:** CloudWatch, SNS, logs estructurados.


## 4 Validación transversal — 21–44 h

### QA-CRM-01 Recorrido comercial y matriz de acceso — 12–24 h

**Fuente:** HU-12, HU-13, HU-14, HU-15. **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Validación transversal de roles, persistencia y móvil.

- Ejecutar Gherkin extremo a extremo con asesor, compañero, gerente y propietario: contacto → compromiso → aviso → cierre y tablero.
- Verificar navegación móvil/teclado y denegación de acceso desde navegador/API real con datos sintéticos. No repetir las unitarias de cada componente.

**Tecnologías:** Playwright, staging, fixtures sintéticas.

### QA-CRM-02 Recuperación e integridad en staging — 9–20 h

**Fuente:** HU-12, HU-14, HU-15. **Estimación:** M1 · H × 0,75–1,25; luego ×1,5–2. Validar scheduler real, consultas y migración entre componentes.

- Interrumpir una ejecución controlada y recuperar; comprobar ausencia de avisos duplicados o de tareas canceladas usando scheduler y worker reales.
- Conciliar tablero con conjunto conocido de clientes/inmuebles y revisar consultas con volumen acordado; ensayar migración/recuperación sin pérdida de historial.
- Conservar evidencias y umbrales acordados; no es certificación de carga ni pentest externo.

**Tecnologías:** pytest/HTTPX, staging AWS, PostgreSQL, CloudWatch.


## 5 Entrega — 6–16 h

### REL-CRM-01 Despliegue, documentación y aceptación — 6–16 h

**Fuente:** HU-12, HU-13, HU-14, HU-15. **Estimación:** M1 · H × 0,5–1; luego ×1,5–2. Activación coordinada del esquema y trabajo programado.

- Desplegar por pipeline existente, ejecutar smoke de ficha/agenda/tablero y verificar alarmas y migraciones antes de habilitar el scheduler.
- Documentar API, ADR, definiciones de métricas y procedimiento de recuperación; entregar guía breve al asesor/gerente y evidencia Gherkin.
- Separar esperas de aprobación de horas-persona; no construir pipeline nuevo en esta partida.

**Tecnologías:** Git, OpenAPI, pipeline AWS y Markdown.

## 6 Base compartida y dependencias

Se presupone autenticación funcional, roles internos, API/web, RDS, despliegue y herramientas de pruebas. La documentación no demuestra que existan. Si están pendientes, aplicar una sola vez las partidas [BASE-01 a BASE-05 del módulo 2](ficha-inmueble-epica.md#6-base-compartida-si-aún-no-está-implementada): **78–176 h**; el JSON conserva los importes. BASE-03 adapta un login existente: construirlo desde cero requiere estimación separada, sin acumular ambas variantes. No cobrar esta base de nuevo si ya se contrató en otro módulo.

Los modelos/contratos de clientes e inmuebles de los módulos 1 y 2 deben estar disponibles. BE-CRM-02 incluye consumirlos y adaptar el vínculo, no construir onboarding o adquisición. Si faltan, sumar las épicas correspondientes sin duplicar la base. Orden sugerido: definición → modelo/permisos → ficha e historial → tareas/recordatorios → tablero → validación y entrega. FE puede avanzar con el contrato API acordado; eso no transforma horas-persona en plazo por simple división.

## 7 Complejidad

| Grupo | S/M/L | Motivo |
|---|---|---|
| Definición de etapas e indicadores | M | Semántica de cliente frente a inmueble y permisos |
| Modelo, ficha y contactos | M | Relaciones, datos personales y trazabilidad |
| Compromisos y recordatorios | L | Vencimientos, concurrencia, reintentos y cancelación |
| Tablero | M | Conteos distintos y filtros consistentes |
| Infraestructura y validación | M | Ejecución programada, alarmas y recorridos entre capas |

Complejidad relativa, independiente de las horas y sin equivalencia automática S/M/L → días.

## 8 Contingencias, consumo y entrega

- **Contingencia no incluida en el total base:** 0–4 h, únicamente si el contrato entregado por módulos 1/2 requiere una corrección acotada de identificadores o paginación para integrar CRM. Dueño: responsable de integración. Totales con esa condición: **191–424 h** sobre base funcional o **269–600 h** con toda la base pendiente. No usarla para cubrir módulos ausentes, nuevas reglas, canales externos o el riesgo ya incluido en M1.
- **Consumo AWS separado y sin precio inventado:** incremento en cómputo del API/worker, consultas/almacenamiento RDS, ejecución programada EventBridge Scheduler y logs/alarmas CloudWatch. No se cotiza un segundo RDS ni infraestructura completa por módulo. El costo monetario requiere región, volumen de clientes/tareas, retención y dimensionamiento; licencias y mensajes externos quedan fuera.
- **Aceptación:** validar los supuestos y Gherkin propuestos, registrar decisiones en ADR, ejecutar pruebas sobre staging y conservar evidencias. Esperas de acceso y aprobación se registran aparte. Esta entrega es documentación de cotización, no implementación del CRM.
