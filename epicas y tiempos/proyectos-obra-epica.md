# Épica del módulo 6. Proyectos de obra

Cotización inicial de **HU-16 a HU-19** de las [historias del proyecto](../historias_de_usuario_plan_del_proyecto.md), según el [contexto del negocio](../contexto.md). Organizada por capas como la [épica del login](login-epica.md), sin trasladar sus ejemplos de otros negocios.

**Referencia funcional:** [criterios Gherkin propuestos](proyectos-obra-criterios-aceptacion.md). No se encontraron criterios aprobados específicos de obra; los supuestos y escenarios deben validarse antes de implementar. Las reglas de adquisición siguen los [criterios aprobados del módulo 2](adquisicion-inmuebles-criterios-aceptacion.md).

## Resumen de horas

| Capa | Rango |
|---|---:|
| Definición | 8–16 h |
| Backend | 111–236 h |
| Frontend | 51–108 h |
| Infraestructura incremental y observabilidad | 18–44 h |
| Validación transversal | 24–48 h |
| Entrega | 6–16 h |
| **Módulo sobre base funcional** | **218–468 h** |
| Base compartida, solo si está pendiente | 78–176 h |
| **Módulo con toda la base pendiente** | **296–644 h** |

**Unidad:** horas-persona; 1 d = 8 h como convención, no plazo de calendario. TDD, pruebas propias y revisión están incluidos en cada tarea funcional. QA corresponde a pruebas transversales en staging. Consumo AWS y esperas no forman parte del esfuerzo. No se identificó una estimación anterior del módulo 6.

## Método y evidencia

Se aplica [estimate-task local](../skills/estimate-task/SKILL.md) y sus [referencias](../skills/estimate-task/references/calibration.md). [Cálculo reproducible](../docs/estimaciones/modulo-6-estimacion.json) y [generador de esta épica](../docs/estimaciones/generar_modulo_6.py): `python docs/estimaciones/generar_modulo_6.py`.

**Confianza baja.** No existen horas reales de Casabra disponibles ni código de base comprobado. A1 (S9.2 / RED-3596, 0,5 d) es una referencia importada no verificada para conectar UI a endpoint, con errores y pruebas básicas: analogía parcial para estas pantallas. H (1 d) es una unidad de hipótesis técnica por entregables, no una medición histórica. Las estimaciones de otros módulos no se usan como tiempos reales.

**Fórmula por extremo:** `ceil(8 × días_referencia × unidades_base × factor_riesgo)`. Las unidades ×ref se indican antes del factor. M0 aplica ×1 a definición; M1 aplica ×1,5–2 una vez por dinero, permisos, migraciones o ausencia de patrón comprobado. No se vuelve a multiplicar el total ni se suma TDD otra vez. No se presume ahorro fijo por IA. Recalibrar con tiempos reales del primer flujo; los rangos no son percentiles estadísticos.

## Alcance confirmado y supuestos de cotización

| Historia | Resultado incluido |
|---|---|
| HU-16 | Proyecto con presupuesto, cronograma y responsables |
| HU-17 | Reporte semanal y fotos desde sitio |
| HU-18 | Archivos de licencias y permisos del proyecto |
| HU-19 | Tablero para identificar retrasos y sobrepresupuesto |

**Confirmado por contexto:** la compañía compra los inmuebles; las adecuaciones son posteriores a adquisición y no cambian la ruta Arriendo/Venta. El propietario original no dirige la obra del activo de la compañía. Finalizar obra no publica automáticamente el inmueble ni modifica su estado de adquisición.

**Supuestos que permiten cotizar:**

