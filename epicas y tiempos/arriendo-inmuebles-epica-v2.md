# Épica del módulo 8. Arriendo de inmuebles adquiridos — v2

Cotización inicial de **HU-34 a HU-39, HU-46, HU-47 y HU-51 a HU-54** de las [historias del proyecto](../historias_de_usuario_plan_del_proyecto.md), según el [contexto del negocio](../contexto.md). Son 12 historias: alta y comercialización, candidatos, contrato, entrega/operación, obligaciones, cartera y portal con pago digital. Se conserva el formato por capas de la [épica del login](login-epica.md).

**Referencia funcional:** [criterios Gherkin propuestos](arriendo-inmuebles-criterios-aceptacion-v2.md), pendientes de validación; no se encontraron criterios aprobados específicos de arriendo. Las reglas de adquisición conservan los [criterios aprobados del módulo 2](adquisicion-inmuebles-criterios-aceptacion.md).

## Resumen de horas

| Capa | Rango |
|---|---:|
| Definición | 12–24 h |
| Backend | 294–640 h |
| Frontend | 114–240 h |
| Infraestructura incremental y observabilidad | 27–60 h |
| Validación transversal | 54–112 h |
| Entrega | 12–24 h |
| **Módulo con base y dependencias funcionales** | **513–1100 h** |
| Base técnica compartida, solo si está pendiente | 78–176 h |
| **Módulo más toda la base técnica pendiente** | **591–1276 h** |

**Estos totales no incluyen construir los módulos dependientes.** El motor contractual/firma del módulo 7, la elegibilidad de adquisición y el servicio privado de archivos deben estar disponibles o presupuestarse aparte. Agregar la base técnica no entrega esos módulos. Ver la sección 6 antes de consolidar una cotización de producto.

Horas-persona; **1 d = 8 h** como convención, no calendario. TDD, pruebas propias y revisión están dentro de las tareas funcionales; QA corresponde a recorridos y fallos entre componentes. Consumo AWS, comisiones/licencias y esperas son partidas ajenas a estas horas. No se identificó estimación anterior del módulo 8.

## Método y evidencia

Se aplica [estimate-task local](../skills/estimate-task/SKILL.md) y sus [referencias](../skills/estimate-task/references/calibration.md). [Datos y cálculo reproducible](../docs/estimaciones/modulo-8-estimacion-v2.json), [generador](../docs/estimaciones/generar_modulo_8_v2.py): `python docs/estimaciones/generar_modulo_8_v2.py`.

**Confianza baja:** sin horas reales Casabra ni patrones implementados comprobados; proveedor y reglas operativas pendientes. A1 (S9.2 / RED-3596, 0,5 d) es conexión UI a endpoint con errores/pruebas. A2 (RED-765 / PR 766, aproximadamente 1 d) es consultas y generación documental con servicios existentes. Son referencias importadas no verificadas, analogías parciales para pantallas y comprobantes. H (1 d) es unidad de hipótesis por entregables, no tiempo histórico. Las estimaciones previas no se tratan como mediciones.

**Fórmula por extremo:** `ceil(8 × días_referencia × unidades_base × factor_riesgo)`. ×ref se indica antes del riesgo. M0 usa ×1 para definición; M1 usa ×1,5–2 una sola vez por dinero, permisos, PII, migraciones o falta de patrón acreditado. No duplicar TDD/revisión ni multiplicar otra vez el total. No se aplica descuento fijo por IA. Recalibrar tras el primer cobro completo; rangos sin interpretación de percentil estadístico.

## Alcance confirmado por historias

| Historia | Resultado incluido |
|---|---|
| HU-34 | Iniciar arriendo solo para inmuebles adquiridos con ruta autorizada |
| HU-35 | Alistamiento, adecuaciones, disponibilidad y condiciones de oferta |
| HU-36 | Ficha, fotos y seguimiento manual de anuncios/enlaces |
| HU-37 | Interesados, documentos, visitas, evaluación y recomendación |
| HU-38 | Condiciones completas y formalización mediante motor contractual |
| HU-39 | Inventario, entrega, novedades y devolución con evidencia |
| HU-46 | Cánones, vencimientos, reajustes, renovación y terminación |
| HU-47 | Tablero de ocupación, cobros, deuda, mora, vacancia y vencimientos |
| HU-51 | Portal propio, estado de cuenta y pago digital del canon |
| HU-52 | Avisos previos, vencidos y pagos sin confirmar |
| HU-53 | Estados de transacción, conciliación y pagos manuales con soporte |
| HU-54 | Comprobante interno descargable de pago confirmado |

**Reglas confirmadas del contexto:** la compañía es dueña del activo y el arrendatario es distinto del propietario original. Arriendo ocurre después de adquisición y asignación de ruta. Un pago digital solo queda confirmado con verificación del proveedor; el módulo contable consume esos movimientos para evitar duplicarlos.

### Supuestos para poder cotizar

