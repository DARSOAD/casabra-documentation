# Módulo 8. Arriendo de inmuebles adquiridos — criterios propuestos v2

**Estado: pendientes de validación; no son criterios aprobados.** Fuente: HU-34 a HU-39, HU-46, HU-47 y HU-51 a HU-54 de las [historias](../historias_de_usuario_plan_del_proyecto.md). Aplican los supuestos de la [épica](arriendo-inmuebles-epica-v2.md): inmueble completo, un arrendatario principal, mensualidad, un proveedor/medio digital y servicios compartidos disponibles. Los escenarios verifican comportamiento, no fijan políticas legales ni se traducen mecánicamente a horas.

## HU-34 y HU-35 — Alta y preparación

```gherkin
Característica: Preparar activos adquiridos para arriendo
  Escenario: Iniciar ruta autorizada
    Dado un inmueble Adquirido y un gerente de activos autorizado
    Cuando confirma la ruta Arriendo mediante el flujo compartido
    Entonces se habilita una ficha de arriendo vinculada al mismo inmueble
    Y no se duplica el activo ni cambia su estado de adquisición

  Escenario: Impedir operación sobre inmueble no adquirido
    Dado un inmueble En proceso de compra
    Cuando se intenta darlo de alta como disponible en arriendo
    Entonces se rechaza la operación

  Escenario: Registrar alistamiento y condiciones
    Dado un administrador de inmuebles autorizado
    Cuando registra adecuaciones, canon, servicios, condiciones y garantías declaradas
    Entonces la ficha conserva esas condiciones y su responsable
    Y mientras esté En alistamiento no permite anunciarlo como disponible
```

## HU-36 — Ficha comercial y anuncios

```gherkin
Característica: Administrar la oferta comercial
  Escenario: Registrar un anuncio manual
    Dado un inmueble Disponible y fotografías seleccionadas como publicables
    Cuando el asesor registra canal, enlace y estado del anuncio
    Entonces el equipo puede consultar su ficha y el anuncio
    Y no se publican documentos privados ni datos de candidatos
    Y no se afirma sincronización automática con el portal externo

  Escenario: Retirar disponibilidad al ocupar
    Dado un inmueble con anuncios registrados
    Cuando pasa a Ocupado por entrega registrada
    Entonces deja de ofrecerse como disponible en la ficha interna
    Y los anuncios requieren retiro o actualización manual en sus canales
```

## HU-37 — Candidatos y selección

```gherkin
Característica: Evaluar interesados con trazabilidad
  Escenario: Registrar seguimiento y recomendación
    Dado un asesor de arriendos autorizado
    Cuando registra solicitud, documentos, visita y resultado de evaluación
    Entonces queda una recomendación atribuida a su autor
    Y el administrador puede revisar la información para seleccionar

  Escenario: Evitar doble selección concurrente
    Dado dos solicitudes para el mismo inmueble disponible
    Cuando dos administradores intentan reservarlo para candidatos distintos
    Entonces solo una selección puede quedar vigente
    Y el otro intento informa conflicto sin sobrescribir la decisión

  Escenario: Proteger documentos de candidatos
    Dado un arrendatario o usuario sin permiso sobre una solicitud
    Cuando intenta descargar sus documentos por identificador
    Entonces se deniega acceso sin entregar enlaces privados
```

## HU-38 — Contrato y formalización

```gherkin
Característica: Formalizar condiciones antes de entregar
  Escenario: Preparar contrato completo
    Dado un candidato seleccionado y un administrador autorizado
    Cuando registra canon, periodicidad mensual, vencimiento, vigencia, reajustes, obligaciones y garantías
    Entonces se prepara una revisión en el motor contractual del módulo 7
    Y se conserva el vínculo entre contrato, inmueble y arrendatario

  Escenario: No entregar por una firma aún pendiente
    Dado un contrato sin confirmación completa de firma del módulo 7
    Cuando se intenta registrar la entrega
    Entonces no se habilita entrega como contrato formalizado

  Escenario: Acceso del arrendatario correcto
    Dado un arrendatario seleccionado que recibe una invitación válida
    Cuando activa su acceso mediante la autenticación compartida
    Entonces accede solo a contratos asociados a su identidad
    Y no obtiene permisos internos ni el rol del propietario original
```