- Una compañía, un proyecto activo por inmueble Adquirido con ruta definida y adecuaciones indicadas; varios proyectos históricos son posibles. Se reutiliza el vínculo del módulo 2, no se construye adquisición en esta épica.
- Jefe de obra con acceso a proyectos asignados y gerente con consulta global. El jefe autorizado crea el proyecto y asigna responsables internos; se valida esa facultad en definición. HU-33 no enumera actualmente jefe de obra: se requiere incorporarlo a la matriz, sin asumir que ya está implementado. No se modifica esa historia como regla aprobada.
- Estados propuestos: Planificado → En ejecución → Finalizado; cancelación motivada desde Planificado/En ejecución. Inicio congela presupuesto y fechas base. Finalización requiere todas las actividades base al 100%. Sin reaperturas ni cambio de línea base; reprogramaciones operativas conservan comparación contra la original.
- Cronograma tabular con actividades, fechas y responsables, sin dependencias, ruta crítica ni Gantt interactivo. Avance por actividad entre 0 y 100%; global = promedio simple de actividades base. Cambios de cantidad de actividades tras inicio y ponderaciones especiales requieren reestimación.
- Un reporte vigente por semana con historial de correcciones. Sin reporte no se infiere avance cero; los datos previos muestran fecha. Fecha límite vencida y último avance conocido menor a 100% identifica atraso confirmado; sin avance conocido se muestra Avance sin confirmar. Al finalizar, puede conservarse señal de cierre tardío comparando fecha real contra fin base.
- Presupuesto por partidas y una moneda COP propuesta. Para HU-19 se añade registro manual operativo de gastos y anulaciones, porque no se definió una fuente de costo real. Sobrecosto = max(costo registrado − presupuesto base, 0); porcentaje solo si presupuesto > 0. Sin movimientos se muestra Sin costos registrados. No representa contabilidad conciliada, pagos o compromisos de compra.
- Fotos JPEG/PNG y documentos PDF como formatos iniciales propuestos; límites de tamaño/cantidad, retención y tratamiento de formatos de cámara como HEIC pendientes. Web adaptable a celular con conexión; no se incluye modo offline. Los adjuntos son privados, versionados y utilizables tras validación/análisis.
- FastAPI, Next.js, AWS, S3 y RDS PostgreSQL propuesto. TDD backend con pytest/HTTPX, componentes con Vitest/Testing Library y recorridos con Playwright. La cotización no obliga a versiones de librerías aún no seleccionadas.

**Pendientes:** aprobar estados, facultades del jefe, número de proyectos simultáneos, partidas/impuestos/redondeo, responsables, definición de semana y zona horaria (propuesta America/Bogota), reglas de corrección, porcentaje/ponderación de avance, fuente y completitud de gastos, fecha de corte de indicadores, volúmenes y límites de archivos. La licencia se archiva: no se comprueba su validez jurídica ni se determinan requisitos legales.

**Exclusiones:** compras/proveedores, inventarios de materiales, nómina, facturación, pagos, integración contable automática, firma electrónica, inspección legal, BIM/CAD, OCR/video, ubicación GPS, portales de contratistas, notificaciones externas, reportes al propietario y aplicaciones nativas. El módulo 10 podrá consumir los mismos IDs de gasto en una integración futura; no volver a cargar movimientos sin conciliación.

## Tabla de estimación por tarea

