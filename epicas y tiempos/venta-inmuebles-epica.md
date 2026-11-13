# Épica del módulo 9. Venta de inmuebles adquiridos

Cotización inicial de **HU-40 a HU-45 y HU-48 a HU-50** de las [historias del proyecto](../historias_de_usuario_plan_del_proyecto.md), según el [contexto del negocio](../contexto.md). Son nueve historias: asignación y ficha comercial, publicación, CRM/visitas, negociación, expediente jurídico, cierre y resultados. Se conserva la estructura por capas de la [épica del login](login-epica.md).

**Referencia funcional:** [criterios Gherkin propuestos](venta-inmuebles-criterios-aceptacion.md). No se encontraron criterios aprobados específicos de ventas; supuestos y escenarios deben validarse antes de implementar. Permanecen las reglas de los [criterios aprobados de adquisición](adquisicion-inmuebles-criterios-aceptacion.md).

## Resumen de horas

| Capa | Rango |
|---|---:|
| Definición | 12–24 h |
| Backend | 210–448 h |
| Frontend | 90–192 h |
| Infraestructura incremental y observabilidad | 21–44 h |
| Validación transversal | 42–92 h |
| Entrega | 9–20 h |
| **Módulo con base y dependencias funcionales** | **384–820 h** |
| Base técnica compartida, solo si está pendiente | 78–176 h |
| **Módulo más toda la base técnica pendiente** | **462–996 h** |

**Ambos escenarios excluyen construir las dependencias funcionales.** Se presupone disponibilidad del inmueble/elegibilidad y archivos privados, componentes de actividades/tareas/avisos del CRM y motor contractual del módulo 7. La base técnica de 78–176 h no entrega esos módulos. Ver sección 6 para consolidar sin duplicidades.

Horas-persona; **1 d = 8 h** como convención, no plazo de calendario. TDD, pruebas propias y revisión están incluidos en tareas funcionales. QA cubre recorridos, permisos y recuperación entre componentes. Consumo AWS, servicios externos y esperas se separan. No se identificó una estimación anterior del módulo 9.

## Método y evidencia

Se aplica [estimate-task local](../skills/estimate-task/SKILL.md) y sus [referencias](../skills/estimate-task/references/calibration.md). [Cálculo reproducible](../docs/estimaciones/modulo-9-estimacion.json), [generador](../docs/estimaciones/generar_modulo_9.py): `python docs/estimaciones/generar_modulo_9.py`.

**Confianza baja:** sin horas reales Casabra ni implementación comprobada de servicios compartidos; canales, aprobación y cierre pendientes. A1 (S9.2 / RED-3596, 0,5 d) es referencia importada no verificada de conexión UI a endpoint con errores y pruebas; se usa como analogía parcial de varias vistas con dinero/PII. H (1 d) es unidad de hipótesis técnica por entregables, no ancla medida. Estimaciones de módulos anteriores no son tiempos reales.

**Fórmula por extremo:** `ceil(8 × días_referencia × unidades_base × factor_riesgo)`. ×ref se expresa antes del factor. M0 usa ×1 en definición; M1 usa ×1,5–2 una sola vez por dinero, permisos, datos personales, migraciones, cierre sensible o ausencia de patrón probado. No multiplicar otra vez el total ni sumar TDD/revisión duplicados. No se aplica descuento fijo por IA. Recalibrar con esfuerzo real del primer recorrido; rangos sin significado de percentil estadístico.

## Alcance confirmado por historias

| Historia | Resultado incluido |
|---|---|
| HU-40 | Asignación a venta de activo adquirido y precio objetivo |
| HU-41 | Ficha comercial, fotos, precio, documentos y alistamiento |
| HU-42 | Publicación y actualización en canales definidos |
| HU-43 | Prospectos, origen, intereses, interacciones, tareas y seguimientos |
| HU-44 | Visitas con comentarios y nivel de interés |
| HU-45 | Ofertas, contraofertas, comparación y aprobaciones de precio |
| HU-48 | Preparación/revisión documental y condiciones de cierre |
| HU-49 | Registro de firma, pago, entrega, cierre e inventario |
| HU-50 | Embudo, tiempos de cierre, ofertas y ventas realizadas |

**Confirmado por contexto:** se venden activos de la compañía ya adquiridos y asignados a Venta. El comprador no es el propietario original de adquisición. Precio aprobado, oferta aceptada, contrato firmado, pago recibido, entrega y cierre son hechos distintos. El cierre comercial no vuelve a ejecutar adquisición ni convierte el registro técnico en un trámite jurídico externo.

### Supuestos para cotizar

