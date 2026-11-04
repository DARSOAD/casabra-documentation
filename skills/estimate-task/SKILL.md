---
name: estimate-task
description: Use when estimating software tasks, stories, epics or pull requests for a quote, reviewing an existing time estimate, or splitting requested work into estimable subtasks.
---

# Estimate Task

Adaptación para Codex de estimate-reddo-task. Estimar el esfuerzo de comprobar que la solución funciona, además de escribirla. Respetar alcance, idioma y formato del proyecto.

## A Elegir el trabajo necesario

- Si hay subtareas claras o se pide solo reestimar, conservar IDs y estructura: pasar a B.
- Si hay una propuesta cruda y se solicita desglose, agrupar por entregables coherentes, normalmente 3–6 grupos; mantener el detalle existente debajo. No cambiar un desglose aprobado para cumplir ese número.
- Cada nueva subtarea incluye contexto/fuente, acciones concretas, componentes afectados, exclusiones, casos difíciles, criterios verificables y QA. Nombrar archivos reales solo tras inspeccionarlos; marcar rutas futuras como propuestas.
- Leer contexto, criterios, memoria y evidencia técnica disponibles. Guardar en el archivo solicitado. No contiene un destino Notion predeterminado: un documento externo requiere destino autorizado y lectura previa para preservar su contenido.

## B Estimar

1. Leer [referencias de calibración](references/calibration.md). Preferir 1–3 tareas cerradas comparables del proyecto. Distinguir horas reales registradas, estimación de ticket cerrado, referencia importada y juicio técnico. No presentar una estimación anterior como tiempo real. Si faltan anclas, declarar confianza baja y estimar provisionalmente; no inventarlas ni bloquear el trabajo.
2. Clasificar cada tarea por el trabajo que realiza:
   - **M0:** análisis/decisión, sin implementación.
   - **M1:** dinero, autenticación, permisos, datos personales, migraciones, acciones irreversibles o ausencia de patrón técnico comprobado.
   - **M2:** patrón implementado y comprobado, sin las condiciones anteriores.
   - **M3:** automatización repetible con controles ya probados; una automatización nueva/sensible sigue siendo M1.
3. Valorar reutilización real, alcance del cambio, corrección/paridad, pruebas, reversibilidad y novedad. Descontar reutilización en pasos posteriores solo si se identifica qué tarea previa aporta el patrón. Una épica escrita no demuestra código existente.
4. Definir unidad: horas-persona y horas por día productivo. Si falta acuerdo, usar 8 h/d como convención explícita, no como dato histórico ni jornada facturable garantizada.
5. Partir de un rango de unidades comparables al ancla. En baseline M2, M1 aplica ×1,5–2 por diseño, revisión detallada y validación de casos positivos/negativos. Aplicarlo **una sola vez**. No multiplicar horas que ya incluyan ese trabajo: reconstruir la base o indicar factor ya incorporado. M0/M3 se estiman por sus acciones, sin reducción automática.
6. Incluir TDD, pruebas propias y revisión dentro de cada tarea. Separar setup compartido y pruebas transversales para no duplicarlos. Herramientas de QA acordes al stack; no imponer Cypress/Jest.
7. Sumar mínimos/máximos y mostrar buffers con condición y dueño del riesgo. Si una discrepancia concreta de contrato/paridad podría requerir una corrección acotada, considerar +0,5 d solo bajo esa condición. No sumar reservas genéricas encima del multiplicador por la misma incertidumbre.

## Contrato de salida

Una fila por tarea: **ID · rango h y d · modo · ancla y ×ref · motivo/casos de verificación**. Aclarar si ×ref es antes o después del factor M1 y usar una fórmula reproducible. Mostrar subtotales, total, contingencias y confianza. Comparar con la estimación anterior sin prometer ahorro ni forzar rebajas.

Si el usuario conserva encabezados con horas, actualizarlos junto con las tablas. Mantener el alcance aprobado. Separar desarrollo, infraestructura compartida, consumo de servicios y esperas. El calendario depende de capacidad y dependencias, no de dividir el esfuerzo por personas sin más.

Validar sumas, unidades, enlaces y correspondencia de IDs antes de entregar. Registrar horas reales al terminar para recalibrar futuras estimaciones; el rango provisional no tiene significado de percentil estadístico.
