# Módulo 7. Contratos y firma electrónica — criterios propuestos

**Estado: pendientes de validación; no son criterios aprobados.** Fuente: HU-20 a HU-22 de las [historias](../historias_de_usuario_plan_del_proyecto.md) y supuestos de la [épica](contratos-firma-epica.md). Se cotizan tres plantillas, un proveedor y dos firmantes en secuencia. La modalidad y evidencia suficientes para cada documento deben ser aprobadas por negocio/abogado; estos escenarios verifican el comportamiento técnico previsto.

## HU-20 — Plantillas y preparación

```gherkin
Característica: Preparar contratos a partir de plantillas versionadas
  Esquema del escenario: Generar un documento por tipo de operación
    Dado un abogado autorizado y una plantilla publicada de "<tipo>"
    Y datos completos y compatibles de la operación y participantes
    Cuando genera el contrato
    Entonces se conserva una revisión PDF con snapshot de datos y plantilla
    Y puede revisar el documento antes de aprobarlo para firma
    Ejemplos:
      | tipo        |
      | Adquisición |
      | Arriendo    |
      | Venta       |

  Escenario: Conservar contratos emitidos al actualizar una plantilla
    Dado contratos generados con una versión publicada
    Cuando el abogado publica una nueva versión
    Entonces los contratos existentes conservan su versión y contenido
    Y los nuevos contratos pueden usar la nueva versión

  Escenario: Rechazar datos o variables inválidos
    Dado un borrador con un campo obligatorio faltante o variable no permitida
    Cuando el abogado intenta generar o aprobar el documento
    Entonces se indica el problema sin habilitar envío a firma

  Escenario: Invalidar aprobación al modificar el contenido
    Dado un contrato Listo para firma aún no enviado
    Cuando se cambia un dato del contrato
    Entonces se genera una revisión que requiere nueva aprobación
    Y no se envía usando la aprobación de la revisión anterior

  Escenario: Impedir edición de documento enviado
    Dado un contrato En firma
    Cuando se intenta sobrescribir su PDF o participantes
    Entonces se rechaza la edición conservando el documento enviado
    Y cualquier sustitución debe seguir el flujo autorizado de cancelación y nuevo contrato
```

## HU-21 — Firma desde celular

```gherkin
Característica: Firmar la revisión aprobada mediante un proveedor
  Escenario: Acceder al contrato asignado desde celular
    Dado una contraparte identificada según el mecanismo acordado con el proveedor
    Y una invitación vigente para la revisión enviada
    Cuando abre la invitación desde celular
    Entonces puede revisar el documento y acceder al flujo alojado de firma
    Y no obtiene acceso a contratos de otras personas

  Escenario: Retorno del navegador sin confirmación
    Dado un firmante que regresa desde la pantalla del proveedor
    Cuando la aplicación aún no tiene confirmación verificada
    Entonces muestra Pendiente de confirmación
    Y no marca Firma completa por parámetros de la URL

  Escenario: Firma parcial
    Dado un contrato que requiere firma de contraparte y representante de compañía
    Cuando el proveedor confirma únicamente la firma de la contraparte
    Entonces el contrato permanece En firma
    Y se identifica al representante pendiente

  Escenario: Confirmar todas las firmas
    Dado el contrato En firma y sus dos participantes requeridos
    Cuando una consulta o evento verificado confirma que todos completaron su firma
    Entonces el contrato queda Firma completa
    Y comienza el archivo de documento y evidencias
    Y no se confirma automáticamente adquisición, pago, entrega ni cierre del inmueble

  Escenario: Evitar doble solicitud ante timeout
    Dado un envío al proveedor cuya respuesta se interrumpió
    Cuando se reintenta procesar el envío
    Entonces se consulta la referencia original antes de crear otra solicitud
    Y si no se resuelve el resultado queda en conciliación sin otro envío

  Esquema del escenario: Tratar una invitación no utilizable
    Dado un contrato cuyo proveedor confirma estado "<estado>"
    Cuando el participante intenta retomar la firma
    Entonces se informa ese estado sin afirmar que se completó la firma
    Ejemplos:
      | estado    |
      | Rechazado |
      | Expirado  |
      | Cancelado |

  Escenario: Autenticar y deduplicar eventos
    Dado un evento sin autenticación válida y un evento válido reenviado
    Cuando llegan al receptor de eventos
    Entonces se rechaza el primero sin cambiar estado
    Y el segundo produce su efecto una sola vez

  Escenario: Recuperar eventos perdidos o desordenados
    Dado un evento antiguo o la ausencia de un evento de finalización
    Cuando se ejecuta la conciliación con el proveedor
    Entonces se conserva o recupera su estado autoritativo
    Y no se regresa de Firma completa a un estado anterior por un evento viejo

  Escenario: Conciliar cancelación concurrente con firma
    Dado una solicitud de cancelación y una firma completada concurrentemente
    Cuando no está confirmado el resultado de la cancelación
    Entonces el sistema consulta al proveedor y conserva la trazabilidad
    Y no afirma Cancelado solo por haber solicitado la cancelación
```

## HU-22 — Archivo y evidencia

```gherkin
Característica: Archivar contratos firmados con trazabilidad
  Escenario: Conservar el paquete de firma completo
    Dado un contrato con Firma completa confirmada
    Cuando se descargan y persisten el PDF firmado y las evidencias del proveedor
    Entonces queda Archivado con referencias de versión y hashes propios
    Y se conserva el PDF original enviado separado del PDF firmado
    Y la trazabilidad identifica plantilla, revisión, participantes y eventos

  Escenario: Recuperar fallo de archivo sin repetir firma
    Dado un contrato con Firma completa cuya descarga o persistencia falló
    Cuando se recupera el proceso de archivo
    Entonces se obtienen los artefactos faltantes para la misma solicitud
    Y no se crea otra solicitud de firma
    Y solo se marca Archivado cuando estén documento y evidencias

  Escenario: Rechazar artefacto no correspondiente
    Dado una descarga que no puede correlacionarse con la solicitud esperada
    Cuando se procesa para archivo
    Entonces no se marca Archivado
    Y queda un error trazable para revisión y recuperación

  Escenario: Consultar con autorización
    Dado un administrador autorizado
    Cuando solicita un contrato archivado
    Entonces puede consultar trazabilidad y descargar artefactos mediante acceso temporal
    Y queda registrado el acceso

  Escenario: Impedir consulta de contrato ajeno
    Dado una contraparte sin autorización sobre otro contrato
    Cuando solicita su archivo por identificador
    Entonces se deniega acceso sin revelar documento, evidencias ni enlace de firma
```
