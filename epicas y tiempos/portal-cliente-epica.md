# Épica del módulo 11. Portal del cliente

Cotización inicial de **HU-30 a HU-32** de las [historias del proyecto](../historias_de_usuario_plan_del_proyecto.md), según el [contexto del negocio](../contexto.md), con el formato por capas de la [épica del login](login-epica.md). Incluye portal del propietario original, publicación controlada/notificaciones y reportes gerenciales; mantiene separados sus permisos.

**Referencia funcional:** [criterios Gherkin propuestos](portal-cliente-criterios-aceptacion.md). No se encontraron criterios aprobados específicos ni una estimación anterior de este módulo; escenarios y límites son propuestas de cotización pendientes de validar. El seguimiento de adquisición conserva los [criterios aprobados del módulo 2](adquisicion-inmuebles-criterios-aceptacion.md).

## Resumen de horas

| Capa | Rango |
|---|---:|
| Definición | 8–16 h |
| Backend | 126–272 h |
| Frontend | 48–100 h |
| Infraestructura incremental y observabilidad | 18–40 h |
| Validación transversal | 27–56 h |
| Entrega | 6–16 h |
| **Módulo con base y fuentes funcionales** | **233–500 h** |
| Base técnica compartida, solo si está pendiente | 78–176 h |
| **Módulo más toda la base técnica pendiente** | **311–676 h** |

**Ambos escenarios excluyen construir los módulos fuente.** Se requieren identidad, vínculos/documentos de adquisición, datos de obra/contratos, ocupación y resultados financieros. La base técnica no entrega contabilidad ni rentabilidad. El [módulo 10 ya tiene estimación](pagos-utilidades-epica.md); HU-32 sigue condicionada a su contrato de datos y disponibilidad real, no a la mera existencia de esa documentación.

Horas-persona; **1 d = 8 h** como convención, no calendario. TDD, pruebas propias y revisión forman parte de cada tarea funcional. QA cubre recorridos, conciliación y recuperación entre componentes, sin repetir unitarias. Consumo AWS, servicios y esperas se separan.

## Método y evidencia

Se aplica [estimate-task local](../skills/estimate-task/SKILL.md) y sus [referencias](../skills/estimate-task/references/calibration.md). [Cálculo reproducible](../docs/estimaciones/modulo-11-estimacion.json) y [generador](../docs/estimaciones/generar_modulo_11.py): `python docs/estimaciones/generar_modulo_11.py`.

**Confianza baja:** no hay horas reales Casabra ni interfaces fuente implementadas comprobadas. A1 (S9.2 / RED-3596, 0,5 d) es referencia importada no verificada de conexión UI a endpoint con errores/pruebas; analogía parcial para las varias vistas con permisos de este módulo. H (1 d) es unidad de hipótesis técnica por entregables, no medición. No se usan estimaciones anteriores como productividad observada.

**Fórmula por extremo:** `ceil(8 × días_referencia × unidades_base × factor_riesgo)`. ×ref se expresa antes del riesgo. M0 usa ×1 para definición; M1 usa ×1,5–2 una sola vez por PII, permisos, importes, migraciones o ausencia de patrón probado. No volver a aplicar el factor al total ni duplicar TDD/revisión; no se presume descuento fijo por IA. Recalibrar con horas reales del primer recorrido; rangos sin significado de percentil estadístico.

## Alcance confirmado y separación de audiencias

| Historia | Actor | Resultado incluido |
|---|---|---|
| HU-30 | Propietario original | Avance de obra, documentos propios accesibles y resultados que la compañía autorice compartir |
| HU-31 | Propietario original | Avisos de hitos de su operación autorizados para compartir |
| HU-32 | Gerente | Reportes consolidados de ingresos, ocupación y rentabilidad |

**Confirmado por contexto:** el inmueble adquirido pertenece a la compañía. Ser propietario original no habilita acceso a su gestión interna posterior, candidatos, arrendatarios, compradores o resultados gerenciales. El portal de pagos/contrato/cartera del arrendatario corresponde a HU-51 a HU-54 del módulo 8 y no se reconstruye aquí. HU-32 se conserva en este módulo porque así aparece en las historias, con acceso exclusivo de gerente.