- Una compañía, un inmueble completo por venta, un comprador principal y moneda COP propuesta. Se aceptan múltiples prospectos/ofertas simultáneos, pero una sola reserva y un solo cierre vigente por inmueble. No se cotizan participaciones, copropietarios compradores, multiunidad o multimoneda.
- El gerente de activos usa la autorización de ruta del módulo 2 y registra precio objetivo. La ficha contempla alistamiento antes de disponibilidad; obras se vinculan al módulo 6 si existen. No se incluye reclasificación de ruta ni venta de activos ocupados con contratos de arriendo vigentes; el sistema bloquea operaciones incompatibles con el inventario compartido.
- HU-42 se estima con un catálogo web propio sencillo (listado paginado y ficha), diseño existente, precio/fotos/descripción y contacto de la compañía. Registro y gestión manual de enlaces/estados para portales externos; no hay conectores automáticos ni publicación externa desde la app. Los canales definitivos pueden cambiar esta partida.
- La ficha pública solo contiene campos permitidos y fotografías expresamente seleccionadas. Precio objetivo interno, negociaciones, compradores, documentos legales y soportes no son públicos. La ficha interna sí referencia documentos autorizados. Sin formulario público de captación, buscador avanzado, mapas, campañas ni nuevo diseño de marca.
- Prospectos creados por equipo de ventas, con origen, intereses y asesor; pueden interesarse por varios inmuebles. Cada relación prospecto-inmueble es una oportunidad distinta. No se exige cuenta de comprador para ser prospecto ni se reutilizan automáticamente datos privados del propietario de adquisición.
- Interacciones, tareas y recordatorios in-app adaptan componentes del módulo 5; la ficha de prospectos/embudo de venta sí es nueva. Visitas con fecha, responsable, resultado e interés bajo/medio/alto como catálogo inicial. Sin correo/SMS/WhatsApp, calendarios externos o scoring de prospectos.
- Cada oferta/contraoferta tiene versión, importe, moneda, condiciones y autor/origen. Precio objetivo no autoriza automáticamente descuentos. Un nivel de aprobación explícita del gerente comercial sobre la versión concreta; límites/delegaciones se confirman en definición. No hay motor multinivel de aprobaciones.
- Aceptación del comprador se registra por asesor con fecha y evidencia. Reserva requiere aceptación y aprobación interna sobre la misma versión. Cambiar precio/condiciones invalida decisiones previas; no modifica contratos firmados. Liberación antes de cierre requiere motivo y ausencia de compromisos contractuales/pagos pendientes de resolución; devoluciones o rescisión con dinero recibido quedan fuera de este alcance inicial.
- Abogado revisa expediente/checklist configurable y preparado por la empresa, con evidencia y validación humana. Se usa una plantilla Venta, un PDF y dos firmantes del módulo 7. Documentos externos de formalización se adjuntan como evidencia; no se automatizan notaría, registro, estudio de títulos, redacción jurídica o validación legal.
- Pagos/abonos por medios externos se registran con referencia y soporte, pendientes hasta validación expresa de administrador. Se mantiene historial y compensaciones antes de cierre. No hay pasarela ni recaudo digital de venta, gestión de crédito o conciliación bancaria automática. La exactitud de la recepción se valida operativamente fuera del sistema.
- Para el cierre inicial se requiere precio final íntegramente cubierto por pagos confirmados, sin excedentes no resueltos; firma/archivo contractual, aprobación jurídica vigente y entrega registradas. Cierre actualiza inventario comercial, oportunidad ganadora y otras oportunidades sin borrar historial. Incidentes posteriores al cierre se registran, sin reapertura o anulación automática de venta.
- Roles: gerente de activos, asesor de ventas, gerente comercial, abogado y administrador. La distinción de los cargos de ventas y sus facultades en HU-33 es pendiente de acuerdo; no se considera ya implementada. El comprador firma mediante módulo 7, sin portal propio ni acceso a comparaciones de otras ofertas.
- FastAPI, Next.js adaptable a celular, AWS, RDS PostgreSQL propuesto y S3. Archivos privados PDF/JPEG/PNG bajo servicio compartido con validación/análisis; límites y retención por acordar. Uso conectado, sin app nativa u offline.

### Estados propuestos, cierre y medición

| Dimensión | Regla propuesta |
|---|---|
| Disponibilidad comercial | En alistamiento → Disponible → Reservado → Vendido; independiente del historial Adquirido y de anuncios |
| Oportunidad | Nueva, Contactada, Visita, Negociación, En cierre, Ganada o Perdida; visitas no obligatorias para todas las oportunidades; pérdida requiere motivo |
| Publicación | Borrador, Publicada o Retirada en web propia; estado externo manual, con retiro pendiente cuando corresponde |
| Oferta | Historial versionado; decisión interna y decisión de comprador separadas; solo revisión vigente aprobada/aceptada habilita reserva |
| Pago externo | Registrado pendiente de validación, Confirmado o Anulado con corrección trazable; no equivale a pago procesado por la plataforma |
| Cierre | Pendiente de requisitos o Cerrado; un commit único registra cierre/inventario y evento de retiro |
| Embudo | Cohorte de oportunidades creadas en período, agrupadas por su etapa actual al corte; no representa toda la historia de conversiones |
| Ofertas | Conteo de ofertas creadas en período y versiones vigentes; mostrar diferencias frente a número de oportunidades |
| Ventas realizadas | Conteo y valor final aprobado de cierres por fecha de cierre; no igualar a cobros ni rentabilidad |
| Tiempo de cierre | Días desde alta de oportunidad ganadora hasta cierre; promedio solo de cierres incluidos; sin cierres se muestra No aplica |

Cerrar requiere versión comercial/contractual consistente, reserva vigente, revisión jurídica y evidencias de firma, pago y entrega. La adquisición histórica se conserva; Vendido describe disponibilidad/operación posterior. El cierre y la reserva compiten bajo restricciones transaccionales para impedir doble venta. La web propia deja de presentar oferta disponible al consultar estado actualizado; invalidación de caché y retiro se reintentan. Los anuncios externos conservan tarea de retiro manual; no se promete borrar copias de terceros.