- Una compañía, inmueble completo por contrato y un arrendatario principal; moneda COP propuesta y periodicidad mensual inicial. No se cotizan habitaciones/unidades independientes, múltiples pagadores, multimoneda ni períodos semanales. Se registran garantías/depósitos como condiciones cuando procedan según definición de negocio; no se presume su exigibilidad ni se implementa custodia/liquidación de depósitos.
- El gerente de activos inicia la ruta Arriendo consumiendo la autorización del módulo 2. El administrador de inmuebles registra alistamiento/entrega, el asesor gestiona candidatos, el administrador confirma selección/condiciones/obligaciones/pagos manuales, y el gerente consulta indicadores. La matriz concreta y separación de funciones deben aprobarse.
- Candidatos y evaluación registrados por equipo interno, con decisión manual y documentos privados. Sin solicitud pública autoservicio, scoring ni consultas externas. Se registra agenda simple de visitas. El contacto seleccionado recibe acceso al portal mediante identidad existente o invitación sobre el login compartido; no se reutiliza el rol de propietario original.
- Publicación consiste en preparar ficha/fotos y registrar anuncios, canales, enlaces y estado manualmente; no hay integración automática con portales ni marketplace. Se habilitan únicamente fotografías seleccionadas como publicables; no se publica el expediente privado.
- Formalización utiliza la plantilla de arriendo y flujo de dos firmantes del módulo 7: arrendatario principal y representante de compañía. Condiciones de garantías se registran como datos; codeudor/garante firmante, anexos u otrosíes requieren ampliar esa dependencia. Renovación se cotiza como nuevo contrato/período vinculado usando la misma plantilla, no como un motor de documentos adicionales.
- Contrato firmado habilita la entrega bajo requisitos acordados, pero no prueba ocupación ni pago. El inicio de obligaciones depende de la fecha efectiva pactada y activación autorizada, no de una redirección de firma. Ocupación depende de entrega/devolución real.
- Cargo mensual con vencimiento por día configurado; si ese día no existe, usar último día del mes, pendiente de acuerdo. Primera/última cuota especial puede tener importe explícito aprobado; no se calcula prorrateo automático. Reajuste por valor/porcentaje y fecha futuros ingresados y aprobados manualmente, sin consulta de índices, topes o fórmulas legales.
- Las reglas de terminación fijan fecha efectiva y cancelación prospectiva de cargos no causados; los cargos causados y saldos permanecen. Cancelaciones y ajustes son auditados, no borrado de historia. Sin penalidades, intereses, gestión judicial ni condonación automática.
- Pagos completos o abonos a una obligación seleccionada; aplicar hasta su saldo y dejar excedente como saldo a favor del mismo contrato. Reasignación manual autorizada y auditada; no aplicar entre contratos ni devolver automáticamente. Mantener suma de importe aplicado y no aplicado igual a pagos confirmados vigentes, netos de reversos.
- Un proveedor y un medio de pago inicial mediante checkout alojado, con API/sandbox, webhook autenticable, consulta de estado/referencia y tratamiento de reversos. No se almacenan tarjetas ni se implementan débitos automáticos. Identificar proveedor, medio, comisiones, límites y posibilidades de prueba antes de implementar.
- Pagos manuales quedan pendientes hasta validación explícita por administrador con referencia y soporte; el equipo contrasta evidencia bancaria fuera del sistema. El soporte solo no confirma pago. No se permite marcar un pago digital exitoso contra el resultado del proveedor.
- Recordatorios in-app y por correo transaccional: antes del vencimiento, vencido y transacción sin confirmar. Antelación/frecuencia configurables acotadas, zona propuesta America/Bogota. Reintentos y deduplicación interna, sin prometer recepción exactamente una vez en el buzón. Sin SMS, WhatsApp, push o llamadas.
- Comprobante interno único por pago confirmado, incluyendo abonos; disponible en portal y aviso con enlace. No se presenta como factura DIAN ni paz y salvo. Reversos conservan original y estado actualizado/registro compensatorio. Emitir recibo o enviar correo no altera el saldo.
- App web Next.js adaptable a celular, FastAPI, RDS PostgreSQL propuesto y S3. Archivos limitados inicialmente a PDF/JPEG/PNG, con tamaños/cantidades pendientes; carga privada validada mediante servicio compartido. Sin modo offline, app nativa ni gestión avanzada de mantenimiento.

### Estados y métricas propuestos

| Dimensión | Regla propuesta |
|---|---|
| Disponibilidad | En alistamiento, Disponible, Reservado u Ocupado; independiente de Adquirido y de publicación |
| Solicitud | Registrada, En evaluación, Recomendada, Seleccionada, Rechazada o Retirada; administrador confirma selección bajo exclusión de concurrencia |
| Contrato operativo | En preparación, Pendiente de firma, Formalizado, Activo, Terminado o Cancelado; sin superposición operativa de vigencias |
| Obligación | Pendiente, Parcial, Saldada o Cancelada; vencida es condición de fecha/saldo, no pérdida de historial |
| Transacción | Pendiente, Confirmada, Fallida o Por conciliar; reverso se registra como movimiento compensatorio ligado a la confirmación original |
| Ocupación | Conteo/ratio al corte por entrega y devolución; indicar total de activos de arriendo y excluir registros incompletos explícitamente |
| Vacancia | Días disponibles sin ocupante; alistamiento se muestra aparte y se excluye de días disponibles |
| Ingresos operativos | Cobros confirmados en período de pago menos reversos en el período, separados de canon causado, saldo y comisiones |
| Mora | Saldo vencido y días desde vencimiento; no implica cálculo de interés ni valoración legal |

La confirmación del navegador nunca mueve dinero. Webhooks verificados y consulta del proveedor determinan resultado. Referencia/moneda/importe inconsistentes pasan a conciliación. Una confirmación tardía puede producir saldo a favor si el cargo ya fue cubierto; no se descarta dinero. Reversos revierten imputaciones de manera trazable y pueden reabrir deuda. Terminar contrato o devolver el inmueble no elimina obligaciones previas.

**Pendientes:** campos y documentos de candidatos, aprobadores, moneda/periodicidad finales, garantías y depósitos, fecha de activación, reglas del primer/último período, reajustes, renovaciones/terminación, proveedor/medio de pago, comisiones, disputas, frecuencia de avisos, política de retención, volumen y metas de rendimiento. Son decisiones de cotización inicial; no se inventan reglas legales ni se las presenta como aprobadas.

**Fuera de alcance adicional:** contabilidad general, factura electrónica/DIAN, rentabilidad consolidada, conciliación bancaria por archivos, ejecución de reembolsos, cartera judicial, portales de proveedores, pólizas, automatización de mantenimiento y exportaciones BI avanzadas. El módulo 10 recibe referencias de movimientos confirmados/compensatorios: no vuelve a registrar un canon ya cobrado.