| ID | h | d | Modo | Referencia × unidades; riesgo | Motivo / verificación |
|---|---:|---:|---|---|---|
| AN-OB-01 | 8–16 | 1–2 | M0 | H × 1–2; ×1–1 | Cerrar reglas y contratos sin implementación. |
| BE-OB-01 | 15–32 | 1,875–4 | M1 | H × 1,25–2; ×1,5–2 | Relaciones nuevas, importes y migraciones. |
| BE-OB-02 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Dinero y fechas con validación de elegibilidad y línea base. |
| BE-OB-03 | 15–32 | 1,875–4 | M1 | H × 1,25–2; ×1,5–2 | Montos y correcciones trazables sin doble registro. |
| BE-OB-04 | 15–32 | 1,875–4 | M1 | H × 1,25–2; ×1,5–2 | Historial, porcentajes y cargas repetidas desde campo. |
| BE-OB-05 | 24–48 | 3–6 | M1 | H × 2–3; ×1,5–2 | Carga privada, validación, cuarentena y versiones sin patrón acreditado. |
| BE-OB-06 | 15–32 | 1,875–4 | M1 | H × 1,25–2; ×1,5–2 | Reglas de comparación con datos incompletos y divisiones por cero. |
| BE-OB-07 | 9–20 | 1,125–2,5 | M1 | H × 0,75–1,25; ×1,5–2 | Rol jefe de obra, aislamiento por proyecto y cambios monetarios. |
| FE-OB-01 | 15–32 | 1,875–4 | M1 | A1 × 2,5–4; ×1,5–2 | Analogía parcial A1: varias vistas con presupuesto y responsables. |
| FE-OB-02 | 15–32 | 1,875–4 | M1 | A1 × 2,5–4; ×1,5–2 | Formulario móvil, progreso de carga y errores de conectividad. |
| FE-OB-03 | 12–24 | 1,5–3 | M1 | A1 × 2–3; ×1,5–2 | Dos paneles reutilizan ficha y componente de archivos. |
| FE-OB-04 | 9–20 | 1,125–2,5 | M1 | A1 × 1,5–2,5; ×1,5–2 | Indicadores restringidos que deben distinguir ausencia de datos. |
| OPS-OB-01 | 12–28 | 1,5–3,5 | M1 | H × 1–1,75; ×1,5–2 | S3 privado, eventos y despliegue del motor de análisis. |
| OPS-OB-02 | 6–16 | 0,75–2 | M1 | H × 0,5–1; ×1,5–2 | Fallos de procesamiento y consultas sin exponer documentos. |
| QA-OB-01 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Validación de flujo real entre capas y roles. |
| QA-OB-02 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Integridad entre RDS, S3, análisis de archivos y tablero. |
| REL-OB-01 | 6–16 | 0,75–2 | M1 | H × 0,5–1; ×1,5–2 | Activación de migraciones, permisos y procesamiento. |

## 0 Definición — 8–16 h

### AN-OB-01 Definir planificación, costos y permisos — 8–16 h

**Fuente:** HU-16, HU-17, HU-18, HU-19. **Estimación:** M0 · H × 1–2; luego ×1–1. Cerrar reglas y contratos sin implementación.

- Definir partidas, actividades, responsables, avance semanal, definición de atraso y fuente de costo ejecutado.
- Acordar acceso por proyecto, estados propuestos, retención, límites de archivos y criterios Gherkin; registrar ADR y supuestos sin presentarlos como aprobaciones.

**Tecnologías:** Markdown, Gherkin, OpenAPI y ADR en Git.


## 1 Backend — 111–236 h

### BE-OB-01 Modelo de proyecto y migraciones — 15–32 h

**Fuente:** HU-16, HU-17, HU-18, HU-19. **Estimación:** M1 · H × 1,25–2; luego ×1,5–2. Relaciones nuevas, importes y migraciones.

- Modelar proyecto, vínculo a inmueble, responsables, partidas, cronograma, reportes, gastos operativos, archivos e historial; usar Decimal para dinero.
- Agregar índices, claves foráneas y restricción de un proyecto activo por inmueble como supuesto de cotización.
- TDD de integridad, unicidad y migración sobre datos previos; no duplicar modelos de adquisición ni usuarios.

**Tecnologías:** SQLAlchemy 2, Alembic, PostgreSQL en RDS, pytest y Testcontainers.

### BE-OB-02 Proyecto, presupuesto y cronograma base — 18–40 h

**Fuente:** HU-16. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Dinero y fechas con validación de elegibilidad y línea base.

