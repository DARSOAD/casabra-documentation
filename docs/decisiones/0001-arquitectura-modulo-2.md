# ADR 0001 Arquitectura del módulo 2

- Estado: Propuesto.
- Fecha: 2026-11-03.
- Responsable: líder técnico por asignar.
- Relacionado: HU-04 a HU-08; AN-FI-01, BE-FI-01/03/04 y BASE-01/02/03.
- Evidencia de aceptación: pendiente.

## Contexto

Se requiere un expediente relacional con permisos, documentos, revisiones jurídicas y clasificación. El usuario establece FastAPI y servicios AWS, con PostgreSQL o MySQL en RDS. La referencia de login usa Next.js, pero este repositorio no contiene evidencia de implementación.

## Alternativas

PostgreSQL y MySQL cubren la persistencia relacional. Mantener ambos aumenta pruebas y migraciones sin un requisito que lo justifique. Para ejecución se consideran contenedores ECS Fargate y Lambda con adaptación de FastAPI; la segunda opción exige revisar conexiones RDS y límites de ejecución. La selección no presume que una sea universalmente más barata.

## Propuesta

Usar PostgreSQL en RDS, SQLAlchemy asíncrono y Alembic. Ejecutar API FastAPI, Next.js y worker en ECS Fargate, con ECR, ALB y ACM. Mantener RDS y procesos en redes privadas. Gestionar infraestructura con CDK Python/CloudFormation y entregar mediante CodeBuild/CodePipeline. Reutilizar login existente, adaptado a los roles de Casabra sin permitir autoasignación de roles internos.

La API y el frontend comparten contratos versionados. Las autorizaciones se verifican en el servidor; la UI no es una barrera de seguridad. La implementación inicialmente admite una empresa y un propietario principal por inmueble.

## Consecuencias y verificación

Se usa un solo motor y una ruta de despliegue. ECS, balanceador, RDS y conectividad tienen costo recurrente incluso con poco tráfico. Antes de implementar se fijan región, versiones soportadas, conectividad y capacidad por ambiente. Cambiar a aplicación móvil nativa o multiempresa requiere nueva estimación.

Probar migraciones contra PostgreSQL real, despliegue en staging y aislamiento de datos/secretos. La base compartida se cobra una sola vez; solo se descuenta cuando existe evidencia funcional. Los totales y dependencias se mantienen en la [épica](../../epicas%20y%20tiempos/ficha-inmueble-epica.md).

## Historial

| Fecha | Cambio | Evidencia |
|---|---|---|
| 2026-11-03 | Propuesta inicial para estimación | Aceptación pendiente |
| 2026-11-03 | Referencias alineadas a las historias vigentes y al nuevo desglose de tareas | Arquitectura todavía propuesta |
