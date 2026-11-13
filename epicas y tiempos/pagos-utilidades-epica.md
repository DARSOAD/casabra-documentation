# Épica del módulo 10. Pagos y utilidades

Cotización inicial de **HU-27 a HU-29** de las [historias del proyecto](../historias_de_usuario_plan_del_proyecto.md), según el [contexto del negocio](../contexto.md) y la estructura por capas de la [épica del login](login-epica.md). Incluye clasificación financiera, resultados por inmueble/proyecto y documentos fiscales mediante un proveedor tecnológico.

**Referencia funcional:** [criterios Gherkin propuestos](pagos-utilidades-criterios-aceptacion.md). No se encontraron criterios aprobados específicos ni una estimación anterior del módulo 10. Las reglas de reconocimiento, fórmulas y aplicabilidad fiscal de esta cotización requieren validación del contador/gerente.

## Resumen de horas

| Capa | Rango |
|---|---:|
| Definición | 12–24 h |
| Backend | 210–448 h |
| Frontend | 69–144 h |
| Infraestructura incremental y observabilidad | 21–48 h |
| Validación transversal | 42–88 h |
| Entrega | 12–24 h |
| **Módulo con base y fuentes funcionales** | **366–776 h** |
| Base técnica compartida, solo si está pendiente | 78–176 h |
| **Módulo más toda la base técnica pendiente** | **444–952 h** |

**Ambos escenarios excluyen construir las fuentes operativas.** Se requieren inmueble/identidad/archivos y contratos de datos de obra, arriendo y venta. Los pagos digitales y cartera del módulo 8 no se cotizan otra vez. Agregar infraestructura no entrega esas funcionalidades.

Horas-persona; **1 d = 8 h** como convención, no calendario. TDD, pruebas propias y revisión están incluidos en tareas funcionales. QA cubre recorridos, integraciones y recuperación entre componentes. Consumo AWS, proveedor fiscal, trámites y esperas son partidas aparte.

## Método y evidencia

Se aplica [estimate-task local](../skills/estimate-task/SKILL.md) y su [calibración](../skills/estimate-task/references/calibration.md). [Cálculo reproducible](../docs/estimaciones/modulo-10-estimacion.json) y [generador](../docs/estimaciones/generar_modulo_10.py): `python docs/estimaciones/generar_modulo_10.py`.

**Confianza baja:** sin tiempos reales Casabra ni fuentes/proveedor comprobados. A1 (S9.2 / RED-3596, 0,5 d) es referencia importada no verificada de UI a endpoint, errores y pruebas; analogía parcial para estas vistas financieras. H (1 d) es unidad de hipótesis por entregables, no medición. No se tratan estimaciones anteriores como productividad observada.

**Fórmula por extremo:** `ceil(8 × días_referencia × unidades_base × factor_riesgo)`. ×ref se expresa antes del riesgo. M0 usa ×1; M1 usa ×1,5–2 una sola vez por dinero, permisos, PII, migraciones y patrón no comprobado. No volver a multiplicar el total ni duplicar TDD/revisión. No se supone descuento fijo por IA; recalibrar con horas reales y no interpretar rangos como percentiles.

## Alcance funcional

| Historia | Resultado incluido |
|---|---|
| HU-27 | Consultar/clasificar costos e ingresos por inmueble/proyecto e importar operaciones sin duplicar pagos |
| HU-28 | Calcular y registrar resultado y retorno simple según política/versiones aprobadas |
| HU-29 | Preparar, transmitir mediante proveedor, consultar y archivar facturas y soportes fiscales |

**Confirmado por contexto:** arriendo y venta explotan inmuebles adquiridos de la compañía; un pago digital se confirma en su operación con evidencia del proveedor. Este módulo consume movimientos y sus correcciones. Emitir factura no cobra dinero, clasificar costo no demuestra desembolso y un comprobante interno del canon no sustituye un documento fiscal.

### Supuestos financieros para cotizar