**Pendientes:** canales exactos, documentos publicables, alistamiento, fases del embudo, reglas de precio/descuento, validez de ofertas, autoridad para reservar/liberar, requisitos de cierre y forma de pago, entidades compradoras/múltiples firmantes, retención, volumen y umbrales de rendimiento. Esta cotización no fija reglas jurídicas ni convierte sus supuestos en decisiones aprobadas.

**Exclusiones adicionales:** automatización de portales, financiación hipotecaria, recaudo/reembolsos, facturación DIAN, comisiones de corredores, contabilidad/rentabilidad consolidada, importación masiva CRM, BI externo y flujo posterior de reversión de una venta cerrada. Los módulos consumidores usarán IDs estables de venta/pagos; no volverán a registrar dinero ya contabilizado operativamente.

## Tabla de estimación por tarea

| ID | h | d | Modo | Referencia × unidades; riesgo | Motivo / verificación |
|---|---:|---:|---|---|---|
| AN-VE-01 | 12–24 | 1,5–3 | M0 | H × 1,5–3; ×1–1 | Definiciones y dependencias sin implementación. |
| BE-VE-01 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | PII, importes, versiones y exclusión de operaciones concurrentes. |
| BE-VE-02 | 15–32 | 1,875–4 | M1 | H × 1,25–2; ×1,5–2 | Elegibilidad, dinero y separación de información pública/privada. |
| BE-VE-03 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Exposición pública controlada y versiones coherentes. |
| BE-VE-04 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Nuevo contexto de comprador y múltiples inmuebles por prospecto. |
| BE-VE-05 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Agenda de venta y adaptación de tareas con permisos propios. |
| BE-VE-06 | 24–48 | 3–6 | M1 | H × 2–3; ×1,5–2 | Dinero y condiciones versionadas sin sobrescribir negociación. |
| BE-VE-07 | 15–32 | 1,875–4 | M1 | H × 1,25–2; ×1,5–2 | Autorización sensible y prevención de doble venta. |
| BE-VE-08 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Requisitos, revisión exacta y dependencia de firma. |
| BE-VE-09 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Dinero con evidencia, abonos y control de duplicados. |
| BE-VE-10 | 24–48 | 3–6 | M1 | H × 2–3; ×1,5–2 | Cierre sensible que coordina evidencia e inventario. |
| BE-VE-11 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Métricas por oportunidad/venta con períodos y versiones diferentes. |
| BE-VE-12 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Roles comerciales/jurídicos y datos privados frente a público. |
| FE-VE-01 | 15–32 | 1,875–4 | M1 | A1 × 2,5–4; ×1,5–2 | Analogía parcial A1: varios formularios de contenido y precio. |
| FE-VE-02 | 12–24 | 1,5–3 | M1 | A1 × 2–3; ×1,5–2 | Vista pública nueva con datos estrictamente limitados. |
| FE-VE-03 | 15–32 | 1,875–4 | M1 | A1 × 2,5–4; ×1,5–2 | Nuevas vistas comerciales reutilizan historial y agenda del módulo 5. |
| FE-VE-04 | 18–40 | 2,25–5 | M1 | A1 × 3–5; ×1,5–2 | Versiones monetarias, comparación y acciones restringidas. |
| FE-VE-05 | 18–40 | 2,25–5 | M1 | A1 × 3–5; ×1,5–2 | Varias evidencias y condiciones antes de una acción sensible. |
| FE-VE-06 | 12–24 | 1,5–3 | M1 | A1 × 2–3; ×1,5–2 | Embudo y resultados con universos de fecha explícitos. |
| OPS-VE-01 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Contenido público separado del privado e invalidación tras cierre. |
| OPS-VE-02 | 9–20 | 1,125–2,5 | M1 | H × 0,75–1,25; ×1,5–2 | Exposición pública, cierres y eventos requieren observabilidad. |
| QA-VE-01 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Integración entre adquisición, web, CRM, contrato y cierre. |
| QA-VE-02 | 15–32 | 1,875–4 | M1 | H × 1,25–2; ×1,5–2 | Venta única e invariantes frente a reintentos/fallos. |
| QA-VE-03 | 9–20 | 1,125–2,5 | M1 | H × 0,75–1,25; ×1,5–2 | Validar límites entre visitante, comprador y roles internos. |
| REL-VE-01 | 9–20 | 1,125–2,5 | M1 | H × 0,75–1,25; ×1,5–2 | Activación coordinada de publicación, permisos y cierre. |

## 0 Definición — 12–24 h

### AN-VE-01 Acordar embudo, canales, precios y cierre — 12–24 h

**Fuente:** HU-40, HU-41, HU-42, HU-43, HU-44, HU-45, HU-48, HU-49, HU-50. **Estimación:** M0 · H × 1,5–3; luego ×1–1. Definiciones y dependencias sin implementación.

- Mapear roles, etapas de oportunidad, fuentes, interés, visitas, versiones de oferta y aprobación; distinguir precio objetivo de precio autorizado y aceptación de comprador.
- Definir catálogo web propio y gestión manual de canales externos como alcance provisional; confirmar datos publicables y política de retiro.
- Acordar checklist de cierre, confirmación manual de pago, reserva exclusiva y métricas; registrar Gherkin y ADR. Negocio/abogado proveen requisitos de formalización, sin inventar requisitos jurídicos.