### Supuestos de cotización

- Una compañía, propietario principal vinculado a su cuenta/operaciones existentes y gerente interno. Una persona puede consultar varias operaciones propias; sin copropietarios delegados, representación de terceros o nuevo onboarding. Autenticación/recuperación de cuenta y asignación general de roles son compartidas.
- Publicación explícita por operador interno autorizado, propuesto administrador: elige operación, destinatario, resumen y referencias/versiones de fotos/documentos/resultados. Denegación por defecto y una aprobación por versión; no aprobación multinivel ni reglas automáticas extensibles.
- Datos propios ya accesibles en módulo 2 conservan su autorización fuente; información de obra y resultados posteriores exige selección/aprobación expresa. La aprobación no otorga al propietario acceso al expediente completo ni a las fuentes internas.
- Resúmenes y selección de fotos/documentos con snapshot de versión aprobada. No se publican cambios posteriores del origen automáticamente. Fuente retirada/inaccesible o permiso revocado bloquean nuevas consultas; correcciones requieren revisión. Retención/historial por acordar, sin borrar auditoría de lo compartido.
- Descarga a través de endpoint autenticado con comprobación actual de acceso y respuestas privadas sin caché pública. No se entrega enlace persistente S3 al propietario. Revocar bloquea nuevas solicitudes; no recupera contenido ya descargado, ni bytes ya entregados en una descarga en curso.
- Portal web adaptable a celular, consulta de avances/fecha, galería de fotos aprobadas, documentos y resultados compartidos. Sin edición del expediente desde el portal, carga nueva, chat, tickets, firma nueva, pagos, extractos bancarios ni app nativa/offline.
- Hitos inicialmente limitados a formalización y pago de adquisición, más publicación/corrección de contenido compartido cuando se acuerde. Deben proceder de una fuente autoritativa confirmada y corresponder a esa operación; no usar un canon de arriendo, cierre de venta o pago pendiente como sustituto del pago al propietario original.
- Avisos in-app y correo transaccional con información mínima y enlace al portal, deduplicación interna, leído, reintentos y rebotes. Se revalida permiso/estado antes de enviar. No se promete recepción exactamente una vez en correo ni retirar mensajes ya entregados. Sin WhatsApp, SMS o push.
- Reporte gerencial en pantalla con período, ruta e inmueble, tablas/gráficos y detalle paginado. Una moneda/base temporal homogénea acordada; sin conversión cambiaria, exportación PDF/Excel, BI externo, diseñador de reportes o previsiones.
- Ingresos/costos/rentabilidad provienen del módulo 10; ocupación del módulo 8. Los pagos de módulos 8/9 se consultan como evidencia si hace falta, pero no se suman de nuevo a los ingresos consolidados. Resultados para propietario, si se autorizan, son publicaciones específicas; no se comparte automáticamente este tablero.
- Ratios consolidados se obtienen del agregado autoritativo o componentes compatibles definidos por los módulos fuente; no se promedian porcentajes por inmueble sin ponderación. Denominador cero = No aplica; fuente ausente = No disponible; un total parcial se etiqueta y lista exclusiones, no se presenta como total completo.
- Se presupone web/API/worker existente: Next.js, FastAPI, AWS, S3 y RDS PostgreSQL propuesto. No se seleccionan versiones de librerías ni se construye almacenamiento/escaneo documental desde cero.

### Estados, datos y controles propuestos

