# Referencias y calibración

## Procedencia

Método adaptado de la copia local de dstack-claude/skills/estimate-reddo-task y su archivo anchors.md. Se conservan dos referencias útiles, sin el enlace ni las escrituras obligatorias a la página Helper específica de Reddo.

El framework externo ai-execution-modes-framework.md referenciado por la fuente no estaba disponible al adaptar el skill. Los modos del SKILL.md proceden del resumen incluido en la propia skill de origen; no se atribuye contenido al archivo ausente.

## Referencias importadas de Reddo

| ID | Referencia declarada | Forma del trabajo | Magnitud reportada |
|---|---|---|---:|
| A1 | S9.2 / RED-3596 | Conectar un componente UI a un endpoint existente, errores/toast y pruebas básicas; patrón reutilizable, sin dinero/PII | 0,5 d |
| A2 | RED-765 / PR 766 | Consultas sobre modelo nuevo y generación de documento; mapeo, varias unidades de código, pruebas y revisiones; reutiliza servicios y no añade migraciones | Aproximadamente 1 d |

La nota de origen las describe como tareas cerradas con esfuerzo observado. Esta adaptación no verificó el tablero, los registros de tiempo ni el calendario de trabajo original. Presentarlas como **referencias importadas declaradas**, no como mediciones verificadas ni productividad garantizada para otro equipo/proyecto.

A2 no representa un CRUD universal. En otro alcance solo puede ser una analogía parcial y debe decirse. Los servicios AWS nuevos, el setup de ambientes y la recuperación no tienen un ancla equivalente en estas dos referencias: usar **H — hipótesis técnica sin ancla comparable**, hasta contar con evidencia.

## Cálculo y evidencia

Registrar para cada ancla: origen, alcance, qué se reutilizó, pruebas/revisión incluidas, unidad temporal, si es estimación o tiempo real y qué se verificó. Mantener el total viejo como antecedente.

Ejemplo aritmético, no nueva ancla: A1 = 0,5 d; trabajo equivalente a 1–2 A1 en baseline; M1 = ×1,5–2. Rango resultante = 0,75–2 d = 6–16 h bajo la convención de 8 h/d. El factor M1 ya cubre revisión/pruebas sensibles; no volver a aplicarlo al total.

Si se usa H, explicar la base por entregables y verificación. Un día de 8 h es una unidad de cálculo, no evidencia de que una tarea haya tomado ese tiempo.

## Ajustes de contexto

- El asistente puede acelerar implementación, pero la referencia no demuestra un descuento fijo por usar IA.
- Si solo hay documentación, la disponibilidad de login, componentes, pipeline y ambientes es una condición a verificar.
- No reducir M1 a M2 solo porque se reutiliza una pantalla: dinero/PII/permisos siguen requiriendo validación reforzada.
- Sin patrón comparable, mantener el riesgo visible y revisar tras el primer entregable completo.
- Calibrar con datos reales del proyecto separando implementación, validación y esperas; anotar diferencias de alcance.