- Proponer GET/POST /api/v1/obras y GET/PATCH /obras/{id}; verificar inmueble Adquirido, ruta definida y adecuaciones indicadas, sin modificar adquisición/ruta.
- Gestionar partidas con cantidad y costo unitario, actividades con inicio/fin y responsable interno; estados propuestos Planificado, En ejecución, Finalizado y Cancelado.
- Al iniciar, congelar presupuesto y fechas de referencia; actualizaciones operativas conservan la base. Validar fechas, importes no negativos, moneda única COP propuesta, responsables y conflictos de versión.
- TDD de redondeo, sumatoria, inicio inválido y doble creación; sin Gantt editable, ruta crítica, dependencias entre actividades ni rebaselining.
- Verificar cierre solo con actividades base al 100%, cancelación motivada y transiciones permitidas; conservar fecha real de cierre sin publicar el inmueble.

**Tecnologías:** FastAPI, Pydantic, SQLAlchemy, Decimal, pytest y HTTPX.

### BE-OB-03 Gastos operativos y comparación presupuestal — 15–32 h

**Fuente:** HU-19 (fuente necesaria de costo real, supuesto). **Estimación:** M1 · H × 1,25–2; luego ×1,5–2. Montos y correcciones trazables sin doble registro.

- Proponer GET/POST /api/v1/obras/{id}/gastos y anulación motivada; registrar partida, fecha, importe y descripción sin ejecutar pagos.
- Mantener identificador estable y clave de idempotencia; sumar gastos vigentes y conservar anulaciones auditadas. Son costos operativos declarados, no conciliados contablemente.
- TDD de reenvío, precisión, gasto anulado, partida ajena y concurrencia. No incluir facturación, compras, proveedores, nómina ni integración automática con módulo 10; definir contrato de IDs para futura integración.

**Tecnologías:** FastAPI, PostgreSQL, Decimal, pytest.

### BE-OB-04 Reportes semanales y avance por actividad — 15–32 h

**Fuente:** HU-17. **Estimación:** M1 · H × 1,25–2; luego ×1,5–2. Historial, porcentajes y cargas repetidas desde campo.

- Proponer GET/POST /api/v1/obras/{id}/avances; registrar semana, comentario y porcentaje acumulado por actividad, vinculando fotos habilitadas por BE-OB-05.
- Mantener una versión vigente por semana y conservar correcciones con autor/fecha; avance global propuesto = promedio simple de actividades de la línea base.
- TDD de límites 0–100, actividad ajena, semana duplicada y corrección concurrente. Sin reporte, mostrar Sin reporte; un dato anterior conserva su fecha, sin inventar avance actual.

**Tecnologías:** FastAPI, SQLAlchemy, Pydantic, pytest.

### BE-OB-05 Fotos y documentos privados de obra — 24–48 h

**Fuente:** HU-17, HU-18. **Estimación:** M1 · H × 2–3; luego ×1,5–2. Carga privada, validación, cuarentena y versiones sin patrón acreditado.

- Proponer solicitudes de carga, confirmación y descarga autorizada bajo /api/v1/obras/{id}/archivos; carga directa a S3 con URL temporal y límites acordados.
- Registrar tipo Foto, Licencia o Permiso, metadatos, versiones y vínculos a reporte/proyecto; reemplazar sin perder versión anterior. No validar suficiencia jurídica de licencias.
- Implementar validación de tamaño/tipo real, cuarentena y adaptador al motor de análisis de archivos: solo habilitar archivos aceptados. Contemplar reintentos y eventos duplicados.
- TDD de ID de proyecto ajeno, URL expirada, archivo rechazado, carga interrumpida y confirmación repetida. Sin OCR, video, edición de imágenes ni geolocalización.

**Tecnologías:** FastAPI, boto3, S3 privado, worker Python, pytest y dobles de almacenamiento/análisis.

### BE-OB-06 Indicadores de retraso y sobrecosto — 15–32 h

**Fuente:** HU-19. **Estimación:** M1 · H × 1,25–2; luego ×1,5–2. Reglas de comparación con datos incompletos y divisiones por cero.