- Una compañía/emisor, moneda COP inicial y un catálogo acotado de categorías aprobado por contador. Sin multicompañía, conversión de moneda, libro mayor de partida doble, nómina, declaraciones tributarias o contabilidad estatutaria completa.
- Se distingue hecho económico, reconocimiento financiero, cargo, cobro y documento fiscal mediante vínculos estables. Un canon facturado y cobrado no crea dos ingresos; un gasto de obra importado y documentado fiscalmente no crea dos costos. La fecha de reconocimiento es definida por política aprobada, no se deduce solo del pago.
- Cánones/pagos/reversos proceden de módulo 8; ventas/pagos del 9; gastos de obra del 6 y activo/adquisición del 2. La ingesta tiene clave de origen, versión, cursor y excepciones. Una fuente ausente no se reemplaza automáticamente por un movimiento manual que pueda duplicarse cuando llegue.
- Contador clasifica y aprueba mapeos simples por fuente; reparte importes manualmente entre inmuebles/proyectos conservando total. Si un proyecto pertenece a un inmueble, sus costos se incluyen una vez en el consolidado. Correcciones son versionadas/compensatorias, sin borrar movimientos originales.
- Costos/ingresos externos faltantes se registran con soporte, referencia y vínculo económico. Pago de adquisición realizado fuera de la plataforma se registra aparte y requiere validación expresa del contador con evidencia; no se ejecutan transferencias. Su confirmación/corrección puede producir el hito consumido por módulo 11.
- Propuesta gerencial de HU-28: I = ingresos reconocidos; C = costos/gastos imputables reconocidos; R = I − C. Retorno simple acumulado al corte = R/B, donde B es base de inversión aprobada con componentes identificados. Se muestran también cobros por separado. La fórmula y qué integra cada variable deben validarse; no se promete equivalencia automática a estados financieros o indicadores NIIF.
- Inversión capitalizada se conserva como base y no se resta como gasto por importar el desembolso. Si corresponde reconocer costo de venta, contador aprueba su reclasificación/importe en C; no se deduce otra vez B al calcular R. Arriendo y venta tienen políticas de reconocimiento distintas que se documentan antes de construir.
- El retorno inicial es simple, no anualizado, acumulado desde inicio de la inversión hasta corte. Reportes de período muestran I/C/R del período y etiquetan la base; no mezclan ese resultado con un retorno de otro intervalo. B cero = No aplica. Pérdida se muestra con signo; no se calcula retorno definitivo con datos incompletos.
- Cálculos registrados conservan entradas, versión de fórmula, política, moneda, inicio/corte, responsable y cobertura. Para consolidar se suman componentes compatibles o se usa un agregado autoritativo; no se promedian porcentajes sin ponderación. Sin TIR, VAN, depreciación, valorización, reparto de dividendos o proyecciones automáticas.

### Supuestos fiscales y fuentes oficiales

