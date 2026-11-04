# Criterios mínimos de aceptación del módulo 2 Adquisición de inmuebles

```gherkin
# language: es
Característica: Adquisición de inmuebles

  @HU-04
  Escenario: Guardar documentos con requisitos pendientes
    Dado que el propietario tiene un inmueble con requisitos pendientes
    Cuando carga un documento permitido desde la app
    Entonces el documento queda asociado al propietario o al inmueble según su tipo
    Y se conservan la información y los documentos cargados anteriormente
    Y el inmueble queda en estado "Documentación faltante"
    Y el propietario puede consultar los requisitos pendientes

  @HU-04
  Escenario: Completar los requisitos para iniciar el estudio
    Dado que el inmueble está en estado "Documentación faltante"
    Cuando el propietario completa todos los datos y documentos requeridos configurados
    Entonces el inmueble pasa a estado "En estudio"
    Y el expediente conserva los documentos entregados

  @HU-04
  Escenario: Reutilizar un documento propio
    Dado que el propietario ya tiene en la app un documento utilizable para su solicitud
    Cuando lo selecciona para completar el requisito correspondiente
    Entonces el documento queda vinculado al expediente
    Y no se le exige cargar nuevamente el mismo archivo

  @HU-05
  Escenario: Consultar la ficha del inmueble
    Dado que el asesor comercial tiene acceso al inmueble
    Cuando abre su ficha
    Entonces puede consultar sus datos, fotos y documentos legales disponibles
    Y puede identificar la información o documentación pendiente

  @HU-06
  Escenario: Registrar el estudio de títulos
    Dado que el inmueble está en estado "En estudio"
    Y el abogado tiene acceso al expediente
    Cuando guarda el estudio de títulos, su conclusión y las alertas identificadas
    Entonces el estudio y las alertas quedan asociados al inmueble
    Y las alertas permiten identificar gravámenes, embargos o falta de licencias cuando correspondan
    Y se conservan la fecha y el responsable del registro
    Y el asesor autorizado puede consultar el resultado para decidir si envía una propuesta o rechaza el inmueble

  @HU-05 @HU-08
  Escenario: Enviar una propuesta económica
    Dado que el inmueble está en estado "En estudio"
    Y el asesor comercial tiene acceso al expediente
    Cuando envía al propietario una propuesta con el valor ofrecido por la compañía
    Entonces el inmueble pasa a estado "Propuesta enviada"
    Y el propietario puede consultar el valor ofrecido en la app

  @HU-05 @HU-08
  Escenario: Rechazar el inmueble durante el estudio
    Dado que el inmueble está en estado "En estudio"
    Y el asesor comercial tiene acceso al expediente
    Cuando rechaza el inmueble e indica el motivo
    Entonces el inmueble pasa a estado "Rechazado"
    Y se registra que el rechazo fue realizado por la compañía

  @HU-08
  Esquema del escenario: Responder a la propuesta económica
    Dado que el inmueble del propietario está en estado "Propuesta enviada"
    Y el propietario puede consultar la oferta económica
    Cuando el propietario decide <decision> la propuesta desde la app
    Entonces el inmueble pasa a estado "<estado>"
    Y se registra la decisión del propietario

    Ejemplos:
      | decision | estado               |
      | aceptar  | En proceso de compra |
      | rechazar | Rechazado            |

  @HU-07 @HU-08
  Escenario: Confirmar la adquisición
    Dado que el inmueble está en estado "En proceso de compra"
    Y quien realiza la acción es un abogado u otra persona con permiso para confirmar la adquisición
    Cuando confirma que la compra se completó
    Entonces el inmueble pasa a estado "Adquirido"
    Y queda registrado como un activo de la compañía

  @HU-07
  Esquema del escenario: Asignar la ruta del inmueble adquirido
    Dado que el inmueble está en estado "Adquirido"
    Y el gerente tiene acceso al inmueble
    Cuando asigna la ruta "<ruta>" e indica que <requiere> requiere adecuaciones
    Entonces se guardan la ruta y la necesidad de adecuaciones
    Y el inmueble queda habilitado para el flujo operativo correspondiente

    Ejemplos:
      | ruta     | requiere |
      | Arriendo | sí       |
      | Arriendo | no       |
      | Venta    | sí       |
      | Venta    | no       |

  @HU-08
  Esquema del escenario: Consultar el avance de la solicitud
    Dado que el propietario tiene una solicitud registrada
    Y su fecha estimada de respuesta está <disponibilidad>
    Cuando consulta el seguimiento desde la app
    Entonces ve el estado actual y los requisitos pendientes si existen
    Y ve como respuesta esperada <respuesta>

    Ejemplos:
      | disponibilidad | respuesta                 |
      | registrada     | la fecha estimada vigente |
      | sin definir    | "Por confirmar"           |

  @Transversal
  Escenario: Conservar el historial de los cambios de estado
    Dado que un usuario tiene permiso para realizar una transición válida
    Cuando cambia el estado del inmueble
    Entonces se registran el estado anterior, el nuevo estado, la fecha y el responsable
    Y se conserva el historial anterior

  @Transversal
  Esquema del escenario: Impedir operaciones incompatibles con el estado
    Dado que el inmueble está en estado "<estado>"
    Y el usuario tiene el permiso correspondiente a la acción
    Cuando intenta <accion>
    Entonces la operación se rechaza y se informa que el estado actual no la permite
    Y el inmueble conserva su estado y sus datos anteriores

    Ejemplos:
      | estado                | accion                         |
      | Documentación faltante | enviar una propuesta          |
      | En estudio            | aceptar una propuesta          |
      | Propuesta enviada     | confirmar la adquisición       |
      | En proceso de compra  | asignar una ruta de operación   |
      | Rechazado             | aceptar una propuesta          |

  @Transversal
  Esquema del escenario: Impedir acciones sin autorización
    Dado que el usuario no tiene <autorizacion>
    Cuando intenta <accion>
    Entonces el sistema deniega la operación
    Y no expone información no autorizada ni modifica el expediente

    Ejemplos:
      | autorizacion                              | accion                                |
      | acceso al expediente                      | consultar su ficha o documentos        |
      | acceso a la solicitud del propietario     | consultar su seguimiento               |
      | permiso para registrar estudios jurídicos | registrar el estudio de títulos        |
      | permiso para enviar propuestas            | enviar una oferta económica            |
      | permiso para rechazar inmuebles           | rechazar el inmueble durante el estudio |
      | ser el propietario de la solicitud        | aceptar o rechazar la propuesta        |
      | permiso para confirmar la adquisición     | cambiar el inmueble a Adquirido        |
      | permiso de gerente para asignar rutas     | asignar arriendo o venta               |
```