- Proponer GET /api/v1/obras/indicadores con filtros por estado y responsable; usar cronograma base y gastos vigentes, sin duplicar importes por joins con fotos/reportes.
- Marcar actividad atrasada si su fin base ya pasó y su último avance conocido es menor a 100%; sin reporte marcar Avance sin confirmar, no asumir avance cero. Proyecto atrasado si tiene alguna actividad atrasada confirmada.
- Sobrecosto = máximo(costo registrado menos presupuesto base, 0); mostrar desviación porcentual solo si base mayor que cero. Sin gastos, mostrar Sin costos registrados, no gasto real cero.
- TDD de límite de fecha en zona acordada, presupuesto cero, gasto anulado, múltiples reportes y finalización tardía; sin proyección de costo final, valor ganado ni alertas externas.

**Tecnologías:** FastAPI, PostgreSQL, SQLAlchemy, datetime/zoneinfo, pytest.

### BE-OB-07 Permisos por proyecto y auditoría — 9–20 h

**Fuente:** HU-16, HU-17, HU-18, HU-19, HU-33 (dependencia transversal). **Estimación:** M1 · H × 0,75–1,25; luego ×1,5–2. Rol jefe de obra, aislamiento por proyecto y cambios monetarios.

- Extender política existente con jefe de obra asignado para operar y gerente para consulta global; permisos de crear proyecto y asignar responsables requieren decisión en AN-OB-01.
- Registrar auditoría atómica para cambios de presupuesto, fechas, avance, gasto y archivo; impedir acceso de propietario original/arrendatario a gestión interna.
- Probar matriz de roles/recurso y asignación no autorizada mediante política común. Sin crear login ni consola de administración; habilitación del rol jefe de obra se documenta como dependencia de HU-33.

**Tecnologías:** Dependencias FastAPI, RDS y pytest.


## 2 Frontend — 51–108 h

### FE-OB-01 Listado, ficha y planificación de obra — 15–32 h

**Fuente:** HU-16. **Estimación:** M1 · A1 × 2,5–4; luego ×1,5–2. Analogía parcial A1: varias vistas con presupuesto y responsables.

- Crear lista/ficha y formularios de proyecto, partidas y cronograma tabular con selector de inmueble elegible y usuarios autorizados.
- Mostrar presupuesto calculado, fechas base frente a actuales y confirmación de inicio; proteger acciones según permiso manteniendo autoridad del backend.
- TDD de validación, vacío/error, conflicto de edición y uso móvil/teclado; sin editor de Gantt ni app nativa.

**Tecnologías:** Next.js, TypeScript, React Hook Form, Zod, Vitest y Testing Library.

### FE-OB-02 Avance semanal con fotografías desde celular — 15–32 h

**Fuente:** HU-17. **Estimación:** M1 · A1 × 2,5–4; luego ×1,5–2. Formulario móvil, progreso de carga y errores de conectividad.

- Integrar reporte por semana, porcentajes por actividad y galería en ficha FE-OB-01; seleccionar fotos del dispositivo o cámara cuando el navegador lo permita.
- Mostrar carga/validación/rechazo y reintento por archivo sin duplicar reporte; conservar fecha y versión del avance.
- TDD de carga fallida, guardado repetido y porcentaje inválido. Uso conectado; sin modo offline, sincronización en segundo plano ni promesa de recuperación tras cerrar navegador.

**Tecnologías:** Next.js, API File del navegador, carga S3 temporal, Testing Library.

### FE-OB-03 Licencias, permisos y costos registrados — 12–24 h

**Fuente:** HU-18, HU-19 (registro manual supuesto). **Estimación:** M1 · A1 × 2–3; luego ×1,5–2. Dos paneles reutilizan ficha y componente de archivos.

- Reutilizar carga de FE-OB-02 para documentos con tipo, versión, estado de validación y descarga autorizada.
- Agregar tabla/formulario de gastos por partida y anulación motivada; distinguir presupuesto de costo registrado y de pago confirmado.
- TDD de archivo rechazado, enlace vencido, importe inválido y anulación visible. Sin emisión de licencias ni módulo contable.

