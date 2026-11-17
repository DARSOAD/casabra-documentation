# Inventario de fuentes de la presentación Casabra

Documento de trabajo para verificar contenido, no una modificación de la cotización. Fecha de revisión: 17/11/2026. No se consultaron sitios web ni APIs externas.

## Método y archivos

- Fuente comercial principal: [Cotización CASABRA V2.pdf](../Cotizaci%C3%B3n%20CASABRA%20V2.pdf), 11 páginas, fecha de portada 17/11/2026.
- Extracción automática: [_fuentes/cotizacion-v2-extraida.txt](_fuentes/cotizacion-v2-extraida.txt). Es parcial: algunas celdas están dibujadas como curvas y no aparecen en la extracción. Los datos de las tablas se transcribieron y verificaron visualmente.
- Render completo verificado: `_fuentes/pagina-01.png` hasta `_fuentes/pagina-11.png`, numeración equivalente a la página física del PDF.
- Fuente funcional vigente: [contexto.md](../../contexto.md), [historias](../../historias_de_usuario_plan_del_proyecto.md), [memoria](../../docs/MEMORY.md) y [criterios aprobados de adquisición](../../epicas%20y%20tiempos/adquisicion-inmuebles-criterios-aceptacion.md).
- Fuente de instrucciones: [AGENTS.md](../../AGENTS.md). No se modifican épicas, memoria, historias ni PDF.

## Inventario página por página

| Página | Encabezado / contenido | Datos y condiciones relevantes |
|---|---|---|
| 1 | CASABRA. PLATAFORMA INTEGRAL. PROPUESTA DE DESARROLLO | Fecha: 17/11/2026. No trae valor de inversión. |
| 2 | VISIÓN DEL PROYECTO. Del conocimiento del cliente al crecimiento financiero | Conectar clientes, inmuebles y operación; comenzar con cliente, autorizaciones, inmueble, evaluaciones y compromisos; luego operación inmobiliaria y capacidad financiera propia. El inmueble es el eje y la información del cliente un activo estratégico. |
| 3 | Tres fases para construir y crecer | Fase 1: Onboarding y vinculación. Fase 2: Operación conectada. Fase 3: Evolución financiera. Resultados detallados abajo. |
| 4 | FASE 1. Onboarding y vinculación | 3 módulos, 600/400/460 horas. Controles transversales de acceso, trazabilidad y gestión de información. Nota de estimación aproximada. |
| 5 | FASE 2. Operación conectada | Se priorizará por valor, necesidades y dependencias; firma disponible donde se requiera; arriendo solo de inmuebles adquiridos. Proveedor financiero especializado para iniciar la línea; funciones sujetas al servicio contratado y alcance acordado. |
| 6 | FASE 2. Módulos propuestos | Obra520, contratos430, arriendo900, venta820, portal500 horas. Nota de estimación aproximada. |
| 7 | FASE 2. Módulos propuestos | Pagos/utilidades730, conexión proveedor100 horas. Propuesta de LeanCore. Cargo mínimo mensual USD1.500; administración cada crédito USD0,3. Nota de estimación aproximada. |
| 8 | FASE 3 CORE FINANCIERO. Evolución financiera | Núcleo propio aprovechando clientes/inmuebles/operaciones, créditos, desembolsos, pagos, cartera y nuevos productos. No define tareas, horas, presupuesto ni fecha. |
| 9 | MODALIDAD DE PAGO Y FLUJO DE TRABAJO | 40% antes de iniciar, 20% hito50, 20% hito75, 20% entrega100. Acumulados40/60/80/100. Condiciones de aprobación/aceptación abajo. |
| 10 | ¿Cómo se comprobará cada entrega? | Funciones acordadas, demostración, entorno de revisión, observaciones y validación. Primer hito con recorrido utilizable; antes revisiones de pantallas/reglas/procesos. Final: validación completa, puesta en marcha y orientación acordadas. |
| 11 | EL FUTURO EMPIEZA CON LA INFORMACIÓN | Beneficios: información que construye valor; control/trazabilidad; herramientas por rol; inversión por etapas con entregas50/75/100; capacitación y respaldo; camino hacia plataforma financiera. Garantía y soporte sujetos a condiciones acordadas. |

## Fases y alcance exacto de la cotización

### Fase 1: Onboarding y vinculación

Resultado de p3: clientes identificados, inmuebles documentados y seguimiento comercial organizado.

Incluye en p4: registro y conocimiento inicial del cliente; autorizaciones de tratamiento de información; verificación de identidad y consulta de listas mediante el proveedor acordado; expediente y proceso de adquisición del inmueble; seguimiento comercial mediante CRM; controles transversales de acceso, trazabilidad y gestión de información.