## Tabla de estimación por tarea

| ID | h | d | Modo | Referencia × unidades; riesgo | Motivo / verificación |
|---|---:|---:|---|---|---|
| AN-AR-01 | 12–24 | 1,5–3 | M0 | H × 1,5–3; ×1–1 | Reglas y proveedor pendientes; decisiones sin implementación. |
| BE-AR-01 | 24–48 | 3–6 | M1 | H × 2–3; ×1,5–2 | Varias relaciones, datos personales y registro monetario consistente. |
| BE-AR-02 | 15–32 | 1,875–4 | M1 | H × 1,25–2; ×1,5–2 | Elegibilidad y disponibilidad no deben alterar adquisición. |
| BE-AR-03 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Separar información publicable de expediente privado. |
| BE-AR-04 | 21–48 | 2,625–6 | M1 | H × 1,75–3; ×1,5–2 | PII, documentos y decisiones de selección trazables. |
| BE-AR-05 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Mapeo contractual, identidad y prevención de doble ocupación. |
| BE-AR-06 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Historial de custodia y evidencias por contrato. |
| BE-AR-07 | 30–64 | 3,75–8 | M1 | H × 2,5–4; ×1,5–2 | Reglas temporales y monetarias con cambios prospectivos. |
| BE-AR-08 | 24–56 | 3–7 | M1 | H × 2–3,5; ×1,5–2 | Dinero: saldos y movimientos deben conservarse bajo concurrencia. |
| BE-AR-09 | 24–56 | 3–7 | M1 | H × 2–3,5; ×1,5–2 | Integración externa nueva, importe autorizado y envío incierto. |
| BE-AR-10 | 30–64 | 3,75–8 | M1 | H × 2,5–4; ×1,5–2 | Eventos duplicados/desordenados y liquidación monetaria consistente. |
| BE-AR-11 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Confirmación manual de dinero con evidencia y control de duplicados. |
| BE-AR-12 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Programación con pagos concurrentes y destinatarios sensibles. |
| BE-AR-13 | 12–24 | 1,5–3 | M1 | A2 × 1–1,5; ×1,5–2 | Analogía parcial A2: PDF derivado de movimientos confirmados. |
| BE-AR-14 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Agregados monetarios y temporales sin duplicar movimientos. |
| BE-AR-15 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Datos privados, acceso del arrendatario y correcciones monetarias. |
| FE-AR-01 | 15–32 | 1,875–4 | M1 | A1 × 2,5–4; ×1,5–2 | Analogía parcial A1: lista, ficha y anuncios con permisos. |
| FE-AR-02 | 15–32 | 1,875–4 | M1 | A1 × 2,5–4; ×1,5–2 | PII, carga de documentos y decisión compartida. |
| FE-AR-03 | 18–40 | 2,25–5 | M1 | A1 × 3–5; ×1,5–2 | Formularios monetarios y cambios efectivos en el tiempo. |
| FE-AR-04 | 12–24 | 1,5–3 | M1 | A1 × 2–3; ×1,5–2 | Formulario móvil de inventario con archivos e historial. |
| FE-AR-05 | 18–40 | 2,25–5 | M1 | A1 × 3–5; ×1,5–2 | Saldo, estados de pago y correcciones con soporte. |
| FE-AR-06 | 24–48 | 3–6 | M1 | A1 × 4–6; ×1,5–2 | Varias vistas móviles con identidad, dinero y retorno externo. |
| FE-AR-07 | 12–24 | 1,5–3 | M1 | A1 × 2–3; ×1,5–2 | Métricas con cortes y denominadores explícitos. |
| OPS-AR-01 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Credenciales, callbacks y trabajos sensibles recuperables. |
| OPS-AR-02 | 9–20 | 1,125–2,5 | M1 | H × 0,75–1,25; ×1,5–2 | Datos privados y fallos de dinero/avisos que requieren visibilidad. |
| QA-AR-01 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Integración entre adquisición, candidatos, contrato y ocupación. |
| QA-AR-02 | 24–48 | 3–6 | M1 | H × 2–3; ×1,5–2 | Dinero bajo concurrencia y contrato real del proveedor. |
| QA-AR-03 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Recorrido del arrendatario y canales de notificación reales. |
| REL-AR-01 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Activar cartera, pagos y avisos requiere coordinación y evidencia. |

## 0 Definición — 12–24 h

### AN-AR-01 Definir operación, obligaciones y contrato de pagos — 12–24 h

**Fuente:** HU-34, HU-35, HU-36, HU-37, HU-38, HU-39, HU-46, HU-47, HU-51, HU-52, HU-53, HU-54. **Estimación:** M0 · H × 1,5–3; luego ×1–1. Reglas y proveedor pendientes; decisiones sin implementación.

- Acordar elegibilidad, alistamiento, selección, entrega/devolución, cronograma mensual, reajustes, abonos, imputación y cierre con deuda.
- Definir métricas de cartera/ocupación, permisos, canales de aviso y mecanismo de alta del arrendatario; mapear las 12 historias a criterios Gherkin y ADR.
- Revisar API/sandbox del proveedor de pagos: checkout alojado, referencias únicas, webhooks verificables, consulta, reversos y estados inciertos. La estimación presupone estas capacidades, no un proveedor elegido.

**Tecnologías:** Markdown, OpenAPI, Gherkin y sandbox del proveedor por seleccionar.


## 1 Backend — 294–640 h

### BE-AR-01 Modelo de arriendo y migraciones — 24–48 h

**Fuente:** HU-34, HU-37, HU-38, HU-39, HU-46, HU-53. **Estimación:** M1 · H × 2–3; luego ×1,5–2. Varias relaciones, datos personales y registro monetario consistente.

