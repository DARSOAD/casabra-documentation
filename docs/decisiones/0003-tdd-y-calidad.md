# ADR 0003 TDD y controles de calidad

- Estado: Propuesto para herramientas y controles; TDD es un requisito del usuario.
- Fecha: 2026-11-03.
- Responsable: líder técnico por asignar.
- Relacionado: todas las historias del módulo; BASE-04, QA-FI-01/02 y tickets funcionales.
- Evidencia de aceptación de herramientas y umbrales: pendiente.

## Contexto y alternativas

Se requiere desarrollar con TDD y cotizarlo explícitamente. Depender solo de pruebas E2E hace más lento localizar errores; usar solo mocks no comprueba la base de datos ni permisos AWS. La propuesta combina pruebas por nivel, con unitarias e integración incluidas en las horas de cada funcionalidad.

## Propuesta

Usar pytest, HTTPX y AnyIO para backend; PostgreSQL temporal mediante Testcontainers y Alembic; botocore Stubber para respuestas AWS simuladas; Vitest, React Testing Library y MSW para interfaz; Playwright Test para flujos web completos; pytest/assertions CDK para infraestructura. Mantener pruebas reales de IAM/S3/KMS y escaneo en staging, más un ensayo Locust y recuperación previo a entrega.

Cada regla inicia con una prueba que falla por el comportamiento ausente, seguida de implementación y refactorización. Una corrección de defecto añade una regresión. Proponer cobertura de ramas del 85 % como control inicial, con todos los casos críticos documentados y sin presentar el porcentaje como garantía de calidad.

## Consecuencias y verificación

La base de pruebas tiene costo compartido; TDD de cada historia ya está en sus horas. QA transversal cubre recorridos entre historias y pruebas de carga/recuperación, sin volver a sumar unitarias. Testcontainers necesita Docker en un job aislado; los tests AWS necesitan recursos y permisos no productivos.

Las PR adjuntan criterios, resultados y reportes. El pipeline bloquea fallos y vulnerabilidades altas/críticas sin mitigación. Staging prueba el artefacto que se promoverá a producción. Los componentes asíncronos de servidor Next.js se cubren mediante E2E.

Fuentes: [FastAPI y pruebas asíncronas](https://fastapi.tiangolo.com/advanced/async-tests/), [Vitest en Next.js](https://nextjs.org/docs/app/guides/testing/vitest), [assertions de AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/testing.html).

## Historial

| Fecha | Cambio | Evidencia |
|---|---|---|
| 2026-11-03 | Propuesta inicial de herramientas para el requisito TDD | Aceptación pendiente |