| Número en PDF | Nombre en PDF | Objetivo del PDF | Horas publicadas | Correspondencia funcional del repositorio |
|---|---|---|---:|---|
| 1 | Onboarding registro y conocimiento del cliente | Facilitar el ingreso del propietario y disponer de información inicial confiable para comenzar la relación con la compañía. | 600 | Módulo1, HU-01/02/03 |
| 2 | Adquisición de inmuebles | Conservar un expediente completo y una trazabilidad clara desde la presentación del inmueble hasta su adquisición o rechazo. | 400 | Módulo2, HU-04/05/06/07/08 |
| 3 | Seguimiento comercial - CRM | Mantener la continuidad de la relación con cada cliente y ayudar al equipo a identificar qué debe atender. | 460 | Módulo5, HU-12/13/14/15 |

Suma aritmética de las cifras publicadas: **1.460 h**. No es una nueva estimación ni un plazo de calendario.

### Fase 2: Operación conectada

Resultado de p3: gestión de obras, contratos, arriendos, ventas y resultados, con apoyo de un proveedor financiero cuando se habilite esa línea.

El PDF permite priorizar módulos según el negocio y sus dependencias. No dice que los módulos sean independientes ni que cualquier selección sea operativa sin servicios fuente.

| Número en PDF | Nombre en PDF | Objetivo del PDF | Horas publicadas | Correspondencia funcional del repositorio |
|---|---|---|---:|---|
| 1 | Proyectos de obra | Presupuestos, cronogramas, responsables, fotografías, avances, permisos y alertas de desviación. | 520 | Módulo6, HU-16/17/18/19 |
| 2 | Contratos y firma electrónica | Plantillas acordadas, revisión y firma desde el celular, archivo y trazabilidad. | 430 | Módulo7, HU-20/21/22 |
| 3 | Arriendo de inmuebles adquiridos | Alistamiento, oferta comercial, interesados, contratación, entrega, obligaciones, pagos, cartera y autoservicio del arrendatario. | 900 | Módulo8, HU-34/35/36/37/38/39/46/47/51/52/53/54 |
| 4 | Venta de inmuebles adquiridos | Preparación comercial, canales definidos, prospectos, visitas, ofertas, negociación, documentos y cierre. | 820 | Módulo9, HU-40/41/42/43/44/45/48/49/50 |
| 5 | Portal del cliente | Consulta de información e hitos autorizados para el propietario original, y reportes gerenciales. | 500 | Módulo11, HU-30/31/32 |
| 6 | Pagos y utilidades | Costos e ingresos por inmueble o proyecto, rentabilidad y facturación mediante el servicio que se acuerde. | 730 | Módulo10, HU-27/28/29 |
| 7 | Conexión con proveedor financiero | Uso de las funciones financieras contratadas con un tercero desde el recorrido acordado para Casabra. | 100 | Propuesta comercial del PDF; no hay historia del core financiero en el catálogo leído. |

Suma aritmética de las cifras publicadas: **4.000 h**. Fases1+2 completas: **5.460 h**. Son sumas de referencias aproximadas, no garantía de cronograma, presupuesto final ni prueba de trabajo ya entregado.

### Fase 3: Evolución financiera / Core financiero

El PDF propone construir el núcleo financiero propio, apoyado en la base de clientes y el conocimiento de inmuebles y operaciones. Menciona gestionar créditos, desembolsos, pagos y cartera, con crecimiento progresivo hacia nuevos productos financieros e ingresos recurrentes.

**No cotizado en detalle:** no hay desglose, horas, costo de desarrollo, fecha de inicio, duración, migración de datos, sustitución contractual del proveedor ni costo operativo del core. El eventual ahorro neto no está calculado.

## Valores monetarios y proveedor