**Tecnologías:** Markdown, Gherkin, OpenAPI y ADR en Git.


## 1 Backend — 210–448 h

### BE-VE-01 Modelos comerciales y migraciones — 18–40 h

**Fuente:** HU-40, HU-43, HU-45, HU-48, HU-49, HU-50. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. PII, importes, versiones y exclusión de operaciones concurrentes.

- Modelar ficha de venta, publicación/versiones, prospecto, oportunidad por prospecto-inmueble, etapas, visitas, ofertas/versiones, aprobaciones, reserva, expediente, pagos y cierre.
- Reutilizar inmueble/identidad y referencias del CRM/contratos; usar Decimal, moneda y restricciones de reserva/cierre únicos por inmueble.
- TDD de relaciones, idempotencia, historial y migración sobre datos previos; no duplicar estados de adquisición ni hacer comprador igual a propietario original.

**Tecnologías:** SQLAlchemy 2, Alembic, RDS PostgreSQL, pytest y Testcontainers.

### BE-VE-02 Asignación, ficha y precio objetivo — 15–32 h

**Fuente:** HU-40, HU-41. **Estimación:** M1 · H × 1,25–2; luego ×1,5–2. Elegibilidad, dinero y separación de información pública/privada.

- Proponer GET/POST /api/v1/ventas/inmuebles y PATCH de ficha; consumir asignación Venta del módulo 2 con gerente de activos autorizado.
- Registrar precio objetivo, descripción, alistamiento, fotos y referencias documentales; distinguir precio objetivo interno, precio publicado y precio acordado.
- Reutilizar archivo privado y seleccionar fotos/datos comerciales publicables; TDD de inmueble no adquirido, ruta incompatible, doble alta e importe inválido. No reclasificar activos arrendados ni ejecutar obras.

**Tecnologías:** FastAPI, Pydantic, SQLAlchemy, servicio compartido de archivos, pytest.

### BE-VE-03 Publicación web y control de canales — 18–40 h

**Fuente:** HU-42, HU-41. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Exposición pública controlada y versiones coherentes.

- Proponer API de catálogo público paginado y ficha por slug con lista permitida de campos; publicar snapshot solo tras validar alistamiento/disponibilidad y datos obligatorios.
- Permitir publicar, actualizar y retirar en web propia; registrar canal, URL, fecha y estado manual de anuncios externos, sin afirmar sincronización con portales.
- Servir solo fotos/copia autorizada; documentos legales siguen privados para equipo/comprador autorizado por proceso contractual. TDD de campos internos excluidos, ficha retirada y versión publicada coherente.
- Al reservar/cerrar bloquear consulta pública de oferta disponible y emitir invalidación/retiro; conservar historial interno y pendientes de retiro externo.

**Tecnologías:** FastAPI, PostgreSQL, S3 público controlado o CDN para copias autorizadas, pytest.

### BE-VE-04 Prospectos y oportunidades sobre el CRM — 18–40 h

**Fuente:** HU-43. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Nuevo contexto de comprador y múltiples inmuebles por prospecto.

- Proponer /api/v1/ventas/prospectos y /oportunidades con contacto, origen, intereses, asesor responsable y etapa; registro por equipo, sin onboarding público del comprador.
- Crear oportunidad por prospecto-inmueble y conservar transiciones con fecha/autor; detectar duplicados básicos por contacto sin fusionar personas automáticamente.
- Adaptar historial/interacciones de BE-CRM-03 del módulo 5 a oportunidad de venta con acceso segregado; no duplicar motor de actividades ni aplicar etapas de adquisición.
- TDD de prospecto sin cuenta, varias oportunidades, duplicados y reasignación autorizada. La compatibilidad del servicio CRM es condición pendiente de comprobar.

**Tecnologías:** FastAPI, PostgreSQL, contrato de servicio CRM compartido, pytest.

### BE-VE-05 Visitas y próximos seguimientos — 12–24 h

**Fuente:** HU-43, HU-44. **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Agenda de venta y adaptación de tareas con permisos propios.

- Registrar visitas con fecha, responsable, resultado y nivel de interés; estados Programada, Realizada o Cancelada como supuesto.
- Adaptar tareas/vencimientos y recordatorios in-app de BE-CRM-04/05 a oportunidades de venta, con reprogramación/cancelación y registro de compromiso.
- TDD de visita ajena, fecha/zona acordada, reenvío, tarea cerrada y aviso obsoleto. Sin calendario externo, optimización de rutas, correo/SMS/WhatsApp ni nuevo motor de avisos.

**Tecnologías:** FastAPI, PostgreSQL, servicios CRM de tareas/avisos, pytest.

### BE-VE-06 Ofertas, contraofertas y comparación — 24–48 h

**Fuente:** HU-45. **Estimación:** M1 · H × 2–3; luego ×1,5–2. Dinero y condiciones versionadas sin sobrescribir negociación.

- Proponer /api/v1/ventas/oportunidades/{id}/ofertas con importe, moneda, condiciones, origen comprador/compañía y referencia a versión anterior.
- Registrar varias ofertas/contraofertas y su vigencia manual; comparar última versión vigente por oportunidad junto con precio objetivo y condiciones relevantes.
- Conservar historial y aceptación/rechazo del comprador registrados por asesor con fecha y evidencia, sin suplantar firma formal ni aprobar precio automáticamente.
- TDD de oferta inválida, moneda incompatible, revisión obsoleta y comparación que no multiplica versiones. Sin subastas, scoring automático, financiamiento ni envíos de ofertas a canales externos.

