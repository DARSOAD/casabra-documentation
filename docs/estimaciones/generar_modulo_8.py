"""Regenera la épica de arriendo desde el cálculo versionado."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def interval(a, b):
    return f'{a:g}–{b:g}'.replace('.', ',')


def render():
    data = json.loads(Path(__file__).with_name('modulo-8-estimacion.json').read_text(encoding='utf-8'))
    totals = {key: [0, 0] for key in data['layers']}
    for task in data['tasks']:
        for i, end in enumerate(('min', 'max')):
            hours = math.ceil(data['hours_per_day'] * data['references'][task['ref']]['days'] * task[f'base_units_{end}'] * task[f'risk_{end}'])
            assert hours == task[f'hours_{end}'], task['id']
            totals[task['layer']][i] += hours
    total = [sum(v[i] for v in totals.values()) for i in range(2)]
    base = [sum(v[i] for v in data['shared_base_if_pending'].values()) for i in range(2)]
    full = [total[i] + base[i] for i in range(2)]
    rows = ['# Épica del módulo 8. Arriendo de inmuebles adquiridos', '',
        'Cotización inicial de **HU-34 a HU-39, HU-46, HU-47 y HU-51 a HU-54** de las [historias del proyecto](../historias_de_usuario_plan_del_proyecto.md), según el [contexto del negocio](../contexto.md). Son 12 historias: alta y comercialización, candidatos, contrato, entrega/operación, obligaciones, cartera y portal con pago digital. Se conserva el formato por capas de la [épica del login](login-epica.md).', '',
        '**Referencia funcional:** [criterios Gherkin propuestos](arriendo-inmuebles-criterios-aceptacion.md), pendientes de validación; no se encontraron criterios aprobados específicos de arriendo. Las reglas de adquisición conservan los [criterios aprobados del módulo 2](adquisicion-inmuebles-criterios-aceptacion.md).', '',
        '## Resumen de horas', '', '| Capa | Rango |', '|---|---:|']
    rows += [f'| {label} | {interval(*totals[layer])} h |' for layer, label in data['layers'].items()]
    rows += [f'| **Módulo con base y dependencias funcionales** | **{interval(*total)} h** |',
        f'| Base técnica compartida, solo si está pendiente | {interval(*base)} h |',
        f'| **Módulo más toda la base técnica pendiente** | **{interval(*full)} h** |', '',
        '**Estos totales no incluyen construir los módulos dependientes.** El motor contractual/firma del módulo 7, la elegibilidad de adquisición y el servicio privado de archivos deben estar disponibles o presupuestarse aparte. Agregar la base técnica no entrega esos módulos. Ver la sección 6 antes de consolidar una cotización de producto.', '',
        'Horas-persona; **1 d = 8 h** como convención, no calendario. TDD, pruebas propias y revisión están dentro de las tareas funcionales; QA corresponde a recorridos y fallos entre componentes. Consumo AWS, comisiones/licencias y esperas son partidas ajenas a estas horas. No se identificó estimación anterior del módulo 8.', '',
        '## Método y evidencia', '',
        'Se aplica [estimate-task local](../skills/estimate-task/SKILL.md) y sus [referencias](../skills/estimate-task/references/calibration.md). [Datos y cálculo reproducible](../docs/estimaciones/modulo-8-estimacion.json), [generador](../docs/estimaciones/generar_modulo_8.py): `python docs/estimaciones/generar_modulo_8.py`.', '',
        '**Confianza baja:** sin horas reales Casabra ni patrones implementados comprobados; proveedor y reglas operativas pendientes. A1 (S9.2 / RED-3596, 0,5 d) es conexión UI a endpoint con errores/pruebas. A2 (RED-765 / PR 766, aproximadamente 1 d) es consultas y generación documental con servicios existentes. Son referencias importadas no verificadas, analogías parciales para pantallas y comprobantes. H (1 d) es unidad de hipótesis por entregables, no tiempo histórico. Las estimaciones previas no se tratan como mediciones.', '',
        '**Fórmula por extremo:** `ceil(8 × días_referencia × unidades_base × factor_riesgo)`. ×ref se indica antes del riesgo. M0 usa ×1 para definición; M1 usa ×1,5–2 una sola vez por dinero, permisos, PII, migraciones o falta de patrón acreditado. No duplicar TDD/revisión ni multiplicar otra vez el total. No se aplica descuento fijo por IA. Recalibrar tras el primer cobro completo; rangos sin interpretación de percentil estadístico.', '',
        '## Alcance confirmado por historias', '', '| Historia | Resultado incluido |', '|---|---|',
        '| HU-34 | Iniciar arriendo solo para inmuebles adquiridos con ruta autorizada |',
        '| HU-35 | Alistamiento, adecuaciones, disponibilidad y condiciones de oferta |',
        '| HU-36 | Ficha, fotos y seguimiento manual de anuncios/enlaces |',
        '| HU-37 | Interesados, documentos, visitas, evaluación y recomendación |',
        '| HU-38 | Condiciones completas y formalización mediante motor contractual |',
        '| HU-39 | Inventario, entrega, novedades y devolución con evidencia |',
        '| HU-46 | Cánones, vencimientos, reajustes, renovación y terminación |',
        '| HU-47 | Tablero de ocupación, cobros, deuda, mora, vacancia y vencimientos |',
        '| HU-51 | Portal propio, estado de cuenta y pago digital del canon |',
        '| HU-52 | Avisos previos, vencidos y pagos sin confirmar |',
        '| HU-53 | Estados de transacción, conciliación y pagos manuales con soporte |',
        '| HU-54 | Comprobante interno descargable de pago confirmado |', '',
        '**Reglas confirmadas del contexto:** la compañía es dueña del activo y el arrendatario es distinto del propietario original. Arriendo ocurre después de adquisición y asignación de ruta. Un pago digital solo queda confirmado con verificación del proveedor; el módulo contable consume esos movimientos para evitar duplicarlos.', '',
        '### Supuestos para poder cotizar', '',
        '- Una compañía, inmueble completo por contrato y un arrendatario principal; moneda COP propuesta y periodicidad mensual inicial. No se cotizan habitaciones/unidades independientes, múltiples pagadores, multimoneda ni períodos semanales. Se registran garantías/depósitos como condiciones cuando procedan según definición de negocio; no se presume su exigibilidad ni se implementa custodia/liquidación de depósitos.',
        '- El gerente de activos inicia la ruta Arriendo consumiendo la autorización del módulo 2. El administrador de inmuebles registra alistamiento/entrega, el asesor gestiona candidatos, el administrador confirma selección/condiciones/obligaciones/pagos manuales, y el gerente consulta indicadores. La matriz concreta y separación de funciones deben aprobarse.',
        '- Candidatos y evaluación registrados por equipo interno, con decisión manual y documentos privados. Sin solicitud pública autoservicio, scoring ni consultas externas. Se registra agenda simple de visitas. El contacto seleccionado recibe acceso al portal mediante identidad existente o invitación sobre el login compartido; no se reutiliza el rol de propietario original.',
        '- Publicación consiste en preparar ficha/fotos y registrar anuncios, canales, enlaces y estado manualmente; no hay integración automática con portales ni marketplace. Se habilitan únicamente fotografías seleccionadas como publicables; no se publica el expediente privado.',
        '- Formalización utiliza la plantilla de arriendo y flujo de dos firmantes del módulo 7: arrendatario principal y representante de compañía. Condiciones de garantías se registran como datos; codeudor/garante firmante, anexos u otrosíes requieren ampliar esa dependencia. Renovación se cotiza como nuevo contrato/período vinculado usando la misma plantilla, no como un motor de documentos adicionales.',
        '- Contrato firmado habilita la entrega bajo requisitos acordados, pero no prueba ocupación ni pago. El inicio de obligaciones depende de la fecha efectiva pactada y activación autorizada, no de una redirección de firma. Ocupación depende de entrega/devolución real.',
        '- Cargo mensual con vencimiento por día configurado; si ese día no existe, usar último día del mes, pendiente de acuerdo. Primera/última cuota especial puede tener importe explícito aprobado; no se calcula prorrateo automático. Reajuste por valor/porcentaje y fecha futuros ingresados y aprobados manualmente, sin consulta de índices, topes o fórmulas legales.',
        '- Las reglas de terminación fijan fecha efectiva y cancelación prospectiva de cargos no causados; los cargos causados y saldos permanecen. Cancelaciones y ajustes son auditados, no borrado de historia. Sin penalidades, intereses, gestión judicial ni condonación automática.',
        '- Pagos completos o abonos a una obligación seleccionada; aplicar hasta su saldo y dejar excedente como saldo a favor del mismo contrato. Reasignación manual autorizada y auditada; no aplicar entre contratos ni devolver automáticamente. Mantener suma de importe aplicado y no aplicado igual a pagos confirmados vigentes, netos de reversos.',
        '- Un proveedor y un medio de pago inicial mediante checkout alojado, con API/sandbox, webhook autenticable, consulta de estado/referencia y tratamiento de reversos. No se almacenan tarjetas ni se implementan débitos automáticos. Identificar proveedor, medio, comisiones, límites y posibilidades de prueba antes de implementar.',
        '- Pagos manuales quedan pendientes hasta validación explícita por administrador con referencia y soporte; el equipo contrasta evidencia bancaria fuera del sistema. El soporte solo no confirma pago. No se permite marcar un pago digital exitoso contra el resultado del proveedor.',
        '- Recordatorios in-app y por correo transaccional: antes del vencimiento, vencido y transacción sin confirmar. Antelación/frecuencia configurables acotadas, zona propuesta America/Bogota. Reintentos y deduplicación interna, sin prometer recepción exactamente una vez en el buzón. Sin SMS, WhatsApp, push o llamadas.',
        '- Comprobante interno único por pago confirmado, incluyendo abonos; disponible en portal y aviso con enlace. No se presenta como factura DIAN ni paz y salvo. Reversos conservan original y estado actualizado/registro compensatorio. Emitir recibo o enviar correo no altera el saldo.',
        '- App web Next.js adaptable a celular, FastAPI, RDS PostgreSQL propuesto y S3. Archivos limitados inicialmente a PDF/JPEG/PNG, con tamaños/cantidades pendientes; carga privada validada mediante servicio compartido. Sin modo offline, app nativa ni gestión avanzada de mantenimiento.', '',
        '### Estados y métricas propuestos', '',
        '| Dimensión | Regla propuesta |', '|---|---|',
        '| Disponibilidad | En alistamiento, Disponible, Reservado u Ocupado; independiente de Adquirido y de publicación |',
        '| Solicitud | Registrada, En evaluación, Recomendada, Seleccionada, Rechazada o Retirada; administrador confirma selección bajo exclusión de concurrencia |',
        '| Contrato operativo | En preparación, Pendiente de firma, Formalizado, Activo, Terminado o Cancelado; sin superposición operativa de vigencias |',
        '| Obligación | Pendiente, Parcial, Saldada o Cancelada; vencida es condición de fecha/saldo, no pérdida de historial |',
        '| Transacción | Pendiente, Confirmada, Fallida o Por conciliar; reverso se registra como movimiento compensatorio ligado a la confirmación original |',
        '| Ocupación | Conteo/ratio al corte por entrega y devolución; indicar total de activos de arriendo y excluir registros incompletos explícitamente |',
        '| Vacancia | Días disponibles sin ocupante; alistamiento se muestra aparte y se excluye de días disponibles |',
        '| Ingresos operativos | Cobros confirmados en período de pago menos reversos en el período, separados de canon causado, saldo y comisiones |',
        '| Mora | Saldo vencido y días desde vencimiento; no implica cálculo de interés ni valoración legal |', '',
        'La confirmación del navegador nunca mueve dinero. Webhooks verificados y consulta del proveedor determinan resultado. Referencia/moneda/importe inconsistentes pasan a conciliación. Una confirmación tardía puede producir saldo a favor si el cargo ya fue cubierto; no se descarta dinero. Reversos revierten imputaciones de manera trazable y pueden reabrir deuda. Terminar contrato o devolver el inmueble no elimina obligaciones previas.', '',
        '**Pendientes:** campos y documentos de candidatos, aprobadores, moneda/periodicidad finales, garantías y depósitos, fecha de activación, reglas del primer/último período, reajustes, renovaciones/terminación, proveedor/medio de pago, comisiones, disputas, frecuencia de avisos, política de retención, volumen y metas de rendimiento. Son decisiones de cotización inicial; no se inventan reglas legales ni se las presenta como aprobadas.', '',
        '**Fuera de alcance adicional:** contabilidad general, factura electrónica/DIAN, rentabilidad consolidada, conciliación bancaria por archivos, ejecución de reembolsos, cartera judicial, portales de proveedores, pólizas, automatización de mantenimiento y exportaciones BI avanzadas. El módulo 10 recibe referencias de movimientos confirmados/compensatorios: no vuelve a registrar un canon ya cobrado.', '',
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
        '| Dependencia | Qué se reutiliza | Qué se cotiza aquí |', '|---|---|---|',
        '| Módulo 2 | Adquisición, inmueble, autorización de ruta y carga privada | Consumo de elegibilidad, vínculos y adaptación de archivos a candidatos/actas |',
        '| Módulo 6, cuando hay obras | Estado de adecuaciones y evidencias existentes | Referencia y verificación operativa de alistamiento, no gestión de obra |',
        '| Módulo 7 | Plantilla de arriendo, firma, archivo contractual y renderizador PDF | Mapeo de condiciones, acceso de arrendatario, consulta de formalización y plantilla de recibo interno |',
        '| Autenticación/HU-33 | Sesión, invitación/activación y roles base | Vincular arrendatario a sus contratos y permisos específicos |',
        '| Módulo 10, consumidor futuro | Contabilidad y facturación fuera de este alcance | IDs/consultas de movimientos para evitar duplicados; no integración contable completa |', '',
        'La documentación no prueba implementación de esas dependencias. Si falta el módulo 7, sus **267–564 h** según la [épica contractual](contratos-firma-epica.md) se consideran aparte una sola vez y se revisan al consolidar. Este módulo no hereda otra vez ese costo. Si falta elegibilidad o servicio de archivos, presupuestar las partidas necesarias de adquisición/archivos, sin asumir que 78–176 h de infraestructura las resuelven.', '',
        'La base técnica pendiente se toma de [BASE-01 a BASE-05 del módulo 2](ficha-inmueble-epica.md#6-base-compartida-si-aún-no-está-implementada): **78–176 h**, una sola vez para el producto. Incluye infraestructura/pipeline/pruebas/logs y adaptación de autenticación existente. BASE-03 no construye login desde cero; esa variante requiere reestimación sin sumar ambas. No volver a cobrar base AWS, motor de escaneo, firma o renderizador por cada módulo.', '',
        'BE-AR-03/04/06/11 y OPS-AR-02 adaptan el servicio de archivos, sin construir cuarentena/antivirus desde cero. Si el CRM del módulo 5 ya aporta agenda/avisos, comprobar compatibilidad antes de descontar trabajo: candidatos de arriendo y comunicaciones de cartera tienen datos/permisos/reglas propias. La estimación no presume esa reutilización adicional.', '',
        'Secuencia: cerrar políticas/proveedor → modelo/permisos → alistamiento/candidatos → contrato/entrega → calendario/cuenta → pagos/conciliación → recibos/avisos → indicadores → validación/activación. Frontend puede avanzar con contratos API acordados. Faltan capacidades/equipo para fijar calendario; los días expresan esfuerzo, no fecha de entrega.', '',
        '## 7 Complejidad', '', '| Grupo | S/M/L | Motivo |', '|---|---|---|',
        '| Ficha, anuncios y candidatos | M | Datos privados, selección y disponibilidad |',
        '| Contrato y ciclo operativo | L | Firma dependiente, vigencias, entrega y cierre |',
        '| Obligaciones y cuenta corriente | L | Fechas, abonos, ajustes e invariantes de dinero |',
        '| Pagos y conciliación | L | Proveedor, eventos, concurrencia y reversos |',
        '| Portal, avisos y recibos | L | Varios recorridos móviles y estados consistentes |',
        '| Indicadores y operación | M | Cortes, conteos, recuperación y trazabilidad |', '',
        'S/M/L expresa complejidad relativa y no se convierte automáticamente a horas.', '',
        '## 8 Contingencias, consumo y entrega', '',
        f"- **Reserva condicionada:** 0–4 h, una sola vez fuera del total base, ante ajuste acotado de ID/campo en contrato de adquisición o firma ya entregado. Dueño: responsable de integración. Totales con esa condición: **{interval(total[0],total[1]+4)} h** con dependencias funcionales o **{interval(full[0],full[1]+4)} h** agregando toda la base técnica. No cubre proveedor incompatible, nuevos medios, reglas financieras adicionales ni construir módulos faltantes. No sumar reserva porcentual sobre el mismo riesgo de M1.",
        '- **Consumo AWS separado:** API/web/worker, RDS, S3/versiones/transferencia, KMS, SQS, EventBridge Scheduler, Secrets Manager, SES y CloudWatch. Se requiere región, volumen de contratos/pagos/correos, tamaño de archivos, concurrencia y retención para dimensionar costos monetarios.',
        '- **Servicios externos separados:** tarifas y comisiones del proveedor de pagos, transacciones de firma del módulo 7 y cualquier licencia contratada. Sin proveedor y volumen no se inventan precios ni capacidades. Importe pagado por arrendatario, comisión y liquidación al comercio son conceptos separados.',
        '- **Esperas:** aprobación de reglas/plantillas, contratación y alta de pagos, credenciales/sandbox, dominio/SES y aceptación de negocio. No forman horas de desarrollo ni garantizan disponibilidad inmediata.',
        '- **Aceptación:** validar supuestos/Gherkin, conservar ADR y evidencia de escenarios reales frente a simulaciones, y recalibrar con horas reales. Esta entrega documenta una cotización; no activa cobros, contratos ni notificaciones reales.', '']
    (ROOT/'epicas y tiempos/arriendo-inmuebles-epica.md').write_text('\n'.join(rows), encoding='utf-8')
    print(json.dumps({'subtotals': totals, 'module':total, 'shared_base':base, 'with_shared_base':full}, ensure_ascii=False))


if __name__ == '__main__':
    render()
