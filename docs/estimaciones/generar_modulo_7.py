"""Regenera la épica contractual desde su cálculo versionado."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def interval(a, b):
    return f'{a:g}–{b:g}'.replace('.', ',')


def render():
    data = json.loads(Path(__file__).with_name('modulo-7-estimacion.json').read_text(encoding='utf-8'))
    totals = {key: [0, 0] for key in data['layers']}
    for task in data['tasks']:
        for i, end in enumerate(('min', 'max')):
            hours = math.ceil(data['hours_per_day'] * data['references'][task['ref']]['days'] * task[f'base_units_{end}'] * task[f'risk_{end}'])
            assert hours == task[f'hours_{end}'], task['id']
            totals[task['layer']][i] += hours
    total = [sum(v[i] for v in totals.values()) for i in range(2)]
    base = [sum(v[i] for v in data['shared_base_if_pending'].values()) for i in range(2)]
    full = [total[i] + base[i] for i in range(2)]
    rows = ['# Épica del módulo 7. Contratos y firma electrónica', '',
        'Cotización inicial de **HU-20 a HU-22** de las [historias del proyecto](../historias_de_usuario_plan_del_proyecto.md), según el [contexto del negocio](../contexto.md). Mantiene la estructura por capas de la [épica del login](login-epica.md). Cubre generación, revisión, firma mediante proveedor y archivo de contratos para adquisición, arriendo y venta.', '',
        '**Referencia funcional:** [criterios Gherkin propuestos](contratos-firma-criterios-aceptacion.md). No se encontraron criterios aprobados específicos de este módulo. Los escenarios y límites de proveedor/plantillas son supuestos de cotización pendientes de validación; se preservan las reglas de los [criterios aprobados de adquisición](adquisicion-inmuebles-criterios-aceptacion.md).', '',
        '## Resumen de horas', '', '| Capa | Rango |', '|---|---:|']
    rows += [f'| {label} | {interval(*totals[layer])} h |' for layer, label in data['layers'].items()]
    rows += [f'| **Módulo sobre base funcional** | **{interval(*total)} h** |',
        f'| Base compartida, solo si está pendiente | {interval(*base)} h |',
        f'| **Módulo con toda la base pendiente** | **{interval(*full)} h** |', '',
        '**Unidad:** horas-persona; 1 d = 8 h como convención, no calendario. TDD, pruebas propias y revisión están incluidos en cada tarea funcional; QA cubre recorridos y fallos entre componentes en staging. Consumo AWS, licencias, transacciones del proveedor y esperas se separan. No se identificó estimación anterior del módulo 7.', '',
        '## Método y evidencia', '',
        'Se aplica [estimate-task local](../skills/estimate-task/SKILL.md) y sus [referencias de calibración](../skills/estimate-task/references/calibration.md). [Datos y cálculo reproducible](../docs/estimaciones/modulo-7-estimacion.json) y [generador](../docs/estimaciones/generar_modulo_7.py): `python docs/estimaciones/generar_modulo_7.py`.', '',
        '**Confianza baja:** proveedor, plantillas, identidad y retención pendientes; no existen tiempos reales Casabra disponibles ni base implementada comprobada. A1 (S9.2 / RED-3596, 0,5 d) representa conexión UI a endpoint con errores/pruebas; A2 (RED-765 / PR 766, aproximadamente 1 d), consultas y generación documental con servicios existentes. Son referencias importadas no verificadas, usadas como analogías parciales, no mediciones de este proyecto. H (1 d) es unidad de hipótesis técnica por entregables, no un antecedente real. Las horas de módulos anteriores no son anclas medidas.', '',
        '**Fórmula por extremo:** `ceil(8 × días_referencia × unidades_base × factor_riesgo)`. ×ref indica unidades antes del riesgo. M0 aplica ×1 a definición; M1 aplica ×1,5–2 una sola vez por permisos, datos personales, documentos sensibles, migraciones o patrón no comprobado. No multiplicar el total de nuevo ni duplicar TDD/revisión. No se presume descuento fijo por IA. Recalibrar con tiempos reales después del primer contrato completo; los rangos no son percentiles estadísticos.', '',
        '## Alcance confirmado y límites de cotización', '',
        '| Historia | Resultado incluido |', '|---|---|',
        '| HU-20 | Abogado maneja plantillas para adquirir, arrendar y vender |',
        '| HU-21 | Contraparte revisa y firma desde celular |',
        '| HU-22 | Administrador consulta documentos firmados y trazabilidad archivados |', '',
        '**Confirmado por contexto:** adquisición tiene como contraparte al propietario original. Arriendo y venta se realizan sobre activos adquiridos de la compañía, con arrendatario y comprador respectivamente. Firma de contrato no cambia por sí sola el inmueble a Adquirido, no confirma pago, no entrega el activo y no cierra la operación. Cada módulo conserva sus decisiones y permisos de negocio.', '',
        '**Supuestos de cotización:**', '',
        '- Una compañía; tres plantillas iniciales, una por tipo de operación, en español y diseño fijo con textos/cláusulas y variables editables mediante esquema acotado. Abogado entrega y aprueba contenido; versionar/publicar/retirar plantillas forma parte de este módulo. Versiones adicionales usan el mismo esquema, sin formatos arbitrarios.',
        '- Un PDF por contrato, sin paquete de anexos a firmar; dos firmantes secuenciales: contraparte y representante designado de la compañía. Ambos deben completar su firma. Copropietarios, codeudores, garantes, testigos, múltiples representantes, anexos firmados y rutas condicionales requieren revisar alcance.',
        '- Un proveedor contratado con API/sandbox, firma alojada adaptable a móvil, invitaciones, verificación de identidad, consulta autoritativa de estados, webhook verificable, expiración/cancelación y descarga de PDF firmado más evidencias. Es un requisito para sostener esta estimación, no una capacidad comprobada de un proveedor seleccionado.',
        '- El proveedor permite idempotencia o consulta por referencia de envío. Si una respuesta es incierta, se concilia antes de reintentar; si la consulta no resuelve, se conserva estado de atención operativa sin emitir otro contrato. La app no implementa criptografía de firma, emisión de certificados ni un sistema propio de OTP/biometría.',
        '- Invitaciones enviadas mediante el proveedor. La contraparte con cuenta existente puede revisar desde la app y abrir su sesión; quien no tenga cuenta usa el enlace personal y verificación del proveedor. No se incluye nuevo onboarding para compradores/arrendatarios ni acceso anónimo al repositorio contractual interno.',
        '- Abogado prepara/aprueba/envía; representante firma la invitación asignada; contraparte firma solo lo asignado; administrador consulta archivo/trazabilidad. La matriz definitiva, reemplazos de representante y facultades para cancelar quedan pendientes. Se adapta identidad existente, sin nueva consola de permisos.',
        '- PDF generado con snapshot de datos, plantilla y participantes. La aprobación se refiere a una revisión exacta. Cambiar datos antes de envío obliga a nueva revisión/aprobación; después de envío, el documento no se edita. Corregirlo exige cancelación confirmada cuando sea posible y un contrato nuevo vinculado; no se elimina la evidencia anterior.',
        '- Archivo automático del PDF firmado y evidencia descargada del proveedor en S3 privado, con versión y hashes propios; eventos/auditoría en RDS. Conservar original enviado y resultado firmado por separado. La firma modifica bytes: sus hashes no tienen que coincidir. Un hash local detecta cambios, no reemplaza la comprobación de identidad o suficiencia de la evidencia.',
        '- FastAPI, Next.js adaptable a celular, AWS, S3 y RDS PostgreSQL propuesto. Acceso conectado; sin app nativa ni firma offline. El tipo de firma y el mecanismo de identidad que requiera cada documento deben ser aprobados por negocio/abogado y soportados por el proveedor.', '',
        '### Estados propuestos y recuperación', '',
        '| Dimensión | Estados / regla |', '|---|---|',
        '| Preparación y firma | Borrador → Listo para firma → En firma → Firma completa; alternativas Rechazado, Expirado o Cancelado confirmadas por proveedor |',
        '| Envío o cancelación inciertos | Conciliación pendiente; no repetir envío ni afirmar cancelación por un timeout |',
        '| Archivo | Pendiente → Archivado o Error de archivo, independiente de firma |',
        '| Firma parcial | Mantener En firma y estado por participante; no dar contrato por completo |', '',
        'El retorno del navegador no confirma firma. Los eventos se autentican y deduplican; una consulta al proveedor resuelve estados ambiguos o desordenados. Firma completa exige todos los participantes requeridos; Archivado exige PDF firmado y evidencias persistidos. Reintentar archivo no vuelve a firmar ni enviar. Una carrera entre cancelación y firma se concilia contra el proveedor y conserva historial.', '',
        '**Pendientes que afectan el rango:** proveedor/API y límites, método de identidad/firma, número/orden de firmantes, formatos y longitud real de plantillas, campos por operación, capacidad de invitar externos, política de expiración/reenvío, retención, volumen mensual, residencia de datos y responsables de aprobación. La suficiencia jurídica de cada documento y mecanismo es una decisión de la empresa y su abogado; estas horas no incluyen redacción ni dictamen legal.', '',
        '**Fuera de alcance:** trámites notariales/registrales, confirmación de pagos/adquisición, operación de arriendo/venta, KYC propio, múltiples proveedores, firma criptográfica propia, validación especializada a largo plazo, sellado de tiempo independiente, almacenamiento WORM, OCR, Word colaborativo/redlining, múltiples idiomas, importación masiva y conservación de documentos históricos externos. Si alguno es requerido, se cotiza antes de implementar.', '',
        '## Tabla de estimación por tarea', '',
        '| ID | h | d | Modo | Referencia × unidades; riesgo | Motivo / verificación |', '|---|---:|---:|---|---|---|']
    for t in data['tasks']:
        rows.append(f"| {t['id']} | {interval(t['hours_min'],t['hours_max'])} | {interval(t['hours_min']/8,t['hours_max']/8)} | {t['mode']} | {t['ref']} × {interval(t['base_units_min'],t['base_units_max'])}; ×{interval(t['risk_min'],t['risk_max'])} | {t['reason']} |")
    for n, (layer, label) in enumerate(data['layers'].items()):
        rows += ['', f'## {n} {label} — {interval(*totals[layer])} h', '']
        for t in data['tasks']:
            if t['layer'] != layer:
                continue
            rows += [f"### {t['id']} {t['title']} — {interval(t['hours_min'],t['hours_max'])} h", '',
                f"**Fuente:** {', '.join(t['stories'])}. **Estimación:** {t['mode']} · {t['ref']} × {interval(t['base_units_min'],t['base_units_max'])}; luego ×{interval(t['risk_min'],t['risk_max'])}. {t['reason']}", '']
            rows += ['- '+activity for activity in t['activities']]
            rows += ['', '**Tecnologías:** '+t['technologies']+'.', '']
    rows += ['## 6 Dependencias y base compartida', '',
        'Se presupone login funcional, roles, API/web/worker, RDS/S3, pipeline y herramientas de pruebas. La documentación no acredita que estén entregados. Si falta toda la base, agregar una sola vez [BASE-01 a BASE-05 del módulo 2](ficha-inmueble-epica.md#6-base-compartida-si-aún-no-está-implementada): **78–176 h**. El JSON conserva el desglose. BASE-03 adapta un login existente: si se debe construir desde cero, reestimar autenticación aparte sin sumar ambas variantes.', '',
        'BE-CT-08 incluye mapeos acotados con contratos de entrada disponibles o acordados, y consulta de estado/archivo para consumidores. Los módulos 2, 8 y 9 suministran operación, partes y condiciones; sus flujos operativos y adaptación de sus pantallas no se construyen aquí. Si faltan, validar con fixtures y completar datos autorizados para preparar documentos, pero no declarar integrada una operación inexistente. Las épicas de arriendo/venta deben reutilizar este motor contractual sin cobrar otro.', '',
        'El archivo adapta los componentes de almacenamiento/autorización existentes; no cotiza de nuevo carga general de documentos de adquisición u obra. La base compartida y los servicios de cola/worker se pagan una sola vez. La configuración incremental del proveedor, renderizado y evidencia contractual sí pertenece a este módulo. Verificar reutilización real antes de consolidar costos.', '',
        'Secuencia: definir proveedor/plantillas → modelo y permisos → generación/aprobación → envío/eventos → archivo → tres recorridos de aceptación → activación. Frontend puede avanzar sobre contratos API acordados. Sin documentación/sandbox útil, integración y QA externo quedan condicionados; la incertidumbre no se resuelve con una reserva pequeña.', '',
        '## 7 Complejidad', '', '| Grupo | S/M/L | Motivo |', '|---|---|---|',
        '| Plantillas y PDF | L | Tres formatos, versiones y revisión exacta del contenido |',
        '| Envío y firma móvil | L | Identidad delegada, enlaces sensibles y timeout ambiguo |',
        '| Eventos y conciliación | L | Estados distribuidos, duplicados y concurrencia |',
        '| Archivo y trazabilidad | L | Artefactos y evidencias recuperables sin alterar originales |',
        '| Pantallas internas | M | Formularios, permisos y estados diferenciados |',
        '| Operación y validación | M | Credenciales, ambientes y pruebas de fallos reales |', '',
        'S/M/L es complejidad relativa, sin equivalencia automática a horas.', '',
        '## 8 Contingencias, servicios y entrega', '',
        f"- **Reserva condicionada:** 0–4 h, fuera del total base, solo ante un ajuste acotado de campos/IDs de un contrato de origen ya entregado. Dueño: responsable de integración con módulos de origen. Totales bajo esa condición: **{interval(total[0],total[1]+4)} h** sobre base funcional o **{interval(full[0],full[1]+4)} h** con toda la base pendiente. No cubre cambio de proveedor, falta de API, otros firmantes/formatos ni requisitos legales nuevos; se reestiman. No duplicar el riesgo tratado con M1.",
        '- **Consumo AWS fuera de horas:** cómputo de renderizado/API/worker, S3/versiones/transferencia, RDS, SQS, EventBridge Scheduler, KMS, Secrets Manager y CloudWatch. Dimensionar con región, tamaño de PDF/evidencia, retención, concurrencia y volumen de contratos.',
        '- **Proveedor fuera de horas:** suscripción, solicitudes de firma, firmantes, identificación/OTP, mensajes, almacenamiento/descargas o funcionalidades adicionales según contrato elegido. Sin proveedor y volumen no se fija precio ni se afirma disponibilidad comercial de una función.',
        '- **Esperas separadas:** selección/contratación, revisión legal, plantillas aprobadas, alta de cuenta, credenciales, validación de identidad y tiempos de firma de terceros. El calendario depende de estas condiciones y capacidad, no de dividir horas entre personas sin más.',
        '- **Aceptación:** validar los Gherkin y supuestos; conservar ADR, evidencias sandbox y limitaciones de simulaciones; registrar horas reales y recalibrar después de la primera plantilla firmada/archivada. Esta entrega es una cotización documentada, no una integración ejecutada ni envío de contratos reales.', '']
    (ROOT/'epicas y tiempos/contratos-firma-epica.md').write_text('\n'.join(rows), encoding='utf-8')
    print(json.dumps({'subtotals': totals, 'module':total, 'shared_base':base, 'with_shared_base':full}, ensure_ascii=False))


if __name__ == '__main__':
    render()