| Elemento | Regla |
|---|---|
| Contenido | Borrador → Publicado → Retirado; nueva versión requiere aprobación propia |
| Aviso | Pendiente, Enviado o Fallido por canal; lectura in-app independiente de envío de correo |
| Hito de pago | Solo fuente confirmada de pago de adquisición; evento pendiente/fallido no prueba recepción |
| Avance | Versión/fecha explícitas; no reconstruye obra ni inventa porcentaje si falta información |
| Reporte | Completo, Parcial o No disponible según cobertura/fuentes al corte; no mezclar monedas ni períodos incompatibles |
| Ingresos | Base y fecha acordadas con módulo 10, visibles; no equiparar valor vendido, canon causado y dinero cobrado |
| Ocupación | Numerador/denominador y universo provenientes del módulo 8; declarar corte y exclusiones |
| Rentabilidad | Definición y componentes provenientes de HU-28; consolidación compatible, sin nuevo motor financiero |

**Pendientes:** operador aprobador, qué resultados se comparten, vínculos de destinatario, reglas de retiro/retención, documentos visibles, fuente efectiva de pago de adquisición, tiempos/frecuencia de avisos, volumen, cortes y bases de indicadores. La política de compartir no está aprobada: estos límites permiten estimar sin exponer por defecto información del activo ya adquirido.

**Fuera de alcance adicional:** administración de arriendos/ventas/obras, KYC, contabilidad, facturación DIAN, cálculo nuevo de retorno/rentabilidad, TIR/VAN, automatización de decisiones de inversión, redacción automática de documentos, migración masiva y auditorías legales/financieras. Se consultan datos y evidencia de sistemas fuente; no se crean allí movimientos mediante este portal.

## Tabla de estimación por tarea

| ID | h | d | Modo | Referencia × unidades; riesgo | Motivo / verificación |
|---|---:|---:|---|---|---|
| AN-PC-01 | 8–16 | 1–2 | M0 | H × 1–2; ×1–1 | Acordar destinatarios, fuentes y semántica sin implementación. |
| BE-PC-01 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Versiones de contenido sensible y permisos por destinatario. |
| BE-PC-02 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | El propietario original no tiene acceso implícito al activo posterior. |
| BE-PC-03 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Múltiples fuentes privadas con filtrado de campos y versiones. |
| BE-PC-04 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Aprobación exacta evita exposición automática de cambios internos. |
| BE-PC-05 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Eventos externos a este módulo y comunicación con autorización vigente. |
| BE-PC-06 | 24–48 | 3–6 | M1 | H × 2–3; ×1,5–2 | Fuentes heterogéneas y riesgo de contar dos veces ingresos/costos. |
| BE-PC-07 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Consolidación y detalle deben usar la misma base de cálculo. |
| FE-PC-01 | 12–24 | 1,5–3 | M1 | A1 × 2–3; ×1,5–2 | Analogía parcial A1: selector de operación y vistas privadas. |
| FE-PC-02 | 9–20 | 1,125–2,5 | M1 | A1 × 1,5–2,5; ×1,5–2 | Descarga privada y avisos con estados de acceso cambiantes. |
| FE-PC-03 | 12–24 | 1,5–3 | M1 | A1 × 2–3; ×1,5–2 | Selección explícita de destinatario y revisión antes de exponer datos. |
| FE-PC-04 | 15–32 | 1,875–4 | M1 | A1 × 2,5–4; ×1,5–2 | Filtros, métricas y desglose con bases y datos parciales visibles. |
| OPS-PC-01 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Comunicación y procesamiento recuperable sobre plataforma compartida. |
| OPS-PC-02 | 6–16 | 0,75–2 | M1 | H × 0,5–1; ×1,5–2 | Privacidad y visibilidad de fuentes/avisos fallidos. |
| QA-PC-01 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Validación transversal de destinatarios, móvil y avisos reales. |
| QA-PC-02 | 15–32 | 1,875–4 | M1 | H × 1,25–2; ×1,5–2 | Consistencia entre fuentes y comportamiento ante datos incompletos. |
| REL-PC-01 | 6–16 | 0,75–2 | M1 | H × 0,5–1; ×1,5–2 | Activación de publicación/avisos con roles y fuentes verificadas. |

## 0 Definición — 8–16 h

### AN-PC-01 Definir acceso, contenido compartible e indicadores — 8–16 h

