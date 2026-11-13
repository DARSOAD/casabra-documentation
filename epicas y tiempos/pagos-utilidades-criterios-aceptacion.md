# Módulo 10. Pagos y utilidades — criterios propuestos

**Estado: pendientes de validación; no son criterios aprobados.** Fuente: HU-27 a HU-29 de las [historias](../historias_de_usuario_plan_del_proyecto.md). Aplican los supuestos de la [épica](pagos-utilidades-epica.md). Las fórmulas, clasificación y tratamiento fiscal deben ser aprobados por contador/gerente; proveedor y fuentes funcionales siguen pendientes de verificación.

## HU-27 — Costos e ingresos sin duplicación

```gherkin
Característica: Clasificar hechos económicos de inmuebles y proyectos
  Escenario: Importar un canon confirmado una sola vez
    Dado un canon y su pago confirmado en el módulo 8
    Cuando su evento se recibe dos veces y posteriormente se vincula una factura
    Entonces el mismo hecho económico no genera ingresos duplicados
    Y quedan relacionadas la obligación, el cobro y la factura

  Escenario: Separar gasto reportado de pago y reconocimiento
    Dado un gasto operativo registrado en obra
    Cuando se importa al módulo financiero
    Entonces conserva origen y estado pendiente de clasificación según política
    Y no se declara automáticamente pagado o reconocido por haber sido registrado

  Escenario: Conservar el total al asignar
    Dado un costo de 1000 COP aprobado
    Cuando el contador asigna 600 COP a un inmueble y 400 COP a otro
    Entonces el total asignado es 1000 COP
    Y una asignación que no conserve el importe se rechaza

  Escenario: Evitar doble costo por proyecto e inmueble
    Dado un gasto de proyecto ligado a un inmueble
    Cuando se consulta el consolidado del inmueble y sus proyectos
    Entonces el gasto se cuenta una sola vez

  Escenario: Corregir un cobro revertido
    Dado un pago importado cuya fuente informa un reverso confirmado
    Cuando se procesa la corrección
    Entonces se conserva el original y su vínculo compensatorio
    Y se actualizan los cobros y el resultado según política sin borrar historial

  Escenario: Registrar pago externo de adquisición
    Dado un desembolso registrado con soporte y operación de adquisición
    Cuando el contador aún no validó la recepción correspondiente
    Entonces no se publica como pago confirmado para el portal
    Cuando lo valida con autorización y evidencia
    Entonces se emite una referencia de confirmación consumible por el módulo 11
    Y esa referencia no ejecuta otra transferencia ni autoriza por sí sola compartirla
```

## HU-28 — Resultado y retorno gerencial

```gherkin
Característica: Calcular resultados reproducibles
  Escenario: Registrar resultado con base aprobada
    Dado ingresos reconocidos I de 1200 COP y costos imputables C de 200 COP
    Y una base de inversión B aprobada de 10000 COP para el mismo cálculo acumulado
    Cuando el gerente registra el cálculo con la fórmula propuesta
    Entonces el resultado R es 1000 COP y el retorno simple es 10%
    Y se conservan período, moneda, fórmula, entradas y responsable

  Escenario: No restar dos veces la inversión
    Dado una adquisición clasificada como inversión capitalizada
    Cuando se importa el pago asociado a esa adquisición
    Entonces no se crea un gasto adicional por el mismo desembolso
    Y cualquier costo de venta requiere reconocimiento según política aprobada

  Escenario: Base cero o información incompleta
    Dado un cálculo cuya base B es cero o cuyas fuentes no están completas
    Cuando se consulta el retorno
    Entonces con B cero se muestra No aplica
    Y con información incompleta se identifica como parcial sin afirmar retorno definitivo

  Escenario: Conservar versiones tras una corrección
    Dado un resultado previamente registrado
    Cuando se corrige un costo y se recalcula
    Entonces se registra una nueva versión
    Y la versión anterior conserva sus entradas y fecha de corte

  Escenario: Consolidar componentes compatibles
    Dado varios activos con bases de inversión distintas
    Cuando se consolida el retorno acordado para un corte compatible
    Entonces se usan sumas de componentes compatibles
    Y no se promedian porcentajes sin ponderación

  Escenario: Restringir acceso a resultados
    Dado un propietario o arrendatario sin permiso financiero
    Cuando solicita resultados internos directamente
    Entonces se deniega acceso
    Y el eventual contenido compartido se controla en el módulo 11
```

## HU-29 — Documentos fiscales mediante proveedor

```gherkin
Característica: Emitir documentos fiscales sin duplicar datos ni dinero
  Esquema del escenario: Preparar el documento aplicable
    Dado un contador que confirmó aplicabilidad y configuración de "<tipo>"
    Y datos completos de operación, tercero y referencias requeridas
    Cuando prepara el documento desde el hecho económico existente
    Entonces puede revisar y aprobar una versión antes de transmitir
    Y no se crea de nuevo el ingreso, costo o pago de origen
    Ejemplos:
      | tipo              |
      | Factura de venta  |
      | Nota crédito      |
      | Nota débito       |
      | Documento soporte |
      | Nota de ajuste    |

  Escenario: Bloquear borrador incompleto
    Dado datos fiscales o configuración obligatoria faltantes
    Cuando se intenta enviar el documento
    Entonces se indican los campos pendientes y no se transmite

  Escenario: Distinguir recepción del proveedor y validación
    Dado un documento recibido por el proveedor sin resultado DIAN confirmado
    Cuando se consulta su estado
    Entonces se muestra pendiente o por conciliar según corresponda
    Y no se afirma que esté validado ni entregado

  Escenario: Resolver timeout sin otra emisión
    Dado un envío cuya respuesta se interrumpió
    Cuando se reintenta el procesamiento
    Entonces se consulta la referencia original antes de emitir de nuevo
    Y si no se conoce el resultado queda Por conciliar

  Escenario: Archivar el resultado sin duplicar el documento
    Dado un documento validado con XML, representación y evidencia disponibles
    Cuando la descarga falla y luego se reintenta
    Entonces se recupera el archivo del mismo documento
    Y no se asigna otro número ni se registra otro ingreso

  Escenario: Corregir con el tipo de nota correspondiente
    Dado un documento validado que requiere corrección
    Cuando el contador aprueba la nota correspondiente según tipo y proveedor
    Entonces se conserva la relación con el original
    Y no se sobrescribe el original ni se ejecuta automáticamente un reembolso

  Escenario: Identificar contingencia sin inventar validación
    Dado un inconveniente tecnológico y un procedimiento aplicable confirmado con proveedor
    Cuando se registra y procesa la contingencia
    Entonces se conservan causa, estado y obligaciones de transmisión/conciliación
    Y un timeout local no cambia automáticamente el documento a Validado

  Escenario: Proteger callbacks y descargas
    Dado un evento externo sin autenticación válida o un usuario sin permiso fiscal
    Cuando se intenta cambiar estado o descargar un documento
    Entonces se rechaza la acción sin modificar el documento ni exponer artefactos
```
