# Épica de onboarding del cliente

Cotización inicial de [HU-01 a HU-03](../historias_de_usuario_plan_del_proyecto.md), según [contexto del negocio](../contexto.md) y [criterios Gherkin propuestos](onboarding-cliente-criterios-aceptacion.md). Horas-persona estimadas, no medidas. El propietario presenta una intención de venta; la adquisición del inmueble se gestiona en el módulo 2.

## Resumen de horas

| Capa | Rango |
|---|---:|
| Definición | 8–16 h |
| Backend | 84–176 h |
| Frontend | 36–80 h |
| Infraestructura incremental y observabilidad | 21–44 h |
| Validación transversal | 18–40 h |
| Entrega | 6–16 h |
| **Módulo sobre base funcional** | **173–372 h** |
| Base compartida pendiente, si aplica | 78–176 h |
| **Módulo con toda la base pendiente** | **251–548 h** |

**Método:** [skill local estimate-task](../skills/estimate-task/SKILL.md); [cálculo reproducible](../docs/estimaciones/modulo-1-estimacion.json). 1 d = 8 h-persona, solo convención de cálculo. A1 = 0,5 d, conexión UI a endpoint existente; A2 = ~1 d, consultas/documento sobre patrón existente. Son referencias importadas declaradas, sin registros originales verificados y solo analogías parciales. H = hipótesis técnica de 1 d por unidad de trabajo, no ancla histórica. M0 indica análisis; M1 indica datos personales, identidad, permisos, migraciones o integración sin patrón comprobado. **Confianza baja**: no se ha acreditado código, ambientes ni contrato del proveedor.

Cada rango resulta de `horas = techo(8 × días de referencia × unidades × factor)`, por extremo. Las unidades y factores se registran en el JSON. `×ref` en cada tarea corresponde a **unidades antes del factor M1**. M1 usa ×1,5–2 una sola vez para diseño, TDD, revisión y verificación positiva/negativa; M0 usa ×1. No se multiplican estimaciones anteriores. Las pruebas propias están dentro de cada tarea; QA cubre recorridos entre componentes y pruebas de fallos externos.

## Alcance y límites

HU-01 cubre cuenta de propietario y datos **iniciales** de intención de venta, adaptables a celular. HU-02 cubre texto y evidencia de aceptación expresa. HU-03 cubre orquestación de verificación de identidad y listas, registro de resultados y revisión interna de casos no concluyentes. El oficial de cumplimiento consulta casos; su revisión no equivale a la gestión de origen de fondos/operaciones inusuales de HU-09. La ficha completa, fotografías, documentos y estados de adquisición corresponden a [módulo 2](ficha-inmueble-epica.md).

## 0 Definición — 8–16 h

### AN-ON-01 Contratos de registro y cumplimiento — 8–16 h

**Estimación:** 1–2 d · M0 · H × 1–2; factor ×1. Delimita campos mínimos, consentimiento, proveedor y decisión operativa.

- Acordar campos iniciales de propietario/inmueble, identificador único, accesibilidad móvil y errores. Mapear HU-01 a HU-03 a contrato API y Gherkin.
- Definir con cumplimiento texto/versionado de autorización, fuentes de listas, criterios de coincidencia, tratamiento de indisponibilidad, acceso y retención. Registrar decisiones pendientes sin inventar reglas legales.
- Definir contrato entre intención inicial y solicitud del módulo 2 para evitar duplicados.

**Tecnologías:** Markdown, OpenAPI, ADR en Git.

## 1 Backend con FastAPI, SQLAlchemy y Pydantic — 84–176 h

Los endpoints son propuestas bajo `/api/v1`; se ajustan al contrato acordado antes de implementar.

### BE-ON-01 Modelos y migraciones — 12–24 h

**Estimación:** 1,5–3 d · M1 · H × 1–1,5; luego ×1,5–2. Datos personales, restricciones y migraciones nuevas.

- Modelar propietario, intención inicial, versión de consentimiento, aceptación y caso/consultas de verificación con índices y claves únicas.
- Probar migración, reversibilidad viable y no duplicación ante reintentos.

**Tecnologías:** PostgreSQL en RDS, SQLAlchemy 2, Alembic, pytest.

### BE-ON-02 Registro y cuenta de propietario — 18–40 h

**Estimación:** 2,25–5 d · M1 · H × 1,5–2,5; luego ×1,5–2. Alta pública y credenciales sin patrón Casabra acreditado.

**Endpoint propuesto:** `POST /owners/signup`.

- Validar datos de cuenta, crear exclusivamente rol Propietario y proteger contraseña/sesión mediante contrato de autenticación seleccionado; impedir que el payload asigne roles internos.
- Mantener operación atómica con consentimiento e intención inicial; controlar duplicados, concurrencia y mensajes sin revelar cuentas ajenas.
- TDD de altas válidas, inválidas, repetidas y fallos parciales.

**Tecnologías:** FastAPI, Pydantic v2, autenticación acordada, PostgreSQL, HTTPX/pytest.

### BE-ON-03 Intención inicial del inmueble — 9–16 h

