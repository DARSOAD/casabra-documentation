# Módulo 9. Venta de inmuebles adquiridos — criterios propuestos

**Estado: pendientes de validación; no son criterios aprobados.** Fuente: HU-40 a HU-45 y HU-48 a HU-50 de las [historias](../historias_de_usuario_plan_del_proyecto.md). Aplican los supuestos de la [épica](venta-inmuebles-epica.md): catálogo web propio, canales externos manuales, un comprador principal, pago externo validado y componentes de CRM/firma/archivos disponibles. No se definen requisitos jurídicos ni se convierten escenarios mecánicamente en horas.

## HU-40 — Asignación y precio objetivo

```gherkin
Característica: Iniciar venta de activos de la compañía
  Escenario: Habilitar venta de un inmueble adquirido
    Dado un inmueble Adquirido y un gerente de activos autorizado
    Cuando asigna la ruta Venta mediante el flujo compartido y registra precio objetivo válido
    Entonces se habilita una ficha de venta vinculada al mismo activo
    Y no se duplica el inmueble ni su adquisición histórica

  Esquema del escenario: Rechazar un activo no elegible
    Dado un inmueble con "<condicion>"
    Cuando se intenta iniciar su venta
    Entonces se rechaza la operación sin modificar su ruta ni disponibilidad
    Ejemplos:
      | condicion                     |
      | adquisición aún no completada |
      | ruta Arriendo vigente         |
      | venta ya cerrada              |
```

## HU-41 — Ficha comercial

```gherkin
Característica: Preparar información para comercializar
  Escenario: Conservar ficha completa y alistamiento
    Dado un asesor autorizado y un activo habilitado para venta
    Cuando registra descripción, fotografías, precio, documentos y alistamiento
    Entonces la ficha interna conserva la información y responsable
    Y distingue precio objetivo, publicado y acordado

  Escenario: No publicar el expediente privado
    Dado fotografías aprobadas y documentos jurídicos privados
    Cuando se prepara la vista pública
    Entonces solo se incluyen campos y fotografías permitidos
    Y no aparecen documentos, precio objetivo interno ni datos de compradores
```

## HU-42 — Publicación y actualización

```gherkin
Característica: Mantener la oferta vigente en los canales acordados
  Escenario: Publicar en la web propia
    Dado un inmueble Disponible con ficha completa y alistamiento validado
    Cuando el asesor publica la versión aprobada
    Entonces aparece en el catálogo y ficha pública con su precio publicado
    Y visitantes pueden consultar información comercial sin autenticarse

  Escenario: Actualizar contenido público
    Dado una ficha publicada
    Cuando se publica una nueva versión válida de descripción o precio
    Entonces la web propia presenta esa versión coherentemente
    Y se conserva historial interno de cambios

  Escenario: Registrar un canal externo manual
    Dado un anuncio gestionado por el equipo en un portal externo
    Cuando el asesor registra su enlace, fecha y estado
    Entonces el equipo puede dar seguimiento al anuncio
    Y no se afirma que la aplicación lo haya publicado o sincronizado automáticamente

  Escenario: Retirar disponibilidad al reservar o vender
    Dado un inmueble con publicación web y anuncios externos registrados
    Cuando deja de estar disponible por reserva o cierre
    Entonces la web propia no lo ofrece como disponible
    Y se genera retiro o actualización pendiente para los canales externos
```

## HU-43 — Prospectos y oportunidades

```gherkin
Característica: Dar seguimiento a compradores potenciales
  Escenario: Registrar un prospecto con varios intereses
    Dado un asesor autorizado
    Cuando registra un prospecto con origen, contacto e interés en dos inmuebles
    Entonces existen dos oportunidades vinculadas al mismo prospecto
    Y cada una conserva etapa y seguimiento propios

  Escenario: Continuar una conversación desde el equipo
    Dado una oportunidad con interacciones y tareas registradas
    Cuando otro asesor autorizado consulta su historial
    Entonces ve contexto, autores, fechas y próximos seguimientos
    Y no se mezclan notas privadas de adquisición de un propietario

  Escenario: Reprogramar un seguimiento
    Dado una tarea pendiente asociada a oportunidad de venta
    Cuando se cambia su fecha mediante el servicio CRM compartido
    Entonces el recordatorio anterior deja de estar vigente
    Y el nuevo seguimiento mantiene el vínculo y acceso correctos
```

## HU-44 — Visitas

```gherkin
Característica: Coordinar visitas con resultado atribuible
  Escenario: Registrar visita realizada
    Dado una visita programada con asesor y oportunidad
    Cuando el asesor registra comentarios y nivel de interés
    Entonces queda Realizada con fecha y responsable
    Y el resultado es visible en la oportunidad autorizada

  Escenario: Cancelar sin perder historial
    Dado una visita programada
    Cuando el asesor la cancela con motivo
    Entonces se conserva el registro como Cancelada
    Y no se presenta como una visita realizada
```

## HU-45 — Ofertas, contraofertas y aprobación

