"""Regenera la épica del portal desde el cálculo versionado."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def interval(a, b):
    return f'{a:g}–{b:g}'.replace('.', ',')


def render():
    data = json.loads(Path(__file__).with_name('modulo-11-estimacion.json').read_text(encoding='utf-8'))
    totals = {key: [0, 0] for key in data['layers']}
    for task in data['tasks']:
        for i, end in enumerate(('min', 'max')):
            hours = math.ceil(data['hours_per_day'] * data['references'][task['ref']]['days'] * task[f'base_units_{end}'] * task[f'risk_{end}'])
            assert hours == task[f'hours_{end}'], task['id']
            totals[task['layer']][i] += hours
    total = [sum(v[i] for v in totals.values()) for i in range(2)]
    base = [sum(v[i] for v in data['shared_base_if_pending'].values()) for i in range(2)]
    full = [total[i] + base[i] for i in range(2)]
    rows = ['# Épica del módulo 11. Portal del cliente', '',
        'Cotización inicial de **HU-30 a HU-32** de las [historias del proyecto](../historias_de_usuario_plan_del_proyecto.md), según el [contexto del negocio](../contexto.md), con el formato por capas de la [épica del login](login-epica.md). Incluye portal del propietario original, publicación controlada/notificaciones y reportes gerenciales; mantiene separados sus permisos.', '',
        '**Referencia funcional:** [criterios Gherkin propuestos](portal-cliente-criterios-aceptacion.md). No se encontraron criterios aprobados específicos ni una estimación anterior de este módulo; escenarios y límites son propuestas de cotización pendientes de validar. El seguimiento de adquisición conserva los [criterios aprobados del módulo 2](adquisicion-inmuebles-criterios-aceptacion.md).', '',
        '## Resumen de horas', '', '| Capa | Rango |', '|---|---:|']
    rows += [f'| {label} | {interval(*totals[layer])} h |' for layer, label in data['layers'].items()]
    rows += [f'| **Módulo con base y fuentes funcionales** | **{interval(*total)} h** |',
        f'| Base técnica compartida, solo si está pendiente | {interval(*base)} h |',
        f'| **Módulo más toda la base técnica pendiente** | **{interval(*full)} h** |', '',
        '**Ambos escenarios excluyen construir los módulos fuente.** Se requieren identidad, vínculos/documentos de adquisición, datos de obra/contratos, ocupación y resultados financieros. La base técnica no entrega contabilidad ni rentabilidad. El [módulo 10 ya tiene estimación](pagos-utilidades-epica.md); HU-32 sigue condicionada a su contrato de datos y disponibilidad real, no a la mera existencia de esa documentación.', '',
        'Horas-persona; **1 d = 8 h** como convención, no calendario. TDD, pruebas propias y revisión forman parte de cada tarea funcional. QA cubre recorridos, conciliación y recuperación entre componentes, sin repetir unitarias. Consumo AWS, servicios y esperas se separan.', '',
        '## Método y evidencia', '',
        'Se aplica [estimate-task local](../skills/estimate-task/SKILL.md) y sus [referencias](../skills/estimate-task/references/calibration.md). [Cálculo reproducible](../docs/estimaciones/modulo-11-estimacion.json) y [generador](../docs/estimaciones/generar_modulo_11.py): `python docs/estimaciones/generar_modulo_11.py`.', '',
        '**Confianza baja:** no hay horas reales Casabra ni interfaces fuente implementadas comprobadas. A1 (S9.2 / RED-3596, 0,5 d) es referencia importada no verificada de conexión UI a endpoint con errores/pruebas; analogía parcial para las varias vistas con permisos de este módulo. H (1 d) es unidad de hipótesis técnica por entregables, no medición. No se usan estimaciones anteriores como productividad observada.', '',
        '**Fórmula por extremo:** `ceil(8 × días_referencia × unidades_base × factor_riesgo)`. ×ref se expresa antes del riesgo. M0 usa ×1 para definición; M1 usa ×1,5–2 una sola vez por PII, permisos, importes, migraciones o ausencia de patrón probado. No volver a aplicar el factor al total ni duplicar TDD/revisión; no se presume descuento fijo por IA. Recalibrar con horas reales del primer recorrido; rangos sin significado de percentil estadístico.', '',
        '## Alcance confirmado y separación de audiencias', '',
        '| Historia | Actor | Resultado incluido |', '|---|---|---|',
        '| HU-30 | Propietario original | Avance de obra, documentos propios accesibles y resultados que la compañía autorice compartir |',
        '| HU-31 | Propietario original | Avisos de hitos de su operación autorizados para compartir |',
        '| HU-32 | Gerente | Reportes consolidados de ingresos, ocupación y rentabilidad |', '',
        '**Confirmado por contexto:** el inmueble adquirido pertenece a la compañía. Ser propietario original no habilita acceso a su gestión interna posterior, candidatos, arrendatarios, compradores o resultados gerenciales. El portal de pagos/contrato/cartera del arrendatario corresponde a HU-51 a HU-54 del módulo 8 y no se reconstruye aquí. HU-32 se conserva en este módulo porque así aparece en las historias, con acceso exclusivo de gerente.', '',
        '### Supuestos de cotización', '',
        '- Una compañía, propietario principal vinculado a su cuenta/operaciones existentes y gerente interno. Una persona puede consultar varias operaciones propias; sin copropietarios delegados, representación de terceros o nuevo onboarding. Autenticación/recuperación de cuenta y asignación general de roles son compartidas.',
        '- Publicación explícita por operador interno autorizado, propuesto administrador: elige operación, destinatario, resumen y referencias/versiones de fotos/documentos/resultados. Denegación por defecto y una aprobación por versión; no aprobación multinivel ni reglas automáticas extensibles.',
        '- Datos propios ya accesibles en módulo 2 conservan su autorización fuente; información de obra y resultados posteriores exige selección/aprobación expresa. La aprobación no otorga al propietario acceso al expediente completo ni a las fuentes internas.',
        '- Resúmenes y selección de fotos/documentos con snapshot de versión aprobada. No se publican cambios posteriores del origen automáticamente. Fuente retirada/inaccesible o permiso revocado bloquean nuevas consultas; correcciones requieren revisión. Retención/historial por acordar, sin borrar auditoría de lo compartido.',
        '- Descarga a través de endpoint autenticado con comprobación actual de acceso y respuestas privadas sin caché pública. No se entrega enlace persistente S3 al propietario. Revocar bloquea nuevas solicitudes; no recupera contenido ya descargado, ni bytes ya entregados en una descarga en curso.',
        '- Portal web adaptable a celular, consulta de avances/fecha, galería de fotos aprobadas, documentos y resultados compartidos. Sin edición del expediente desde el portal, carga nueva, chat, tickets, firma nueva, pagos, extractos bancarios ni app nativa/offline.',
        '- Hitos inicialmente limitados a formalización y pago de adquisición, más publicación/corrección de contenido compartido cuando se acuerde. Deben proceder de una fuente autoritativa confirmada y corresponder a esa operación; no usar un canon de arriendo, cierre de venta o pago pendiente como sustituto del pago al propietario original.',
        '- Avisos in-app y correo transaccional con información mínima y enlace al portal, deduplicación interna, leído, reintentos y rebotes. Se revalida permiso/estado antes de enviar. No se promete recepción exactamente una vez en correo ni retirar mensajes ya entregados. Sin WhatsApp, SMS o push.',
        '- Reporte gerencial en pantalla con período, ruta e inmueble, tablas/gráficos y detalle paginado. Una moneda/base temporal homogénea acordada; sin conversión cambiaria, exportación PDF/Excel, BI externo, diseñador de reportes o previsiones.',
        '- Ingresos/costos/rentabilidad provienen del módulo 10; ocupación del módulo 8. Los pagos de módulos 8/9 se consultan como evidencia si hace falta, pero no se suman de nuevo a los ingresos consolidados. Resultados para propietario, si se autorizan, son publicaciones específicas; no se comparte automáticamente este tablero.',
        '- Ratios consolidados se obtienen del agregado autoritativo o componentes compatibles definidos por los módulos fuente; no se promedian porcentajes por inmueble sin ponderación. Denominador cero = No aplica; fuente ausente = No disponible; un total parcial se etiqueta y lista exclusiones, no se presenta como total completo.',
        '- Se presupone web/API/worker existente: Next.js, FastAPI, AWS, S3 y RDS PostgreSQL propuesto. No se seleccionan versiones de librerías ni se construye almacenamiento/escaneo documental desde cero.', '',
        '### Estados, datos y controles propuestos', '',
        '| Elemento | Regla |', '|---|---|',
        '| Contenido | Borrador → Publicado → Retirado; nueva versión requiere aprobación propia |',
        '| Aviso | Pendiente, Enviado o Fallido por canal; lectura in-app independiente de envío de correo |',
        '| Hito de pago | Solo fuente confirmada de pago de adquisición; evento pendiente/fallido no prueba recepción |',
        '| Avance | Versión/fecha explícitas; no reconstruye obra ni inventa porcentaje si falta información |',
        '| Reporte | Completo, Parcial o No disponible según cobertura/fuentes al corte; no mezclar monedas ni períodos incompatibles |',
        '| Ingresos | Base y fecha acordadas con módulo 10, visibles; no equiparar valor vendido, canon causado y dinero cobrado |',
        '| Ocupación | Numerador/denominador y universo provenientes del módulo 8; declarar corte y exclusiones |',
        '| Rentabilidad | Definición y componentes provenientes de HU-28; consolidación compatible, sin nuevo motor financiero |', '',
        '**Pendientes:** operador aprobador, qué resultados se comparten, vínculos de destinatario, reglas de retiro/retención, documentos visibles, fuente efectiva de pago de adquisición, tiempos/frecuencia de avisos, volumen, cortes y bases de indicadores. La política de compartir no está aprobada: estos límites permiten estimar sin exponer por defecto información del activo ya adquirido.', '',
        '**Fuera de alcance adicional:** administración de arriendos/ventas/obras, KYC, contabilidad, facturación DIAN, cálculo nuevo de retorno/rentabilidad, TIR/VAN, automatización de decisiones de inversión, redacción automática de documentos, migración masiva y auditorías legales/financieras. Se consultan datos y evidencia de sistemas fuente; no se crean allí movimientos mediante este portal.', '',
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
        '| Fuente/dependencia | Se reutiliza | Incremento de este módulo |', '|---|---|---|',
        '| Login y módulo 2 | Cuenta, vínculo propietario-operación, seguimiento y documentos privados | Consulta consolidada y política de compartir posterior; no reimplementar HU-08 |',
        '| Módulo 6 | Reportes/fotos/avance de obra existentes | Selección y snapshot del contenido autorizado; no CRUD de obra |',
        '| Módulo 7 | Firma/archivo y estado de contrato de adquisición | Hito y acceso permitido a documento; no motor de firma |',
        '| Módulo 8 | Ocupación con definición/corte, y correo compartido si existe | Adaptador de reportes y plantilla de aviso del portal |',
        '| Módulos 9/10 | Resultados operativos y financieros por inmueble | Consultas consolidadas sin duplicar movimientos ni calcular otra rentabilidad |',
        '| Fuente de pago al propietario | Estado/evidencia de pago de adquisición | Filtrar y notificar un hito confirmado; no ejecutar ni conciliar ese pago |', '',
        '**Implementación del módulo 10 pendiente de verificar:** HU-27/HU-28 se detallan en la [épica financiera](pagos-utilidades-epica.md). BE-PU-06 cotiza la API fuente; AN-PC-01 y BE-PC-06 mantienen aquí el acuerdo/adaptación del consumidor, sin duplicar el motor financiero. HU-32 no se considera operativamente completa hasta contar con datos reales validados, agregados compatibles e historial.', '',
        'BE-PU-04 del módulo 10 contempla registrar y validar pagos de adquisición realizados fuera de la plataforma y emitir su referencia de confirmación/corrección. No se verificó implementación: el motor de firma no acredita dinero recibido ni basta un costo registrado. El portal conserva autorización de compartición y no sustituye esa fuente por pagos de arriendo o venta. Fixtures permiten avanzar, no acreditan integración real.', '',
        'Arriendo tiene [versión original](arriendo-inmuebles-epica.md) y [nuestra v2](arriendo-inmuebles-epica-v2.md). Son alternativas conservadas por solicitud del usuario, no costos acumulables. Elegir la implementación/contrato disponible para la fuente de ocupación no convierte ninguna estimación en aprobada ni suma ambas.', '',
        'Si falta la base técnica, sumar una sola vez [BASE-01 a BASE-05 del módulo 2](ficha-inmueble-epica.md#6-base-compartida-si-aún-no-está-implementada): **78–176 h**, detalladas en el JSON. Incluye ambientes, pipeline, adaptación del login existente, pruebas y observabilidad. BASE-03 no construye autenticación desde cero; esa variante se reestima. No cobrar otra base AWS, almacenamiento o motor de correo por cada módulo.', '',
        'La extensión de permisos/publicaciones y adaptadores se cotiza aquí; las fuentes funcionales se presupuestan aparte solo si faltan. Secuencia: política/datos → modelo/permisos → contenido/descarga → hitos/avisos → reportes → validación/activación. Frontend puede avanzar con contrato acordado; capacidad y disponibilidad de fuentes determinan calendario, no dividir esfuerzo entre personas sin más.', '',
        '## 7 Complejidad', '', '| Grupo | S/M/L | Motivo |', '|---|---|---|',
        '| Publicación y autorización | L | Destinatario, versión, retiro y límite de acceso al activo |',
        '| Portal y documentos | M | Varias fuentes privadas y lectura móvil |',
        '| Hitos y avisos | M | Confirmación fuente, deduplicación y permisos al enviar |',
        '| Consolidación gerencial | L | Bases homogéneas, ratios y datos faltantes |',
        '| Operación y validación | M | Recuperación, correo y aislamiento entre roles |', '',
        'S/M/L es complejidad relativa; no se traduce automáticamente a horas.', '',
        '## 8 Contingencias, consumo y aceptación', '',
        f"- **Reserva condicionada:** 0–4 h una sola vez, fuera del total base, para corregir un campo/ID de un contrato fuente ya entregado. Dueño: responsable de integración. Totales bajo esa condición: **{interval(total[0],total[1]+4)} h** con fuentes funcionales o **{interval(full[0],full[1]+4)} h** agregando toda la base técnica. No cubre crear módulo 10, nuevos canales, cálculo financiero adicional o nuevas reglas de compartición. No duplicar riesgo ya incluido con M1.",
        '- **Consumo AWS separado:** API/web/worker, RDS, S3/transferencia privada, SES, SQS, programación de eventos, KMS y CloudWatch. Requiere región, usuarios, consultas, tamaño de archivos, correos y retención para precio monetario; no se inventan importes.',
        '- **Esperas externas:** política de contenido/datos, definición financiera, entrega de fuentes, acceso a ambientes y habilitación de correo. No son horas de desarrollo ni garantía de calendario.',
        '- **Aceptación:** aprobar supuestos/Gherkin, conservar ADR y evidencia de pruebas reales frente a simuladas, y registrar horas reales para recalibrar. Esta entrega documenta la cotización; no publica datos ni envía notificaciones reales.', '']
    (ROOT/'epicas y tiempos/portal-cliente-epica.md').write_text('\n'.join(rows), encoding='utf-8')
    print(json.dumps({'subtotals': totals, 'module':total, 'shared_base':base, 'with_shared_base':full}, ensure_ascii=False))


if __name__ == '__main__':
    render()
