# Módulo 5. CRM — criterios propuestos para cotización

**Estado: propuesta, pendiente de validación; no son criterios aprobados.** Fuente: HU-12 a HU-15 de las [historias](../historias_de_usuario_plan_del_proyecto.md). Alcance y supuestos en la [épica](crm-epica.md). Se presupone equipo comercial con acceso compartido autorizado, etapas manuales, historial sin borrado y avisos dentro de la app. Los escenarios no fijan horas por sí mismos.

## HU-12 — Ficha y etapa del cliente

```gherkin
Característica: Consultar el seguimiento comercial
  Escenario: Consultar una ficha con varios inmuebles
    Dado un asesor autorizado y un cliente con dos solicitudes de adquisición
    Cuando consulta su ficha comercial
    Entonces ve su etapa de cliente y ambas solicitudes autorizadas
    Y cada inmueble conserva su estado de adquisición independiente

  Escenario: Registrar una etapa comercial sin confirmar una compra
    Dado un cliente en la etapa "En evaluación" y un asesor autorizado
    Cuando registra la etapa comercial "Contrato firmado"
    Entonces se conservan etapa anterior, etapa nueva, fecha y responsable
    Y ningún inmueble cambia a "Adquirido" por esa acción

  Escenario: Evitar sobrescritura simultánea
    Dado que otro asesor modificó la etapa desde que se abrió la ficha
    Cuando se intenta guardar usando la versión anterior
    Entonces se informa el conflicto y se solicita actualizar la ficha
    Y no se sobrescribe el cambio más reciente

  Escenario: Rechazar acceso a notas internas
    Dado un propietario original o un arrendatario autenticado
    Cuando solicita una ficha o historial interno por su identificador
    Entonces se deniega el acceso sin devolver datos internos
```

## HU-13 — Interacciones y compromisos

```gherkin
Característica: Conservar el contexto del equipo
  Esquema del escenario: Registrar un contacto
    Dado un asesor autorizado en la ficha de un cliente
    Cuando registra una actividad de tipo "<tipo>" con fecha y resultado
    Entonces queda visible para un compañero autorizado con su fecha y autor
    Y reenviar la misma solicitud no duplica la actividad
    Ejemplos:
      | tipo    |
      | Llamada |
      | Visita  |

  Escenario: Corregir una nota sin perder trazabilidad
    Dado una actividad registrada
    Cuando un asesor autorizado registra una corrección vinculada
    Entonces se conservan la entrada original y la corrección con su autor

  Escenario: Programar un compromiso
    Dado un cliente y un miembro autorizado del equipo
    Cuando un asesor registra un compromiso con responsable y vencimiento
    Entonces aparece como pendiente en la agenda del responsable
    Y conserva fecha y hora según la zona acordada
```

## HU-14 — Recordatorios de seguimiento

```gherkin
Característica: Recordar compromisos pendientes dentro de la app
  Escenario: Avisar un compromiso vencido una sola vez
    Dado un compromiso pendiente cuyo vencimiento ya llegó
    Cuando el proceso programado se ejecuta y se reintenta
    Entonces existe un solo aviso vigente para ese vencimiento y responsable
    Y el responsable puede consultarlo y marcarlo como leído
    Y otro usuario sin permiso no puede leerlo ni modificarlo

  Escenario: Reprogramar un compromiso
    Dado un compromiso con un aviso del vencimiento anterior
    Cuando un asesor autorizado modifica el vencimiento
    Entonces el aviso anterior deja de estar vigente
    Y el nuevo vencimiento podrá generar un único aviso

  Esquema del escenario: Evitar avisos después del cierre
    Dado un compromiso que pasa a estado "<estado>"
    Cuando el proceso programado revisa tareas incluso tras un reintento
    Entonces no queda un recordatorio vigente para ese compromiso
    Ejemplos:
      | estado     |
      | Completada |
      | Cancelada  |

  Escenario: Recuperarse de una interrupción
    Dado un lote de compromisos que quedó parcialmente procesado
    Cuando se recupera la ejecución
    Entonces se generan los avisos faltantes sin duplicar los existentes
```

## HU-15 — Tablero gerencial

La definición provisional de captado es inmueble distinto presentado a evaluación. El gerente debe validarla, junto con filtros y fechas, antes de implementar.

```gherkin
Característica: Medir el avance comercial de adquisición
  Escenario: Contar sin multiplicar por interacciones
    Dado un cliente con dos inmuebles presentados dentro del período
    Y varias llamadas y compromisos registrados para ese cliente
    Cuando el gerente consulta el tablero para el período de alta y presentación
    Entonces ese cliente se cuenta una vez en su etapa actual
    Y se cuentan dos inmuebles captados
    Y no se presentan esos inmuebles como adquiridos por haber sido captados

  Escenario: Aplicar el período acordado
    Dado clientes e inmuebles registrados dentro y fuera del período
    Cuando el gerente filtra el tablero
    Entonces clientes se filtra por fecha de alta e inmuebles por primera presentación
    Y se explica la definición de cada métrica y el período aplicado

  Escenario: Distinguir cero de indisponibilidad
    Dado que la consulta de indicadores falla
    Cuando el gerente abre el tablero
    Entonces se muestra un error con opción de reintentar
    Y no se presentan ceros como si fueran resultados válidos

  Escenario: Proteger indicadores
    Dado un usuario sin permiso gerencial
    Cuando solicita los indicadores mediante la API
    Entonces se deniega el acceso sin devolver conteos
```