- Modelar ficha de arriendo, anuncio, candidato/solicitud, visitas, vínculo contractual, entrega/devolución, novedades, obligaciones, transacciones, imputaciones, avisos y comprobantes.
- Reutilizar identidad/inmueble del proyecto; usar Decimal y moneda por contrato, referencias externas únicas e índices por vencimiento/contrato.
- Probar migraciones, integridad y exclusión de contratos operativos superpuestos para un inmueble completo. Sin multiunidad ni modelo de copropiedad.

**Tecnologías:** SQLAlchemy 2, Alembic, RDS PostgreSQL, pytest y Testcontainers.

### BE-AR-02 Alta en arriendo y alistamiento — 15–32 h

**Fuente:** HU-34, HU-35. **Estimación:** M1 · H × 1,25–2; luego ×1,5–2. Elegibilidad y disponibilidad no deben alterar adquisición.

- Proponer GET/POST /api/v1/arriendos/inmuebles y PATCH de condiciones; consumir la asignación Arriendo del módulo 2 con permiso de gerente de activos, sin construir otra máquina de adquisición.
- Registrar adecuaciones, alistamiento, disponibilidad, canon de oferta, depósitos/garantías declarados, servicios y condiciones; distinguir disponibilidad operativa de estado de publicación.
- Validar Adquirido y ruta Arriendo, impedir doble alta y publicación no disponible. Adecuaciones se vinculan al módulo 6 si existe; no se gestiona obra aquí.

**Tecnologías:** FastAPI, Pydantic, SQLAlchemy, pytest.

### BE-AR-03 Ficha comercial y seguimiento de anuncios — 12–24 h

**Fuente:** HU-36. **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Separar información publicable de expediente privado.

- Gestionar descripción, selección de fotos autorizadas, precio, canales, enlaces y estados de anuncios registrados manualmente.
- Reutilizar servicio privado de archivos; habilitar solo copia/selección expresamente publicable de fotografías, sin exponer documentos o datos de candidatos.
- TDD de visibilidad, anuncio duplicado, enlace inválido y retiro al ocupar/no disponer. No publicar automáticamente en portales ni construir un marketplace público.

**Tecnologías:** FastAPI, S3 mediante servicio compartido, PostgreSQL, pytest.

### BE-AR-04 Interesados, solicitudes, visitas y evaluación — 21–48 h

**Fuente:** HU-37. **Estimación:** M1 · H × 1,75–3; luego ×1,5–2. PII, documentos y decisiones de selección trazables.

- Proponer /api/v1/arriendos/solicitudes con contacto, inmueble, documentos, visitas, resultado y recomendación; registrar evaluación manual y motivo por asesor autorizado.
- Validar coincidencias básicas por identificación/contacto para alertar duplicados, sin fusiones automáticas; administrador confirma candidato elegido y reserva bajo control de concurrencia.
- Probar acceso a documentos por solicitud, transiciones, visitas y dos selecciones simultáneas. Reutilizar carga/validación privada; sin scoring, aseguradora, centrales de riesgo ni KYC externo.

**Tecnologías:** FastAPI, Pydantic, PostgreSQL, servicio compartido de archivos, pytest.

### BE-AR-05 Formalización y acceso del arrendatario — 18–40 h

**Fuente:** HU-38, HU-51. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Mapeo contractual, identidad y prevención de doble ocupación.

- Construir snapshot de canon, periodicidad, día de pago, vigencia, reajustes, obligaciones y garantías; enviarlo al motor del módulo 7 y consultar firma/archivo confirmados.
- Vincular arrendatario a identidad existente o invitación de activación usando autenticación compartida; comprobar titularidad de invitación, expiración y no elevación de privilegios.
- Proteger contra contratos superpuestos; habilitar entrega cuando contrato esté formalizado y requisitos acordados cumplidos. Firma no prueba entrega ni pago.
- TDD de contrato rechazado/pendiente, usuario equivocado y activación repetida. No reconstruir plantillas, firma o archivo contractual; no crear onboarding/KYC del propietario.

**Tecnologías:** FastAPI, API del módulo 7, autenticación compartida, pytest.

### BE-AR-06 Inventario, entrega, novedades y devolución — 18–40 h

**Fuente:** HU-39. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Historial de custodia y evidencias por contrato.

- Proponer /api/v1/arriendos/contratos/{id}/actas y /novedades; registrar inventario por ítem, estado, observación, fotos y fechas reales de entrega/devolución.
- Mantener correcciones versionadas y novedades con responsable/estado; usar archivos privados compartidos. Devolución cambia ocupación y deja alistamiento pendiente, sin borrar deudas.
- TDD de doble entrega/devolución, archivo ajeno y corrección con autor. Sin órdenes de mantenimiento, proveedores, tasación automática de daños ni nueva firma de actas.

**Tecnologías:** FastAPI, PostgreSQL, S3 compartido, pytest.

### BE-AR-07 Calendario, reajustes, renovaciones y terminación — 30–64 h

**Fuente:** HU-38, HU-46. **Estimación:** M1 · H × 2,5–4; luego ×1,5–2. Reglas temporales y monetarias con cambios prospectivos.

- Generar obligaciones mensuales con clave única contrato/período/concepto; día configurable y último día de mes cuando no exista el día indicado, bajo supuesto a validar.
- Aplicar reajuste futuro con fecha y valor/porcentaje introducido y aprobado por administrador; conservar versiones, sin índices legales o tasas automáticos.
- Renovar mediante nuevo período/contrato vinculado usando módulo 7; terminar con fecha efectiva y motivo, cancelar prospectivamente obligaciones futuras no causadas según regla acordada y conservar las causadas/impagadas.
- TDD de febrero/bisiesto, fechas límite, generación concurrente, cambio retroactivo rechazado, renovación sin superposición y cierre con deuda. Prorrateos especiales, penalidades e intereses automáticos no incluidos.

