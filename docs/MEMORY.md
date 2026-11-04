# Memoria del proyecto Casabra

Esta memoria y la skill de estimación se conservan en el repositorio por solicitud del usuario. Las instrucciones de entrada están en [AGENTS.md](../AGENTS.md); la copia de referencia para Casabra está en [skills/estimate-task/SKILL.md](../skills/estimate-task/SKILL.md), con sus [referencias de calibración](../skills/estimate-task/references/calibration.md). Leer estos archivos locales al estimar; no depender de la instalación global de un equipo. Actualizar memoria, skill y documentación relacionada en Git cuando se acuerden cambios.

## Convención de épicas solicitada por el usuario

El usuario pidió completar el módulo 2 con el mismo formato de la épica del login y conservar esa forma de trabajo para las próximas épicas.

Referencias: [login](../epicas%20y%20tiempos/login-epica.md) para la estructura y [adquisición de inmuebles](../epicas%20y%20tiempos/ficha-inmueble-epica.md) para su aplicación actual. El Word del login contiene ejemplos de otro negocio y subtotales incorrectos; no trasladar esos errores a nuevas épicas.

### Estructura que se debe repetir

1. Título del módulo, alcance y enlace a historias/criterios.
2. Resumen de horas por capa y total calculado desde las tareas.
3. Backend y frontend como secciones principales. Añadir definición, infraestructura, observabilidad, pruebas transversales y entrega cuando correspondan.
4. Cada tarea con encabezado `ID Título — mínimo–máximo h`, actividades concretas, tecnologías y endpoints cuando aporten claridad. Añadir modo, referencia/hipótesis, multiplicador y motivo de la estimación. Usar prefijos BE/FE/OPS/QA/REL y un código estable del módulo.
5. Tabla de complejidad S/M/L con motivo, independiente de las horas.
6. Supuestos, dependencias y pendientes de cotización. Infraestructura compartida y reserva visibles por separado; consumo AWS fuera de las horas de desarrollo.

Los criterios de aceptación se redactan en Gherkin, en español, con los escenarios mínimos que verifican los requisitos. Pueden estar en un archivo separado enlazado desde la épica. Los escenarios describen comportamiento; no sustituyen el desglose de implementación ni se convierten mecánicamente en horas.

### Método de estimación solicitado después

El usuario pidió aplicar la skill de Claude `dstack-claude:estimate-reddo-task` y crear su adaptación para Codex con nombre `estimate-task`. Conservar el formato del login y usar este método para los tiempos:

- Si ya hay tareas claras, conservar los IDs y estimarlas; no redescomponer ni escribir en una página externa por defecto.
- Estimar verificación/correctitud, no solo volumen de código. Usar modos M0/M1/M2/M3 según la skill y explicar por qué corresponden.
- Documentar referencias comparables y su nivel de evidencia. Las anclas Reddo importadas no se verificaron contra tickets/tiempos; no son mediciones de Casabra.
- Dinero, permisos, datos personales, migraciones y ausencia de patrón probado requieren M1. Su factor de revisión se incorpora una vez, nunca sobre horas que ya incluyan ese costo.
- Mostrar rangos por tarea y totales, base compartida y contingencias con condiciones específicas. Evitar acumular multiplicador, QA duplicado y reserva porcentual por el mismo riesgo.
- Declarar horas por día; 8 h/d es una convención de cálculo, no plazo de calendario ni productividad histórica comprobada.
- Las cifras revisadas del módulo 2 están en [su cálculo reproducible](estimaciones/modulo-2-estimacion.json) y en la épica. Las cifras anteriores se conservan como antecedente, no como ancla medida.

### Preferencias técnicas

- Requisito del usuario: API en FastAPI, infraestructura AWS, archivos/imágenes en S3 y base relacional en RDS.
- PostgreSQL es la propuesta usada para estimar; MySQL fue una alternativa inicial. No afirmar que se deben soportar ambos ni que la elección ya fue implementada.
- Next.js es la referencia de frontend proveniente del login; la cotización presupone web adaptable a celular.
- TDD forma parte de las tareas funcionales. Mantener herramientas y tipos de pruebas explícitos; evitar cobrar otra vez las mismas unitarias/integración dentro de QA.
- Conservar decisiones técnicas mediante ADR en Git; auditoría de negocio en RDS; logs/errores y alarmas en CloudWatch. No mezclar sus propósitos.
- Cotización inicial: registrar como pendientes los datos aún desconocidos y proponer configuración o supuestos acotados. No exigir una especificación exhaustiva para avanzar ni presentar supuestos como aprobaciones.
- No considerar entregado el login o AWS por aparecer en documentación. Verificar implementación antes de descontar trabajo compartido.

## Decisiones funcionales confirmadas para el módulo 2

Nombre actual: **Adquisición de inmuebles**. Numeración vigente: HU-04 documentos, HU-05 ficha, HU-06 estudio jurídico, HU-07 ruta y adecuaciones, HU-08 seguimiento. Usar [criterios aprobados](../epicas%20y%20tiempos/adquisicion-inmuebles-criterios-aceptacion.md) y [contexto del negocio](../contexto.md).

Estados: **Documentación faltante**, **En estudio**, **Propuesta enviada**, **En proceso de compra**, **Adquirido** y **Rechazado**.

| Origen | Acción | Responsable | Destino |
|---|---|---|---|
| Documentación faltante | Completar requisitos configurados | Propietario | En estudio |
| En estudio | Enviar propuesta económica | Asesor | Propuesta enviada |
| En estudio | Rechazar inmueble | Asesor | Rechazado |
| Propuesta enviada | Aceptar oferta | Propietario | En proceso de compra |
| Propuesta enviada | Rechazar oferta | Propietario | Rechazado |
| En proceso de compra | Confirmar compra completada | Abogado o persona con permiso explícito | Adquirido |

La empresa compra los inmuebles. Solo después de adquirirlos el gerente asigna Arriendo o Venta y define si requieren adecuaciones. Aceptar una oferta no equivale a adquirir el inmueble. Los cambios de estado conservan estado anterior/nuevo, fecha y responsable.

La lista exacta de requisitos documentales y datos obligatorios no está definida: estamos preparando la cotización inicial. No inventar una lista cerrada ni plazos legales. Los cargos adicionales con permiso de confirmar adquisición siguen por definir.

## Supuestos técnicos pendientes

Las propuestas de tecnología detallada, límites, retención, una sola oferta por solicitud, alcance de reemplazos documentales y horas estimadas están en la épica/ADR. No convertirlos en reglas de negocio confirmadas por el usuario. Reaperturas, contraofertas, renegociaciones y cambios de ruta posteriores requieren nuevo alcance.

Al cambiar una regla, actualizar la épica, sus criterios y la memoria que corresponda. Mantener los ADR con estado real y conservar su historial.
