# Instrucciones del proyecto Casabra

Antes de crear o modificar una épica, leer `docs/MEMORY.md`, `contexto.md` y las historias correspondientes de `historias_de_usuario_plan_del_proyecto.md`.

La convención solicitada por el usuario es el formato de `epicas y tiempos/login-epica.md`: resumen de horas, secciones por capa, tareas con identificador y horas, actividades concretas, tecnologías y tabla de complejidad. `epicas y tiempos/ficha-inmueble-epica.md` aplica esa convención al alcance actual del módulo 2.

Usar los criterios Gherkin aprobados como referencia funcional. Distinguir reglas confirmadas, supuestos de cotización y decisiones pendientes. No reutilizar ejemplos de jugadores/dueños de cancha del login ni estados antiguos del módulo 2.

Incluir TDD dentro de las horas funcionales; separar pruebas transversales, infraestructura compartida y consumo AWS. Verificar sumas, referencias de historias y coherencia de roles/estados antes de entregar.

## Skill de estimación incluida en el repositorio

- **Nombre:** `estimate-task`, adaptación de `dstack-claude:estimate-reddo-task` para Codex.
- **Descripción:** estimar tareas, historias, épicas y cambios de software para cotizaciones; revisar estimaciones existentes o desglosar trabajo en subtareas estimables, considerando riesgo, reutilización, pruebas y evidencia disponible.
- **Instrucciones:** [skills/estimate-task/SKILL.md](skills/estimate-task/SKILL.md).
- **Referencias de calibración:** [skills/estimate-task/references/calibration.md](skills/estimate-task/references/calibration.md).
- **Metadatos de la skill:** [skills/estimate-task/agents/openai.yaml](skills/estimate-task/agents/openai.yaml).

Al calcular o revisar tiempos, leer y aplicar el `SKILL.md` local y sus referencias. Esta copia versionada es la referencia del proyecto: puede utilizarse leyendo estos archivos, sin depender de una instalación global ni de rutas personales del equipo original. Si también existe una skill global con el mismo nombre, usar la versión de este repositorio para el trabajo de Casabra.

Mantener el formato por capas del login, pero expresar rangos por tarea, modo de riesgo, referencia o hipótesis, multiplicador y motivo. Conservar IDs y desglose aprobados. No tratar estimaciones previas como tiempos reales ni aplicar dos veces el costo de TDD/revisión. La reestimación del módulo 2 y sus cálculos están en `docs/estimaciones/modulo-2-estimacion.json`.

Guardar el resultado en la épica correspondiente y actualizar su cálculo reproducible cuando exista. Verificar sumas, enlaces y correspondencia de IDs antes de entregar. La skill no requiere escribir en Notion ni en otros destinos externos.

## Memoria compartida

Conservar estas preferencias en `docs/MEMORY.md` cuando el usuario acuerde cambios para futuras épicas. Las instrucciones nuevas del usuario prevalecen sobre esta memoria.

Mantener la skill y la memoria en Git junto con la documentación que afecten para que las próximas sesiones y otros integrantes del equipo utilicen las mismas instrucciones.