**Tecnologías:** FastAPI, PostgreSQL, Decimal, datetime/zoneinfo, worker Python, pytest.

### BE-AR-08 Cuenta corriente, abonos e imputación — 24–56 h

**Fuente:** HU-46, HU-47, HU-51, HU-53. **Estimación:** M1 · H × 2–3,5; luego ×1,5–2. Dinero: saldos y movimientos deben conservarse bajo concurrencia.

- Implementar registro de movimientos e imputaciones por contrato/obligación: cargos, pagos confirmados, abonos y movimientos compensatorios, sin borrar historia.
- Imputar primero a la obligación seleccionada sin superar su saldo; excedente queda como saldo a favor no aplicado. Reasignaciones manuales autorizadas conservan trazabilidad; no cruzar contratos automáticamente.
- Calcular saldo, deuda vencida y mora en días sin inferir intereses; pagos pendientes/fallidos no disminuyen deuda. Separar monto bruto pagado de comisiones del proveedor.
- TDD de pagos parciales, dos confirmaciones simultáneas, exceso, reverso y conservación entre total confirmado vigente, importe aplicado y no aplicado. Exponer IDs estables para futuro consumo contable sin replicar contabilidad.

**Tecnologías:** PostgreSQL con transacciones/bloqueos, SQLAlchemy, Decimal, pytest.

### BE-AR-09 Inicio de pago digital del canon — 24–56 h

**Fuente:** HU-51, HU-53. **Estimación:** M1 · H × 2–3,5; luego ×1,5–2. Integración externa nueva, importe autorizado y envío incierto.

- Proponer POST /api/v1/arriendos/contratos/{id}/intentos-pago: verificar arrendatario, moneda, obligación e importe/abono contra saldo y crear referencia única antes de invocar proveedor.
- Integrar un checkout alojado, un proveedor y un medio habilitado; usar consulta por referencia/idempotencia ante timeout y limitar intentos activos sin perder confirmaciones tardías.
- TDD de importe manipulado, contrato ajeno, doble clic, intento expirado y respuesta ambigua. No almacenar datos de tarjeta, crear débitos recurrentes ni implementar billetera.

**Tecnologías:** FastAPI, HTTPX, API/sandbox de pagos por seleccionar, pytest.

### BE-AR-10 Confirmación, conciliación y reversos de pagos — 30–64 h

**Fuente:** HU-51, HU-53, HU-54. **Estimación:** M1 · H × 2,5–4; luego ×1,5–2. Eventos duplicados/desordenados y liquidación monetaria consistente.

- Verificar autenticidad de webhooks, consultar estado autoritativo cuando corresponda y comparar referencia, contrato, moneda e importe; registrar evento antes de procesar idempotentemente.
- Modelar transacción Pendiente, Confirmada, Fallida o Por conciliar; el retorno del navegador nunca confirma. Conciliar pendientes por consulta programada, con errores visibles y reproceso autorizado.
- Registrar reversos/contracargos informados como movimientos compensatorios vinculados, sin borrar la confirmación histórica; recalcular imputaciones/saldo y estado del recibo. Datos inconsistentes quedan Por conciliar sin aplicar dinero.
- TDD de evento falso, duplicado, fuera de orden, confirmación tardía, reverso y caída entre persistencia/aviso. Sin iniciar reembolsos desde la app ni conciliación bancaria masiva por extractos.

**Tecnologías:** FastAPI, HTTPX, PostgreSQL, worker Python, pytest.

### BE-AR-11 Pagos por otros medios y bandeja de conciliación — 18–40 h

**Fuente:** HU-53. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Confirmación manual de dinero con evidencia y control de duplicados.

- Registrar medio, referencia, fecha, importe y soporte privado; mantener pendiente de validación hasta confirmación explícita de administrador autorizado.
- Aplicar movimientos mediante BE-AR-08, exigir motivo para correcciones/reversiones y conservar responsable; alertar referencias duplicadas incluso frente a pagos digitales conciliados.
- Resolver bandeja Por conciliar solo con evidencia y correlación explícita; no permitir que un administrador declare exitoso un pago digital contradiciendo al proveedor.
- TDD de soporte ausente, doble registro, permisos y corrección. Comprobación bancaria queda a cargo del equipo; adjuntar soporte no confirma por sí solo.

**Tecnologías:** FastAPI, PostgreSQL, servicio compartido de archivos, pytest.

### BE-AR-12 Recordatorios y avisos de cobro — 18–40 h

**Fuente:** HU-52. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Programación con pagos concurrentes y destinatarios sensibles.

- Generar avisos antes del vencimiento, vencido y pago sin confirmar, con bandeja in-app y correo transaccional; parámetros de antelación/frecuencia configurables y acotados.
- Revalidar saldo/estado antes de enviar, deduplicar obligación/tipo/fecha/destinatario y registrar intentos, reintentos y rebotes; un pago conciliado cancela avisos futuros, no elimina correos ya enviados.
- TDD de límite horario, pago concurrente, contacto inválido, aviso duplicado y reintento. En correo incluir información mínima y enlace autenticado, sin adjuntos privados ni afirmar deuda saldada por pago pendiente.

**Tecnologías:** Worker Python, PostgreSQL, AWS SES, FastAPI, pytest.

### BE-AR-13 Comprobante interno de pago confirmado — 12–24 h

**Fuente:** HU-54. **Estimación:** M1 · A2 × 1–1,5; luego ×1,5–2. Analogía parcial A2: PDF derivado de movimientos confirmados.