**Fuente:** HU-30, HU-31, HU-32. **Estimación:** M0 · H × 1–2; luego ×1–1. Acordar destinatarios, fuentes y semántica sin implementación.

- Separar propietario original, arrendatario y gerente; definir vínculo de cada cuenta a operaciones y quién autoriza compartir avances, documentos y resultados.
- Acordar catálogo acotado de hitos, evidencia requerida, canales, vigencia/revocación y política de correcciones; redactar Gherkin propuestos y ADR.
- Definir período, moneda, base de ingresos y denominadores de ocupación/rentabilidad; confirmar contratos de datos con módulos 2, 6, 7, 8, 9 y 10 sin asumir que están implementados.

**Tecnologías:** Markdown, Gherkin, OpenAPI y ADR en Git.


## 1 Backend — 126–272 h

### BE-PC-01 Modelo de publicaciones y migraciones — 12–24 h

**Fuente:** HU-30, HU-31. **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Versiones de contenido sensible y permisos por destinatario.

- Modelar publicación/versiones, operación origen, destinatario, recurso/versión fuente, snapshot compartible, aprobación, retiro, hitos y estado de avisos.
- Reutilizar persona/cuenta y vínculo de adquisición; agregar claves de idempotencia e índices por destinatario/operación/fecha.
- TDD de integridad, migración con datos previos y unicidad de evento/aviso; no crear otra ficha de inmueble, repositorio documental genérico o registro contable.

**Tecnologías:** SQLAlchemy 2, Alembic, PostgreSQL en RDS, pytest y Testcontainers.

### BE-PC-02 Autorización por operación y auditoría — 18–40 h

**Fuente:** HU-30, HU-31, HU-32, HU-33 (dependencia transversal). **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. El propietario original no tiene acceso implícito al activo posterior.

- Integrar autenticación existente y verificar vínculo sujeto-operación en cada consulta/descarga; denegar por defecto información de terceros y gestión interna posterior a adquisición.
- Autorizar aprobación/retiro a un rol interno designado y reportes solo a gerente; mantener compartición por contenido/revisión sin propagar permisos generales del inmueble.
- Auditar publicación, retiro y acceso documental con actor/fecha; revalidar derechos antes de entregar contenido, sin cachés compartidas de respuesta privada.
- TDD de cambio de vínculo, ID ajeno, rol arrendatario/propietario sin acceso gerencial y revocación. No crear login, gestión de representantes ni consola general de permisos.

**Tecnologías:** Dependencias FastAPI, PostgreSQL, pytest y HTTPX.

### BE-PC-03 Consulta de operación, avances y documentos autorizados — 18–40 h

**Fuente:** HU-30. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Múltiples fuentes privadas con filtrado de campos y versiones.

- Proponer GET /api/v1/portal/operaciones y /operaciones/{id} con avance compartido, fecha de actualización, documentos propios accesibles y resultados expresamente autorizados.
- Consumir expediente/seguimiento existente del módulo 2, reportes de obra del 6 y archivos contractuales del 7; mostrar datos ausentes como No disponible, sin inventar progreso ni exponer notas internas.
- Proponer descarga autenticada mediante proxy/streaming con nueva verificación de acceso por solicitud y Cache-Control privado/no-store; no devolver URL pública o persistente a documentos.
- TDD de paginación, fuente caída, archivo retirado, documento de otro participante y versión no aprobada. Sin construir carga documental, obra o firma; no impedir que un usuario conserve archivos ya descargados.

**Tecnologías:** FastAPI, HTTPX/servicios internos, S3 privado compartido, pytest.

### BE-PC-04 Preparación, aprobación y retiro de contenido — 18–40 h

**Fuente:** HU-30, HU-31. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Aprobación exacta evita exposición automática de cambios internos.