**Tecnologías:** FastAPI, Pydantic, Decimal, PostgreSQL, pytest.

### BE-VE-07 Aprobación comercial y reserva exclusiva — 15–32 h

**Fuente:** HU-45, HU-49. **Estimación:** M1 · H × 1,25–2; luego ×1,5–2. Autorización sensible y prevención de doble venta.

- Registrar aprobación/rechazo motivado por gerente comercial sobre versión exacta de importe y condiciones; todas las versiones negociadas requieren decisión explícita bajo el supuesto inicial.
- Invalidar aprobación/aceptación vigente al cambiar términos; reservar solo tras aprobación interna y aceptación del comprador registradas sobre la misma versión.
- Bloquear reserva concurrente por otro comprador mediante transacción/restricción compartida; liberar antes de cierre con motivo sin borrar negociación, coordinando restricciones contractuales si ya se envió a firma.
- TDD de dos reservas simultáneas, rol incorrecto, aprobación desactualizada y liberación prohibida si ya cerró. No calcular automáticamente una política de descuentos aún no aprobada.

**Tecnologías:** FastAPI, PostgreSQL con bloqueos/restricciones, pytest.

### BE-VE-08 Expediente jurídico e integración contractual — 18–40 h

**Fuente:** HU-48. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Requisitos, revisión exacta y dependencia de firma.

- Crear checklist versionado de documentos/condiciones de cierre configurado por negocio/abogado, sin consola de reglas; adjuntar referencias/evidencias mediante servicio privado existente.
- Preparar snapshot de comprador, inmueble, oferta aceptada y condiciones; usar plantilla Venta y contrato de entrada del módulo 7, sin rehacer generación/firma/archivo.
- Registrar revisión y aprobación jurídica con actor/fecha sobre expediente y términos concretos; cambios relevantes invalidan aprobación y exigen nueva revisión.
- TDD de requisito incompleto, documento ajeno, discrepancia precio-contrato y firma parcial. No validar títulos automáticamente ni realizar trámites notariales/registrales; evidencia externa se registra manualmente.

**Tecnologías:** FastAPI, API del módulo 7, S3/archivos compartidos, PostgreSQL, pytest.

### BE-VE-09 Registro y validación de pagos de la venta — 18–40 h

**Fuente:** HU-49. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Dinero con evidencia, abonos y control de duplicados.

- Registrar pagos/abonos por medios externos con importe, moneda, referencia, fecha y soporte; administrador valida explícitamente recepción, no basta adjuntar un archivo.
- Sumar confirmados vigentes por venta contra precio aprobado; excluir pendientes/anulados, detectar referencia duplicada y conservar correcciones compensatorias con motivo.
- Proveer IDs estables de movimientos para consumo contable futuro sin duplicación; impedir cierre con faltantes o excedentes no resueltos según supuesto de pago completo.
- TDD de dos registros iguales, importe/moneda incorrectos, abonos, anulación y soporte ausente. No incluye checkout, recaudo digital, liquidación bancaria, gestión de crédito, reembolsos ni factura DIAN.

**Tecnologías:** FastAPI, Decimal, PostgreSQL, servicio privado de soportes, pytest.

### BE-VE-10 Entrega y cierre atómico de la venta — 24–48 h

**Fuente:** HU-49. **Estimación:** M1 · H × 2–3; luego ×1,5–2. Cierre sensible que coordina evidencia e inventario.

- Registrar entrega con fecha, responsable, inventario/observaciones y evidencia; proponer POST /api/v1/ventas/{id}/cierre con clave idempotente y versión esperada.
- Verificar reserva válida, términos/contrato coincidentes, firma y archivo confirmados, checklist jurídico vigente, pago total validado y entrega registrada; no cerrar por firma sola.
- En transacción registrar cierre, marcar disponibilidad comercial Vendido, oportunidad Ganada y demás oportunidades del inmueble Perdidas por inmueble vendido; conservar Adquirido como hecho histórico de adquisición.
- Persistir evento/outbox de retiro web y pendientes externos; reintentar integración sin duplicar cierre. TDD de carreras, cierre parcial, repetición y fallo posterior al commit.
- Tras cierre no habilitar edición de precio/pago o reapertura ordinaria: registrar incidente/corrección pendiente para flujo fuera del alcance inicial, sin falsear consistencia del cierre.

**Tecnologías:** FastAPI, PostgreSQL, patrón outbox/worker, pytest.

### BE-VE-11 Embudo, ofertas y tiempos de cierre — 18–40 h

**Fuente:** HU-50. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Métricas por oportunidad/venta con períodos y versiones diferentes.

- Proponer GET /api/v1/ventas/indicadores con filtros por asesor/origen/período y conteos de oportunidades por etapa, ofertas vigentes y ventas cerradas.
- Calcular tiempo de cierre desde creación de oportunidad ganadora hasta cierre; comparar precio objetivo y precio final, sin calcular rentabilidad ni confundir valor vendido con cobros.
- Definir embudo de cohorte creada en período con etapa actual al corte; ventas filtradas por fecha de cierre y ofertas por fecha de creación, explicando universos.
- TDD de varias ofertas/versiones por inmueble, prospecto con varios intereses, cero cierres y fechas límite; evitar contar múltiples veces una venta por pagos/documentos.