- Generar comprobante interno único por pago confirmado con contrato, arrendatario, referencia, fecha, monto y aplicación/abono; guardar snapshot y PDF privado.
- Publicar en portal y avisar por canal BE-AR-12; reintentar generación/aviso sin duplicar recibo ni mover dinero. No emitir por pagos pendientes/fallidos.
- Ante reverso conservar original con estado de reversión y evidencia vinculada; reflejar vigencia en consulta. TDD de doble evento, permiso y recuperación; no es factura DIAN ni certificación de paz y salvo.

**Tecnologías:** FastAPI, renderizador PDF compartido del módulo 7, S3, pytest.

### BE-AR-14 Indicadores de operación y cartera — 18–40 h

**Fuente:** HU-47. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Agregados monetarios y temporales sin duplicar movimientos.

- Proponer GET /api/v1/arriendos/indicadores por inmueble/contrato con ocupación, vacancia, cobros confirmados vigentes, saldo, vencidos y próximos vencimientos.
- Definir ocupación por entrega/devolución, no por firma; ingresos operativos = pagos confirmados netos de reversos en período de pago, diferenciados de canon causado y comisiones.
- Vacancia = días sin ocupante estando disponible; excluir alistamiento del denominador disponible y explicarlo. Exponer fecha de corte y falta de datos.
- TDD de varias obligaciones/pagos/fotos sin multiplicar conteos, período vacío, fin de contrato con deuda y límites temporales; no calcular rentabilidad consolidada del módulo 10.

**Tecnologías:** SQLAlchemy, PostgreSQL, Decimal, pytest.

### BE-AR-15 Permisos por contrato y auditoría de negocio — 12–24 h

**Fuente:** HU-34, HU-37, HU-38, HU-39, HU-47, HU-51, HU-53, HU-33 (dependencia). **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Datos privados, acceso del arrendatario y correcciones monetarias.

- Implementar matriz de gerente de activos, asesor de arriendos, administrador de inmuebles, administrador y arrendatario sobre autenticación existente.
- Arrendatario accede solo a sus contratos/cuenta/recibos; no a evaluaciones internas ni contratos ajenos. Propietario original no obtiene acceso operativo del activo adquirido.
- Auditar cambios de condiciones, decisiones, entregas, imputaciones y pagos manuales con actor/fecha/motivo; comprobar matriz y atomicidad, sin duplicar pruebas de negocio ni construir consola de roles.

**Tecnologías:** Dependencias FastAPI, PostgreSQL, pytest.


## 2 Frontend — 114–240 h

### FE-AR-01 Inventario comercial y alistamiento — 15–32 h

**Fuente:** HU-34, HU-35, HU-36. **Estimación:** M1 · A1 × 2,5–4; luego ×1,5–2. Analogía parcial A1: lista, ficha y anuncios con permisos.

- Construir listado/ficha de arriendo con elegibilidad, condiciones, adecuaciones y disponibilidad; gestionar fotos publicables, canales y enlaces manuales.
- Mostrar por separado adquisición, ruta, ocupación y publicación; no trasladar estados del módulo 2 a disponibilidad.
- TDD de filtros, formulario, publicación no disponible, vacíos/errores y acceso móvil/teclado; sin web pública de búsqueda.

**Tecnologías:** Next.js, TypeScript, React Hook Form, Zod, Testing Library.

### FE-AR-02 Bandeja de candidatos y visitas — 15–32 h

**Fuente:** HU-37. **Estimación:** M1 · A1 × 2,5–4; luego ×1,5–2. PII, carga de documentos y decisión compartida.

- Crear solicitud/ficha de interesado, documentos, agenda simple de visitas, resultados y recomendación; selección por administrador autorizado.
- Reutilizar componentes de carga privada e historial existentes cuando estén comprobados; avisar duplicados y conflictos de selección.
- TDD de archivo rechazado, permiso, validación y cambio concurrente; sin calendario externo ni CRM de adquisición duplicado.

**Tecnologías:** Next.js, TypeScript, componentes privados de archivos, Testing Library.

### FE-AR-03 Contrato y administración de obligaciones — 18–40 h

**Fuente:** HU-38, HU-46. **Estimación:** M1 · A1 × 3–5; luego ×1,5–2. Formularios monetarios y cambios efectivos en el tiempo.

- Preparar condiciones, consultar firma/archivo del módulo 7 y administrar calendario, reajuste futuro, renovación y terminación con confirmación de efectos.
- Mostrar cargos causados frente a futuros, deuda que permanece al terminar y nueva versión contractual; no editar movimientos históricos silenciosamente.
- TDD de fecha inválida, firma pendiente, cambio retroactivo y renovación solapada; reutilizar pantallas de firma del módulo 7.

**Tecnologías:** Next.js, TypeScript, Zod, Testing Library.

### FE-AR-04 Entrega, novedades y devolución — 12–24 h

**Fuente:** HU-39. **Estimación:** M1 · A1 × 2–3; luego ×1,5–2. Formulario móvil de inventario con archivos e historial.

- Construir acta operativa por ítems, fotografías y observaciones, lista de novedades y devolución con fecha real.
- Reutilizar carga/estado de archivos y navegación contractual; mostrar alistamiento pendiente después de devolución.
- TDD de reintento, permisos y doble envío; sin offline, tasación automática ni firma de acta adicional.

**Tecnologías:** Next.js, TypeScript, File API, Testing Library.

### FE-AR-05 Cartera y conciliación administrativa — 18–40 h

**Fuente:** HU-47, HU-53. **Estimación:** M1 · A1 × 3–5; luego ×1,5–2. Saldo, estados de pago y correcciones con soporte.

- Crear bandeja de obligaciones/transacciones con filtros, detalle de abonos/imputación, pagos manuales y soporte, validación y resolución de excepciones.
- Distinguir Pendiente, Confirmada, Fallida y Por conciliar; presentar reversos históricos y saldo a favor, sin acción que confirme digital por mera declaración.
- TDD de duplicados, referencia/soporte faltante, permiso y conflicto; sin extractos bancarios masivos ni contabilidad completa.

