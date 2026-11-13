# Criterios mínimos de aceptación — Módulo 1

Referencia: [HU-01 a HU-03](../historias_de_usuario_plan_del_proyecto.md). Estos escenarios proponen criterios verificables para la cotización; requieren validación funcional antes de construirlos.

## HU-01 Registro móvil e intención de venta

```gherkin
Característica: Alta del propietario y presentación inicial del inmueble
  Escenario: Registro válido desde celular
    Dado que una persona no tiene cuenta de propietario
    Cuando registra sus datos obligatorios, acepta el tratamiento de datos e indica los datos iniciales del inmueble
    Entonces el sistema crea una cuenta de propietario y una intención de venta vinculada
    Y confirma la recepción sin afirmar que la compañía adquirió el inmueble

  Escenario: Datos inválidos o cuenta duplicada
    Cuando la persona envía datos inválidos o un identificador de cuenta ya registrado
    Entonces el sistema muestra un error comprensible
    Y no crea otra cuenta ni otra intención de venta
```

## HU-02 Autorización de datos

```gherkin
Característica: Consentimiento informado
  Escenario: Aceptación expresa
    Dado que la persona puede consultar el texto vigente de tratamiento de datos
    Cuando marca voluntariamente la aceptación y continúa
    Entonces el sistema registra la versión del texto, fecha, sujeto y evidencia de la aceptación

  Escenario: Falta de aceptación
    Cuando la persona intenta completar el registro sin aceptar
    Entonces el sistema impide el alta
    Y explica que la autorización es necesaria para continuar con este flujo
```

## HU-03 Verificación de identidad y listas

```gherkin
Característica: Control inicial de cumplimiento
  Escenario: Consulta realizada
    Dado que se completó el registro con autorización
    Cuando el sistema consulta al proveedor de identidad y listas configurado
    Entonces conserva el resultado, fecha, fuente y referencia de la consulta para el oficial de cumplimiento
    Y limita el acceso al resultado a personal autorizado

  Escenario: Coincidencia o verificación inconclusa
    Cuando una consulta presenta coincidencia o no puede concluirse
    Entonces el caso queda pendiente de revisión del oficial de cumplimiento
    Y no se marca automáticamente como aprobado

  Escenario: Proveedor no disponible
    Cuando el proveedor no responde o expira la solicitud
    Entonces el sistema registra el fallo y permite un reintento controlado
    Y no interpreta la ausencia de respuesta como verificación satisfactoria
```

La política de decisión final, fuentes exigidas, falsos positivos, conservación y acciones permitidas mientras el caso está pendiente requieren definición de cumplimiento. Los estados anteriores describen el **control de onboarding**, no los estados de adquisición del módulo 2.
