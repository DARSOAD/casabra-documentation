"""Regenera la épica de venta desde sus datos de estimación versionados."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def interval(a, b):
    return f'{a:g}–{b:g}'.replace('.', ',')


def render():
    data = json.loads(Path(__file__).with_name('modulo-9-estimacion.json').read_text(encoding='utf-8'))
    totals = {key: [0, 0] for key in data['layers']}
    for task in data['tasks']:
        for i, end in enumerate(('min', 'max')):
            hours = math.ceil(data['hours_per_day'] * data['references'][task['ref']]['days'] * task[f'base_units_{end}'] * task[f'risk_{end}'])
            assert hours == task[f'hours_{end}'], task['id']
            totals[task['layer']][i] += hours
    total = [sum(v[i] for v in totals.values()) for i in range(2)]
    base = [sum(v[i] for v in data['shared_base_if_pending'].values()) for i in range(2)]
    full = [total[i] + base[i] for i in range(2)]
    rows = ['# Épica del módulo 9. Venta de inmuebles adquiridos', '',
        'Cotización inicial de **HU-40 a HU-45 y HU-48 a HU-50** de las [historias del proyecto](../historias_de_usuario_plan_del_proyecto.md), según el [contexto del negocio](../contexto.md). Son nueve historias: asignación y ficha comercial, publicación, CRM/visitas, negociación, expediente jurídico, cierre y resultados. Se conserva la estructura por capas de la [épica del login](login-epica.md).', '',
        '**Referencia funcional:** [criterios Gherkin propuestos](venta-inmuebles-criterios-aceptacion.md). No se encontraron criterios aprobados específicos de ventas; supuestos y escenarios deben validarse antes de implementar. Permanecen las reglas de los [criterios aprobados de adquisición](adquisicion-inmuebles-criterios-aceptacion.md).', '',
        '## Resumen de horas', '', '| Capa | Rango |', '|---|---:|']
    rows += [f'| {label} | {interval(*totals[layer])} h |' for layer, label in data['layers'].items()]
    rows += [f'| **Módulo con base y dependencias funcionales** | **{interval(*total)} h** |',
        f'| Base técnica compartida, solo si está pendiente | {interval(*base)} h |',
        f'| **Módulo más toda la base técnica pendiente** | **{interval(*full)} h** |', '',
        '**Ambos escenarios excluyen construir las dependencias funcionales.** Se presupone disponibilidad del inmueble/elegibilidad y archivos privados, componentes de actividades/tareas/avisos del CRM y motor contractual del módulo 7. La base técnica de 78–176 h no entrega esos módulos. Ver sección 6 para consolidar sin duplicidades.', '',
        'Horas-persona; **1 d = 8 h** como convención, no plazo de calendario. TDD, pruebas propias y revisión están incluidos en tareas funcionales. QA cubre recorridos, permisos y recuperación entre componentes. Consumo AWS, servicios externos y esperas se separan. No se identificó una estimación anterior del módulo 9.', '',
        '## Método y evidencia', '',
        'Se aplica [estimate-task local](../skills/estimate-task/SKILL.md) y sus [referencias](../skills/estimate-task/references/calibration.md). [Cálculo reproducible](../docs/estimaciones/modulo-9-estimacion.json), [generador](../docs/estimaciones/generar_modulo_9.py): `python docs/estimaciones/generar_modulo_9.py`.', '',
        '**Confianza baja:** sin horas reales Casabra ni implementación comprobada de servicios compartidos; canales, aprobación y cierre pendientes. A1 (S9.2 / RED-3596, 0,5 d) es referencia importada no verificada de conexión UI a endpoint con errores y pruebas; se usa como analogía parcial de varias vistas con dinero/PII. H (1 d) es unidad de hipótesis técnica por entregables, no ancla medida. Estimaciones de módulos anteriores no son tiempos reales.', '',
        '**Fórmula por extremo:** `ceil(8 × días_referencia × unidades_base × factor_riesgo)`. ×ref se expresa antes del factor. M0 usa ×1 en definición; M1 usa ×1,5–2 una sola vez por dinero, permisos, datos personales, migraciones, cierre sensible o ausencia de patrón probado. No multiplicar otra vez el total ni sumar TDD/revisión duplicados. No se aplica descuento fijo por IA. Recalibrar con esfuerzo real del primer recorrido; rangos sin significado de percentil estadístico.', '',
        '## Alcance confirmado por historias', '', '| Historia | Resultado incluido |', '|---|---|',
        '| HU-40 | Asignación a venta de activo adquirido y precio objetivo |',
        '| HU-41 | Ficha comercial, fotos, precio, documentos y alistamiento |',
        '| HU-42 | Publicación y actualización en canales definidos |',
        '| HU-43 | Prospectos, origen, intereses, interacciones, tareas y seguimientos |',
        '| HU-44 | Visitas con comentarios y nivel de interés |',
        '| HU-45 | Ofertas, contraofertas, comparación y aprobaciones de precio |',
        '| HU-48 | Preparación/revisión documental y condiciones de cierre |',
        '| HU-49 | Registro de firma, pago, entrega, cierre e inventario |',
        '| HU-50 | Embudo, tiempos de cierre, ofertas y ventas realizadas |', '',
        '**Confirmado por contexto:** se venden activos de la compañía ya adquiridos y asignados a Venta. El comprador no es el propietario original de adquisición. Precio aprobado, oferta aceptada, contrato firmado, pago recibido, entrega y cierre son hechos distintos. El cierre comercial no vuelve a ejecutar adquisición ni convierte el registro técnico en un trámite jurídico externo.', '',
        '### Supuestos para cotizar', '',
        '- Una compañía, un inmueble completo por venta, un comprador principal y moneda COP propuesta. Se aceptan múltiples prospectos/ofertas simultáneos, pero una sola reserva y un solo cierre vigente por inmueble. No se cotizan participaciones, copropietarios compradores, multiunidad o multimoneda.',
        '- El gerente de activos usa la autorización de ruta del módulo 2 y registra precio objetivo. La ficha contempla alistamiento antes de disponibilidad; obras se vinculan al módulo 6 si existen. No se incluye reclasificación de ruta ni venta de activos ocupados con contratos de arriendo vigentes; el sistema bloquea operaciones incompatibles con el inventario compartido.',
        '- HU-42 se estima con un catálogo web propio sencillo (listado paginado y ficha), diseño existente, precio/fotos/descripción y contacto de la compañía. Registro y gestión manual de enlaces/estados para portales externos; no hay conectores automáticos ni publicación externa desde la app. Los canales definitivos pueden cambiar esta partida.',
        '- La ficha pública solo contiene campos permitidos y fotografías expresamente seleccionadas. Precio objetivo interno, negociaciones, compradores, documentos legales y soportes no son públicos. La ficha interna sí referencia documentos autorizados. Sin formulario público de captación, buscador avanzado, mapas, campañas ni nuevo diseño de marca.',
        '- Prospectos creados por equipo de ventas, con origen, intereses y asesor; pueden interesarse por varios inmuebles. Cada relación prospecto-inmueble es una oportunidad distinta. No se exige cuenta de comprador para ser prospecto ni se reutilizan automáticamente datos privados del propietario de adquisición.',
        '- Interacciones, tareas y recordatorios in-app adaptan componentes del módulo 5; la ficha de prospectos/embudo de venta sí es nueva. Visitas con fecha, responsable, resultado e interés bajo/medio/alto como catálogo inicial. Sin correo/SMS/WhatsApp, calendarios externos o scoring de prospectos.',
        '- Cada oferta/contraoferta tiene versión, importe, moneda, condiciones y autor/origen. Precio objetivo no autoriza automáticamente descuentos. Un nivel de aprobación explícita del gerente comercial sobre la versión concreta; límites/delegaciones se confirman en definición. No hay motor multinivel de aprobaciones.',
        '- Aceptación del comprador se registra por asesor con fecha y evidencia. Reserva requiere aceptación y aprobación interna sobre la misma versión. Cambiar precio/condiciones invalida decisiones previas; no modifica contratos firmados. Liberación antes de cierre requiere motivo y ausencia de compromisos contractuales/pagos pendientes de resolución; devoluciones o rescisión con dinero recibido quedan fuera de este alcance inicial.',
        '- Abogado revisa expediente/checklist configurable y preparado por la empresa, con evidencia y validación humana. Se usa una plantilla Venta, un PDF y dos firmantes del módulo 7. Documentos externos de formalización se adjuntan como evidencia; no se automatizan notaría, registro, estudio de títulos, redacción jurídica o validación legal.',
        '- Pagos/abonos por medios externos se registran con referencia y soporte, pendientes hasta validación expresa de administrador. Se mantiene historial y compensaciones antes de cierre. No hay pasarela ni recaudo digital de venta, gestión de crédito o conciliación bancaria automática. La exactitud de la recepción se valida operativamente fuera del sistema.',
        '- Para el cierre inicial se requiere precio final íntegramente cubierto por pagos confirmados, sin excedentes no resueltos; firma/archivo contractual, aprobación jurídica vigente y entrega registradas. Cierre actualiza inventario comercial, oportunidad ganadora y otras oportunidades sin borrar historial. Incidentes posteriores al cierre se registran, sin reapertura o anulación automática de venta.',
        '- Roles: gerente de activos, asesor de ventas, gerente comercial, abogado y administrador. La distinción de los cargos de ventas y sus facultades en HU-33 es pendiente de acuerdo; no se considera ya implementada. El comprador firma mediante módulo 7, sin portal propio ni acceso a comparaciones de otras ofertas.',
        '- FastAPI, Next.js adaptable a celular, AWS, RDS PostgreSQL propuesto y S3. Archivos privados PDF/JPEG/PNG bajo servicio compartido con validación/análisis; límites y retención por acordar. Uso conectado, sin app nativa u offline.', '',
        '### Estados propuestos, cierre y medición', '',
        '| Dimensión | Regla propuesta |', '|---|---|',
        '| Disponibilidad comercial | En alistamiento → Disponible → Reservado → Vendido; independiente del historial Adquirido y de anuncios |',
        '| Oportunidad | Nueva, Contactada, Visita, Negociación, En cierre, Ganada o Perdida; visitas no obligatorias para todas las oportunidades; pérdida requiere motivo |',
        '| Publicación | Borrador, Publicada o Retirada en web propia; estado externo manual, con retiro pendiente cuando corresponde |',
        '| Oferta | Historial versionado; decisión interna y decisión de comprador separadas; solo revisión vigente aprobada/aceptada habilita reserva |',
        '| Pago externo | Registrado pendiente de validación, Confirmado o Anulado con corrección trazable; no equivale a pago procesado por la plataforma |',
        '| Cierre | Pendiente de requisitos o Cerrado; un commit único registra cierre/inventario y evento de retiro |',
        '| Embudo | Cohorte de oportunidades creadas en período, agrupadas por su etapa actual al corte; no representa toda la historia de conversiones |',
        '| Ofertas | Conteo de ofertas creadas en período y versiones vigentes; mostrar diferencias frente a número de oportunidades |',
        '| Ventas realizadas | Conteo y valor final aprobado de cierres por fecha de cierre; no igualar a cobros ni rentabilidad |',
        '| Tiempo de cierre | Días desde alta de oportunidad ganadora hasta cierre; promedio solo de cierres incluidos; sin cierres se muestra No aplica |', '',
        'Cerrar requiere versión comercial/contractual consistente, reserva vigente, revisión jurídica y evidencias de firma, pago y entrega. La adquisición histórica se conserva; Vendido describe disponibilidad/operación posterior. El cierre y la reserva compiten bajo restricciones transaccionales para impedir doble venta. La web propia deja de presentar oferta disponible al consultar estado actualizado; invalidación de caché y retiro se reintentan. Los anuncios externos conservan tarea de retiro manual; no se promete borrar copias de terceros.', '',
        '**Pendientes:** canales exactos, documentos publicables, alistamiento, fases del embudo, reglas de precio/descuento, validez de ofertas, autoridad para reservar/liberar, requisitos de cierre y forma de pago, entidades compradoras/múltiples firmantes, retención, volumen y umbrales de rendimiento. Esta cotización no fija reglas jurídicas ni convierte sus supuestos en decisiones aprobadas.', '',
        '**Exclusiones adicionales:** automatización de portales, financiación hipotecaria, recaudo/reembolsos, facturación DIAN, comisiones de corredores, contabilidad/rentabilidad consolidada, importación masiva CRM, BI externo y flujo posterior de reversión de una venta cerrada. Los módulos consumidores usarán IDs estables de venta/pagos; no volverán a registrar dinero ya contabilizado operativamente.', '',
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
        '| Dependencia | Se reutiliza | Trabajo incremental aquí |', '|---|---|---|',
        '| Módulo 2 | Inmueble adquirido, autorización de ruta y servicio privado de archivos | Ficha comercial/objetivo y vínculos; permisos/copia publicable; control de disponibilidad |',
        '| Módulo 5 | BE-CRM-03/04/05 para actividades/tareas/avisos; FE-CRM-02/03 y ejecución compartida | BE-VE-04/05 y FE-VE-03 adaptan recurso oportunidad, prospectos y visitas; embudo de venta nuevo |',
        '| Módulo 6, si hay adecuaciones | Estado/evidencias de obra | Referencia de alistamiento, sin gestionar obra |',
        '| Módulo 7 | Plantilla Venta, revisión de PDF, firma y archivo | BE-VE-08 y FE-VE-05 preparan expediente/términos, consumen contrato de entrada y validan requisitos de cierre |',
        '| Inventario/arriendo | Disponibilidad y contratos activos si ya existe módulo 8 | Verificar incompatibilidad; no mover automáticamente un activo de Arriendo a Venta |',
        '| Módulo 10, consumidor futuro | Contabilidad y rentabilidad | Referencias de cierre/pago para consumo sin duplicar; sin integración contable completa |', '',
        'No se verificó código entregado de esas dependencias. Si faltan, hay que estimar/implementar lo necesario antes de declarar completo el flujo de venta. La base técnica no sustituye CRM, archivos, adquisición ni contratos. Mocks sirven para desarrollo, no prueban integración operativa.', '',
        'El [módulo 5](crm-epica.md) está estimado en **191–420 h**, pero incluye funciones de adquisición no requeridas por venta: no sumar toda esa épica por defecto. Revisar qué motor genérico se necesita y asignar su creación una sola vez; el escenario aquí presupone esos componentes funcionales. BE-VE-04/05 incluyen adaptación real a compradores/oportunidades, no un descuento por una épica escrita.', '',
        'El [módulo 7](contratos-firma-epica.md) está estimado en **267–564 h** y se contrata una sola vez si falta. Su BE-CT-08 define mapeos genéricos; BE-VE-08 agrega expediente y chequeos propios de venta y consume ese contrato, sin rehacer plantilla/motor de firma. Si módulo 8 ya entrega componentes de ficha/pagos manuales, evaluar compatibilidad antes de descontar trabajo; no se presume su disponibilidad ni se depende de su pasarela.', '',
        'La base técnica pendiente se toma de [BASE-01 a BASE-05 del módulo 2](ficha-inmueble-epica.md#6-base-compartida-si-aún-no-está-implementada): **78–176 h**. Se paga una sola vez para el producto: ambientes, pipeline, adaptación del login existente, pruebas y logs. BASE-03 no construye autenticación desde cero; esa variante se reestima aparte. BE-VE-02/08/09 adaptan archivos privados, sin volver a crear escaneo/cuarentena; si ese servicio falta, presupuestar su implementación específica.', '',
        'Secuencia: definir canales/reglas → modelo/permisos → ficha/publicación y CRM → ofertas/aprobaciones/reserva → expediente/firma → pagos/entrega/cierre → indicadores/validación/activación. Frontend puede avanzar con contratos API acordados. Capacidad del equipo y dependencias definen el calendario; días-persona no equivalen a fechas.', '',
        '## 7 Complejidad', '', '| Grupo | S/M/L | Motivo |', '|---|---|---|',
        '| Ficha y publicación | M | Versiones de contenido y separación pública/privada |',
        '| CRM y visitas | M | Varios intereses por prospecto y adaptación de agenda |',
        '| Ofertas y reserva | L | Dinero, versiones aprobadas y exclusión de concurrencia |',
        '| Expediente y cierre | L | Requisitos, firma, pagos, entrega e inventario atómico |',
        '| Indicadores | M | Cohortes, períodos y conteos sin duplicar versiones |',
        '| Operación y pruebas | M | Retiro recuperable, permisos y validación entre módulos |', '',
        'S/M/L indica complejidad relativa y no se convierte automáticamente a horas.', '',
        '## 8 Contingencias, consumo y aceptación', '',
        f"- **Reserva condicionada:** 0–4 h, una sola vez fuera del total base, ante corrección acotada de ID/campo de un contrato compartido de CRM, adquisición o firma ya entregado. Dueño: responsable de integración. Totales con esa condición: **{interval(total[0],total[1]+4)} h** con dependencias funcionales o **{interval(full[0],full[1]+4)} h** agregando toda la base técnica. No cubre nuevos canales, firma/CRM faltante, reglas de crédito ni reapertura de ventas cerradas; esos cambios se reestiman. No sumar una reserva porcentual por el riesgo ya incluido en M1.",
        '- **Consumo AWS separado:** API/web/worker, RDS, S3/versiones/transferencia, CDN si se usa, KMS y CloudWatch. Dimensionar con región, tráfico público, cantidad/tamaño de fotos, oportunidades, documentos y retención. El catálogo no justifica crear otra infraestructura completa por módulo.',
        '- **Servicios externos:** transacciones/licencias de firma del módulo 7, cuentas/publicidad en portales y cualquier servicio contratado. Sin canales/volumen no se inventan tarifas. No hay comisiones de pasarela de venta previstas porque no se integra recaudo digital en este alcance.',
        '- **Esperas separadas:** aprobación de contenidos/precios/checklist, datos de comprador, firmas, confirmación operativa de pago y trámites externos. No son horas de desarrollo ni garantizan fecha de cierre.',
        '- **Aceptación:** validar supuestos/Gherkin, conservar ADR y evidencia de integración real frente a simulaciones, registrar horas reales para recalibrar. Esta entrega es documentación de cotización; no publica inmuebles ni ejecuta transacciones reales.', '']
    (ROOT/'epicas y tiempos/venta-inmuebles-epica.md').write_text('\n'.join(rows), encoding='utf-8')
    print(json.dumps({'subtotals': totals, 'module':total, 'shared_base':base, 'with_shared_base':full}, ensure_ascii=False))


if __name__ == '__main__':
    render()