| Dato | Valor / estado | Fuente y límite |
|---|---|---|
| Nombre | **LeanCore** | Nombre y logo coinciden visualmente en p7. No aparece Linkore. Mantener LeanCore como referencia del PDF y tratar Linkore como denominación del usuario pendiente de confirmar si refiere a otro proveedor. |
| Funciones descritas | Creación, administración y recaudo de créditos | Descripción p7. Son capacidades generales del proveedor propuesto; las contratadas dependen del servicio y del alcance acordado. |
| Cargo mínimo del servicio mensual | **1.500 USD** | Tabla p7. No implica precio total fijo ni incluye condiciones tributarias/volumen. |
| Administración de cada crédito | **0,3 USD** | Tabla p7. No aclara periodicidad, unidad de facturación precisa, inclusión o adicionalidad frente al mínimo. No presentar una fórmula contractual sumando los dos rubros sin confirmar. |
| Anualización del mínimo | **18.000 USD/año = 1.500 × 12** | Cálculo simple derivado; no aparece como total anual en PDF. Antes de variables y otras condiciones no descritas. |
| Ahorro neto al reemplazar proveedor | **Por determinar** | USD18.000 no es ahorro neto: faltan desarrollo, infraestructura, operación, mantenimiento, migración y condiciones del contrato. No hay base de retorno o plazo de recuperación. |
| Conversión a COP / TRM | **No disponible** | No hay tipo de cambio en las fuentes. No inventar conversión. |
| Precio de desarrollo por módulo | **Por definir** | PDF publica horas, sin tarifa/hora ni valores monetarios de desarrollo. |
| Total monetario del proyecto | **Por definir** | No se puede inferir solo de horas. |
| AWS y otros terceros | **Por definir / separado** | El PDF no cotiza importe de infraestructura. La memoria exige separar consumo AWS de desarrollo. |

## Pagos y entregas

La tabla p9 usa el **valor del módulo**, no el total de todos los módulos ni una mensualidad.

| Momento | Pago sobre valor del módulo | Acumulado | Condición del PDF |
|---|---:|---:|---|
| Antes de iniciar | 40% | 40% | Aprobación del alcance y programación del trabajo. |
| Hito del50% | 20% | 60% | Demostración y aceptación del primer entregable acordado. |
| Hito del75% | 20% | 80% | Demostración y aceptación del segundo entregable acordado. |
| Entrega del100% | 20% | 100% | Validación final y entrega del alcance contratado. |

Los hitos50/75/100 son avance/entregas; **no son porcentajes de los pagos**. Por módulo los pagos suman100%.

Verificación de cada entrega según p10:

1. Funciones concretas acordadas antes de iniciar.
2. Demostración con casos representativos.
3. Acceso al entorno de revisión correspondiente.
4. Registro de observaciones y validación del entregable.
5. Primer hito: recorrido que el cliente pueda utilizar y entender; antes, avances de revisión de pantallas, reglas y procesos.
6. Final: validación completa, puesta en marcha acordada y orientación de uso prevista en el alcance.

El PDF no precisa días de aceptación, procedimiento de cambio, propiedad intelectual, impuestos, vigencia de oferta, SLA, duración de garantía o soporte, horas de capacitación, ni tarifa de mantenimiento. No inventarlos. P11 sí menciona orientación, acompañamiento de puesta en marcha, garantía y soporte **bajo las condiciones acordadas**.

## Condición de las horas

P4/6/7 repiten: las horas y plazos son aproximados según información disponible; tras levantar requerimientos de cada módulo se validan alcance, complejidad y dependencias, y se acuerdan una estimación más precisa y cronograma antes de iniciar su desarrollo.

Las horas del PDF son referencias comerciales publicadas; los rangos técnicos del repositorio son estimaciones diferentes. No reemplazarlos ni mezclarlos al presentar, no llamarlos tiempos reales, y no descontar login/AWS como implementados sin evidencia. No sumar las dos versiones alternativas de arriendo.

## Relaciones funcionales vigentes

### Adquisición e inventario

La compañía **compra** los inmuebles. El propietario original aporta sus datos/documentos y participa en la adquisición. Aceptar una oferta no equivale a comprar ni autoriza todavía arriendo o venta.

| Origen | Acción | Responsable | Destino |
|---|---|---|---|
| Documentación faltante | Completar todos los datos/documentos configurados | Propietario | En estudio |
| En estudio | Enviar propuesta económica | Asesor con permiso | Propuesta enviada |
| En estudio | Rechazar indicando motivo | Asesor con permiso | Rechazado |
| Propuesta enviada | Aceptar oferta desde la app | Propietario | En proceso de compra |
| Propuesta enviada | Rechazar oferta desde la app | Propietario | Rechazado |
| En proceso de compra | Confirmar compra completada | Abogado u otra persona con permiso explícito | Adquirido |

Después de **Adquirido**, el gerente asigna **Arriendo** o **Venta** e indica si requiere adecuaciones. Las adecuaciones pueden preceder a la comercialización. Cada cambio conserva estado anterior/nuevo, fecha y responsable; permisos y estados impiden acciones incompatibles. Estados aprobados exactos: Documentación faltante; En estudio; Propuesta enviada; En proceso de compra; Adquirido; Rechazado.

La lista documental exacta y datos obligatorios son configurables/pendientes; ejemplos de HU no constituyen lista cerrada. La fecha estimada de respuesta, si no está definida, se muestra como **Por confirmar**. No inventar promesas de respuesta o plazos legales.