- Proponer /api/v1/portal/publicaciones para preparar resumen, fotos/documentos seleccionados y resultados con lista permitida de campos y destinatario vinculado.
- Permitir Borrador → Publicado mediante aprobación explícita y Publicado → Retirado con motivo; conservar snapshot de contenido/versión aprobados, autor y fecha.
- Cambios en el origen no reemplazan silenciosamente contenido publicado: requieren nueva revisión; retiro o pérdida de permiso bloquea consulta futura y avisos aún no enviados.
- TDD de doble publicación, versión obsoleta, fuente eliminada o inaccesible y retiro concurrente. Se comparte resumen/fotos seleccionados, sin editor de redacción automática de PII, reglas multinivel ni redacción de documentos legales.

**Tecnologías:** FastAPI, Pydantic, PostgreSQL, referencias S3, pytest.

### BE-PC-05 Hitos y notificaciones al propietario original — 18–40 h

**Fuente:** HU-31. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Eventos externos a este módulo y comunicación con autorización vigente.

- Recibir/consultar eventos de formalización o pago de adquisición desde su fuente autoritativa, con referencia única; asociarlos solo a la operación y destinatario correctos.
- Crear aviso persistente in-app y correo con información mínima/enlace autenticado tras autorización de compartición; revalidar estado fuente y permiso antes del envío.
- Mantener outbox, deduplicación por evento/revisión/destinatario/canal, leído, reintentos y rebotes; corrección posterior conserva trazabilidad, no borra correos entregados.
- TDD de evento repetido/desordenado, pago pendiente no notificable como confirmado, retiro previo a envío y fuente ausente. Sin fuente de confirmación, el hito no se inventa; no implementar pagos de adquisición ni firma aquí.

**Tecnologías:** FastAPI, worker Python, PostgreSQL, AWS SES, pytest.

### BE-PC-06 Contratos de datos para reportes consolidados — 24–48 h

**Fuente:** HU-32. **Estimación:** M1 · H × 2–3; luego ×1,5–2. Fuentes heterogéneas y riesgo de contar dos veces ingresos/costos.

- Definir y adaptar lectura de ingresos/costos/rentabilidad desde módulo 10 y ocupación desde módulo 8, con inmueble, período, moneda, corte y versión/estado de dato.
- Evitar sumar los pagos de arriendo/venta de nuevo a los ingresos ya consolidados del módulo 10; esos módulos son origen de trazabilidad y no una segunda fuente acumulable.
- Exigir definición homogénea y componentes agregables para ratios, o usar agregado autoritativo del módulo 10. No promediar porcentajes de rentabilidad u ocupación sin ponderación y universo acordados.
- TDD de IDs duplicados, fuentes con cortes/monedas distintos, denominador cero y dato incompleto; devolver estado parcial/indisponible sin reemplazarlo por cero. No construir contabilidad ni motor de rentabilidad.

**Tecnologías:** FastAPI, Pydantic, HTTPX/consultas de servicios internos, Decimal, pytest.

### BE-PC-07 Consultas gerenciales y conciliación de agregados — 18–40 h

**Fuente:** HU-32. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Consolidación y detalle deben usar la misma base de cálculo.

- Proponer GET /api/v1/gerencia/reportes con período, ruta e inmueble, resumen y detalle paginado; incluir ingresos, ocupación y rentabilidad según contrato BE-PC-06.
- Mantener misma definición/corte entre resumen y desglose; separar total completo de parcial y explicar activos excluidos. Exponer fecha de actualización y fuentes consultadas.
- Agregar índices/consultas o caché privada por usuario/filtros/corte si se justifica con volumen; invalidar al cambiar permisos/datos.
- TDD de un inmueble con varias operaciones, filtros combinados, vista vacía y suma de detalle consistente. Sin cubo BI, proyecciones, TIR/VAN nuevos, exportaciones o reportes regulatorios.

**Tecnologías:** FastAPI, SQLAlchemy/PostgreSQL, Decimal, pytest.


## 2 Frontend — 48–100 h

### FE-PC-01 Inicio del portal y avance compartido — 12–24 h

**Fuente:** HU-30. **Estimación:** M1 · A1 × 2–3; luego ×1,5–2. Analogía parcial A1: selector de operación y vistas privadas.