## HU-39 — Entrega, novedades y devolución

```gherkin
Característica: Conservar evidencia de ocupación
  Escenario: Entregar con inventario
    Dado un contrato formalizado y requisitos de entrega cumplidos
    Cuando el administrador registra inventario, fotos y fecha real de entrega
    Entonces comienza el período de ocupación
    Y un reenvío de la misma operación no crea otra entrega

  Escenario: Registrar novedades sin perder contexto
    Dado un inmueble ocupado
    Cuando se registra una novedad con responsable, descripción y evidencia
    Entonces permanece vinculada al contrato con su historial de cambios

  Escenario: Devolver conservando deuda
    Dado un contrato con cánones pendientes
    Cuando se registra devolución con inventario y fecha real
    Entonces finaliza la ocupación y queda pendiente el alistamiento
    Y la deuda previa permanece consultable y cobrable
```

## HU-46 — Obligaciones y vigencia

```gherkin
Característica: Mantener un calendario de cobro consistente
  Escenario: Generar un cargo por período
    Dado un contrato activado con canon mensual y vencimiento configurado
    Cuando el proceso de generación se ejecuta dos veces para el mismo período
    Entonces existe una sola obligación de canon para ese período

  Escenario: Vencimiento en un mes corto
    Dado un contrato con día de pago 31
    Cuando se genera una obligación para un mes sin día 31
    Entonces se usa el último día del mes según la convención propuesta

  Escenario: Reajuste futuro sin reescribir historia
    Dado un contrato con obligaciones causadas
    Cuando un administrador aprueba nuevo canon con vigencia futura
    Entonces el nuevo valor aplica a los períodos futuros correspondientes
    Y se conservan los importes e historial de períodos causados

  Escenario: Renovar sin solapamiento
    Dado un contrato próximo a finalizar
    Cuando se formaliza una renovación como nuevo período contractual vinculado
    Entonces no se duplican obligaciones ni se superponen contratos operativos

  Escenario: Terminar con saldo pendiente
    Dado un contrato con deuda causada y obligaciones futuras aún no causadas
    Cuando se registra terminación efectiva autorizada
    Entonces las futuras se cancelan según la regla aprobada y con trazabilidad
    Y la deuda causada no se elimina
```

## HU-47 — Indicadores

```gherkin
Característica: Consultar operación y cartera
  Escenario: Conciliar tablero con movimientos
    Dado un contrato con pagos confirmados, pendientes y reversos
    Cuando el gerente consulta un período
    Entonces los cobros incluyen solo confirmaciones menos reversos del período
    Y los pendientes no se presentan como ingresos cobrados
    Y se distinguen saldo, deuda vencida y próximos vencimientos

  Escenario: Diferenciar ocupación de firma y vacancia de obra
    Dado un contrato firmado sin entrega y un inmueble en alistamiento
    Cuando el gerente consulta los indicadores
    Entonces la firma sola no cuenta como ocupación
    Y los días en alistamiento se muestran separados de vacancia disponible

  Escenario: Evitar multiplicar cifras por relaciones
    Dado un contrato con varios pagos, documentos y reportes
    Cuando se calcula el tablero
    Entonces cada movimiento monetario se cuenta una sola vez
    Y la falta de datos o un error no se presenta como cero confirmado
```

## HU-51 — Portal y pago digital

```gherkin
Característica: Consultar y pagar el canon propio
  Escenario: Consultar estado de cuenta
    Dado un arrendatario autenticado
    Cuando abre su portal
    Entonces ve contrato, próximos vencimientos, saldo y pagos propios
    Y no ve evaluaciones internas ni contratos de otras personas

  Escenario: Iniciar un pago válido
    Dado una obligación propia con saldo pendiente
    Cuando el arrendatario inicia un pago o abono válido
    Entonces el backend valida monto y crea referencia antes del checkout
    Y no se aceptan montos o contratos manipulados desde el navegador

  Escenario: Retorno externo sin confirmación
    Dado un intento de pago y retorno del checkout al navegador
    Cuando no existe confirmación verificada del proveedor
    Entonces se muestra Pendiente o Por conciliar según corresponda
    Y no se disminuye el saldo ni se emite comprobante confirmado
```