**Tecnologías:** SQLAlchemy, PostgreSQL, Decimal, pytest.

### BE-VE-12 Permisos por operación y auditoría — 12–24 h

**Fuente:** HU-40, HU-41, HU-43, HU-45, HU-48, HU-49, HU-50, HU-33 (dependencia transversal). **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Roles comerciales/jurídicos y datos privados frente a público.

- Adaptar identidad existente: gerente de activos asigna ruta/objetivo; asesor registra ficha/prospectos/visitas; gerente comercial aprueba precio; abogado revisa; administrador valida pagos/entrega/cierre.
- Asegurar aislamiento del catálogo público y acceso interno; comprador usa solo su sesión contractual del módulo 7, sin obtener CRM ni datos de otras ofertas.
- Auditar cambios con actor, fecha, versión y motivo; probar matriz de permisos/ID ajeno y consistencia dato-auditoría. Los cargos específicos de ventas se acuerdan en HU-33; no construir nueva consola de roles.

**Tecnologías:** Dependencias FastAPI, RDS, pytest.


## 2 Frontend — 90–192 h

### FE-VE-01 Ficha de venta y administración de anuncios — 15–32 h

**Fuente:** HU-40, HU-41, HU-42. **Estimación:** M1 · A1 × 2,5–4; luego ×1,5–2. Analogía parcial A1: varios formularios de contenido y precio.

- Crear listado/ficha con elegibilidad, alistamiento, objetivo, precio publicado, fotos y documentos internos; publicación/retiro y registro de enlaces externos.
- Mostrar qué campos son públicos y vista previa de la versión a publicar; separar precio objetivo de autorizado y estado de adquisición de disponibilidad.
- TDD de validación, permisos, reintentos, contenido incompleto y retirada pendiente externa; reutilizar componentes privados de archivos.

**Tecnologías:** Next.js, TypeScript, React Hook Form, Zod, Testing Library.

### FE-VE-02 Catálogo web propio de inmuebles en venta — 12–24 h

**Fuente:** HU-42. **Estimación:** M1 · A1 × 2–3; luego ×1,5–2. Vista pública nueva con datos estrictamente limitados.

- Crear listado paginado y ficha por slug con fotos aprobadas, descripción, precio y contacto de la compañía; enlace de contacto existente sin formulario público de captación.
- Usar diseño web existente adaptable a celular, títulos/metadatos básicos y estados retirado/no disponible; no prometer retirar copias ya descargadas o cacheadas por terceros.
- TDD de navegación móvil/teclado, publicación/actualización y campos privados ausentes. Sin mapas, buscador avanzado, campañas SEO, marketplace ni branding nuevo.

**Tecnologías:** Next.js, TypeScript, API pública de venta, Testing Library.

### FE-VE-03 CRM de prospectos, visitas y seguimientos — 15–32 h

**Fuente:** HU-43, HU-44. **Estimación:** M1 · A1 × 2,5–4; luego ×1,5–2. Nuevas vistas comerciales reutilizan historial y agenda del módulo 5.

- Crear bandeja/ficha de prospectos y oportunidades por inmueble con origen, interés, responsable y etapas; adaptar FE-CRM-02/03 para actividades, visitas y pendientes.
- Mostrar correcciones y cambios de responsable; agendar/reprogramar visita y registrar interés/resultado, sin duplicar el componente de recordatorios.
- TDD de múltiples oportunidades, ID ajeno, conflicto, filtros y uso móvil; sin portal del comprador ni CRM externo.

**Tecnologías:** Next.js, TypeScript, componentes CRM compartidos, Testing Library.

### FE-VE-04 Negociación y aprobación de ofertas — 18–40 h

**Fuente:** HU-45. **Estimación:** M1 · A1 × 3–5; luego ×1,5–2. Versiones monetarias, comparación y acciones restringidas.

- Construir formulario y tabla comparativa de ofertas/contraofertas, historial de términos y decisiones motivadas del gerente comercial.
- Registrar aceptación del comprador con evidencia y reservar solo la versión elegible; mostrar invalidación de aprobación al cambiar condiciones.
- TDD de revisión antigua, importes, permiso y reserva concurrente; no aceptar automáticamente por superar el precio objetivo.

**Tecnologías:** Next.js, TypeScript, Zod, Testing Library.

### FE-VE-05 Expediente, pagos, entrega y cierre — 18–40 h

**Fuente:** HU-48, HU-49. **Estimación:** M1 · A1 × 3–5; luego ×1,5–2. Varias evidencias y condiciones antes de una acción sensible.

- Crear panel de checklist jurídico/documentos y enlace al flujo contractual existente; mostrar firma/archivo separados de aceptación comercial.
- Registrar y validar abonos/soportes, entrega y pendientes; presentar resumen de precio, pago total, requisitos y confirmación de cierre con permisos específicos.
- TDD de requisito faltante, firma parcial, pago no validado, cierre repetido y error recuperable. Sin nuevas pantallas de firma, checkout ni trámites externos.

**Tecnologías:** Next.js, TypeScript, componentes de archivo/contrato compartidos, Testing Library.

### FE-VE-06 Tablero de resultados comerciales — 12–24 h

**Fuente:** HU-50. **Estimación:** M1 · A1 × 2–3; luego ×1,5–2. Embudo y resultados con universos de fecha explícitos.