- Crear inicio adaptable a celular con operaciones vinculadas, avance/última actualización, fotos y resultados que la compañía haya autorizado.
- Distinguir estado de su operación de gestión del activo; no mostrar por defecto ventas, arriendos, costos internos o reportes gerenciales.
- TDD de varias operaciones, sin publicaciones, fuente no disponible, sesión vencida y navegación móvil/teclado; reutilizar login y seguimiento existente del módulo 2.

**Tecnologías:** Next.js, TypeScript, componentes accesibles, Vitest y Testing Library.

### FE-PC-02 Documentos y bandeja de avisos — 9–20 h

**Fuente:** HU-30, HU-31. **Estimación:** M1 · A1 × 1,5–2,5; luego ×1,5–2. Descarga privada y avisos con estados de acceso cambiantes.

- Mostrar documentos propios/autorizados, fecha y versión, descarga autenticada y mensajes ante retiro/indisponibilidad.
- Integrar bandeja de hitos, no leídos y navegación a contenido aún autorizado; no exponer detalles privados en notificaciones fuera del portal.
- TDD de aviso duplicado, enlace retirado, contrato ajeno y estado leído. Sin carga documental nueva, mensajería bidireccional ni portal de pagos.

**Tecnologías:** Next.js, TypeScript, cliente HTTP autenticado, Testing Library.

### FE-PC-03 Panel interno de contenido compartido — 12–24 h

**Fuente:** HU-30, HU-31. **Estimación:** M1 · A1 × 2–3; luego ×1,5–2. Selección explícita de destinatario y revisión antes de exponer datos.

- Crear bandeja interna para preparar resumen/selección de fotos y documentos, previsualizar contenido permitido, aprobar o retirar con motivo.
- Mostrar destinatario, operación y versión fuente, y avisar que cambios del origen requieren nueva publicación; la vista previa no habilita acceso al propietario por sí sola.
- TDD de destinatario inválido, versión obsoleta, campos no permitidos y permiso insuficiente. Sin editor libre ni administración general de roles.

**Tecnologías:** Next.js, TypeScript, React Hook Form, Zod, Testing Library.

### FE-PC-04 Tablero gerencial consolidado — 15–32 h

**Fuente:** HU-32. **Estimación:** M1 · A1 × 2,5–4; luego ×1,5–2. Filtros, métricas y desglose con bases y datos parciales visibles.

- Construir reporte de ingresos, ocupación y rentabilidad con filtros de período/ruta/inmueble, tarjetas/tablas/gráficos y detalle paginado.
- Mostrar moneda, definición, corte, actualización, fuentes y datos excluidos; diferenciar parcial, sin datos, No aplica y cero válido.
- TDD de combinación de filtros, permiso gerencial, denominador cero y suma/detalle; sin diseñador de reportes, exportación PDF/Excel ni BI externo.

**Tecnologías:** Next.js, TypeScript, componentes gráficos accesibles, Testing Library.


## 3 Infraestructura incremental y observabilidad — 18–40 h

### OPS-PC-01 Entrega de avisos y procesos de integración — 12–24 h

**Fuente:** HU-31, HU-32. **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Comunicación y procesamiento recuperable sobre plataforma compartida.

- Configurar consumidores/consulta programada de eventos, outbox, reintentos y cola de fallos sobre worker existente; permisos mínimos para fuentes y archivos.
- Configurar/adaptar SES, identidad de remitente, plantilla transaccional y rebotes por ambiente; si módulo 8 ya ofrece correo, reutilizarlo sin cobrar otra base de entrega.
- Verificar invocación, fallo/reproceso y correo a destinatarios de prueba; separar espera de verificación de dominio/aprobación SES.

**Tecnologías:** ECS/worker, SQS, EventBridge Scheduler según fuente, SES, IAM, CDK/CloudFormation.

### OPS-PC-02 Protección de respuestas y observabilidad — 6–16 h

