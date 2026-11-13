"""Regenera la épica financiera desde su cálculo versionado."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def interval(a, b):
    return f'{a:g}–{b:g}'.replace('.', ',')


def render():
    data = json.loads(Path(__file__).with_name('modulo-10-estimacion.json').read_text(encoding='utf-8'))
    totals = {key: [0, 0] for key in data['layers']}
    for task in data['tasks']:
        for i, end in enumerate(('min', 'max')):
            hours = math.ceil(data['hours_per_day'] * data['references'][task['ref']]['days'] * task[f'base_units_{end}'] * task[f'risk_{end}'])
            assert hours == task[f'hours_{end}'], task['id']
            totals[task['layer']][i] += hours
    total = [sum(v[i] for v in totals.values()) for i in range(2)]
    base = [sum(v[i] for v in data['shared_base_if_pending'].values()) for i in range(2)]
    full = [total[i] + base[i] for i in range(2)]
    rows = ['# Épica del módulo 10. Pagos y utilidades', '',
        'Cotización inicial de **HU-27 a HU-29** de las [historias del proyecto](../historias_de_usuario_plan_del_proyecto.md), según el [contexto del negocio](../contexto.md) y la estructura por capas de la [épica del login](login-epica.md). Incluye clasificación financiera, resultados por inmueble/proyecto y documentos fiscales mediante un proveedor tecnológico.', '',
        '**Referencia funcional:** [criterios Gherkin propuestos](pagos-utilidades-criterios-aceptacion.md). No se encontraron criterios aprobados específicos ni una estimación anterior del módulo 10. Las reglas de reconocimiento, fórmulas y aplicabilidad fiscal de esta cotización requieren validación del contador/gerente.', '',
        '## Resumen de horas', '', '| Capa | Rango |', '|---|---:|']
    rows += [f'| {label} | {interval(*totals[layer])} h |' for layer, label in data['layers'].items()]
    rows += [f'| **Módulo con base y fuentes funcionales** | **{interval(*total)} h** |',
        f'| Base técnica compartida, solo si está pendiente | {interval(*base)} h |',
        f'| **Módulo más toda la base técnica pendiente** | **{interval(*full)} h** |', '',
        '**Ambos escenarios excluyen construir las fuentes operativas.** Se requieren inmueble/identidad/archivos y contratos de datos de obra, arriendo y venta. Los pagos digitales y cartera del módulo 8 no se cotizan otra vez. Agregar infraestructura no entrega esas funcionalidades.', '',
        'Horas-persona; **1 d = 8 h** como convención, no calendario. TDD, pruebas propias y revisión están incluidos en tareas funcionales. QA cubre recorridos, integraciones y recuperación entre componentes. Consumo AWS, proveedor fiscal, trámites y esperas son partidas aparte.', '',
        '## Método y evidencia', '',
        'Se aplica [estimate-task local](../skills/estimate-task/SKILL.md) y su [calibración](../skills/estimate-task/references/calibration.md). [Cálculo reproducible](../docs/estimaciones/modulo-10-estimacion.json) y [generador](../docs/estimaciones/generar_modulo_10.py): `python docs/estimaciones/generar_modulo_10.py`.', '',
        '**Confianza baja:** sin tiempos reales Casabra ni fuentes/proveedor comprobados. A1 (S9.2 / RED-3596, 0,5 d) es referencia importada no verificada de UI a endpoint, errores y pruebas; analogía parcial para estas vistas financieras. H (1 d) es unidad de hipótesis por entregables, no medición. No se tratan estimaciones anteriores como productividad observada.', '',
        '**Fórmula por extremo:** `ceil(8 × días_referencia × unidades_base × factor_riesgo)`. ×ref se expresa antes del riesgo. M0 usa ×1; M1 usa ×1,5–2 una sola vez por dinero, permisos, PII, migraciones y patrón no comprobado. No volver a multiplicar el total ni duplicar TDD/revisión. No se supone descuento fijo por IA; recalibrar con horas reales y no interpretar rangos como percentiles.', '',
        '## Alcance funcional', '', '| Historia | Resultado incluido |', '|---|---|',
        '| HU-27 | Consultar/clasificar costos e ingresos por inmueble/proyecto e importar operaciones sin duplicar pagos |',
        '| HU-28 | Calcular y registrar resultado y retorno simple según política/versiones aprobadas |',
        '| HU-29 | Preparar, transmitir mediante proveedor, consultar y archivar facturas y soportes fiscales |', '',
        '**Confirmado por contexto:** arriendo y venta explotan inmuebles adquiridos de la compañía; un pago digital se confirma en su operación con evidencia del proveedor. Este módulo consume movimientos y sus correcciones. Emitir factura no cobra dinero, clasificar costo no demuestra desembolso y un comprobante interno del canon no sustituye un documento fiscal.', '',
        '### Supuestos financieros para cotizar', '',
        '- Una compañía/emisor, moneda COP inicial y un catálogo acotado de categorías aprobado por contador. Sin multicompañía, conversión de moneda, libro mayor de partida doble, nómina, declaraciones tributarias o contabilidad estatutaria completa.',
        '- Se distingue hecho económico, reconocimiento financiero, cargo, cobro y documento fiscal mediante vínculos estables. Un canon facturado y cobrado no crea dos ingresos; un gasto de obra importado y documentado fiscalmente no crea dos costos. La fecha de reconocimiento es definida por política aprobada, no se deduce solo del pago.',
        '- Cánones/pagos/reversos proceden de módulo 8; ventas/pagos del 9; gastos de obra del 6 y activo/adquisición del 2. La ingesta tiene clave de origen, versión, cursor y excepciones. Una fuente ausente no se reemplaza automáticamente por un movimiento manual que pueda duplicarse cuando llegue.',
        '- Contador clasifica y aprueba mapeos simples por fuente; reparte importes manualmente entre inmuebles/proyectos conservando total. Si un proyecto pertenece a un inmueble, sus costos se incluyen una vez en el consolidado. Correcciones son versionadas/compensatorias, sin borrar movimientos originales.',
        '- Costos/ingresos externos faltantes se registran con soporte, referencia y vínculo económico. Pago de adquisición realizado fuera de la plataforma se registra aparte y requiere validación expresa del contador con evidencia; no se ejecutan transferencias. Su confirmación/corrección puede producir el hito consumido por módulo 11.',
        '- Propuesta gerencial de HU-28: I = ingresos reconocidos; C = costos/gastos imputables reconocidos; R = I − C. Retorno simple acumulado al corte = R/B, donde B es base de inversión aprobada con componentes identificados. Se muestran también cobros por separado. La fórmula y qué integra cada variable deben validarse; no se promete equivalencia automática a estados financieros o indicadores NIIF.',
        '- Inversión capitalizada se conserva como base y no se resta como gasto por importar el desembolso. Si corresponde reconocer costo de venta, contador aprueba su reclasificación/importe en C; no se deduce otra vez B al calcular R. Arriendo y venta tienen políticas de reconocimiento distintas que se documentan antes de construir.',
        '- El retorno inicial es simple, no anualizado, acumulado desde inicio de la inversión hasta corte. Reportes de período muestran I/C/R del período y etiquetan la base; no mezclan ese resultado con un retorno de otro intervalo. B cero = No aplica. Pérdida se muestra con signo; no se calcula retorno definitivo con datos incompletos.',
        '- Cálculos registrados conservan entradas, versión de fórmula, política, moneda, inicio/corte, responsable y cobertura. Para consolidar se suman componentes compatibles o se usa un agregado autoritativo; no se promedian porcentajes sin ponderación. Sin TIR, VAN, depreciación, valorización, reparto de dividendos o proyecciones automáticas.', '',
        '### Supuestos fiscales y fuentes oficiales', '',
        'La DIAN describe la validación de factura electrónica y notas crédito/débito como un proceso distinto de su preparación y transmisión. Por eso el modelo separa recepción del proveedor, resultado DIAN, archivo y entrega. [DIAN: validación previa](https://www.dian.gov.co/impuestos/factura-electronica/factura-electronica/Paginas/validacion-previa.aspx).', '',
        'El documento soporte de adquisiciones a no obligados a facturar y sus notas de ajuste tienen un flujo específico. Se incluyen como familia adicional de cotización, no como sinónimo de PDF de recibo. La aplicabilidad concreta a Casabra la decide el contador. [DIAN: documento soporte](https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/documento-soporte-en-adquisiciones-efectuadas-a-sujetos-no-obligados-a-expedir-factura-de-venta-o-documento-equivalente-3/).', '',
        'Las contingencias distinguen causas y procedimientos; un timeout local no prueba una contingencia DIAN ni valida un documento. Se incluye registro/seguimiento del procedimiento delegado al proveedor y su posterior conciliación, sin fijar plazos legales en esta estimación. [DIAN: inconvenientes tecnológicos](https://www.dian.gov.co/impuestos/factura-electronica/inconvenientes-tecnologicos/Paginas/default.aspx). Fuentes consultadas el 13 de noviembre de 2026; confirmar normativa/anexos aplicables con proveedor y contador al implementar.', '',
        '- Un proveedor tecnológico con API/sandbox para cinco tipos: factura electrónica de venta, nota crédito, nota débito, documento soporte y nota de ajuste del soporte. Selección pendiente; no se verificó una API comercial concreta. Su contrato debe cubrir firma/formato fiscal, transmisión, consulta, artefactos y entrega según documento.',
        '- El contador determina si corresponde emitir y aprueba datos, impuestos/retenciones y tratamiento por concepto. No se asume que todas las adquisiciones, ventas o arriendos tienen el mismo tratamiento ni que facturación ocurre al confirmar el pago. Parámetros/rangos y cambios vigentes se validan antes de emitir.',
        '- Se reutilizan tercero/operación y líneas para preparar borrador; no volver a digitar hechos económicos. Una aprobación corresponde a versión exacta. Cambios previos al envío requieren revisión; documentos validados se corrigen por el mecanismo fiscal que corresponda, sin sobrescritura.',
        '- Numeración coordinada con un único asignador en proveedor, o mecanismo documentado equivalente. Se controla referencia/idempotencia; timeout produce consulta/conciliación, no otra emisión a ciegas. Reglas de número ante rechazo se siguen según proveedor/norma vigente, sin reutilización arbitraria.',
        '- Se archivan XML, representación gráfica y respuesta/evidencias disponibles, con identificador fiscal correspondiente a cada tipo. La entrega al destinatario se delega al proveedor y se registra por separado. Reintentar descarga o entrega no crea otro documento ni ingreso.',
        '- No se incluyen integración directa propia a DIAN, habilitación como proveedor tecnológico, RADIAN, documentos equivalentes POS, nómina electrónica, recepción automática de todas las facturas de proveedores, certificados propios implementados desde cero ni trámites tributarios por cuenta del cliente.', '',
        '### Estados y pendientes', '', '| Dimensión | Regla |', '|---|---|',
        '| Movimiento financiero | Pendiente de clasificación/revisión, Aprobado o Corregido con vínculo e historial |',
        '| Cobro/pago | Estado operativo de su fuente; un documento fiscal no lo confirma ni revierte |',
        '| Cálculo | Preliminar/Parcial o Registrado con política, corte y versión de entradas |',
        '| Fiscal | Borrador, Aprobado para envío, En proceso, Validado, Rechazado o Por conciliar |',
        '| Contingencia | Estado/procedimiento específico registrado y conciliado con proveedor; no equivalente a Validado |',
        '| Archivo/entrega | Pendiente, Disponible/Entregado o Error, separados del resultado fiscal |', '',
        '**Pendientes:** catálogo y política de reconocimiento, inversión/costo de venta, reparto entre proyectos/activos, impuestos/redondeos, fuentes/IDs, proveedor, tipos efectivos de soporte, volumen, numeración, certificados, responsables, contingencia y retención. Son supuestos acotados para estimar, no aprobaciones fiscales ni configuración productiva.', '',
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
    rows += ['## 6 Dependencias y ausencia de doble cobro', '',
        '| Dependencia | Se reutiliza | Incremento del módulo 10 |', '|---|---|---|',
        '| Módulo 2 / login | Inmueble, operación, identidad y archivos privados | Referencias, permisos financieros y costos/pagos de adquisición registrados |',
        '| Módulo 6 | IDs de gastos operativos de obra y correcciones | Importación, clasificación y reconocimiento; no registrar de nuevo esos gastos |',
        '| Módulo 8 | Cánones, cobros/abonos confirmados y reversos | Ingesta/relación con ingresos y documentos fiscales; no pasarela/cartera nueva |',
        '| Módulo 9 | Venta, precio, pagos externos validados y soportes | Clasificación, referencia fiscal y resultado de la operación; no otro cierre de venta |',
        '| Módulo 11 | Portal, compartición y tablero transversal | API autoritativa de resultados y evento de pago de adquisición; no repetir UI de HU-32 |',
        '| Proveedor fiscal | Formato/firma/transmisión/validación/artefactos/entrega contratados | Adaptador, reglas de aprobación, archivo local y operación desde Casabra |', '',
        'No se verificó código entregado de las fuentes. Sin datos/contratos disponibles puede desarrollarse con fixtures, pero no declararse integrada la operación. Construcción de fuentes, regularización de datos históricos y adaptación de procesos que no existen se estiman aparte. Arriendo conserva [original](arriendo-inmuebles-epica.md) y [v2](arriendo-inmuebles-epica-v2.md): son alternativas, no se suman y ninguna se considera aprobada por esta referencia.', '',
        'La [épica del portal](portal-cliente-epica.md) consume BE-PU-06 y el evento de BE-PU-04; el portal mantiene su propia autorización de compartición. Ahora existe estimación del módulo 10, no implementación: formalización contractual sola no confirma el pago al propietario. La confirmación aquí prevista es un registro manual validado con evidencia de un desembolso externo.', '',
        'Si falta la base técnica, agregar una sola vez [BASE-01 a BASE-05 del módulo 2](ficha-inmueble-epica.md#6-base-compartida-si-aún-no-está-implementada): **78–176 h**, desglosadas en JSON. BASE-03 adapta login existente, no lo construye desde cero. Servicios S3/worker/colas/pipeline y archivo seguro no se cobran íntegros otra vez por módulo; solo su configuración incremental.', '',
        'Secuencia: política/proveedor → modelo/permisos → ingesta/clasificación → resultados/API → configuración fiscal → emisión/ajustes/archivo → pruebas → activación. Frontend puede avanzar con contrato acordado. Calendario depende de capacidad, entrega de fuentes y habilitación del proveedor; días-persona no son fechas.', '',
        '## 7 Complejidad', '', '| Grupo | S/M/L | Motivo |', '|---|---|---|',
        '| Ingesta y clasificación | L | Múltiples fuentes, hechos económicos y duplicados |',
        '| Resultado y retorno | L | Reconocimiento, base de inversión y versiones |',
        '| Emisión fiscal y ajustes | L | Cinco tipos documentales, proveedor y estados externos |',
        '| Pantallas y configuración | M | Formularios monetarios, revisión y permisos |',
        '| Recuperación y operación | L | Emisión incierta, contingencia, integridad y archivo |', '',
        'S/M/L es complejidad relativa sin conversión automática a horas.', '',
        '## 8 Contingencias, consumo y aceptación', '',
        f"- **Reserva condicionada:** 0–4 h una sola vez, fuera del total base, por ajuste acotado de ID/campo de un contrato fuente ya entregado. Dueño: responsable de integración. Totales con esa condición: **{interval(total[0],total[1]+4)} h** con fuentes funcionales o **{interval(full[0],full[1]+4)} h** agregando toda la base técnica. No cubre un proveedor incompatible, nuevos documentos fiscales, cambios de política complejos o integración DIAN directa; se reestiman. No sumar porcentaje por el riesgo ya incluido en M1.",
        '- **Consumo AWS separado:** API/web/worker, RDS, S3/versiones/transferencia, KMS, Secrets Manager, colas/programación y CloudWatch. Precio monetario requiere región, volumen, retención y concurrencia; no se inventan tarifas.',
        '- **Proveedor y trámites separados:** suscripción, documentos/transacciones, certificados y servicios contratados; alta/habilitación/rangos y revisión tributaria de la empresa. No se presupone precio ni compatibilidad de un proveedor no seleccionado.',
        '- **Aceptación:** validar política, fórmulas y Gherkin; conservar evidencia sandbox y limitaciones de simulación, configurar contingencia vigente y registrar horas reales para recalibrar. Esta entrega es cotización documental; no emite facturas ni realiza pagos reales.', '']
    (ROOT/'epicas y tiempos/pagos-utilidades-epica.md').write_text('\n'.join(rows), encoding='utf-8')
    print(json.dumps({'subtotals': totals, 'module':total, 'shared_base':base, 'with_shared_base':full}, ensure_ascii=False))


if __name__ == '__main__':
    render()
