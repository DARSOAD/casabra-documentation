# Épica de arriendo de inmuebles adquiridos

Estimación técnica preliminar del módulo 8 para cotización. Comprende la operación de arriendo de activos ya adquiridos por la compañía, desde su alistamiento hasta la administración del contrato, el autoservicio del arrendatario, los cobros digitales y el control de cartera.

**Historias de referencia:** HU-34 a HU-39, HU-46, HU-47, HU-51 a HU-54; roles transversales de HU-33. Ver [historias del proyecto](../historias_de_usuario_plan_del_proyecto.md) y [contexto de negocio](../contexto.md).

> Estimación de esfuerzo por persona, no tiempo calendario, compromiso contractual ni costo monetario. No hay horas reales de Casabra ni código de este módulo inspeccionado para demostrar reutilización; confianza baja. Cálculo reproducible: [estimación JSON](../docs/estimaciones/modulo-8-estimacion.json).

## Resumen de horas

| Capa | Rango estimado |
|---|---:|
| Análisis funcional | 8–16 h |
| Diseño UX/UI adaptable | 20–32 h |
| Backend | 195–336 h |
| Frontend | 114–204 h |
| Infraestructura incremental y observabilidad | 24–48 h |
| Validación transversal | 24–40 h |
| Entrega y documentación | 6–16 h |
| **Módulo sobre base funcional existente** | **391–692 h** |
| Base compartida, solo si aún no existe | 48–96 h |
| **Módulo más base compartida pendiente** | **439–788 h** |

Los rangos por tarea incluyen su TDD, pruebas propias y revisión. La validación transversal cubre recorridos completos y pruebas de integración que no sustituyen ni repiten las unitarias de cada tarea. Los costos de proveedor de pagos, mensajería, AWS y otras esperas externas no son horas de desarrollo y quedan fuera.

## Método, referencias y confianza

Se aplica la skill local [estimate-task](../skills/estimate-task/SKILL.md) y su [calibración](../skills/estimate-task/references/calibration.md). No existen tareas cerradas comparables de Casabra. Las referencias importadas A1 (integración de UI a endpoint existente) y A2 (consultas/documento con patrones existentes) no se consideran equivalentes a crear este módulo y no se usan para inferir productividad. Se usa **H**, hipótesis técnica por entregable y pruebas, sin presentarla como tiempo observado.

- **Unidad:** 1 día productivo = 8 horas-persona, convención de cálculo; no fija horas facturables ni plazo calendario.
- **M0:** análisis o diseño sin implementación; factor ×1.
- **M1:** dinero, transacciones, contratos, roles/permisos, documentos personales o patrón no comprobado; factor ×1,5–2 sobre la base H. Se aplica una sola vez; sus revisiones y validaciones sensibles ya están incorporadas en el rango.
- **Fórmula:** horas = 8 h/d × unidades H × factor de modo. Las unidades H son juicio técnico explícito, no anclas históricas.
- **No se descuenta reutilización** por la mera existencia de documentación o por suponer autenticación, contratos, inventario, API, AWS o componentes listos. La base compartida se cotiza aparte solo si la inspección confirma que falta.

## Alcance funcional estimado

| Historias | Trabajo incluido |
|---|---|
| HU-34–36 | Ingresar activos adquiridos a arriendo; registrar alistamiento, condiciones, canon y oferta comercial; administrar anuncios/enlaces manualmente. |
| HU-37–39 | Gestionar interesados y candidatos, formalizar el contrato aprobado, inventario, entrega, novedades y devolución. |
| HU-46 | Configurar obligaciones, calendario de cánones, vencimientos, reajustes, renovaciones y terminación. |
| HU-51–54 | Portal adaptable para contrato/estado de cuenta, pago digital, estados de transacción, registro de pagos externos, recordatorios y comprobantes internos. |
| HU-47 | Tablero de inmuebles y contratos con ocupación, ingresos, deuda/mora y próximos vencimientos. |
| HU-33 | Aplicar permisos por rol a la información y acciones del módulo; arrendatario separado del propietario original. |

### 0. Análisis funcional — 8–16 h

#### AN-AR-01 Reglas, estados y decisiones pendientes — 8–16 h

**Estimación:** 1–2 d · M0 · H (1 d) × 1–2 unidades × factor 1. Incluye concretar los criterios de aceptación y registrar decisiones, no implementación.