**Tecnologías:** Next.js, TypeScript, Zod, Testing Library.

### FE-AR-06 Portal del arrendatario, pago y comprobantes — 24–48 h

**Fuente:** HU-51, HU-52, HU-54. **Estimación:** M1 · A1 × 4–6; luego ×1,5–2. Varias vistas móviles con identidad, dinero y retorno externo.

- Integrar activación de cuenta existente/invitada y portal con contrato, próximos vencimientos, deuda, pagos, avisos y recibos propios.
- Ofrecer pago/abono mediante checkout alojado; al volver consultar backend y mostrar pendiente hasta confirmación verificada, con reintento seguro cuando corresponda.
- Descargar comprobante confirmado, indicar reversión y error de archivo; TDD de contrato ajeno, importe manipulado, URL de retorno falsa y uso móvil/teclado. Sin guardar tarjetas.

**Tecnologías:** Next.js, TypeScript, autenticación compartida, checkout externo y Testing Library.

### FE-AR-07 Tablero de ocupación y cartera — 12–24 h

**Fuente:** HU-47. **Estimación:** M1 · A1 × 2–3; luego ×1,5–2. Métricas con cortes y denominadores explícitos.

- Mostrar ocupación, vacancia, cobros, vencidos y vencimientos por inmueble/contrato; navegación al detalle y filtros de período/estado.
- Explicar fecha de corte, ingresos cobrados y exclusión de alistamiento; distinguir sin datos, cero y falla.
- TDD de filtros, permiso gerencial y consistencia de cifras; sin BI externo ni exportación analítica avanzada.

**Tecnologías:** Next.js, TypeScript, componentes accesibles, Testing Library.


## 3 Infraestructura incremental y observabilidad — 27–60 h

### OPS-AR-01 Proveedor, procesos programados y correo — 18–40 h

**Fuente:** HU-46, HU-51, HU-52, HU-53, HU-54. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Credenciales, callbacks y trabajos sensibles recuperables.

- Configurar secretos de pago, webhook HTTPS, permisos de worker/colas y ejecución periódica de cargos, conciliación y avisos sobre base existente.
- Configurar SES transaccional con dominio verificado, plantillas de aviso/enlace de recibo, manejo de rebotes y ambientes de prueba; separar esperas por aprobación del servicio.
- Verificar conectividad, reintentos y DLQ/reproceso sin crear otro clúster o pipeline por módulo.

**Tecnologías:** Secrets Manager, IAM, ECS, SQS, EventBridge Scheduler, SES, CDK/CloudFormation.

### OPS-AR-02 Archivos y observabilidad de cartera — 9–20 h

**Fuente:** HU-37, HU-39, HU-53, HU-54. **Estimación:** M1 · H × 0,75–1,25; luego ×1,5–2. Datos privados y fallos de dinero/avisos que requieren visibilidad.

- Extender permisos/prefijos S3 para soportes, actas y recibos; reutilizar validación/análisis de archivos ya entregados por módulos 2/6.
- Agregar métricas de pagos sin conciliar, cargos omitidos, recibos pendientes y avisos fallidos, con alarmas de prueba; redactar PII, secretos y enlaces de pago en logs.
- Conservar auditoría en RDS; no replicar infraestructura de escaneo ni archivo contractual del módulo 7.

**Tecnologías:** S3/KMS, IAM, CloudWatch, SNS y logs estructurados.


## 4 Validación transversal — 54–112 h

### QA-AR-01 Recorrido de arriendo completo — 18–40 h

**Fuente:** HU-34, HU-35, HU-36, HU-37, HU-38, HU-39, HU-46. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Integración entre adquisición, candidatos, contrato y ocupación.

- Ejecutar inmueble adquirido → alistamiento/anuncio → candidato/visita → selección → firma sandbox módulo 7 → entrega → reajuste/renovación → devolución/terminación.
- Comprobar no superposición, evidencias y preservación de deuda tras cierre. Verificar integraciones reales disponibles y declarar mocks usados.
- No repetir unitarias ni pruebas del motor genérico de firma.

**Tecnologías:** Playwright, staging, sandbox de firma, datos sintéticos.

### QA-AR-02 Pagos, saldos y recuperación ante fallos — 24–48 h

**Fuente:** HU-46, HU-47, HU-51, HU-53, HU-54. **Estimación:** M1 · H × 2–3; luego ×1,5–2. Dinero bajo concurrencia y contrato real del proveedor.

- Ejecutar pago completo/parcial/manual, sobrepago, confirmación tardía, evento repetido, reverso y conciliación; contrastar saldo/aplicaciones/recibos con conjunto conocido.
- Inyectar caída entre confirmación e imputación/recibo y recuperar sin duplicar dinero; probar cierre de mes y ejecución programada real, migración y recuperación en staging.
- Separar escenarios reales de sandbox de simulados; no certificar conciliación bancaria o procesamiento del proveedor fuera de evidencia disponible.

**Tecnologías:** pytest/HTTPX, sandbox de pagos, PostgreSQL, S3 y CloudWatch.

### QA-AR-03 Acceso móvil, avisos y aislamiento — 12–24 h

**Fuente:** HU-37, HU-47, HU-51, HU-52, HU-54. **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Recorrido del arrendatario y canales de notificación reales.

- Validar invitación, portal móvil, pago externo y descarga de comprobante con usuarios distintos; intentar acceso cruzado a contrato/documentos.
- Comprobar antes de vencer/vencido/sin confirmar y supresión tras pago, reintento y rebote de correo con destinatarios de prueba.
- Revisar accesibilidad básica y volumen acordado; sin pentest externo ni certificación formal de carga.

**Tecnologías:** Playwright, SES de prueba, staging y fixtures sintéticas.


## 5 Entrega — 12–24 h