**Fuente:** HU-30, HU-31, HU-32. **Estimación:** M1 · H × 0,5–1; luego ×1,5–2. Privacidad y visibilidad de fuentes/avisos fallidos.

- Configurar no-store/ausencia de caché pública para portal y descargas; mantener S3 privado y credenciales de integración por ambiente.
- Instrumentar errores de fuente, retraso de eventos, avisos fallidos y latencia de reportes, con alarmas de prueba y logs sin contenido/PII.
- Auditoría de negocio en RDS; sin recrear almacenamiento, pipeline o plataforma de observabilidad compartida.

**Tecnologías:** CloudWatch, SNS, S3/IAM, configuración de API/web.


## 4 Validación transversal — 27–56 h

### QA-PC-01 Recorridos por rol y revocación de contenido — 12–24 h

**Fuente:** HU-30, HU-31, HU-32. **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Validación transversal de destinatarios, móvil y avisos reales.

- Ejecutar preparación → aprobación → consulta del propietario → aviso → descarga → retiro; comprobar operación ajena, arrendatario y acceso gerencial prohibido.
- Verificar cambio de permisos durante consulta/cola, no-store y enlaces retirados, móvil/teclado y correo de prueba; no repetir unitarias de política.
- Separar evidencia real de servicios disponibles frente a mocks; no certificar un módulo fuente aún inexistente.

**Tecnologías:** Playwright, HTTPX, SES de prueba y staging.

### QA-PC-02 Conciliación de reportes y recuperación — 15–32 h

**Fuente:** HU-31, HU-32. **Estimación:** M1 · H × 1,25–2; luego ×1,5–2. Consistencia entre fuentes y comportamiento ante datos incompletos.

- Conciliar ingresos/costos/ocupación y rentabilidad agregada con dataset conocido del módulo 10/8; incluir varias operaciones por activo, períodos y denominadores distintos.
- Simular fuente caída, evento repetido/desordenado y recuperación del worker sin doble aviso lógico; comprobar migración/recuperación e índices con volumen acordado.
- Verificar que valores parciales no se presentan como totales completos ni se mezclan monedas/cortes; sin auditoría financiera, pentest externo o certificación de carga.

**Tecnologías:** pytest/HTTPX, PostgreSQL, servicios de staging, CloudWatch.


## 5 Entrega — 6–16 h

### REL-PC-01 Activación y aceptación del portal — 6–16 h

**Fuente:** HU-30, HU-31, HU-32. **Estimación:** M1 · H × 0,5–1; luego ×1,5–2. Activación de publicación/avisos con roles y fuentes verificadas.

- Desplegar mediante pipeline existente, comprobar fuentes/permisos y habilitar publicación/avisos por ambiente; smoke del portal y reporte gerencial.
- Entregar guía de propietario/operador/gerente, ADR, OpenAPI y procedimiento de retiro/fallo de datos; registrar aceptación y horas reales para recalibrar.
- Separar esperas de aprobación de contenido/políticas y entrega de módulos fuente. La cotización no envía mensajes ni comparte documentos reales.

**Tecnologías:** Git, pipeline AWS, OpenAPI y Markdown.

## 6 Dependencias y base compartida

| Fuente/dependencia | Se reutiliza | Incremento de este módulo |
|---|---|---|
| Login y módulo 2 | Cuenta, vínculo propietario-operación, seguimiento y documentos privados | Consulta consolidada y política de compartir posterior; no reimplementar HU-08 |
| Módulo 6 | Reportes/fotos/avance de obra existentes | Selección y snapshot del contenido autorizado; no CRUD de obra |
| Módulo 7 | Firma/archivo y estado de contrato de adquisición | Hito y acceso permitido a documento; no motor de firma |
| Módulo 8 | Ocupación con definición/corte, y correo compartido si existe | Adaptador de reportes y plantilla de aviso del portal |
| Módulos 9/10 | Resultados operativos y financieros por inmueble | Consultas consolidadas sin duplicar movimientos ni calcular otra rentabilidad |
| Fuente de pago al propietario | Estado/evidencia de pago de adquisición | Filtrar y notificar un hito confirmado; no ejecutar ni conciliar ese pago |