- Mostrar etapas, ofertas, ventas cerradas, valores y tiempos de cierre; filtros por asesor/origen/período y enlace a detalle autorizado.
- Explicar diferencia entre cohorte de oportunidades y cierres del período; mostrar No aplica para promedio sin cierres y error distinto de cero.
- TDD de filtros, permiso gerencial y presentación móvil; sin BI externo, atribución publicitaria avanzada ni exportaciones masivas.

**Tecnologías:** Next.js, TypeScript, componentes gráficos accesibles, Testing Library.


## 3 Infraestructura incremental y observabilidad — 21–44 h

### OPS-VE-01 Publicación segura y retiro recuperable — 12–24 h

**Fuente:** HU-42, HU-49. **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Contenido público separado del privado e invalidación tras cierre.

- Configurar rutas/dominio existente para catálogo, copias de fotos autorizadas, permisos y política de caché; no habilitar acceso público al bucket privado de expedientes.
- Desplegar procesamiento de outbox/retiro y reintentos sobre worker compartido; verificar que ficha retirada no siga mostrando oferta disponible en origen/caché controlada.
- Sin integrar portales externos ni crear infraestructura completa por módulo.

**Tecnologías:** Next.js desplegado, S3, CloudFront si se usa, IAM, worker y CDK/CloudFormation.

### OPS-VE-02 Métricas, trazas y alarmas operativas — 9–20 h

**Fuente:** HU-43, HU-49, HU-50. **Estimación:** M1 · H × 0,75–1,25; luego ×1,5–2. Exposición pública, cierres y eventos requieren observabilidad.

- Instrumentar fallos de publicación/retiro, eventos de cierre pendientes, integraciones CRM/firma y latencia de indicadores.
- Extender alarmas/logs existentes y comprobar señal de prueba; excluir PII, soportes y URLs privadas. Auditoría de negocio permanece en RDS.

**Tecnologías:** CloudWatch, SNS, logs estructurados.


## 4 Validación transversal — 42–92 h

### QA-VE-01 Recorrido comercial hasta inventario vendido — 18–40 h

**Fuente:** HU-40, HU-41, HU-42, HU-43, HU-44, HU-45, HU-48, HU-49. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Integración entre adquisición, web, CRM, contrato y cierre.

- Ejecutar activo elegible → ficha/publicación → prospecto/visita → contraoferta/aprobación/aceptación → reserva → revisión jurídica → firma sandbox → pago validado → entrega → cierre.
- Verificar retiro web y pendientes externos, conservación del histórico y métricas finales; declarar simulaciones si una dependencia no está disponible.
- No repetir unitarias ni validación del motor genérico de firma/CRM ya entregado.

**Tecnologías:** Playwright, staging, sandbox del módulo 7, fixtures sintéticas.

### QA-VE-02 Concurrencia, dinero y recuperación de cierre — 15–32 h

**Fuente:** HU-45, HU-49, HU-50. **Estimación:** M1 · H × 1,25–2; luego ×1,5–2. Venta única e invariantes frente a reintentos/fallos.

- Probar dos reservas/cierres competidores, aprobación obsoleta, abonos duplicados, faltante/excedente y cambio de condiciones tras revisión.
- Interrumpir retiro después del commit y recuperar sin doble venta; ensayar migración/recuperación y conciliar tablero con dataset conocido de ofertas/versiones/pagos.
- Separar validación transversal de las unitarias de transacción; no certificar conciliación bancaria externa.

**Tecnologías:** pytest/HTTPX, PostgreSQL, worker, CloudWatch en staging.

### QA-VE-03 Privacidad pública y matriz de acceso — 9–20 h

**Fuente:** HU-41, HU-42, HU-43, HU-45, HU-48, HU-49, HU-50. **Estimación:** M1 · H × 0,75–1,25; luego ×1,5–2. Validar límites entre visitante, comprador y roles internos.

- Comprobar catálogo sin datos privados, acceso directo a IDs/archivos y permisos de asesor/gerentes/abogado/administrador/propietario original.
- Verificar móvil/teclado, retiro de contenido y filtros con volumen acordado; no incluye pentest externo ni auditoría SEO.

**Tecnologías:** Playwright, HTTPX, staging y datos sintéticos.


## 5 Entrega — 9–20 h

### REL-VE-01 Despliegue, guía y aceptación de venta — 9–20 h

**Fuente:** HU-40, HU-41, HU-42, HU-43, HU-44, HU-45, HU-48, HU-49, HU-50. **Estimación:** M1 · H × 0,75–1,25; luego ×1,5–2. Activación coordinada de publicación, permisos y cierre.

- Preparar migraciones, publicación por ambientes y smoke de catálogo/ficha/expediente/indicadores usando pipeline existente.
- Entregar ADR, OpenAPI, matriz de evidencia, guía por rol y procedimientos de reserva/retiro/incidentes posteriores a cierre.
- Separar aprobaciones de negocio, contenidos y tiempos de firma/trámites de las horas-persona. Esta cotización no publica anuncios ni ejecuta ventas reales.

**Tecnologías:** Git, pipeline AWS, OpenAPI y Markdown.

## 6 Dependencias y base compartida