- Acordar vencimientos, pagos parciales, pagos tardíos, reversos, pagos externos, qué origina mora y cuándo se considera saldada una obligación.
- Precisar el estado de solicitud/contrato/inmueble y la transición entre disponibilidad, reservado, ocupado y vacante sin duplicar la máquina de adquisición.
- Definir datos que el arrendatario puede consultar, manejo de varios pagadores y medios/canales de notificación.
- Confirmar si firma electrónica, identidad, contratos, inmueble y login existentes se integran o son dependencias externas.

**Tecnologías/artefactos:** criterios Gherkin en Markdown, decisiones versionadas en Git y contrato de API OpenAPI.

## 1. Diseño UX/UI adaptable — 20–32 h

#### UX-AR-01 Flujos del administrador y arrendatario — 20–32 h

**Estimación:** 2,5–4 d · M0 · H (1 d) × 2,5–4 unidades × factor 1. El diseño no presupone componentes implementados.

- Diseñar preparación/publicación, candidato, contrato/entrega, tablero de cartera y vistas responsivas del arrendatario.
- Diseñar selección de obligación y flujo de pago con estados pendiente, confirmando, pagado, fallido y por conciliar; no mostrar pagado antes de confirmación verificable.
- Diseñar estados vacíos, errores, mora, indisponibilidad de pasarela y comprobante descargable.
- Revisar accesibilidad básica y navegación en celular; validar roles y separación de datos.

**Tecnologías:** prototipos Figma o equivalente; la herramienta y el sistema visual son pendientes de confirmar.

## 2. Backend — 195–336 h

Referencia propuesta: FastAPI, SQLAlchemy/Pydantic, PostgreSQL en RDS. Es una base de estimación, no evidencia de implementación ya disponible. API bajo `/api/v1`; rutas ilustrativas a concretar en OpenAPI.

### BE-AR-01 Modelos de inmueble, contrato y obligaciones — 15–28 h

**Estimación:** 15–28 h (1,88–3,5 d) · M1 · H (1 d) × 1,25–1,75 unidades × factor 1,5–2. Incluye TDD de modelos y restricciones.

- Modelar datos de alistamiento, anuncio, interesados, contrato, entrega, obligación periódica y estado de cuenta.
- Definir claves, unicidad, índices, fechas y relaciones; versionar migraciones.
- Probar restricciones, valores límite y compatibilidad de migración.

**Tecnologías:** SQLAlchemy, Alembic y PostgreSQL/RDS.

### BE-AR-02 Alistamiento, oferta e interesados — 24–40 h

**Estimación:** 24–40 h (3–5 d) · M1 · H (1 d) × 2–2,5 unidades × factor 1,5–2. Incluye autorización de candidatos/documentos.

- Crear/actualizar ficha de arriendo solo para activo adquirido y asignado a esta ruta.
- Registrar preparación, canon objetivo, condiciones, disponibilidad, fotos y anuncio/enlace manual.
- Registrar solicitudes, documentos, visitas, evaluación y recomendación; filtrar y consultar según rol.
- Validar transiciones y evitar publicación si no se cumplen condiciones operativas acordadas.

**Tecnologías:** FastAPI, Pydantic, SQLAlchemy y S3 privado para archivos, si se confirma disponible.

### BE-AR-03 Contrato, inventario y entrega — 24–40 h

**Estimación:** 24–40 h (3–5 d) · M1 · H (1 d) × 2–2,5 unidades × factor 1,5–2. Contratos y datos personales, con integración legal pendiente.

- Crear expediente de contrato con canon, periodicidad, fechas, reajustes, obligaciones y garantías aprobadas.
- Integrarse al flujo de firma electrónica existente si se verifica; no construir un proveedor de firma nuevo.
- Registrar inventario, evidencia de entrega, acta/novedades y devolución; vincularlos al contrato y al inmueble.
- Evitar entrega antes del estado contractual que se acuerde en los criterios.

**Tecnologías:** FastAPI, PostgreSQL y almacenamiento privado de archivos.

### BE-AR-04 Calendario de cobros y estado de cartera — 24–40 h

**Estimación:** 24–40 h (3–5 d) · M1 · H (1 d) × 2–2,5 unidades × factor 1,5–2. Lógica de dinero/fechas y cálculos idempotentes.

- Generar obligaciones de canon con base en los datos del contrato, evitando duplicados al reintentar.
- Calcular saldo y estado de cuenta; determinar vencido/mora según reglas aprobadas, sin inventar penalidades.
- Registrar reajustes, vencimientos, renovaciones y terminaciones según condiciones y permisos.
- Cubrir cambios de fecha, zona horaria, cierres de contrato y pagos que cubren una parte del saldo.

**Tecnologías:** Python, SQLAlchemy y PostgreSQL; tareas programadas solo tras confirmar infraestructura.