### Operación y flujos de información

- Onboarding aporta identidad/autorizaciones/verificaciones; adquisición aporta inmueble, expediente y titularidad; CRM conserva actividades, compromisos y seguimiento, tanto de oportunidades de adquisición como del ciclo comercial pertinente.
- Arriendo y venta son rutas de activos **ya comprados por Casabra**. No son intermediación de terceros. Propietario original, compañía y arrendatario son actores distintos.
- Contratos/firma apoya adquisición, arriendo y venta donde el proceso lo requiera. No se promete firma disponible antes de implementar y contratar su dependencia.
- Obra recibe un activo cuya ruta/adecuaciones se definieron; genera presupuesto, progreso y costos.
- Arriendo administra contrato, entrega, obligaciones, cartera, pagos y comprobantes. Pago digital se confirma solo al recibir confirmación del proveedor. Estados de transacción citados en HU-53: pendiente, confirmada, fallida o por conciliar. No emitir comprobante interno del canon como pago confirmado antes de esa confirmación.
- Venta usa CRM/prospectos, visitas, ofertas, negociación, formalización y cierre. Su cierre registra firma, pago y entrega.
- Pagos/utilidades consume movimientos operativos para costos, ingresos y rentabilidad, sin volver a registrar un pago conciliado. Facturación mediante servicio acordado; no es el core de crédito propio.
- Portal del cliente muestra información/hitos que la compañía autorice compartir con el propietario original y reportes gerenciales. No concede acceso automático a gestión interna ni convierte al antiguo dueño en administrador del activo.
- Permisos HU-33 y cumplimiento HU-09/10/11 son transversales; las autorizaciones, firmas, verificaciones y decisiones requieren trazabilidad y acceso por rol.

## Discrepancias y decisiones de presentación

| Tema | Evidencia | Tratamiento correcto para la presentación |
|---|---|---|
| Proveedor en fase1 conceptual | Usuario solicita mostrar conexión conceptual dentro del flujo inicial; PDF p7 la cotiza en fase2 por100h. | Mostrar el puente conceptual si se necesita, con nota explícita: referencia PDF fase2/100h; adelantar depende de alcance y contratación. No incorporar100h ni cargo proveedor silenciosamente en base1.460h. |
| LeanCore / Linkore | PDF dice LeanCore; nombre del usuario difiere. | Usar LeanCore como fuente y conservar aclaración pendiente, sin inventar proveedor alterno. |
| Módulos renumerados por fase | PDF reinicia numeración en fase2; repo mantiene IDs1,2,5,6...11. | Nombrar módulos con claridad y conservar correspondencia; no llamar al CRM Módulo3 del repositorio. |
| Fases del repo vs PDF | Repo Fase1 Base; Fase2 Operación; Fase3 Crecimiento (pagos/utilidades+portal). PDF lleva pagos/utilidades y portal a fase2, y propone fase3 core financiero. | Usar fases del PDF para narrativa comercial y avisar que es una agrupación de propuesta, sin reescribir historias. |
| Arriendo estimaciones alternativas | Memoria conserva original391-692h y v2513-1.100h; PDF900h. | Mostrar900h como referencia PDF, sin sumar alternativas ni presentarla como estimación técnica aprobada. |
| Precio / inversión | PDF solo da horas para desarrollo. | Mostrar precio por definir; no convertir horas a dinero ni ofrecer totales monetarios inventados. |
| Infraestructura | Repo requiere FastAPI/AWS/S3/RDS; PostgreSQL y Next.js son referencia propuesta. | Infraestructura consumo aparte por definir; no declarar elección implementada o arquitectura cerrada por aparecer documentada. |
| Core vs pagos/utilidades | El primero gestiona crédito financiero propio; el segundo resultados/facturación de operación inmobiliaria. | Mantener funciones y fronteras claras. |
| Ahorro al construir core | Solo consta costo mínimo1500USD/mes. | Mostrar18.000USD/año como mínimo actual anualizado o costo recurrente de referencia, sin afirmación de ahorro neto, rentabilidad o ROI. |

## Verificación de este inventario

- Revisadas visualmente las11 páginas del PDF, incluidas todas las tablas omitidas por extracción.
- Sumas verificadas:600+400+460=1.460;520+430+900+820+500+730+100=4.000;1.460+4.000=5.460;40+20+20+20=100;1.500×12=18.000.
- Estados/roles contrastados con criterios Gherkin aprobados y memoria.
- Este inventario distingue datos publicados, cálculos simples derivados y decisiones pendientes. No supone que la oferta del proveedor siga vigente fuera de este PDF.