**Implementación del módulo 10 pendiente de verificar:** HU-27/HU-28 se detallan en la [épica financiera](pagos-utilidades-epica.md). BE-PU-06 cotiza la API fuente; AN-PC-01 y BE-PC-06 mantienen aquí el acuerdo/adaptación del consumidor, sin duplicar el motor financiero. HU-32 no se considera operativamente completa hasta contar con datos reales validados, agregados compatibles e historial.

BE-PU-04 del módulo 10 contempla registrar y validar pagos de adquisición realizados fuera de la plataforma y emitir su referencia de confirmación/corrección. No se verificó implementación: el motor de firma no acredita dinero recibido ni basta un costo registrado. El portal conserva autorización de compartición y no sustituye esa fuente por pagos de arriendo o venta. Fixtures permiten avanzar, no acreditan integración real.

Arriendo tiene [versión original](arriendo-inmuebles-epica.md) y [nuestra v2](arriendo-inmuebles-epica-v2.md). Son alternativas conservadas por solicitud del usuario, no costos acumulables. Elegir la implementación/contrato disponible para la fuente de ocupación no convierte ninguna estimación en aprobada ni suma ambas.

Si falta la base técnica, sumar una sola vez [BASE-01 a BASE-05 del módulo 2](ficha-inmueble-epica.md#6-base-compartida-si-aún-no-está-implementada): **78–176 h**, detalladas en el JSON. Incluye ambientes, pipeline, adaptación del login existente, pruebas y observabilidad. BASE-03 no construye autenticación desde cero; esa variante se reestima. No cobrar otra base AWS, almacenamiento o motor de correo por cada módulo.

La extensión de permisos/publicaciones y adaptadores se cotiza aquí; las fuentes funcionales se presupuestan aparte solo si faltan. Secuencia: política/datos → modelo/permisos → contenido/descarga → hitos/avisos → reportes → validación/activación. Frontend puede avanzar con contrato acordado; capacidad y disponibilidad de fuentes determinan calendario, no dividir esfuerzo entre personas sin más.

## 7 Complejidad

| Grupo | S/M/L | Motivo |
|---|---|---|
| Publicación y autorización | L | Destinatario, versión, retiro y límite de acceso al activo |
| Portal y documentos | M | Varias fuentes privadas y lectura móvil |
| Hitos y avisos | M | Confirmación fuente, deduplicación y permisos al enviar |
| Consolidación gerencial | L | Bases homogéneas, ratios y datos faltantes |
| Operación y validación | M | Recuperación, correo y aislamiento entre roles |

S/M/L es complejidad relativa; no se traduce automáticamente a horas.

## 8 Contingencias, consumo y aceptación

- **Reserva condicionada:** 0–4 h una sola vez, fuera del total base, para corregir un campo/ID de un contrato fuente ya entregado. Dueño: responsable de integración. Totales bajo esa condición: **233–504 h** con fuentes funcionales o **311–680 h** agregando toda la base técnica. No cubre crear módulo 10, nuevos canales, cálculo financiero adicional o nuevas reglas de compartición. No duplicar riesgo ya incluido con M1.
- **Consumo AWS separado:** API/web/worker, RDS, S3/transferencia privada, SES, SQS, programación de eventos, KMS y CloudWatch. Requiere región, usuarios, consultas, tamaño de archivos, correos y retención para precio monetario; no se inventan importes.
- **Esperas externas:** política de contenido/datos, definición financiera, entrega de fuentes, acceso a ambientes y habilitación de correo. No son horas de desarrollo ni garantía de calendario.
- **Aceptación:** aprobar supuestos/Gherkin, conservar ADR y evidencia de pruebas reales frente a simuladas, y registrar horas reales para recalibrar. Esta entrega documenta la cotización; no publica datos ni envía notificaciones reales.
