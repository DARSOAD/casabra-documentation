# Módulo 11. Portal del cliente — criterios propuestos

**Estado: pendientes de validación; no son criterios aprobados.** Fuente: HU-30, HU-31 y HU-32 de las [historias](../historias_de_usuario_plan_del_proyecto.md). Aplican los límites de la [épica](portal-cliente-epica.md). Se presupone autenticación y módulos fuente funcionales; no se convierte la documentación de esos módulos en evidencia de implementación.

## HU-30 — Información autorizada del propietario original

```gherkin
Característica: Consultar información compartida de mi operación
  Escenario: Consultar varias operaciones propias
    Dado un propietario original autenticado vinculado a dos operaciones
    Cuando abre el portal
    Entonces puede seleccionar esas dos operaciones
    Y no recibe información de operaciones de otras personas

  Escenario: Ver avance expresamente compartido
    Dado un reporte de obra interno con fotos, notas y costos
    Y un operador autorizado aprobó un resumen y dos fotografías para el propietario
    Cuando el propietario consulta el avance
    Entonces ve solo el resumen y las fotografías de la versión aprobada
    Y ve fecha de actualización sin notas o costos internos no autorizados

  Escenario: Cambiar origen sin publicar automáticamente
    Dado un resumen de obra ya publicado
    Cuando cambia el reporte interno de origen
    Entonces el cambio no sustituye automáticamente el contenido compartido
    Y requiere nueva revisión para publicarse al propietario

  Escenario: Consultar documentos propios autorizados
    Dado un documento del propietario cuyo acceso permite el módulo fuente
    Cuando solicita su descarga autenticada
    Entonces se comprueban vínculo, permiso y versión en la solicitud
    Y se entrega mediante respuesta privada sin URL pública persistente

  Escenario: Retirar contenido compartido
    Dado una publicación accesible para el propietario
    Cuando un operador autorizado la retira con motivo
    Entonces nuevas consultas y descargas se deniegan para ese contenido
    Y se conserva trazabilidad del retiro
    Y no se afirma recuperar copias ya descargadas por el usuario

  Escenario: Proteger el activo después de adquisición
    Dado un propietario original cuyo inmueble ya fue adquirido por la compañía
    Cuando intenta acceder a candidatos, cartera de arriendo o reportes internos
    Entonces se deniega el acceso por su rol de propietario original
    Y solo puede consultar contenidos específicos autorizados para compartir

  Escenario: Distinguir ausencia de datos
    Dado una operación sin avance compartido o con fuente no disponible
    Cuando se consulta el portal
    Entonces se explica la ausencia de información disponible
    Y no se inventa porcentaje de avance ni se muestra como cero confirmado
```

## HU-31 — Hitos y notificaciones

```gherkin
Característica: Recibir avisos autorizados sobre mi operación
  Escenario: Notificar formalización confirmada
    Dado un evento autoritativo de formalización de la operación del propietario
    Y autorización vigente para compartir ese hito
    Cuando se procesa el aviso
    Entonces aparece en su bandeja y se procesa correo con información mínima
    Y el enlace conduce a contenido que exige autenticación y autorización

  Escenario: No afirmar un pago pendiente
    Dado un pago de adquisición pendiente, fallido o sin fuente confirmada
    Cuando se evalúa el hito de pago
    Entonces no se envía un aviso de pago confirmado
    Y no se utiliza un pago de arriendo o venta como sustituto

  Escenario: Reprocesar sin duplicar el aviso lógico
    Dado un evento ya procesado para una revisión y destinatario
    Cuando se recibe nuevamente
    Entonces no se crea otro aviso lógico para la misma combinación
    Y un fallo de entrega puede reintentarse conservando historial

  Escenario: Retiro mientras el aviso está en cola
    Dado un aviso aún no enviado
    Cuando se retira el contenido o permiso antes de la validación de envío
    Entonces no se envía ese aviso con contenido retirado
    Y se conserva el motivo del bloqueo

  Escenario: Corregir un hito notificado
    Dado un aviso enviado basado en una confirmación posteriormente corregida
    Cuando se aprueba una corrección para compartir
    Entonces se conserva historial de la notificación anterior y la corrección
    Y no se afirma eliminar un correo ya entregado

  Escenario: Proteger una notificación ajena
    Dado un propietario sin vínculo con otra operación
    Cuando intenta leer o marcar como leído un aviso de esa operación
    Entonces se deniega acceso sin revelar su contenido
```

## HU-32 — Reportes exclusivos del gerente

```gherkin
Característica: Consultar resultados consolidados consistentes
  Escenario: Consolidar ingresos sin duplicar movimientos
    Dado ingresos del módulo 10 que ya incluyen pagos de arriendo y venta
    Cuando el gerente consulta el reporte consolidado
    Entonces esos ingresos se cuentan una sola vez
    Y el detalle usa la misma base, moneda y fecha de corte del resumen

  Escenario: Consolidar ratios con bases compatibles
    Dado dos inmuebles con porcentajes y denominadores diferentes
    Cuando se calcula ocupación o rentabilidad consolidada
    Entonces se usa el agregado autoritativo o sus componentes compatibles acordados
    Y no se promedian porcentajes sin considerar sus denominadores

  Escenario: Denominador cero
    Dado un indicador cuyo denominador acordado es cero
    Cuando el gerente consulta el reporte
    Entonces se muestra No aplica
    Y no se inventa una rentabilidad ni un porcentaje de ocupación

  Escenario: Identificar datos parciales
    Dado una fuente incompleta o indisponible para algunos inmuebles
    Cuando se consulta el período
    Entonces se marca el resultado como Parcial o No disponible según corresponda
    Y se indican fuentes o activos excluidos
    Y no se presenta una cifra parcial como total completo

  Escenario: No mezclar bases incompatibles
    Dado datos con monedas o cortes incompatibles
    Cuando se solicita consolidarlos
    Entonces se informa la incompatibilidad y no se suma un total engañoso

  Escenario: Restringir el reporte gerencial
    Dado un propietario original o arrendatario autenticado sin permiso de gerente
    Cuando solicita el endpoint de reportes
    Entonces se deniega acceso sin devolver métricas internas

  Escenario: Verificar filtros y desglose
    Dado un gerente autorizado y datos completos para el período
    Cuando filtra por ruta e inmueble y abre el detalle
    Entonces detalle y resumen aplican los mismos filtros y definición
    Y se muestra fecha de actualización y base del indicador
```