```gherkin
Característica: Negociar con versiones y autorizaciones
  Escenario: Comparar ofertas vigentes
    Dado dos compradores con ofertas y una contraoferta posterior
    Cuando el gerente comercial consulta la comparación
    Entonces ve la revisión vigente y condiciones de cada oportunidad
    Y puede consultar versiones previas sin contarlas como nuevas ventas

  Escenario: Separar aprobación de aceptación
    Dado una oferta aprobada internamente por gerente comercial
    Cuando todavía no se registró aceptación del comprador
    Entonces no se reserva como negociación aceptada
    Y la aprobación no se interpreta como contrato firmado ni pago recibido

  Escenario: Invalidar decisiones antiguas
    Dado una oferta aprobada y aceptada en una versión
    Cuando se modifican el importe o las condiciones
    Entonces la nueva versión requiere nueva aprobación y aceptación
    Y no puede reservarse o cerrarse usando decisiones anteriores

  Escenario: Impedir dos reservas simultáneas
    Dado dos oportunidades con versiones aprobadas y aceptadas para el mismo inmueble
    Cuando se intenta reservar para ambas simultáneamente
    Entonces solo una reserva puede quedar vigente
    Y el otro intento informa conflicto sin sobrescribir la primera

  Escenario: Restringir la aprobación de precio
    Dado un asesor sin facultad de gerente comercial
    Cuando intenta aprobar una oferta mediante la API
    Entonces se deniega la aprobación aunque el precio supere el objetivo
```

## HU-48 — Revisión y formalización

```gherkin
Característica: Verificar expediente antes del cierre
  Escenario: Preparar contrato con condiciones vigentes
    Dado una reserva y términos aprobados y aceptados vigentes
    Cuando el abogado prepara el expediente y contrato de venta
    Entonces se usa la plantilla y flujo de firma del módulo 7
    Y el contrato conserva los términos y comprador de esa versión

  Escenario: Rechazar aprobación jurídica incompleta
    Dado un expediente con un requisito obligatorio pendiente según el checklist acordado
    Cuando se intenta aprobarlo para cierre
    Entonces se identifica el requisito y no se habilita cierre

  Escenario: Revalidar ante cambio relevante
    Dado un expediente aprobado
    Cuando cambian términos o documentos relevantes para esa revisión
    Entonces se invalida la aprobación vigente
    Y se requiere revisión del abogado sobre la nueva versión
```

## HU-49 — Pago, entrega y cierre

```gherkin
Característica: Cerrar ventas con evidencia e inventario consistente
  Escenario: Validar un pago externo
    Dado un pago registrado con referencia, importe y soporte
    Cuando el administrador aún no confirmó recepción
    Entonces el pago no suma como recibido para el cierre
    Cuando confirma recepción con autorización y trazabilidad
    Entonces suma una sola vez a la venta correspondiente

  Escenario: Registrar abonos sin confundir pago completo
    Dado un precio final aprobado de 1000 COP y abonos confirmados por 600 COP
    Cuando se verifica el pago para cierre
    Entonces se identifica un faltante de 400 COP
    Y no se habilita cierre por precio íntegramente cubierto

  Escenario: No cerrar solo por firma
    Dado un contrato con firma completa y un requisito de pago o entrega pendiente
    Cuando se solicita cierre
    Entonces se rechaza el cierre indicando el requisito pendiente
    Y el inmueble no queda Vendido

  Escenario: Cerrar una venta completa
    Dado reserva exclusiva, términos consistentes y revisión jurídica vigente
    Y contrato firmado y archivado, precio íntegramente pagado y entrega registrada
    Cuando el administrador autorizado confirma el cierre
    Entonces se registra un cierre único y la disponibilidad pasa a Vendido
    Y la oportunidad ganadora queda Ganada y las demás Perdidas por inmueble vendido
    Y se conservan adquisición histórica, documentos, pagos y responsables

  Escenario: Recuperar retiro después del cierre
    Dado un cierre persistido cuyo retiro de publicación falló
    Cuando se reintenta el evento de retiro o se repite la solicitud de cierre
    Entonces no se crea otra venta ni otro pago
    Y se completa el retiro pendiente sin revertir el cierre confirmado

  Escenario: Impedir reapertura ordinaria
    Dado una venta Cerrada
    Cuando se intenta alterar precio, anular pagos o liberar el inmueble mediante edición normal
    Entonces se rechaza el cambio
    Y se permite registrar un incidente para resolución por el procedimiento acordado
```

## HU-50 — Resultados comerciales

```gherkin
Característica: Medir el embudo y las ventas
  Escenario: Distinguir oportunidades de ventas realizadas
    Dado un prospecto con dos oportunidades y varias versiones de oferta
    Y solo una venta cerrada
    Cuando el gerente consulta indicadores
    Entonces las oportunidades se cuentan por su identificador y etapa
    Y la venta y su valor final se cuentan una sola vez

  Escenario: Explicar fechas de cada indicador
    Dado un período seleccionado
    Cuando el gerente consulta el tablero
    Entonces el embudo incluye oportunidades creadas en el período con etapa actual al corte
    Y las ventas se filtran por fecha de cierre y ofertas por fecha de creación
    Y las definiciones quedan visibles para evitar comparar universos distintos

  Escenario: Calcular tiempo de cierre
    Dado una oportunidad ganadora creada el día 1 y cerrada el día 11
    Cuando se mide su duración en días
    Entonces aporta 10 días al cálculo de tiempo de cierre
    Y si no hay cierres en el período el promedio se muestra como No aplica

  Escenario: Proteger datos gerenciales
    Dado un visitante público o usuario sin permiso gerencial
    Cuando solicita indicadores comerciales internos
    Entonces se deniega acceso sin revelar ofertas, compradores o valores internos
```