### BE-AR-05 Integración con pasarela de pago — 30–48 h

**Estimación:** 30–48 h (3,75–6 d) · M1 · H (1 d) × 2,5–3 unidades × factor 1,5–2. No hay proveedor ni patrón de pago existente verificado.

- Crear intención de pago vinculada a contrato, obligación e importe; impedir duplicidad/cobro concurrente.
- Validar autenticidad de notificaciones del proveedor y procesar confirmaciones de forma idempotente.
- Mantener estados pendiente, confirmada, fallida o por conciliar; tratar reintentos, notificaciones repetidas y fallas.
- No guardar datos sensibles de tarjeta; manejar cancelación/reverso de acuerdo con capacidades documentadas del proveedor.
- Probar sandbox y casos negativos acordados. La conciliación bancaria automática y los reembolsos avanzados no se presuponen.

**Tecnologías:** cliente HTTP de Python, webhook FastAPI, gestor de secretos y sandbox del proveedor por seleccionar.

### BE-AR-06 Pagos externos, conciliación y comprobante interno — 18–32 h

**Estimación:** 18–32 h (2,25–4 d) · M1 · H (1 d) × 1,5–2 unidades × factor 1,5–2. Impacta dinero y evidencia del arrendatario.

- Permitir registrar pagos no digitales con fecha, valor, referencia, medio y soporte, según permisos.
- Vincular confirmación y movimiento a obligaciones/saldos sin registrar dos veces una transacción.
- Generar comprobante interno descargable solo para pagos confirmados; conservar estado, identificador y fecha.
- Probar abonos, saldos restantes, duplicados y pagos sin aplicación automática.

**Tecnologías:** FastAPI, PostgreSQL, generación PDF según librería aprobada y S3 si se conserva el documento.

### BE-AR-07 Recordatorios y avisos — 12–28 h

**Estimación:** 12–28 h (1,5–3,5 d) · M1 · H (1 d) × 1–1,75 unidades × factor 1,5–2. Automatización nueva con efectos a usuarios; canal/proveedor no definido.

- Programar avisos antes y después del vencimiento conforme a calendario acordado.
- Notificar fallas o falta de confirmación del pago y evitar avisos contradictorios después de confirmar.
- Guardar resultado/envío e impedir duplicados por reintentos.
- Aplicar preferencias, consentimiento y protección de datos de contacto.

**Tecnologías:** cola/tareas programadas y proveedor de correo/notificación por confirmar; no se supone SMS incluido.

### BE-AR-08 API del portal de arrendatario — 18–28 h

**Estimación:** 18–28 h (2,25–3,5 d) · M1 · H (1 d) × 1,5–1,75 unidades × factor 1,5–2. Datos de contrato/pagos privados y permisos por usuario.

- Exponer contrato y obligaciones del usuario autenticado, historial, saldo y comprobantes disponibles.
- Crear solicitud de pago y devolver estados seguros sin exponer datos internos o de otros arrendatarios.
- Validar autenticación, límites y acceso cruzado negativo.

**Tecnologías:** FastAPI, Pydantic y autorización basada en rol/relación.

### BE-AR-09 Consultas del tablero de administración — 18–28 h

**Estimación:** 18–28 h (2,25–3,5 d) · M1 · H (1 d) × 1,5–1,75 unidades × factor 1,5–2. Cifras de cartera deben corresponder al ledger operacional.

- Consultar ocupación, inmuebles disponibles/vacantes, ingresos, obligaciones al día/vencidas y próximos vencimientos.
- Agregar filtros por inmueble, contrato, estado y periodo, con paginación/ordenamiento donde aplique.
- Validar sumas y estados contra movimientos y obligaciones; no duplicar contabilidad.

**Tecnologías:** FastAPI, SQLAlchemy y PostgreSQL.

### BE-AR-10 Permisos y auditoría del módulo — 12–24 h

**Estimación:** 12–24 h (1,5–3 d) · M1 · H (1 d) × 1–1,5 unidades × factor 1,5–2. No se asume que el RBAC/auditoría del producto existe.

- Aplicar roles y relaciones para gerente de activos, administrador, asesor de arriendos, contador y arrendatario.
- Registrar cambios relevantes de contrato, obligación, aplicación de pago y estado de mora con usuario/fecha.
- Restringir acciones y datos por inmueble/contrato; pruebas de accesos permitidos y denegados.

**Tecnologías:** dependencias de autorización FastAPI y auditoría transaccional en PostgreSQL/RDS.

## 3. Frontend web adaptable — 114–204 h