### REL-AR-01 Activación y entrega operativa — 12–24 h

**Fuente:** HU-34, HU-35, HU-36, HU-37, HU-38, HU-39, HU-46, HU-47, HU-51, HU-52, HU-53, HU-54. **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Activar cartera, pagos y avisos requiere coordinación y evidencia.

- Preparar migraciones/configuración productiva, habilitación por etapas de cobros/avisos, smoke y reconciliación de partida mediante pipeline existente.
- Entregar OpenAPI, ADR, guía de administrador/arrendatario y procedimientos para pagos inciertos, reversos, correo y cierre; registrar aceptación y evidencia.
- Separar contratación de proveedor, credenciales, aprobación de políticas y tiempos de firma/pago de las horas-persona. Esta estimación no cobra ni notifica a arrendatarios reales.

**Tecnologías:** Git, pipeline AWS, OpenAPI y Markdown.

## 6 Dependencias y base compartida

| Dependencia | Qué se reutiliza | Qué se cotiza aquí |
|---|---|---|
| Módulo 2 | Adquisición, inmueble, autorización de ruta y carga privada | Consumo de elegibilidad, vínculos y adaptación de archivos a candidatos/actas |
| Módulo 6, cuando hay obras | Estado de adecuaciones y evidencias existentes | Referencia y verificación operativa de alistamiento, no gestión de obra |
| Módulo 7 | Plantilla de arriendo, firma, archivo contractual y renderizador PDF | Mapeo de condiciones, acceso de arrendatario, consulta de formalización y plantilla de recibo interno |
| Autenticación/HU-33 | Sesión, invitación/activación y roles base | Vincular arrendatario a sus contratos y permisos específicos |
| Módulo 10, consumidor futuro | Contabilidad y facturación fuera de este alcance | IDs/consultas de movimientos para evitar duplicados; no integración contable completa |

La documentación no prueba implementación de esas dependencias. Si falta el módulo 7, sus **267–564 h** según la [épica contractual](contratos-firma-epica.md) se consideran aparte una sola vez y se revisan al consolidar. Este módulo no hereda otra vez ese costo. Si falta elegibilidad o servicio de archivos, presupuestar las partidas necesarias de adquisición/archivos, sin asumir que 78–176 h de infraestructura las resuelven.

La base técnica pendiente se toma de [BASE-01 a BASE-05 del módulo 2](ficha-inmueble-epica.md#6-base-compartida-si-aún-no-está-implementada): **78–176 h**, una sola vez para el producto. Incluye infraestructura/pipeline/pruebas/logs y adaptación de autenticación existente. BASE-03 no construye login desde cero; esa variante requiere reestimación sin sumar ambas. No volver a cobrar base AWS, motor de escaneo, firma o renderizador por cada módulo.

BE-AR-03/04/06/11 y OPS-AR-02 adaptan el servicio de archivos, sin construir cuarentena/antivirus desde cero. Si el CRM del módulo 5 ya aporta agenda/avisos, comprobar compatibilidad antes de descontar trabajo: candidatos de arriendo y comunicaciones de cartera tienen datos/permisos/reglas propias. La estimación no presume esa reutilización adicional.

Secuencia: cerrar políticas/proveedor → modelo/permisos → alistamiento/candidatos → contrato/entrega → calendario/cuenta → pagos/conciliación → recibos/avisos → indicadores → validación/activación. Frontend puede avanzar con contratos API acordados. Faltan capacidades/equipo para fijar calendario; los días expresan esfuerzo, no fecha de entrega.

## 7 Complejidad

| Grupo | S/M/L | Motivo |
|---|---|---|
| Ficha, anuncios y candidatos | M | Datos privados, selección y disponibilidad |
| Contrato y ciclo operativo | L | Firma dependiente, vigencias, entrega y cierre |
| Obligaciones y cuenta corriente | L | Fechas, abonos, ajustes e invariantes de dinero |
| Pagos y conciliación | L | Proveedor, eventos, concurrencia y reversos |
| Portal, avisos y recibos | L | Varios recorridos móviles y estados consistentes |
| Indicadores y operación | M | Cortes, conteos, recuperación y trazabilidad |

S/M/L expresa complejidad relativa y no se convierte automáticamente a horas.

## 8 Contingencias, consumo y entrega

- **Reserva condicionada:** 0–4 h, una sola vez fuera del total base, ante ajuste acotado de ID/campo en contrato de adquisición o firma ya entregado. Dueño: responsable de integración. Totales con esa condición: **513–1104 h** con dependencias funcionales o **591–1280 h** agregando toda la base técnica. No cubre proveedor incompatible, nuevos medios, reglas financieras adicionales ni construir módulos faltantes. No sumar reserva porcentual sobre el mismo riesgo de M1.
- **Consumo AWS separado:** API/web/worker, RDS, S3/versiones/transferencia, KMS, SQS, EventBridge Scheduler, Secrets Manager, SES y CloudWatch. Se requiere región, volumen de contratos/pagos/correos, tamaño de archivos, concurrencia y retención para dimensionar costos monetarios.
- **Servicios externos separados:** tarifas y comisiones del proveedor de pagos, transacciones de firma del módulo 7 y cualquier licencia contratada. Sin proveedor y volumen no se inventan precios ni capacidades. Importe pagado por arrendatario, comisión y liquidación al comercio son conceptos separados.
- **Esperas:** aprobación de reglas/plantillas, contratación y alta de pagos, credenciales/sandbox, dominio/SES y aceptación de negocio. No forman horas de desarrollo ni garantizan disponibilidad inmediata.
- **Aceptación:** validar supuestos/Gherkin, conservar ADR y evidencia de escenarios reales frente a simulaciones, y recalibrar con horas reales. Esta entrega documenta una cotización; no activa cobros, contratos ni notificaciones reales.