## HU-52 — Recordatorios

```gherkin
Característica: Avisar obligaciones sin duplicar gestión
  Esquema del escenario: Generar el aviso correspondiente
    Dado una obligación o transacción en situación "<situacion>"
    Cuando se cumple la regla de aviso configurada
    Entonces se registra un aviso in-app y se procesa correo al arrendatario
    Y se identifica la situación sin afirmar un pago aún no confirmado
    Ejemplos:
      | situacion          |
      | Próxima a vencer   |
      | Vencida con saldo  |
      | Pago sin confirmar |

  Escenario: Revalidar antes de avisar
    Dado un aviso de deuda pendiente de procesar
    Cuando el saldo se paga antes de la comprobación de envío
    Entonces se cancela ese aviso de deuda
    Y un reintento no crea otro aviso lógico para la misma regla y fecha
```

## HU-53 — Confirmación y conciliación

```gherkin
Característica: Registrar pagos una sola vez con evidencia
  Escenario: Confirmar con referencia e importe válidos
    Dado una transacción Pendiente y una confirmación verificable del proveedor
    Cuando coinciden referencia, contrato, moneda e importe
    Entonces se registra Confirmada y se aplica una sola vez a la cuenta
    Y reenviar el mismo evento no duplica el dinero

  Escenario: Rechazar evento o valores inconsistentes
    Dado un evento no auténtico o una confirmación con importe distinto
    Cuando se procesa
    Entonces el evento no auténtico se rechaza
    Y una confirmación auténtica inconsistente queda Por conciliar sin aplicar dinero

  Escenario: Aplicar abono y saldo a favor
    Dado una obligación de 1000 COP y un pago confirmado de 400 COP
    Cuando se imputa el pago
    Entonces quedan 600 COP pendientes
    Y si después se confirman 700 COP se aplican 600 COP y quedan 100 COP a favor

  Escenario: Recuperar una confirmación tardía
    Dado un intento con respuesta incierta y otra vía que ya cubrió la obligación
    Cuando el proveedor confirma el primer intento
    Entonces se registra el dinero una sola vez
    Y el excedente queda a favor sin perderse ni descontar otra deuda automáticamente

  Escenario: Registrar pago por otro medio
    Dado un administrador con referencia, importe y soporte de pago
    Cuando registra el pago manual
    Entonces queda pendiente de validación explícita
    Y solo tras esa validación se aplica a la cuenta con responsable registrado

  Escenario: Evitar referencia duplicada y preservar correcciones
    Dado un pago ya registrado con una referencia
    Cuando se intenta registrar de nuevo o corregirlo
    Entonces se alerta el duplicado y se exige resolución autorizada
    Y cualquier corrección conserva el movimiento original y su trazabilidad

  Escenario: Registrar reverso confirmado
    Dado un pago confirmado e imputado
    Cuando el proveedor informa un reverso verificado
    Entonces se registra un movimiento compensatorio vinculado
    Y se recalcula saldo e imputación sin borrar la confirmación histórica
    Y se actualiza la vigencia del comprobante asociado
```

## HU-54 — Comprobante interno

```gherkin
Característica: Entregar evidencia de pagos confirmados
  Escenario: Generar recibo una sola vez
    Dado un pago digital confirmado o un pago manual validado
    Cuando se procesa la emisión del comprobante
    Entonces existe un recibo interno único con monto, referencia y aplicación
    Y el arrendatario puede descargarlo desde su portal y recibe aviso con enlace
    Y no se presenta como factura DIAN ni paz y salvo

  Escenario: Recuperar una generación fallida
    Dado un pago confirmado cuyo PDF no pudo generarse
    Cuando se reintenta la emisión
    Entonces se genera el mismo comprobante lógico sin repetir el pago
    Y el estado de cuenta no depende del éxito de la descarga o correo

  Escenario: Descargar solo el comprobante propio
    Dado un arrendatario autenticado
    Cuando solicita un recibo de otro contrato
    Entonces se deniega acceso sin entregar una URL privada
```
