"""Regenera la épica CRM desde sus datos de estimación versionados."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = Path(__file__).with_name('modulo-5-estimacion.json')

def fmt(value):
    return f'{value:g}'.replace('.', ',')

def span(low, high):
    return f'{fmt(low)}–{fmt(high)}'

def render():
    data = json.loads(DATA.read_text(encoding='utf-8'))
    totals = {}
    rows = []
    for task in data['tasks']:
        hours = [math.ceil(8 * data['references'][task['ref']]['days'] * task[f'base_units_{end}'] * task[f'risk_{end}']) for end in ('min', 'max')]
        assert hours == [task['hours_min'], task['hours_max']], task['id']
        subtotal = totals.setdefault(task['layer'], [0, 0])
        for i in range(2):
            subtotal[i] += hours[i]
    total = [sum(t[i] for t in totals.values()) for i in range(2)]
    base = [sum(t[i] for t in data['shared_base_if_pending'].values()) for i in range(2)]
    rows.extend(['# Épica del módulo 5. CRM', '',
        'Cotización inicial de **HU-12 a HU-15**, según las [historias del proyecto](../historias_de_usuario_plan_del_proyecto.md) y el [contexto del negocio](../contexto.md). Cubre seguimiento de propietarios y oportunidades de adquisición. El CRM de venta de activos de la compañía (HU-43 a HU-45 y HU-50) se estima en el módulo 9.', '',
        '**Referencia funcional:** [criterios Gherkin propuestos](crm-criterios-aceptacion.md). No se encontraron criterios aprobados específicos para CRM: los escenarios y supuestos aquí documentados están pendientes de validación.', '',
        '## Resumen de horas', '', '| Capa | Rango |', '|---|---:|'])
    for layer, label in data['layers'].items():
        rows.append(f'| {label} | {span(*totals[layer])} h |')
    rows.extend([f'| **Módulo sobre base funcional** | **{span(*total)} h** |', f'| Base compartida, solo si está pendiente | {span(*base)} h |', f'| **Módulo con toda la base pendiente** | **{span(total[0]+base[0], total[1]+base[1])} h** |', '',
        'Horas-persona; **1 d = 8 h** como convención, no plazo de calendario. TDD, pruebas propias y revisión están dentro de cada tarea funcional. QA cubre recorridos entre capas y operación real, sin repetir esas pruebas. Consumo AWS, esperas y módulos dependientes se separan.', '',
        '## Método y evidencia', '',
        'Se aplica la [skill local estimate-task](../skills/estimate-task/SKILL.md) y sus [referencias de calibración](../skills/estimate-task/references/calibration.md). [Datos y cálculo reproducible](../docs/estimaciones/modulo-5-estimacion.json); [generador](../docs/estimaciones/generar_modulo_5.py). Ejecutar `python docs/estimaciones/generar_modulo_5.py` desde el repositorio.', '',
        '**Confianza baja:** no hay horas reales de Casabra ni implementación comprobada de la base. A1 (S9.2 / RED-3596, 0,5 d) es una referencia importada no verificada para conectar una UI a un endpoint, con errores y pruebas. Su uso es una analogía parcial: aquí hay varias vistas y datos personales. H (1 d) es únicamente una unidad de hipótesis técnica por entregables; no es un tiempo medido. No se identificó una estimación anterior del módulo 5 que comparar.', '',
        '**Fórmula por extremo:** `ceil(8 × días_referencia × unidades_base × factor_riesgo)`. Las unidades ×ref se expresan antes del riesgo. M0 usa ×1; M1 usa ×1,5–2 una sola vez por permisos, datos personales, migraciones o falta de patrón comprobado. No aplicar el factor de nuevo al total ni agregar un descuento fijo por IA. Recalibrar tras el primer recorrido completo con horas reales; los rangos no son percentiles estadísticos.', '',
        '## Alcance, supuestos y pendientes', '',
        '- **Confirmado por HU-12 a HU-15:** ficha del cliente con etapa, llamadas/visitas/compromisos compartidos, recordatorios de seguimiento y tablero de clientes por etapa e inmuebles captados para gerente.',
        '- **Supuesto de cotización:** una compañía y equipo comercial autorizado con historial compartido; asesor consulta y registra, gerente consulta tablero. Propietario original y arrendatario no acceden a notas internas. Segmentación por sucursal/cartera y administración completa de permisos quedan pendientes, no incluidas.',
        '- **Supuesto:** clientes existentes del onboarding, sin nueva captación, importación masiva ni deduplicación avanzada. Vínculos a inmuebles/solicitudes del módulo 2, sin copiar documentos o crear otro expediente. Una ficha de cliente puede vincular varias solicitudes.',
        '- **Etapas propuestas:** Contactado, En evaluación y Contrato firmado, tomadas de HU-12; catálogo fijo y registro manual trazable para cotizar. Falta definir etapa inicial, transiciones, significado del contrato y quién puede registrarlo. Contrato firmado no significa Adquirido ni cambia estados del inmueble. Firma y sincronización automática pertenecen al módulo 7 y no están incluidas.',
        '- **Supuesto HU-14:** tareas con responsable, vencimiento y estados Pendiente, Completada o Cancelada; recordatorio dentro de la app al vencimiento, bandeja persistente y marca de leído. Frecuencia técnica propuesta de revisión de cinco minutos, sin SLA contratado; sin correo, WhatsApp, SMS, push ni calendarios externos. Reprogramación invalida el recordatorio anterior y permite uno por nueva versión del vencimiento.',
        '- **Supuesto HU-15:** clientes distintos por etapa actual y captados = inmuebles distintos presentados a evaluación en el período, no comprados. Clientes se filtran por fecha de alta; captados por fecha de primera presentación. No hay histórico de embudo, conversiones o rendimiento individual. Esta definición de captado requiere confirmación del gerente; adquiridos sigue siendo otra métrica.',
        '- **Pendientes antes de implementar:** visibilidad y permisos definitivos, responsable inicial, campos obligatorios, edición/corrección de notas, zona horaria de negocio (propuesta America/Bogota), tolerancia de recordatorios, período/filtros de indicadores, volumen, retención y significado de etapas. Se cotiza historial append-only y correcciones mediante nueva entrada; sin borrado de notas.',
        '- **Tecnologías:** FastAPI, SQLAlchemy, Pydantic, RDS PostgreSQL propuesto y Next.js adaptable a celular. No se necesitan adjuntos propios del CRM: documentos/imágenes siguen en S3 bajo el módulo 2. No se cotiza app nativa, grabación de llamadas, BI externo ni integración con CRM de terceros.', '',
        '## Tabla de estimación por tarea', '',
        '| ID | h | d | Modo | Referencia × unidades; riesgo | Motivo / verificación |', '|---|---:|---:|---|---|---|'])
    for t in data['tasks']:
        rows.append(f"| {t['id']} | {span(t['hours_min'],t['hours_max'])} | {span(t['hours_min']/8,t['hours_max']/8)} | {t['mode']} | {t['ref']} × {span(t['base_units_min'],t['base_units_max'])}; ×{span(t['risk_min'],t['risk_max'])} | {t['reason']} |")
    for n, (layer, label) in enumerate(data['layers'].items()):
        rows.extend(['', f'## {n} {label} — {span(*totals[layer])} h', ''])
        for t in data['tasks']:
            if t['layer'] != layer:
                continue
            rows.extend([f"### {t['id']} {t['title']} — {span(t['hours_min'],t['hours_max'])} h", '', f"**Fuente:** {', '.join(t['stories'])}. **Estimación:** {t['mode']} · {t['ref']} × {span(t['base_units_min'],t['base_units_max'])}; luego ×{span(t['risk_min'],t['risk_max'])}. {t['reason']}", ''])
            rows.extend('- '+a for a in t['activities'])
            rows.extend(['', '**Tecnologías:** '+t['technologies']+'.', ''])
    rows.extend(['## 6 Base compartida y dependencias', '',
        'Se presupone autenticación funcional, roles internos, API/web, RDS, despliegue y herramientas de pruebas. La documentación no demuestra que existan. Si están pendientes, aplicar una sola vez las partidas [BASE-01 a BASE-05 del módulo 2](ficha-inmueble-epica.md#6-base-compartida-si-aún-no-está-implementada): **78–176 h**; el JSON conserva los importes. BASE-03 adapta un login existente: construirlo desde cero requiere estimación separada, sin acumular ambas variantes. No cobrar esta base de nuevo si ya se contrató en otro módulo.', '',
        'Los modelos/contratos de clientes e inmuebles de los módulos 1 y 2 deben estar disponibles. BE-CRM-02 incluye consumirlos y adaptar el vínculo, no construir onboarding o adquisición. Si faltan, sumar las épicas correspondientes sin duplicar la base. Orden sugerido: definición → modelo/permisos → ficha e historial → tareas/recordatorios → tablero → validación y entrega. FE puede avanzar con el contrato API acordado; eso no transforma horas-persona en plazo por simple división.', '',
        '## 7 Complejidad', '', '| Grupo | S/M/L | Motivo |', '|---|---|---|',
        '| Definición de etapas e indicadores | M | Semántica de cliente frente a inmueble y permisos |',
        '| Modelo, ficha y contactos | M | Relaciones, datos personales y trazabilidad |',
        '| Compromisos y recordatorios | L | Vencimientos, concurrencia, reintentos y cancelación |',
        '| Tablero | M | Conteos distintos y filtros consistentes |',
        '| Infraestructura y validación | M | Ejecución programada, alarmas y recorridos entre capas |', '',
        'Complejidad relativa, independiente de las horas y sin equivalencia automática S/M/L → días.', '',
        '## 8 Contingencias, consumo y entrega', '',
        f"- **Contingencia no incluida en el total base:** 0–4 h, únicamente si el contrato entregado por módulos 1/2 requiere una corrección acotada de identificadores o paginación para integrar CRM. Dueño: responsable de integración. Totales con esa condición: **{span(total[0],total[1]+4)} h** sobre base funcional o **{span(total[0]+base[0],total[1]+base[1]+4)} h** con toda la base pendiente. No usarla para cubrir módulos ausentes, nuevas reglas, canales externos o el riesgo ya incluido en M1.",
        '- **Consumo AWS separado y sin precio inventado:** incremento en cómputo del API/worker, consultas/almacenamiento RDS, ejecución programada EventBridge Scheduler y logs/alarmas CloudWatch. No se cotiza un segundo RDS ni infraestructura completa por módulo. El costo monetario requiere región, volumen de clientes/tareas, retención y dimensionamiento; licencias y mensajes externos quedan fuera.',
        '- **Aceptación:** validar los supuestos y Gherkin propuestos, registrar decisiones en ADR, ejecutar pruebas sobre staging y conservar evidencias. Esperas de acceso y aprobación se registran aparte. Esta entrega es documentación de cotización, no implementación del CRM.', ''])
    (ROOT/'epicas y tiempos/crm-epica.md').write_text('\n'.join(rows), encoding='utf-8')
    print(json.dumps({'subtotals':totals,'module':total,'shared_base':base,'with_shared_base':[total[i]+base[i] for i in range(2)]},ensure_ascii=False))

if __name__ == '__main__':
    render()