**Estimación:** 1,12–2 d · M1 · A2 × 0,75–1; luego ×1,5–2. Analogía parcial: nueva relación privada y contrato con módulo 2.

**Endpoints propuestos:** `POST /sale-intents`, `GET /sale-intents/{id}`.

- Guardar características/ubicación mínimas acordadas y vincularlas al propietario sin crear un activo adquirido.
- Restringir consulta al titular/equipo autorizado y evitar nuevas intenciones por reintento del alta.
- Probar validaciones, acceso ajeno y enlace al expediente posterior.

**Tecnologías:** FastAPI, SQLAlchemy, Pydantic, pytest.

### BE-ON-04 Consentimiento versionado — 12–24 h

**Estimación:** 1,5–3 d · M1 · H × 1–1,5; luego ×1,5–2. Evidencia de autorización sobre datos sensibles.

**Endpoints propuestos:** `GET /privacy-notices/current`, `POST /consents`.

- Publicar texto vigente con versión; registrar aceptación expresa, fecha UTC, sujeto y referencia del texto en transacción con el alta.
- Rechazar casilla ausente o versión obsoleta; impedir alteración de la evidencia desde el API público.
- Probar cambio de versión y auditoría autorizada sin exponer datos innecesarios.

**Tecnologías:** FastAPI, PostgreSQL, Pydantic, pytest.

### BE-ON-05 Integración de identidad y listas — 21–48 h

**Estimación:** 2,63–6 d · M1 · H × 1,75–3; luego ×1,5–2. Proveedor, errores, reintentos y datos de alto riesgo; sin ancla comparable.

- Crear adaptador de proveedor configurable para identidad y listas acordadas; enviar solo datos necesarios y guardar referencia/resultado, no respuestas crudas innecesarias.
- Controlar timeout, tasa, reintentos e idempotencia; distinguir aprobado, coincidencia, inconcluso e indisponible según política acordada.
- Probar respuestas positivas/negativas, coincidencias, fallas y duplicados con simuladores; el coste/contrato del proveedor queda aparte.

**Tecnologías:** FastAPI, cliente HTTP, SQS si el contrato requiere asincronía, Secrets Manager, pytest.

### BE-ON-06 Bandeja y permisos de cumplimiento — 12–24 h

**Estimación:** 1,5–3 d · M1 · H × 1–1,5; luego ×1,5–2. Acceso restringido y resolución auditable.

**Endpoints propuestos:** `GET /compliance/cases`, `GET /compliance/cases/{id}`, `POST /compliance/cases/{id}/decision`.

- Mostrar al oficial resultados mínimos, fuente, fecha y estado; permitir decisión manual con motivo, responsable y hora bajo permiso explícito.
- Registrar decisión de manera atómica y rechazar acceso del propietario u otros roles no autorizados.
- Probar casos pendientes, decisiones duplicadas y acceso indebido.

**Tecnologías:** dependencias FastAPI, SQLAlchemy, pytest/HTTPX.

## 2 Frontend con Next.js — 36–80 h

### FE-ON-01 Registro móvil — 12–24 h

**Estimación:** 1,5–3 d · M1 · A1 × 2–3; luego ×1,5–2. A1 es analogía parcial para integración UI; aquí hay PII y alta nueva.

- Crear formulario adaptable a celular, validación, errores accesibles y confirmación de recepción; conectar alta e intención inicial.
- Probar teclado móvil, validaciones, envío repetido y estados de carga/error.

**Tecnologías:** Next.js, TypeScript, React Hook Form, Zod, Vitest/Testing Library.

### FE-ON-02 Aviso y aceptación expresa — 9–16 h

**Estimación:** 1,12–2 d · M1 · A1 × 1,5–2; luego ×1,5–2. Presentación clara del texto y versión; datos personales.

- Mostrar texto vigente antes de la aceptación, casilla sin premarcar y enlace descargable/consultable.
- Impedir envío sin aceptación y presentar error por versión cambiada.
- Probar accesibilidad y asociación correcta de versión en el envío.

**Tecnologías:** Next.js, componentes accesibles, Testing Library.

### FE-ON-03 Consulta interna de casos — 15–40 h

**Estimación:** 1,88–5 d · M1 · A1 × 2,5–5; luego ×1,5–2. Varias vistas, permisos y decisión sensible; analogía parcial.

- Crear lista, detalle y decisión motivada para oficial de cumplimiento; filtros básicos, estados vacíos y errores.
- Ocultar acciones no permitidas y probar coincidencia, indisponibilidad y conflicto de decisión; backend conserva autoridad.

**Tecnologías:** Next.js, TypeScript, cliente HTTP, Testing Library.

## 3 Infraestructura incremental y observabilidad — 21–44 h

### OPS-ON-01 Secretos, red e integración del proveedor — 12–24 h

**Estimación:** 1,5–3 d · M1 · H × 1–1,5; luego ×1,5–2. Credenciales y conectividad sin patrón comprobado.

- Configurar secretos, permisos mínimos, parámetros por ambiente y conectividad saliente; probar integración en staging con credenciales de prueba.
- Si se usa cola, configurar reintentos y DLQ; no incluir una plataforma de mensajería ajena al flujo.

