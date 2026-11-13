# Módulo 6. Proyectos de obra — criterios propuestos

**Estado: pendientes de validación; no son criterios aprobados.** Se derivan de HU-16 a HU-19 de las [historias](../historias_de_usuario_plan_del_proyecto.md) y de los supuestos acotados en la [épica](proyectos-obra-epica.md). Las reglas de adquisición aprobadas conservan prioridad. No se convierten escenarios mecánicamente en horas.

## HU-16 — Planificar una obra

```gherkin
Característica: Planificar obras de activos adquiridos
  Escenario: Crear un proyecto elegible
    Dado un jefe de obra autorizado y un inmueble Adquirido
    Y el inmueble tiene ruta definida y requiere adecuaciones
    Cuando crea un proyecto con partidas, fechas y responsables internos válidos
    Entonces el proyecto queda Planificado y vinculado al inmueble
    Y el presupuesto es la suma de cantidades por costos unitarios
    Y no cambia la ruta ni el estado de adquisición

  Escenario: Rechazar inmueble no adquirido
    Dado un inmueble en proceso de compra
    Cuando se intenta crear su proyecto de obra
    Entonces la operación se rechaza sin crear el proyecto

  Escenario: Conservar la línea base
    Dado un proyecto Planificado con presupuesto y cronograma válidos
    Cuando el jefe autorizado lo inicia
    Entonces queda En ejecución con presupuesto y fechas base conservados
    Y una reprogramación operativa posterior no sobrescribe esa referencia

  Esquema del escenario: Validar planificación
    Dado un jefe de obra autorizado
    Cuando intenta guardar un proyecto con "<problema>"
    Entonces se informa el error sin persistir cambios parciales
    Ejemplos:
      | problema                             |
      | fecha final anterior al inicio       |
      | importe negativo                     |
      | responsable no autorizado            |
      | otro proyecto activo en ese inmueble |

  Escenario: Finalizar obra sin publicar el inmueble
    Dado un proyecto En ejecución con todas sus actividades base al 100%
    Cuando el jefe autorizado lo finaliza
    Entonces se registra fecha real y autor del cierre
    Y no se publica el inmueble ni se modifica su ruta automáticamente
```

## HU-17 — Avance y fotografías

```gherkin
Característica: Registrar avance semanal desde sitio
  Escenario: Registrar un avance válido
    Dado un jefe asignado al proyecto y una conexión disponible
    Cuando registra la semana, comentario y avance de actividades entre 0 y 100
    Entonces se conserva el reporte con fecha y autor
    Y el avance global es el promedio simple de las actividades base

  Escenario: Carga interrumpida sin duplicación
    Dado un reporte con varias fotos y una carga que falla
    Cuando el usuario reintenta el archivo fallido y confirma el reporte
    Entonces no se duplican el reporte ni los archivos ya confirmados
    Y las fotos solo pueden consultarse tras validación y análisis aceptados

  Escenario: Corregir un reporte semanal
    Dado un reporte existente para la semana
    Cuando el jefe registra una corrección válida
    Entonces queda una versión vigente conservando el historial y autor
    Y un envío con versión obsoleta informa conflicto sin sobrescribirla

  Escenario: Rechazar porcentaje inválido
    Dado un jefe autorizado
    Cuando registra un porcentaje fuera de 0 a 100
    Entonces se rechaza el cambio sin alterar el avance anterior
```

## HU-18 — Licencias y permisos

```gherkin
Característica: Conservar documentación privada de obra
  Escenario: Adjuntar y consultar un permiso
    Dado un jefe asignado al proyecto
    Cuando carga un PDF permitido y el análisis lo acepta
    Entonces el permiso queda vinculado al proyecto con fecha y autor
    Y un usuario autorizado puede obtener una descarga temporal
    Y archivarlo no certifica su validez jurídica

  Escenario: Reemplazar un documento
    Dado una licencia previamente archivada
    Cuando se carga una nueva versión válida
    Entonces la versión anterior se conserva con su historial

  Esquema del escenario: Bloquear archivos no habilitados
    Dado un archivo de obra con estado "<estado>"
    Cuando se solicita su descarga
    Entonces no se entrega acceso al contenido
    Ejemplos:
      | estado              |
      | Pendiente de análisis |
      | Rechazado           |

  Escenario: Rechazar acceso fuera del proyecto
    Dado otro jefe no asignado o un propietario original
    Cuando solicita el documento por su identificador
    Entonces se deniega el acceso sin generar una URL de descarga
```

## HU-19 — Atrasos y sobrecostos

Los gastos manuales, línea base, promedio simple y definiciones de atraso son supuestos pendientes de aprobación.

```gherkin
Característica: Detectar desviaciones con datos trazables
  Escenario: Identificar atraso confirmado
    Dado una actividad cuya fecha final base ya pasó
    Y su último avance conocido es menor al 100%
    Cuando el gerente consulta el tablero
    Entonces el proyecto se identifica como atrasado
    Y se muestra la fecha del reporte usado para la evaluación

  Escenario: No inventar avance ni costos
    Dado un proyecto sin reportes de avance ni gastos registrados
    Cuando el gerente consulta sus indicadores
    Entonces se muestra Avance sin confirmar y Sin costos registrados
    Y no se afirma que el costo real sea cero ni que la obra esté al día

  Escenario: Calcular sobrecosto sin duplicar registros
    Dado un presupuesto base de 1000 COP y un gasto vigente de 1200 COP
    Y múltiples fotos y reportes del proyecto
    Cuando el gerente consulta el tablero
    Entonces ve 200 COP de sobrecosto y 20% de desviación
    Y reenviar el mismo gasto no altera esos resultados

  Escenario: Anular un gasto con trazabilidad
    Dado un gasto registrado por error
    Cuando el jefe autorizado lo anula con un motivo
    Entonces se conserva la entrada y su anulación
    Y el gasto deja de sumar al costo registrado

  Escenario: Presupuesto cero
    Dado un proyecto con presupuesto base cero y gasto registrado positivo
    Cuando se calculan las desviaciones
    Entonces se muestra el sobrecosto monetario
    Y la desviación porcentual se muestra como No aplica

  Escenario: Proteger el tablero gerencial
    Dado un usuario sin permiso gerencial
    Cuando solicita los indicadores globales mediante la API
    Entonces se deniega el acceso
```