**Tecnologías:** Next.js, TypeScript, Zod, Testing Library.

### FE-OB-04 Tablero gerencial de obra — 9–20 h

**Fuente:** HU-19. **Estimación:** M1 · A1 × 1,5–2,5; luego ×1,5–2. Indicadores restringidos que deben distinguir ausencia de datos.

- Construir tabla y resumen por proyecto con presupuesto, costo registrado, desviación, avance y atraso; filtrar por estado/responsable y navegar al detalle.
- Explicar base de cálculo y fecha del último reporte; distinguir Sin reporte, Sin costos registrados, cero y error.
- TDD de filtros, permiso gerencial y casos sin denominador; sin exportación PDF/Excel ni BI externo.

**Tecnologías:** Next.js, TypeScript, componentes accesibles y Testing Library.


## 3 Infraestructura incremental y observabilidad — 18–44 h

### OPS-OB-01 Almacenamiento y análisis de archivos — 12–28 h

**Fuente:** HU-17, HU-18. **Estimación:** M1 · H × 1–1,75; luego ×1,5–2. S3 privado, eventos y despliegue del motor de análisis.

- Configurar prefijos/permisos S3, CORS acotado, cifrado, eventos de cuarentena y recuperación de cargas huérfanas con retención acordada.
- Configurar motor de análisis propuesto ClamAV en worker y actualización de firmas, permisos mínimos y reintentos; verificar archivo limpio/rechazado en staging.
- Reutilizar base AWS existente. Si módulo 2 ya entrega motor de análisis, descontar trabajo común al consolidar; no instalar/cobrar un motor por módulo.

**Tecnologías:** S3/KMS, IAM, ECS/worker ClamAV, SQS, CDK/CloudFormation.

### OPS-OB-02 Observabilidad de archivos e indicadores — 6–16 h

**Fuente:** HU-17, HU-18, HU-19. **Estimación:** M1 · H × 0,5–1; luego ×1,5–2. Fallos de procesamiento y consultas sin exponer documentos.

- Extender logs, métricas y alarmas para cargas rechazadas/atascadas, fallos de análisis y latencia del tablero.
- Verificar alarmas de prueba y redacción de URLs temporales/datos personales; mantener auditoría de negocio en RDS separada de logs.

**Tecnologías:** CloudWatch, SNS y logs estructurados.


## 4 Validación transversal — 24–48 h

### QA-OB-01 Recorrido de obra y acceso desde móvil — 12–24 h

**Fuente:** HU-16, HU-17, HU-18, HU-19. **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Validación de flujo real entre capas y roles.

- Ejecutar Gherkin: inmueble elegible → proyecto/presupuesto → inicio → avance/fotos → permisos → costo → tablero.
- Comprobar uso móvil/teclado, conexión interrumpida y acceso denegado de otro jefe de obra/propietario; no duplicar pruebas unitarias de cada tarea.

**Tecnologías:** Playwright, staging y datos sintéticos.

### QA-OB-02 Conciliación de cifras y recuperación — 12–24 h

**Fuente:** HU-17, HU-18, HU-19. **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Integridad entre RDS, S3, análisis de archivos y tablero.

- Conciliar presupuesto/costo/avance con conjunto conocido, probar cortes de fecha y ausencia de multiplicación por documentos o reportes.
- Ensayar evento duplicado, caída del worker, acceso antes del análisis, aplicación de migración y recuperación con evidencias en staging.
- Revisar consultas y cargas con volumen/límites acordados; no incluye pentest externo ni certificación de rendimiento.

**Tecnologías:** pytest/HTTPX, PostgreSQL, S3 y CloudWatch en staging.


## 5 Entrega — 6–16 h

### REL-OB-01 Despliegue y aceptación operativa — 6–16 h