**Tecnologías:** CDK/CloudFormation, IAM, Secrets Manager, ECS, SQS condicional.

### OPS-ON-02 Eventos, trazas y alarmas — 9–20 h

**Estimación:** 1,12–2,5 d · M1 · H × 0,75–1,25; luego ×1,5–2. Visibilidad de fallos con supresión de PII.

- Instrumentar llamadas, correlación, tiempos, tasa de errores y casos pendientes; alarmar fallos de proveedor/cola.
- Verificar retención, redacción de identificadores/documentos y aviso al canal operativo.

**Tecnologías:** CloudWatch, OpenTelemetry/ADOT, SNS.

## 4 Validación transversal — 18–40 h

### QA-ON-01 Recorrido móvil y permisos — 9–20 h

**Estimación:** 1,12–2,5 d · M1 · H × 0,75–1,25; luego ×1,5–2. Flujo completo y roles entre capas.

- Ejecutar Gherkin en navegador móvil: registro, consentimiento, intención, resultado y consulta interna.
- Probar duplicados, rol interno no asignable, sesión y acceso a caso ajeno.

**Tecnologías:** Playwright, staging, datos sintéticos.

### QA-ON-02 Contrato externo y recuperación — 9–20 h

**Estimación:** 1,12–2,5 d · M1 · H × 0,75–1,25; luego ×1,5–2. Fallas reales de red/proveedor y recuperación.

- Verificar contrato sandbox, timeout, reintentos, coincidencias, indisponibilidad y resultado no aprobado por defecto.
- Comprobar migración y restauración de datos sintéticos con evidencias; no duplicar unitarias de BE-ON-05.

**Tecnologías:** pytest, sandbox del proveedor, RDS/staging.

## 5 Entrega — 6–16 h

### REL-ON-01 Despliegue y aceptación — 6–16 h

**Estimación:** 0,75–2 d · M1 · H × 0,5–1; luego ×1,5–2. Migración, activación por ambiente y aceptación de cumplimiento.

- Desplegar mediante pipeline, revisar resultados Gherkin y evidencias del proveedor, documentar contrato y procedimiento de fallos.
- Registrar decisiones técnicas en ADR y versión desplegada; separar espera de aprobación de horas-persona.

**Tecnologías:** Git, OpenAPI, pipeline AWS, Markdown.

## 6 Base compartida condicionada

Se presupone una base funcional de login, API/web, RDS, pipeline y pruebas. La documentación existente no acredita su implementación. Si no existe, agregar una sola vez las partidas [BASE-01 a BASE-05 del módulo 2](ficha-inmueble-epica.md#6-base-compartida-si-aún-no-está-implementada): **78–176 h**. BASE-03 adapta un login existente; si debe construirse desde cero, reestimar la autenticación por separado y no sumar ambas variantes. Estas partidas se comparten entre módulos y no se cobran de nuevo en cada épica. El cálculo JSON conserva su desglose.

## 7 Complejidad

| Grupo | S/M/L | Motivo |
|---|---|---|
| Contrato y consentimiento | M | Versión/evidencia y decisiones de cumplimiento |
| Alta y primera intención | M | Datos personales, atomicidad y duplicados |
| Identidad y listas | L | Proveedor externo, coincidencias, errores y auditoría |
| Bandeja interna | M | Permisos y decisión trazable |
| Infraestructura y validación | M | Secretos, observabilidad y recuperación |

S/M/L es complejidad relativa, sin conversión automática a horas.

## 8 Condiciones de cotización

- **Confirmado por historias:** registro desde celular con inmueble inicial, aceptación consciente y verificación de identidad/listas al registrarse. La compañía compra el inmueble solo tras el flujo posterior.
- **Supuesto:** web adaptable a celular; una persona natural propietaria por cuenta; un proveedor contratado que ofrece identidad y listas mediante API/sandbox; revisión manual de coincidencias. RDS PostgreSQL, FastAPI y Next.js son referencias técnicas del proyecto. Las reglas de aprobación y posibilidad de continuar con caso pendiente se definen antes de implementar.
- **Pendiente:** campos obligatorios, política y texto legal, jurisdicción/fuentes, proveedor y precios, umbrales de coincidencia, tratamiento de falsos positivos, retención, tiempos de respuesta, volumen, recuperación de cuenta, identidad de personas jurídicas y responsabilidades de aprobación. Una integración no documentada o verificación presencial puede cambiar el alcance.
- **Contingencia condicionada:** 0–4 h, una sola vez, si el contrato real del login/base entregada exige una corrección acotada de integración; responsable: integrador de autenticación. Totales con contingencia: **173–376 h** sobre base funcional o **251–552 h** con toda la base pendiente. Un proveedor sin API útil o cambios de política se reestiman, no se cubren con 4 h.
- **Fuera de horas:** consumo AWS, licencias/consultas del proveedor, esperas de contrato, credenciales y decisiones de cumplimiento. El calendario depende de capacidad y dependencias. Recalibrar con horas reales tras el primer flujo completo; el rango no es un percentil estadístico.
