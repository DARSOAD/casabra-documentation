"""Regenera la épica de obra y valida sus importes desde el JSON versionado."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def interval(a, b):
    return f'{a:g}–{b:g}'.replace('.', ',')


def render():
    data = json.loads(Path(__file__).with_name('modulo-6-estimacion.json').read_text(encoding='utf-8'))
    totals = {key: [0, 0] for key in data['layers']}
    for task in data['tasks']:
        for i, end in enumerate(('min', 'max')):
            hours = math.ceil(data['hours_per_day'] * data['references'][task['ref']]['days'] * task[f'base_units_{end}'] * task[f'risk_{end}'])
            assert hours == task[f'hours_{end}'], task['id']
            totals[task['layer']][i] += hours
    total = [sum(v[i] for v in totals.values()) for i in range(2)]
    base = [sum(v[i] for v in data['shared_base_if_pending'].values()) for i in range(2)]
    full = [total[i] + base[i] for i in range(2)]
    rows = ['# Épica del módulo 6. Proyectos de obra', '',
        'Cotización inicial de **HU-16 a HU-19** de las [historias del proyecto](../historias_de_usuario_plan_del_proyecto.md), según el [contexto del negocio](../contexto.md). Organizada por capas como la [épica del login](login-epica.md), sin trasladar sus ejemplos de otros negocios.', '',
        '**Referencia funcional:** [criterios Gherkin propuestos](proyectos-obra-criterios-aceptacion.md). No se encontraron criterios aprobados específicos de obra; los supuestos y escenarios deben validarse antes de implementar. Las reglas de adquisición siguen los [criterios aprobados del módulo 2](adquisicion-inmuebles-criterios-aceptacion.md).', '',
        '## Resumen de horas', '', '| Capa | Rango |', '|---|---:|']
    rows += [f'| {label} | {interval(*totals[layer])} h |' for layer, label in data['layers'].items()]
    rows += [f'| **Módulo sobre base funcional** | **{interval(*total)} h** |',
        f'| Base compartida, solo si está pendiente | {interval(*base)} h |',
        f'| **Módulo con toda la base pendiente** | **{interval(*full)} h** |', '',
        '**Unidad:** horas-persona; 1 d = 8 h como convención, no plazo de calendario. TDD, pruebas propias y revisión están incluidos en cada tarea funcional. QA corresponde a pruebas transversales en staging. Consumo AWS y esperas no forman parte del esfuerzo. No se identificó una estimación anterior del módulo 6.', '',
        '## Método y evidencia', '',
        'Se aplica [estimate-task local](../skills/estimate-task/SKILL.md) y sus [referencias](../skills/estimate-task/references/calibration.md). [Cálculo reproducible](../docs/estimaciones/modulo-6-estimacion.json) y [generador de esta épica](../docs/estimaciones/generar_modulo_6.py): `python docs/estimaciones/generar_modulo_6.py`.', '',
        '**Confianza baja.** No existen horas reales de Casabra disponibles ni código de base comprobado. A1 (S9.2 / RED-3596, 0,5 d) es una referencia importada no verificada para conectar UI a endpoint, con errores y pruebas básicas: analogía parcial para estas pantallas. H (1 d) es una unidad de hipótesis técnica por entregables, no una medición histórica. Las estimaciones de otros módulos no se usan como tiempos reales.', '',
        '**Fórmula por extremo:** `ceil(8 × días_referencia × unidades_base × factor_riesgo)`. Las unidades ×ref se indican antes del factor. M0 aplica ×1 a definición; M1 aplica ×1,5–2 una vez por dinero, permisos, migraciones o ausencia de patrón comprobado. No se vuelve a multiplicar el total ni se suma TDD otra vez. No se presume ahorro fijo por IA. Recalibrar con tiempos reales del primer flujo; los rangos no son percentiles estadísticos.', '',
        '## Alcance confirmado y supuestos de cotización', '',
        '| Historia | Resultado incluido |', '|---|---|',
        '| HU-16 | Proyecto con presupuesto, cronograma y responsables |',
        '| HU-17 | Reporte semanal y fotos desde sitio |',
        '| HU-18 | Archivos de licencias y permisos del proyecto |',
        '| HU-19 | Tablero para identificar retrasos y sobrepresupuesto |', '',
        '**Confirmado por contexto:** la compañía compra los inmuebles; las adecuaciones son posteriores a adquisición y no cambian la ruta Arriendo/Venta. El propietario original no dirige la obra del activo de la compañía. Finalizar obra no publica automáticamente el inmueble ni modifica su estado de adquisición.', '',
        '**Supuestos que permiten cotizar:**', '',
        '- Una compañía, un proyecto activo por inmueble Adquirido con ruta definida y adecuaciones indicadas; varios proyectos históricos son posibles. Se reutiliza el vínculo del módulo 2, no se construye adquisición en esta épica.',
        '- Jefe de obra con acceso a proyectos asignados y gerente con consulta global. El jefe autorizado crea el proyecto y asigna responsables internos; se valida esa facultad en definición. HU-33 no enumera actualmente jefe de obra: se requiere incorporarlo a la matriz, sin asumir que ya está implementado. No se modifica esa historia como regla aprobada.',
        '- Estados propuestos: Planificado → En ejecución → Finalizado; cancelación motivada desde Planificado/En ejecución. Inicio congela presupuesto y fechas base. Finalización requiere todas las actividades base al 100%. Sin reaperturas ni cambio de línea base; reprogramaciones operativas conservan comparación contra la original.',
        '- Cronograma tabular con actividades, fechas y responsables, sin dependencias, ruta crítica ni Gantt interactivo. Avance por actividad entre 0 y 100%; global = promedio simple de actividades base. Cambios de cantidad de actividades tras inicio y ponderaciones especiales requieren reestimación.',
        '- Un reporte vigente por semana con historial de correcciones. Sin reporte no se infiere avance cero; los datos previos muestran fecha. Fecha límite vencida y último avance conocido menor a 100% identifica atraso confirmado; sin avance conocido se muestra Avance sin confirmar. Al finalizar, puede conservarse señal de cierre tardío comparando fecha real contra fin base.',
        '- Presupuesto por partidas y una moneda COP propuesta. Para HU-19 se añade registro manual operativo de gastos y anulaciones, porque no se definió una fuente de costo real. Sobrecosto = max(costo registrado − presupuesto base, 0); porcentaje solo si presupuesto > 0. Sin movimientos se muestra Sin costos registrados. No representa contabilidad conciliada, pagos o compromisos de compra.',
        '- Fotos JPEG/PNG y documentos PDF como formatos iniciales propuestos; límites de tamaño/cantidad, retención y tratamiento de formatos de cámara como HEIC pendientes. Web adaptable a celular con conexión; no se incluye modo offline. Los adjuntos son privados, versionados y utilizables tras validación/análisis.',
        '- FastAPI, Next.js, AWS, S3 y RDS PostgreSQL propuesto. TDD backend con pytest/HTTPX, componentes con Vitest/Testing Library y recorridos con Playwright. La cotización no obliga a versiones de librerías aún no seleccionadas.', '',
        '**Pendientes:** aprobar estados, facultades del jefe, número de proyectos simultáneos, partidas/impuestos/redondeo, responsables, definición de semana y zona horaria (propuesta America/Bogota), reglas de corrección, porcentaje/ponderación de avance, fuente y completitud de gastos, fecha de corte de indicadores, volúmenes y límites de archivos. La licencia se archiva: no se comprueba su validez jurídica ni se determinan requisitos legales.', '',
        '**Exclusiones:** compras/proveedores, inventarios de materiales, nómina, facturación, pagos, integración contable automática, firma electrónica, inspección legal, BIM/CAD, OCR/video, ubicación GPS, portales de contratistas, notificaciones externas, reportes al propietario y aplicaciones nativas. El módulo 10 podrá consumir los mismos IDs de gasto en una integración futura; no volver a cargar movimientos sin conciliación.', '',
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
        'El escenario principal presupone login funcional, roles, API/web, RDS/S3, worker, pipeline y herramientas de pruebas. La documentación no acredita su implementación. Si faltan, sumar una sola vez [BASE-01 a BASE-05 del módulo 2](ficha-inmueble-epica.md#6-base-compartida-si-aún-no-está-implementada): **78–176 h**. BASE-03 adapta autenticación existente; construir login desde cero exige estimación independiente, sin acumular ambas variantes.', '',
        'El contrato de elegibilidad de inmuebles debe provenir del módulo 2; BE-OB-02 cubre su consumo, no construir todo ese módulo. Si adquisición no está disponible, su desarrollo y esperas se presupuestan aparte. No se requiere que contabilidad esté implementada para el supuesto de gasto manual.', '',
        '**Archivos compartidos:** BE-OB-05 incluye el flujo de obra y adaptador de análisis; OPS-OB-01 incluye desplegar/configurar el motor si no está disponible. No se ha descontado una reutilización no verificada. Si módulo 2 ya entrega carga privada, validación, escaneo y versiones, revisar esas dos partidas contra evidencia y cobrar únicamente adaptaciones. En una cotización conjunta, asignar una sola vez la creación del motor común; no sumar íntegramente ambas implementaciones. Las cifras aquí son del módulo aislado sobre base técnica, no un total consolidado de producto.', '',
        'Secuencia: definir reglas → modelo/permisos → planificación y presupuesto → avance/archivos/gastos → tablero → validación → entrega. Frontend puede avanzar con contratos acordados. Capacidad y dependencias determinan el calendario; días-persona no equivalen a fechas.', '',
        '## 7 Complejidad', '', '| Grupo | S/M/L | Motivo |', '|---|---|---|',
        '| Proyecto, presupuesto y cronograma | L | Línea base, dinero y reglas de cambio |',
        '| Avance y gastos | M | Historial, idempotencia y correcciones |',
        '| Fotos, licencias y permisos | L | Conectividad, archivos privados y procesamiento asíncrono |',
        '| Tablero gerencial | M | Integridad de agregados y datos incompletos |',
        '| Operación y entrega | M | Recuperación entre RDS, S3 y worker |', '',
        'S/M/L expresa complejidad relativa; no se convierte automáticamente a horas.', '',
        '## 8 Contingencias y costos externos', '',
        f"- **Reserva condicionada:** 0–4 h, fuera del total base, solo ante ajuste acotado de identificadores/campos de elegibilidad del contrato entregado por módulo 2. Dueño: responsable de integración. Totales bajo esa condición: **{interval(total[0],total[1]+4)} h** sobre base funcional o **{interval(full[0],full[1]+4)} h** con toda la base pendiente. No cubre construir adquisición, cambiar fuente de gastos o introducir offline; esos cambios se reestiman. No añadir reserva porcentual por el riesgo ya tratado con M1.",
        '- **Consumo AWS separado:** almacenamiento, versiones, solicitudes y transferencia S3; RDS; cómputo API/web/worker y análisis de archivos; SQS; KMS y CloudWatch. Costos monetarios pendientes de región, tamaño/cantidad de fotos, concurrencia, retención y tráfico. No se inventan precios ni se cobra infraestructura completa por cada módulo.',
        '- **Entrega y confianza:** aprobar supuestos/Gherkin antes de implementar, conservar ADR y evidencias, registrar horas reales para recalibrar. Esperas por permisos, decisiones y aceptación se separan. Esta entrega es documentación de cotización; no implementa la aplicación de obra.', '']
    (ROOT/'epicas y tiempos/proyectos-obra-epica.md').write_text('\n'.join(rows), encoding='utf-8')
    print(json.dumps({'subtotals': totals, 'module':total, 'shared_base':base, 'with_shared_base':full}, ensure_ascii=False))


if __name__ == '__main__':
    render()