La DIAN describe la validación de factura electrónica y notas crédito/débito como un proceso distinto de su preparación y transmisión. Por eso el modelo separa recepción del proveedor, resultado DIAN, archivo y entrega. [DIAN: validación previa](https://www.dian.gov.co/impuestos/factura-electronica/factura-electronica/Paginas/validacion-previa.aspx).

El documento soporte de adquisiciones a no obligados a facturar y sus notas de ajuste tienen un flujo específico. Se incluyen como familia adicional de cotización, no como sinónimo de PDF de recibo. La aplicabilidad concreta a Casabra la decide el contador. [DIAN: documento soporte](https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/documento-soporte-en-adquisiciones-efectuadas-a-sujetos-no-obligados-a-expedir-factura-de-venta-o-documento-equivalente-3/).

Las contingencias distinguen causas y procedimientos; un timeout local no prueba una contingencia DIAN ni valida un documento. Se incluye registro/seguimiento del procedimiento delegado al proveedor y su posterior conciliación, sin fijar plazos legales en esta estimación. [DIAN: inconvenientes tecnológicos](https://www.dian.gov.co/impuestos/factura-electronica/inconvenientes-tecnologicos/Paginas/default.aspx). Fuentes consultadas el 13 de noviembre de 2026; confirmar normativa/anexos aplicables con proveedor y contador al implementar.

- Un proveedor tecnológico con API/sandbox para cinco tipos: factura electrónica de venta, nota crédito, nota débito, documento soporte y nota de ajuste del soporte. Selección pendiente; no se verificó una API comercial concreta. Su contrato debe cubrir firma/formato fiscal, transmisión, consulta, artefactos y entrega según documento.
- El contador determina si corresponde emitir y aprueba datos, impuestos/retenciones y tratamiento por concepto. No se asume que todas las adquisiciones, ventas o arriendos tienen el mismo tratamiento ni que facturación ocurre al confirmar el pago. Parámetros/rangos y cambios vigentes se validan antes de emitir.
- Se reutilizan tercero/operación y líneas para preparar borrador; no volver a digitar hechos económicos. Una aprobación corresponde a versión exacta. Cambios previos al envío requieren revisión; documentos validados se corrigen por el mecanismo fiscal que corresponda, sin sobrescritura.
- Numeración coordinada con un único asignador en proveedor, o mecanismo documentado equivalente. Se controla referencia/idempotencia; timeout produce consulta/conciliación, no otra emisión a ciegas. Reglas de número ante rechazo se siguen según proveedor/norma vigente, sin reutilización arbitraria.
- Se archivan XML, representación gráfica y respuesta/evidencias disponibles, con identificador fiscal correspondiente a cada tipo. La entrega al destinatario se delega al proveedor y se registra por separado. Reintentar descarga o entrega no crea otro documento ni ingreso.
- No se incluyen integración directa propia a DIAN, habilitación como proveedor tecnológico, RADIAN, documentos equivalentes POS, nómina electrónica, recepción automática de todas las facturas de proveedores, certificados propios implementados desde cero ni trámites tributarios por cuenta del cliente.

### Estados y pendientes

| Dimensión | Regla |
|---|---|
| Movimiento financiero | Pendiente de clasificación/revisión, Aprobado o Corregido con vínculo e historial |
| Cobro/pago | Estado operativo de su fuente; un documento fiscal no lo confirma ni revierte |
| Cálculo | Preliminar/Parcial o Registrado con política, corte y versión de entradas |
| Fiscal | Borrador, Aprobado para envío, En proceso, Validado, Rechazado o Por conciliar |
| Contingencia | Estado/procedimiento específico registrado y conciliado con proveedor; no equivalente a Validado |
| Archivo/entrega | Pendiente, Disponible/Entregado o Error, separados del resultado fiscal |

**Pendientes:** catálogo y política de reconocimiento, inversión/costo de venta, reparto entre proyectos/activos, impuestos/redondeos, fuentes/IDs, proveedor, tipos efectivos de soporte, volumen, numeración, certificados, responsables, contingencia y retención. Son supuestos acotados para estimar, no aprobaciones fiscales ni configuración productiva.

## Tabla de estimación por tarea

| ID | h | d | Modo | Referencia × unidades; riesgo | Motivo / verificación |
|---|---:|---:|---|---|---|
| AN-PU-01 | 12–24 | 1,5–3 | M0 | H × 1,5–3; ×1–1 | Acuerdos sobre clasificación, indicadores y proveedor sin implementación. |
| BE-PU-01 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Dinero, relaciones entre fuentes y versiones auditables. |
| BE-PU-02 | 24–48 | 3–6 | M1 | H × 2–3; ×1,5–2 | La misma operación puede aparecer como cargo, pago, gasto y factura. |
| BE-PU-03 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Reconocimiento y asignaciones deben conservar el importe total. |
| BE-PU-04 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Completar datos no presentes en fuentes sin duplicar dinero. |
| BE-PU-05 | 24–48 | 3–6 | M1 | H × 2–3; ×1,5–2 | Fórmulas y reconocimiento con riesgo de restar dos veces inversión. |
| BE-PU-06 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Totales, corte y cobertura deben ser explícitos para consumidores. |
| BE-PU-07 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Terceros, impuestos y numeración dependen de configuración validada. |
| BE-PU-08 | 24–56 | 3–7 | M1 | H × 2–3,5; ×1,5–2 | Integración fiscal externa y envíos con respuesta incierta. |
| BE-PU-09 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | Familia documental distinta de factura y recibo interno. |
| BE-PU-10 | 24–48 | 3–6 | M1 | H × 2–3; ×1,5–2 | Recepción del proveedor no equivale a validación DIAN ni entrega. |
| BE-PU-11 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Cambios monetarios y emisión requieren autoría y roles internos. |
| FE-PU-01 | 18–40 | 2,25–5 | M1 | A1 × 3–5; ×1,5–2 | Vistas monetarias con asignación y trazabilidad de fuentes. |
| FE-PU-02 | 15–32 | 1,875–4 | M1 | A1 × 2,5–4; ×1,5–2 | El usuario debe poder verificar fórmula y entradas de cada resultado. |
| FE-PU-03 | 24–48 | 3–6 | M1 | A1 × 4–6; ×1,5–2 | Cinco tipos documentales, validación y correcciones con roles. |
| FE-PU-04 | 12–24 | 1,5–3 | M1 | A1 × 2–3; ×1,5–2 | Parámetros aprobados con vigencia, no decisiones tributarias automáticas. |
| OPS-PU-01 | 12–28 | 1,5–3,5 | M1 | H × 1–1,75; ×1,5–2 | Integración externa, callbacks y credenciales por ambiente. |
| OPS-PU-02 | 9–20 | 1,125–2,5 | M1 | H × 0,75–1,25; ×1,5–2 | Artefactos fiscales y sincronización necesitan protección y alarmas. |
| QA-PU-01 | 18–40 | 2,25–5 | M1 | H × 1,5–2,5; ×1,5–2 | La consolidación requiere comprobar invariantes entre módulos. |
| QA-PU-02 | 24–48 | 3–6 | M1 | H × 2–3; ×1,5–2 | Cinco tipos, contrato real del proveedor y fallos de transmisión. |
| REL-PU-01 | 12–24 | 1,5–3 | M1 | H × 1–1,5; ×1,5–2 | Activación monetaria/fiscal requiere configuración y evidencias verificadas. |

## 0 Definición — 12–24 h

### AN-PU-01 Definir política financiera y alcance fiscal — 12–24 h

**Fuente:** HU-27, HU-28, HU-29. **Estimación:** M0 · H × 1,5–3; luego ×1–1. Acuerdos sobre clasificación, indicadores y proveedor sin implementación.

- Acordar fuentes, identificación de hechos económicos, reconocimiento de ingresos/costos, base de inversión y diferencias entre cobro, resultado y documento fiscal.
- Definir fórmulas gerenciales, períodos, moneda, categorías y correcciones; documentar Gherkin y ADR con contador/gerente.
- Revisar API/sandbox de un proveedor tecnológico para factura, notas crédito/débito, documento soporte y nota de ajuste; definir responsabilidades de numeración, firma, validación, entrega y contingencia. Contador decide aplicabilidad y tratamiento fiscal; no se redacta un dictamen tributario.

**Tecnologías:** Markdown, OpenAPI, documentación DIAN/proveedor y ADR.


## 1 Backend — 210–448 h

### BE-PU-01 Modelo financiero, fiscal y migraciones — 18–40 h

**Fuente:** HU-27, HU-28, HU-29. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Dinero, relaciones entre fuentes y versiones auditables.

- Modelar movimiento origen, hecho económico, clasificación/asignación, pago relacionado, corrección, cálculo/versiones y documento fiscal/solicitud/artefactos.
- Usar Decimal y moneda, claves únicas fuente-tipo-ID-versión, vínculos a inmueble/proyecto y restricciones de importes; separar estado financiero, fiscal y de cobro.
- TDD de integridad, migración y unicidad; no crear otra cuenta corriente de arriendo ni contabilidad general de partida doble.

**Tecnologías:** SQLAlchemy 2, Alembic, PostgreSQL en RDS, pytest y Testcontainers.

### BE-PU-02 Ingesta idempotente y conciliación con módulos fuente — 24–48 h

**Fuente:** HU-27. **Estimación:** M1 · H × 2–3; luego ×1,5–2. La misma operación puede aparecer como cargo, pago, gasto y factura.

- Consumir costos de obra del módulo 6, cánones/pagos confirmados y reversos del 8, venta/pagos del 9 y referencias de adquisición del 2; registrar procedencia y cursor de sincronización.
- Relacionar cargo/cobro/factura con un hecho económico en lugar de sumarlos como ingresos distintos; no asumir que gasto operativo reportado equivale a costo reconocido o desembolso confirmado.
- Aplicar cambios/reversos mediante correcciones trazables; dejar desajustes en bandeja de conciliación y recuperar eventos duplicados/desordenados o perdidos por consulta.
- TDD de doble ingestión, pago parcial, reverso, misma compra registrada en obra y manualmente y falta de fuente. No reejecutar pasarela ni alterar unilateralmente la conciliación operativa del módulo 8.

**Tecnologías:** FastAPI, HTTPX/servicios internos, PostgreSQL, worker Python, pytest.

### BE-PU-03 Clasificación, asignación y consulta financiera — 18–40 h

**Fuente:** HU-27. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Reconocimiento y asignaciones deben conservar el importe total.

- Proponer /api/v1/finanzas/movimientos con filtros y detalle; clasificar ingreso, costo/gasto, inversión u otro concepto según catálogo aprobado, con fecha de reconocimiento y evidencias.
- Asignar a inmueble/proyecto mediante importe o porcentaje manual; validar suma exacta y evitar que consultar proyecto e inmueble cuente dos veces el mismo componente.
- Permitir reglas simples de mapeo por tipo de fuente aprobadas por contador y revisión de excepciones; correcciones conservan clasificación/versiones anteriores.
- TDD de asignación superior/inferior al total, categoría inválida, impuesto recuperable/no recuperable según configuración aprobada y transiciones pendientes/aprobadas. Sin ERP ni motor fiscal automático.

**Tecnologías:** FastAPI, Pydantic, SQLAlchemy, Decimal, pytest.

### BE-PU-04 Costos externos y pagos de adquisición registrados — 18–40 h

**Fuente:** HU-27, HU-31 (consumidor futuro). **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Completar datos no presentes en fuentes sin duplicar dinero.

- Registrar compras/costos/ingresos externos faltantes con referencia, tercero, monto, fecha y soporte privado, vinculándolos a hecho económico existente cuando corresponda.
- Registrar por separado desembolsos de adquisición realizados fuera de la plataforma; validación explícita por contador autorizado y evidencia antes de exponer estado confirmado por operación.
- Emitir evento con ID/versión de confirmación o corrección para el módulo 11, que decide compartición; registro contable o factura por sí solos no confirman pago al propietario.
- TDD de soporte faltante, referencia duplicada contra fuentes, abonos, pago corregido y permiso. No ejecutar transferencias, conciliar extractos bancarios ni recrear pagos manuales de arriendo/venta.

**Tecnologías:** FastAPI, PostgreSQL, servicio privado de archivos, outbox, pytest.

### BE-PU-05 Resultado, retorno simple y cálculo versionado — 24–48 h

**Fuente:** HU-28. **Estimación:** M1 · H × 2–3; luego ×1,5–2. Fórmulas y reconocimiento con riesgo de restar dos veces inversión.

- Calcular por inmueble/proyecto resultado gerencial R = ingresos reconocidos I menos costos/gastos imputables C; retorno simple sobre inversión = R/B con base B aprobada y consistente en el corte.
- Separar inversión capitalizada de gasto y costo imputable de venta; no restar una adquisición como inversión y nuevamente como gasto por mera importación de un pago. Política de reconocimiento y reclasificación definida por contador.
- Guardar cálculo con versión de fórmula, entradas/categorías, período, corte, moneda, base y responsable; correcciones producen nueva versión, sin alterar histórico registrado.
- TDD de B cero, pérdidas, activo no vendido, costo de venta reconocido, fuentes parciales y consolidación por suma de componentes compatibles. Sin TIR/VAN, anualización, depreciación o valorización automáticas.

**Tecnologías:** FastAPI, Decimal, SQLAlchemy/PostgreSQL, pytest.

### BE-PU-06 API de indicadores para gerencia y portal — 12–24 h

**Fuente:** HU-27, HU-28, HU-32 (consumidor). **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Totales, corte y cobertura deben ser explícitos para consumidores.

- Proponer GET /api/v1/finanzas/resultados con filtros período/inmueble/proyecto/ruta, detalle y componentes I/C/B/R, versión y estado completo/parcial.
- Exponer cobros netos de reversos separados de ingresos reconocidos, sin confundir precio de venta con dinero recibido; no sumar monedas o bases incompatibles.
- Contrato de datos para BE-PC-06 del módulo 11: fuentes, cortes, exclusiones y denominadores; ocupación sigue en módulo 8.
- TDD de suma del detalle, proyectos ligados a activo, universo vacío y permisos; sin crear de nuevo el tablero consolidado del portal.

**Tecnologías:** FastAPI, Pydantic, PostgreSQL, pytest.

### BE-PU-07 Configuración fiscal y preparación de borradores — 18–40 h

**Fuente:** HU-29. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Terceros, impuestos y numeración dependen de configuración validada.

- Configurar una entidad emisora, datos fiscales de terceros, conceptos, tratamientos/tasas aprobados por contador y referencias de rangos/prefijos gestionados con proveedor.
- Preparar borrador desde el hecho económico, conservando fuente, líneas, base, impuestos/retenciones, totales y representación previa; emitir no depende de que el cobro ya exista.
- Revisar configuración y aplicabilidad antes de envío; validar redondeo, datos obligatorios, vigencia de rango y no duplicidad de documento objetivo.
- TDD de tercero incompleto, cambio de datos después de aprobación y monto inconsistente. Sin inferir automáticamente tributación de cada inmueble ni solicitar resoluciones DIAN por el usuario.

**Tecnologías:** FastAPI, Pydantic, Decimal, PostgreSQL, pytest.

### BE-PU-08 Factura electrónica y notas por proveedor — 24–56 h

**Fuente:** HU-29. **Estimación:** M1 · H × 2–3,5; luego ×1,5–2. Integración fiscal externa y envíos con respuesta incierta.

- Integrar un proveedor para factura y notas crédito/débito referenciadas, con aprobación del contador y snapshot exacto enviado; delegar formato fiscal/firma/transmisión conforme a contrato del proveedor.
- Reservar referencia e intento antes de envío, coordinar numeración con un único asignador y consultar por referencia ante timeout sin emitir otro documento a ciegas.
- Correcciones siguen el flujo del proveedor y tipo de documento; documento validado no se sobrescribe. Una nota no implica reembolso ni nuevo cobro por sí sola.
- TDD de envío repetido, rechazo, rango agotado, nota inválida y dos emisiones concurrentes. Sin integración directa propia con DIAN ni certificación como proveedor tecnológico.

**Tecnologías:** FastAPI, HTTPX, API/sandbox de proveedor por elegir, PostgreSQL, worker, pytest.

### BE-PU-09 Documento soporte y notas de ajuste — 18–40 h

**Fuente:** HU-29. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. Familia documental distinta de factura y recibo interno.

- Adaptar modelo y flujo de BE-PU-07/08 a documento soporte de adquisiciones a no obligados a facturar y su nota de ajuste, cuando contador determine aplicabilidad.
- Mapear comprador/emisor, tercero vendedor, concepto e identificación del documento y rangos específicos soportados por proveedor; conservar vínculo al costo ya registrado sin crearlo de nuevo.
- TDD de tercero/documento incorrecto, ajuste repetido y referencia a original; reutilizar transporte/idempotencia, sin asumir mismos campos o notas que una factura de venta.
- Sin documento de nómina, documento equivalente POS, RADIAN u otras familias fiscales no enumeradas.

**Tecnologías:** FastAPI, API del mismo proveedor, Pydantic, PostgreSQL, pytest.

### BE-PU-10 Estado fiscal, contingencia y archivo recuperable — 24–48 h

**Fuente:** HU-29. **Estimación:** M1 · H × 2–3; luego ×1,5–2. Recepción del proveedor no equivale a validación DIAN ni entrega.

- Verificar callbacks/consultas y correlación documento-intento; separar recibido por proveedor, pendiente DIAN, validado, rechazado y resultado por conciliar.
- Descargar XML, representación gráfica y respuesta/evidencia disponibles, conservar identificador fiscal correspondiente, versiones y hashes en S3 privado; entrega por proveedor con estado independiente.
- Integrar el procedimiento de contingencia soportado por proveedor/contador, con causa, estado y posterior transmisión/conciliación. Un timeout local no declara contingencia normativa ni validación exitosa.
- TDD de evento falso/duplicado/desordenado, validación sin archivo, error de entrega, contingencia y reproceso. Reintentar descarga/entrega sin emitir otra factura ni mover dinero; plazos normativos se validan al implementar, no se fijan aquí.

**Tecnologías:** FastAPI, HTTPX, PostgreSQL, S3, worker, pytest.

### BE-PU-11 Permisos financieros y auditoría — 12–24 h

**Fuente:** HU-27, HU-28, HU-29, HU-33 (dependencia). **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Cambios monetarios y emisión requieren autoría y roles internos.

- Asignar contador para clasificación/validación/operación fiscal y gerente para consulta/registro de cálculos; separar aprobación de configuración y operación según matriz acordada.
- Auditar cambios de categoría, reconocimiento, pago de adquisición, fórmula, borrador y envío con antes/después, actor y motivo; originales no se eliminan por corregirlos.
- TDD de ID ajeno, acceso de propietario/arrendatario y acción no permitida; consumidores del portal reciben únicamente datos autorizados. No recrear autenticación ni consola de roles.

**Tecnologías:** Dependencias FastAPI, PostgreSQL, pytest.


## 2 Frontend — 69–144 h

### FE-PU-01 Movimientos, clasificación y excepciones — 18–40 h

**Fuente:** HU-27. **Estimación:** M1 · A1 × 3–5; luego ×1,5–2. Vistas monetarias con asignación y trazabilidad de fuentes.

- Crear bandeja por inmueble/proyecto, detalle de origen/cobro/documento, clasificación y asignación, registro externo con soporte y validación de pagos de adquisición.
- Mostrar duplicados/desajustes y correcciones; no permitir reingresar un pago de arriendo ya sincronizado como otro ingreso.
- TDD de suma de asignaciones, formulario, conflicto y permiso; reutilizar archivos privados y tablas existentes.

**Tecnologías:** Next.js, TypeScript, React Hook Form, Zod, Testing Library.

### FE-PU-02 Resultados y cálculos de rentabilidad — 15–32 h

**Fuente:** HU-28. **Estimación:** M1 · A1 × 2,5–4; luego ×1,5–2. El usuario debe poder verificar fórmula y entradas de cada resultado.

- Crear vista por inmueble/proyecto con ingresos, costos, base de inversión, resultado, retorno simple y evolución de versiones registradas.
- Permitir calcular/registrar snapshot autorizado, revisar composición y filtros de período; mostrar parcial, No aplica o pérdida sin ocultarlos.
- TDD de denominador cero, cambios de corte y versión; no duplicar el tablero transversal de HU-32 ni mostrar previsiones como resultados reales.

**Tecnologías:** Next.js, TypeScript, componentes accesibles, Testing Library.

### FE-PU-03 Bandeja fiscal, emisión y ajustes — 24–48 h

**Fuente:** HU-29. **Estimación:** M1 · A1 × 4–6; luego ×1,5–2. Cinco tipos documentales, validación y correcciones con roles.

- Construir listado/detalle y preparación desde datos existentes para factura, notas crédito/débito, documento soporte y nota de ajuste; revisar antes de enviar.
- Mostrar estados separados de proveedor/DIAN/archivo/entrega, errores y acciones permitidas de corrección/reconsulta, con descargas autorizadas.
- TDD de documento incompleto, envío doble, rechazo, nota sobre original y archivo aún pendiente; sin edición silenciosa de documentos validados ni envío desde el frontend sin aprobación backend.

**Tecnologías:** Next.js, TypeScript, Zod, Testing Library.

### FE-PU-04 Configuración financiera y fiscal acotada — 12–24 h

**Fuente:** HU-27, HU-28, HU-29. **Estimación:** M1 · A1 × 2–3; luego ×1,5–2. Parámetros aprobados con vigencia, no decisiones tributarias automáticas.

- Crear formularios de categorías, asignación por fuente, parámetros de fórmula y metadatos fiscales/rangos consultados al proveedor, con permisos y revisión.
- Mantener historial/vigencia y avisos de configuración incompleta; secretos se gestionan por infraestructura, nunca se devuelven en pantalla.
- TDD de tasas/valores inválidos, cambio retroactivo y rol incorrecto; sin diseñador libre de fórmulas ni motor de reglas multinivel.

**Tecnologías:** Next.js, TypeScript, Zod, Testing Library.


## 3 Infraestructura incremental y observabilidad — 21–48 h

### OPS-PU-01 Proveedor fiscal, secretos y procesos de sincronización — 12–28 h

**Fuente:** HU-27, HU-29. **Estimación:** M1 · H × 1–1,75; luego ×1,5–2. Integración externa, callbacks y credenciales por ambiente.

- Configurar credenciales, conectividad, callback verificable y worker/colas para ingesta, conciliación fiscal, archivos y entrega mediante proveedor.
- Configurar reintentos y cola de fallos; verificar sandbox, aislamiento de producción y acceso mínimo a S3/secretos.
- Preparar parámetros de habilitación/rangos entregados por negocio/proveedor; no realizar trámites de la compañía ni crear nueva plataforma AWS.

**Tecnologías:** Secrets Manager, IAM, ECS, SQS, EventBridge Scheduler, CDK/CloudFormation.

### OPS-PU-02 Archivo privado y observabilidad financiera — 9–20 h

**Fuente:** HU-27, HU-29. **Estimación:** M1 · H × 0,75–1,25; luego ×1,5–2. Artefactos fiscales y sincronización necesitan protección y alarmas.

- Extender S3 privado/versionado para XML/PDF/respuestas y soportes; permisos, cifrado y retención según política acordada, sin rehacer motor documental.
- Agregar métricas/alertas de desajustes, documentos sin resultado, rechazos, rango próximo a agotarse y archivo/entrega pendientes.
- Probar alarmas y redacción de datos fiscales/secretos en logs; auditoría de negocio en RDS.

**Tecnologías:** S3/KMS, CloudWatch, SNS, IAM.


## 4 Validación transversal — 42–88 h

### QA-PU-01 Conciliación de fuentes y resultados — 18–40 h

**Fuente:** HU-27, HU-28. **Estimación:** M1 · H × 1,5–2,5; luego ×1,5–2. La consolidación requiere comprobar invariantes entre módulos.

- Validar con datos conocidos importación de obra/arriendo/venta, abonos/reversos, asignaciones y correcciones; no duplicar hechos económicos al aparecer documento fiscal.
- Contrastar I/C/B/R, retorno y versiones por activo/proyecto y contrato de salida al módulo 11; comprobar fuente caída, corte y moneda incompatible.
- Probar roles y recuperación de ingesta/migración; distinguir mocks de fuentes reales. No sustituye auditoría contable profesional.

**Tecnologías:** pytest/HTTPX, Playwright, PostgreSQL, staging y fixtures sintéticas.

### QA-PU-02 Ciclo fiscal completo y recuperación — 24–48 h

**Fuente:** HU-29. **Estimación:** M1 · H × 2–3; luego ×1,5–2. Cinco tipos, contrato real del proveedor y fallos de transmisión.

- Probar factura y notas, documento soporte y ajuste en sandbox: borrador → aprobación → envío → resultado DIAN → archivo → entrega según tipo.
- Ensayar rechazo, timeout, duplicados, número/ID inconsistente, contingencia, descarga fallida y reproceso sin doble emisión; validar integridad de XML/PDF/respuesta y permisos.
- Registrar escenarios reales frente a simulados, límites del sandbox y requisitos pendientes antes de activar; no afirmar homologación o certificación obtenida por esta cotización.

**Tecnologías:** Sandbox del proveedor, pytest/HTTPX, Playwright, S3 y CloudWatch.


## 5 Entrega — 12–24 h

### REL-PU-01 Preparación productiva y aceptación del contador — 12–24 h

**Fuente:** HU-27, HU-28, HU-29. **Estimación:** M1 · H × 1–1,5; luego ×1,5–2. Activación monetaria/fiscal requiere configuración y evidencias verificadas.

- Preparar despliegue por pipeline existente, migraciones, sincronización inicial controlada y verificación de diferencias antes de habilitar emisión.
- Entregar ADR, OpenAPI, definiciones financieras, guía de contador/gerente y runbook de contingencia/reproceso; acordar aceptación funcional con datos de prueba.
- Separar contratación, habilitación DIAN/proveedor, certificados/rangos, revisión fiscal y esperas de las horas-persona. No emitir facturas reales ni ejecutar pagos durante esta estimación.

**Tecnologías:** Git, pipeline AWS, OpenAPI y Markdown.

## 6 Dependencias y ausencia de doble cobro

| Dependencia | Se reutiliza | Incremento del módulo 10 |
|---|---|---|
| Módulo 2 / login | Inmueble, operación, identidad y archivos privados | Referencias, permisos financieros y costos/pagos de adquisición registrados |
| Módulo 6 | IDs de gastos operativos de obra y correcciones | Importación, clasificación y reconocimiento; no registrar de nuevo esos gastos |
| Módulo 8 | Cánones, cobros/abonos confirmados y reversos | Ingesta/relación con ingresos y documentos fiscales; no pasarela/cartera nueva |
| Módulo 9 | Venta, precio, pagos externos validados y soportes | Clasificación, referencia fiscal y resultado de la operación; no otro cierre de venta |
| Módulo 11 | Portal, compartición y tablero transversal | API autoritativa de resultados y evento de pago de adquisición; no repetir UI de HU-32 |
| Proveedor fiscal | Formato/firma/transmisión/validación/artefactos/entrega contratados | Adaptador, reglas de aprobación, archivo local y operación desde Casabra |

No se verificó código entregado de las fuentes. Sin datos/contratos disponibles puede desarrollarse con fixtures, pero no declararse integrada la operación. Construcción de fuentes, regularización de datos históricos y adaptación de procesos que no existen se estiman aparte. Arriendo conserva [original](arriendo-inmuebles-epica.md) y [v2](arriendo-inmuebles-epica-v2.md): son alternativas, no se suman y ninguna se considera aprobada por esta referencia.

La [épica del portal](portal-cliente-epica.md) consume BE-PU-06 y el evento de BE-PU-04; el portal mantiene su propia autorización de compartición. Ahora existe estimación del módulo 10, no implementación: formalización contractual sola no confirma el pago al propietario. La confirmación aquí prevista es un registro manual validado con evidencia de un desembolso externo.

Si falta la base técnica, agregar una sola vez [BASE-01 a BASE-05 del módulo 2](ficha-inmueble-epica.md#6-base-compartida-si-aún-no-está-implementada): **78–176 h**, desglosadas en JSON. BASE-03 adapta login existente, no lo construye desde cero. Servicios S3/worker/colas/pipeline y archivo seguro no se cobran íntegros otra vez por módulo; solo su configuración incremental.

Secuencia: política/proveedor → modelo/permisos → ingesta/clasificación → resultados/API → configuración fiscal → emisión/ajustes/archivo → pruebas → activación. Frontend puede avanzar con contrato acordado. Calendario depende de capacidad, entrega de fuentes y habilitación del proveedor; días-persona no son fechas.

## 7 Complejidad

| Grupo | S/M/L | Motivo |
|---|---|---|
| Ingesta y clasificación | L | Múltiples fuentes, hechos económicos y duplicados |
| Resultado y retorno | L | Reconocimiento, base de inversión y versiones |
| Emisión fiscal y ajustes | L | Cinco tipos documentales, proveedor y estados externos |
| Pantallas y configuración | M | Formularios monetarios, revisión y permisos |
| Recuperación y operación | L | Emisión incierta, contingencia, integridad y archivo |

S/M/L es complejidad relativa sin conversión automática a horas.

## 8 Contingencias, consumo y aceptación

- **Reserva condicionada:** 0–4 h una sola vez, fuera del total base, por ajuste acotado de ID/campo de un contrato fuente ya entregado. Dueño: responsable de integración. Totales con esa condición: **366–780 h** con fuentes funcionales o **444–956 h** agregando toda la base técnica. No cubre un proveedor incompatible, nuevos documentos fiscales, cambios de política complejos o integración DIAN directa; se reestiman. No sumar porcentaje por el riesgo ya incluido en M1.
- **Consumo AWS separado:** API/web/worker, RDS, S3/versiones/transferencia, KMS, Secrets Manager, colas/programación y CloudWatch. Precio monetario requiere región, volumen, retención y concurrencia; no se inventan tarifas.
- **Proveedor y trámites separados:** suscripción, documentos/transacciones, certificados y servicios contratados; alta/habilitación/rangos y revisión tributaria de la empresa. No se presupone precio ni compatibilidad de un proveedor no seleccionado.
- **Aceptación:** validar política, fórmulas y Gherkin; conservar evidencia sandbox y limitaciones de simulación, configurar contingencia vigente y registrar horas reales para recalibrar. Esta entrega es cotización documental; no emite facturas ni realiza pagos reales.