Referencia propuesta: Next.js/TypeScript, interfaz web adaptable a celular. No se presupone aplicación móvil nativa ni componentes reutilizables comprobados.

### FE-AR-01 Gestión de alistamiento, publicación e interesados — 24–40 h

**Estimación:** 24–40 h (3–5 d) · M1 · H (1 d) × 2–2,5 unidades × factor 1,5–2.

- Formularios/listados de activos, alistamiento, datos comerciales, anuncio/enlace y disponibilidad.
- Vistas de interesado, documentos, visitas, evaluación y recomendación con estados visibles.
- Validación, errores, carga de fotos y permisos por rol.

### FE-AR-02 Contrato, inventario y entrega — 18–32 h

**Estimación:** 18–32 h (2,25–4 d) · M1 · H (1 d) × 1,5–2 unidades × factor 1,5–2.

- Capturar/revisar datos del contrato aprobado y mostrar estado de formalización.
- Registrar inventario de entrega/devolución, observaciones y evidencia.
- Adaptar controles a móvil y mostrar errores/estados de firma si el sistema actual los expone.

### FE-AR-03 Portal de autoservicio del arrendatario — 24–40 h

**Estimación:** 24–40 h (3–5 d) · M1 · H (1 d) × 2–2,5 unidades × factor 1,5–2.

- Mostrar contrato, obligaciones, saldo, historial y vencimientos del usuario autenticado.
- Diseñar estados de carga/vacío/error y acceso restringido por sesión.
- Adaptar navegación al celular; no crear app nativa independiente.

### FE-AR-04 Interfaz para pagar el canon — 18–32 h

**Estimación:** 18–32 h (2,25–4 d) · M1 · H (1 d) × 1,5–2 unidades × factor 1,5–2. Incluye estados de pago y reintentos; proveedor pendiente.

- Iniciar pago de una obligación y mostrar la respuesta del proveedor o redirección segura.
- Mostrar pendiente/confirmado/fallido, sin asumir éxito por retorno del navegador.
- Evitar doble envío y permitir volver a consultar el estado.

### FE-AR-05 Recibo interno descargable — 6–12 h

**Estimación:** 6–12 h (0,75–1,5 d) · M1 · H (1 d) × 0,5–0,75 unidades × factor 1,5–2.

- Consultar y descargar comprobantes de pagos confirmados.
- Mostrar referencia, fecha, valor y periodo/obligación cubiertos; etiquetar como comprobante interno, no factura DIAN.

### FE-AR-06 Tablero de cartera — 18–32 h

**Estimación:** 18–32 h (2,25–4 d) · M1 · H (1 d) × 1,5–2 unidades × factor 1,5–2.

- Presentar filtros y métricas de ocupación, ingresos, obligaciones al día/mora y vencimientos.
- Permitir navegar de resumen a inmueble/contrato y revisar pagos por conciliar.
- Validar estados vacíos, permisos, carga y errores de consulta.

### FE-AR-07 Visualización de avisos y estados — 6–16 h

**Estimación:** 6–16 h (0,75–2 d) · M1 · H (1 d) × 0,5–1 unidades × factor 1,5–2.

- Mostrar avisos de vencimiento, confirmación y fallas disponibles en la sesión.
- Explicar estado de una obligación sin duplicar el envío del servicio de notificaciones.

## 4. Infraestructura incremental y observabilidad — 24–48 h

### OPS-AR-01 Recursos y operación de integraciones — 24–48 h

**Estimación:** 24–48 h (3–6 d) · M1 · H (1 d) × 2–3 unidades × factor 1,5–2. AWS e integraciones nuevas no tienen ancla comparable.

- Configurar recursos incrementales para secretos/webhooks, cola o scheduler de avisos, permisos IAM mínimos y alertas.
- Incorporar métricas/logs para errores de pagos y notificaciones sin registrar datos financieros sensibles.
- Preparar configuración por ambiente y pruebas de despliegue/rollback.
- Validar que el proveedor y entorno AWS del proyecto permitan la solución concreta; cambios mayores de arquitectura quedan por cotizar.

**Tecnologías:** AWS según arquitectura aprobada (p. ej., RDS, S3, SQS/EventBridge, Secrets Manager y CloudWatch); no se fija consumo.

## 5. Validación transversal — 24–40 h

### QA-AR-01 Recorridos integrales, seguridad y regresión — 24–40 h

**Estimación:** 24–40 h (3–5 d) · M1 · H (1 d) × 2–2,5 unidades × factor 1,5–2. Esta tarea valida integración completa y no vuelve a cobrar TDD/unitarias propias.