**Fuente:** HU-16, HU-17, HU-18, HU-19. **Estimación:** M1 · H × 0,5–1; luego ×1,5–2. Activación de migraciones, permisos y procesamiento.

- Desplegar mediante pipeline existente y verificar ficha, carga privada y tablero antes de habilitar operación.
- Entregar OpenAPI, ADR, guía de jefe de obra/gerente, evidencias Gherkin y procedimiento de recuperación; separar espera de aceptación de horas-persona.

**Tecnologías:** Git, OpenAPI, pipeline AWS y Markdown.

## 6 Dependencias y base compartida

El escenario principal presupone login funcional, roles, API/web, RDS/S3, worker, pipeline y herramientas de pruebas. La documentación no acredita su implementación. Si faltan, sumar una sola vez [BASE-01 a BASE-05 del módulo 2](ficha-inmueble-epica.md#6-base-compartida-si-aún-no-está-implementada): **78–176 h**. BASE-03 adapta autenticación existente; construir login desde cero exige estimación independiente, sin acumular ambas variantes.

El contrato de elegibilidad de inmuebles debe provenir del módulo 2; BE-OB-02 cubre su consumo, no construir todo ese módulo. Si adquisición no está disponible, su desarrollo y esperas se presupuestan aparte. No se requiere que contabilidad esté implementada para el supuesto de gasto manual.

**Archivos compartidos:** BE-OB-05 incluye el flujo de obra y adaptador de análisis; OPS-OB-01 incluye desplegar/configurar el motor si no está disponible. No se ha descontado una reutilización no verificada. Si módulo 2 ya entrega carga privada, validación, escaneo y versiones, revisar esas dos partidas contra evidencia y cobrar únicamente adaptaciones. En una cotización conjunta, asignar una sola vez la creación del motor común; no sumar íntegramente ambas implementaciones. Las cifras aquí son del módulo aislado sobre base técnica, no un total consolidado de producto.

Secuencia: definir reglas → modelo/permisos → planificación y presupuesto → avance/archivos/gastos → tablero → validación → entrega. Frontend puede avanzar con contratos acordados. Capacidad y dependencias determinan el calendario; días-persona no equivalen a fechas.

## 7 Complejidad

| Grupo | S/M/L | Motivo |
|---|---|---|
| Proyecto, presupuesto y cronograma | L | Línea base, dinero y reglas de cambio |
| Avance y gastos | M | Historial, idempotencia y correcciones |
| Fotos, licencias y permisos | L | Conectividad, archivos privados y procesamiento asíncrono |
| Tablero gerencial | M | Integridad de agregados y datos incompletos |
| Operación y entrega | M | Recuperación entre RDS, S3 y worker |

S/M/L expresa complejidad relativa; no se convierte automáticamente a horas.

## 8 Contingencias y costos externos

- **Reserva condicionada:** 0–4 h, fuera del total base, solo ante ajuste acotado de identificadores/campos de elegibilidad del contrato entregado por módulo 2. Dueño: responsable de integración. Totales bajo esa condición: **218–472 h** sobre base funcional o **296–648 h** con toda la base pendiente. No cubre construir adquisición, cambiar fuente de gastos o introducir offline; esos cambios se reestiman. No añadir reserva porcentual por el riesgo ya tratado con M1.
- **Consumo AWS separado:** almacenamiento, versiones, solicitudes y transferencia S3; RDS; cómputo API/web/worker y análisis de archivos; SQS; KMS y CloudWatch. Costos monetarios pendientes de región, tamaño/cantidad de fotos, concurrencia, retención y tráfico. No se inventan precios ni se cobra infraestructura completa por cada módulo.
- **Entrega y confianza:** aprobar supuestos/Gherkin antes de implementar, conservar ADR y evidencias, registrar horas reales para recalibrar. Esperas por permisos, decisiones y aceptación se separan. Esta entrega es documentación de cotización; no implementa la aplicación de obra.