| Dependencia | Se reutiliza | Trabajo incremental aquí |
|---|---|---|
| Módulo 2 | Inmueble adquirido, autorización de ruta y servicio privado de archivos | Ficha comercial/objetivo y vínculos; permisos/copia publicable; control de disponibilidad |
| Módulo 5 | BE-CRM-03/04/05 para actividades/tareas/avisos; FE-CRM-02/03 y ejecución compartida | BE-VE-04/05 y FE-VE-03 adaptan recurso oportunidad, prospectos y visitas; embudo de venta nuevo |
| Módulo 6, si hay adecuaciones | Estado/evidencias de obra | Referencia de alistamiento, sin gestionar obra |
| Módulo 7 | Plantilla Venta, revisión de PDF, firma y archivo | BE-VE-08 y FE-VE-05 preparan expediente/términos, consumen contrato de entrada y validan requisitos de cierre |
| Inventario/arriendo | Disponibilidad y contratos activos si ya existe módulo 8 | Verificar incompatibilidad; no mover automáticamente un activo de Arriendo a Venta |
| Módulo 10, consumidor futuro | Contabilidad y rentabilidad | Referencias de cierre/pago para consumo sin duplicar; sin integración contable completa |

No se verificó código entregado de esas dependencias. Si faltan, hay que estimar/implementar lo necesario antes de declarar completo el flujo de venta. La base técnica no sustituye CRM, archivos, adquisición ni contratos. Mocks sirven para desarrollo, no prueban integración operativa.

El [módulo 5](crm-epica.md) está estimado en **191–420 h**, pero incluye funciones de adquisición no requeridas por venta: no sumar toda esa épica por defecto. Revisar qué motor genérico se necesita y asignar su creación una sola vez; el escenario aquí presupone esos componentes funcionales. BE-VE-04/05 incluyen adaptación real a compradores/oportunidades, no un descuento por una épica escrita.

El [módulo 7](contratos-firma-epica.md) está estimado en **267–564 h** y se contrata una sola vez si falta. Su BE-CT-08 define mapeos genéricos; BE-VE-08 agrega expediente y chequeos propios de venta y consume ese contrato, sin rehacer plantilla/motor de firma. Si módulo 8 ya entrega componentes de ficha/pagos manuales, evaluar compatibilidad antes de descontar trabajo; no se presume su disponibilidad ni se depende de su pasarela.

La base técnica pendiente se toma de [BASE-01 a BASE-05 del módulo 2](ficha-inmueble-epica.md#6-base-compartida-si-aún-no-está-implementada): **78–176 h**. Se paga una sola vez para el producto: ambientes, pipeline, adaptación del login existente, pruebas y logs. BASE-03 no construye autenticación desde cero; esa variante se reestima aparte. BE-VE-02/08/09 adaptan archivos privados, sin volver a crear escaneo/cuarentena; si ese servicio falta, presupuestar su implementación específica.

Secuencia: definir canales/reglas → modelo/permisos → ficha/publicación y CRM → ofertas/aprobaciones/reserva → expediente/firma → pagos/entrega/cierre → indicadores/validación/activación. Frontend puede avanzar con contratos API acordados. Capacidad del equipo y dependencias definen el calendario; días-persona no equivalen a fechas.

## 7 Complejidad

| Grupo | S/M/L | Motivo |
|---|---|---|
| Ficha y publicación | M | Versiones de contenido y separación pública/privada |
| CRM y visitas | M | Varios intereses por prospecto y adaptación de agenda |
| Ofertas y reserva | L | Dinero, versiones aprobadas y exclusión de concurrencia |
| Expediente y cierre | L | Requisitos, firma, pagos, entrega e inventario atómico |
| Indicadores | M | Cohortes, períodos y conteos sin duplicar versiones |
| Operación y pruebas | M | Retiro recuperable, permisos y validación entre módulos |

S/M/L indica complejidad relativa y no se convierte automáticamente a horas.

## 8 Contingencias, consumo y aceptación

- **Reserva condicionada:** 0–4 h, una sola vez fuera del total base, ante corrección acotada de ID/campo de un contrato compartido de CRM, adquisición o firma ya entregado. Dueño: responsable de integración. Totales con esa condición: **384–824 h** con dependencias funcionales o **462–1000 h** agregando toda la base técnica. No cubre nuevos canales, firma/CRM faltante, reglas de crédito ni reapertura de ventas cerradas; esos cambios se reestiman. No sumar una reserva porcentual por el riesgo ya incluido en M1.
- **Consumo AWS separado:** API/web/worker, RDS, S3/versiones/transferencia, CDN si se usa, KMS y CloudWatch. Dimensionar con región, tráfico público, cantidad/tamaño de fotos, oportunidades, documentos y retención. El catálogo no justifica crear otra infraestructura completa por módulo.
- **Servicios externos:** transacciones/licencias de firma del módulo 7, cuentas/publicidad en portales y cualquier servicio contratado. Sin canales/volumen no se inventan tarifas. No hay comisiones de pasarela de venta previstas porque no se integra recaudo digital en este alcance.
- **Esperas separadas:** aprobación de contenidos/precios/checklist, datos de comprador, firmas, confirmación operativa de pago y trámites externos. No son horas de desarrollo ni garantizan fecha de cierre.
- **Aceptación:** validar supuestos/Gherkin, conservar ADR y evidencia de integración real frente a simulaciones, registrar horas reales para recalibrar. Esta entrega es documentación de cotización; no publica inmuebles ni ejecuta transacciones reales.