- Probar flujo disponible → candidato → contrato → entrega → obligación → pago → comprobante.
- Probar pago confirmado, pendiente, fallido, repetido, externo y por conciliar con sandbox/stubs permitidos.
- Verificar recordatorios y tablero al día/mora frente a eventos y cálculos del backend.
- Ejecutar pruebas de autorización entre arrendatarios/roles, regresión y aceptación con datos de prueba.

**Herramientas:** pytest/HTTPX para API y la herramienta de pruebas del stack frontend que el repositorio ya use; Playwright solo si está disponible/acordado.

## 6. Entrega y documentación — 6–16 h

### REL-AR-01 Preparar salida, manual y transferencia — 6–16 h

**Estimación:** 6–16 h (0,75–2 d) · M1 · H (1 d) × 0,5–1 unidades × factor 1,5–2.

- Documentar configuración de pasarela/notificaciones, variables secretas sin valores sensibles y operación de pagos por conciliar.
- Preparar lista de verificación para migraciones, despliegue, monitoreo y recuperación.
- Hacer transferencia a administradores; coordinar activación productiva condicionada a aprobación del proveedor.

## Base compartida, si se confirma pendiente — 48–96 h adicionales

### SH-AR-01 Plataforma mínima reutilizable — 48–96 h

**Estimación condicional:** 48–96 h (6–12 d) · M1 · H (1 d) × 4–6 unidades × factor 1,5–2. **No está incluida** en las 391–692 h; no cobrar si se comprueba que ya existe y funciona.

- Confirmar/crear esqueleto API y web, ambientes, configuración y pipeline de despliegue.
- Confirmar/crear login, roles base, RDS/PostgreSQL, migraciones y almacenamiento S3 privado, si forman parte del producto.
- Establecer secretos, logs, alarmas y procedimiento de recuperación compartidos.
- El tiempo de proveedores, accesos, aprobaciones y aprovisionamiento no es esfuerzo de desarrollo y se registra como espera.

## Tabla de complejidad

Complejidad es una clasificación cualitativa de dependencias y riesgo; no se calcula solo a partir de horas.

| Tamaño | Trabajo representativo | Motivo |
|---|---|---|
| S | Comprobante interno, vista de aviso o configuración de un campo comercial | Alcance acotado; aun así requiere permisos y comprobación del estado. |
| M | Alistamiento/interesados, inventario/entrega, portal y tablero | Cruza varias vistas/endpoints y roles, con integración en la operación del inmueble. |
| L | Ledger de cánones, pasarela/webhooks, conciliación y reglas de mora | Dinero, idempotencia, estados asíncronos, exactitud de saldos y dependencia de terceros. |

## Supuestos y exclusiones

- El inmueble ya fue adquirido por la compañía y asignado a la ruta de arriendo; adquisición y obras no se vuelven a estimar aquí.
- Se estima una web adaptable a móvil. No se estima aplicación nativa.
- El anuncio y sus enlaces se administran manualmente; no hay sincronización automática con portales inmobiliarios.
- Se contempla una pasarela, todavía por seleccionar, y el comprobante es interno. Factura electrónica DIAN queda fuera.
- Pagos externos se pueden registrar manualmente. Pagos parciales/reversos/mora requieren confirmar reglas antes de cerrar criterios.
- No se incluyen varios proveedores de pago, conciliación bancaria automática, recuperación de cartera automatizada, scoring externo ni asesoría legal.
- Los HUs están disponibles, pero los criterios Gherkin del módulo y estados exactos no constan aprobados. AN-AR-01 debe cerrarlos antes de implementar.
- La existencia y capacidad de login, inmuebles, contratos/firma, RBAC, S3/RDS, pipeline y monitoreo son dependencias por verificar; no se descuentan como reutilización confirmada.
- Uso/costos de AWS, pasarela y mensajería, tarifas transaccionales, impuestos y tiempos de respuesta de terceros son externos a las horas aquí estimadas.

## Contingencias y confianza

El rango 391–692 h no tiene una reserva porcentual genérica adicional: los riesgos de dinero, permisos, datos personales y patrón nuevo ya están reflejados una sola vez mediante M1. Si la inspección confirma que la base compartida falta, agregar solo SH-AR-01 (48–96 h). Si el contrato/pasarela seleccionados no permiten el flujo previsto y requieren una corrección acotada, revisar esa tarea y considerar hasta 0,5 d adicional bajo esa condición; no sumar como reserva automática. Confianza **baja** hasta validar stack, reutilización, proveedor de pago, reglas de cobro y criterios Gherkin. Registrar horas reales al terminar para recalibrar.
