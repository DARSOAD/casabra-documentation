# Épica de autenticación y gestión de identidad

Desglose de tareas técnicas del módulo de autenticación y usuarios con FastAPI y Next.js, organizado para trasladarlo a un gestor de tareas. El diseño de referencia contempla separación de responsabilidades, seguridad y tipado.

Fuente: [Login epica.docx](Login%20epica.docx). Se conservan las tareas, estimaciones, alternativas tecnológicas y ejemplos del documento. Los ejemplos de jugadores y dueños de cancha pertenecen a esa referencia y requieren adaptación a Casabra.

## Resumen de horas

| Capa | Horas del encabezado original | Suma de las tareas |
|---|---:|---:|
| Backend | 20 h | 36 h |
| Frontend | 28 h | 29 h |
| **Total** | **48 h** | **65 h** |

Los subtotales usados a continuación corresponden a la suma de las tareas. No se modificaron las horas individuales. El documento original no desglosa TDD, pruebas, infraestructura AWS, observabilidad ni despliegue; no se puede determinar si están incluidos en estas horas.

## 1 Backend con FastAPI SQLAlchemy y Pydantic

**Subtotal por tareas: 36 h.** La capa debe ser stateless para escalar horizontalmente.

### BE-AUTH-01 Configuración de modelos de base de datos — 7 h

- Definir el modelo `User` en SQLAlchemy.
- Implementar un enum para `Role`: `OWNER`, `PLAYER`, `ADMIN`.
- Agregar índices en columnas críticas: `email` y `username`.

**Tecnologías de referencia:** SQLAlchemy 2.0 asíncrono y PostgreSQL.

### BE-AUTH-02 Utilidades de seguridad y JWT — 8 h

- Implementar `AuthService` para hashear contraseñas con bcrypt o Argon2.
- Crear funciones para generar `access_token` y `refresh_token` con JWT.
- Configurar las variables de entorno `SECRET_KEY` y `ALGORITHM`.

**Tecnologías de referencia:** Passlib y PyJWT o python-jose.

### BE-AUTH-03 Esquemas de validación con Pydantic v2 — 4 h

- Crear `UserCreateDTO` con validación estricta de email y complejidad de contraseña.
- Crear `UserLoginDTO`.
- Crear `TokenResponseDTO`.
- Crear `UserResponseDTO`, excluyendo `password_hash` de la respuesta.

### BE-AUTH-04 Endpoint de registro de usuario — 4 h

**Endpoint:** `POST /auth/signup`.

- Validar que el email no exista.
- Crear el usuario con el rol seleccionado en el payload, según el ejemplo original.
- Retornar código `201` y los datos del usuario.
- Definir si el registro obliga a iniciar sesión después o entrega un token; el original deja abierta esa decisión.

### BE-AUTH-05 Endpoint de login — 6 h

**Endpoint:** `POST /auth/token`.

- Implementar `OAuth2PasswordRequestForm`.
- Validar las credenciales.
- Retornar un `access_token` con vigencia de 15 minutos y un `refresh_token` con vigencia de 7 días.

### BE-AUTH-06 Dependencia get_current_user — 4 h

- Crear una dependencia reutilizable para proteger rutas.
- Validar la firma del JWT.
- Buscar al usuario en la base de datos; el original menciona Redis como alternativa futura de caché.
- Lanzar `HTTPException` con código `401` si el token es inválido.

### BE-AUTH-07 Recuperación de contraseña — 3 h

**Endpoint 1:** `POST /auth/forgot-password`.

- Generar un token temporal único.
- Simular el envío de email o integrar de forma básica AWS SES o SendGrid.
- Guardar el token en una tabla `PasswordResetTokens` o en Redis.

**Endpoint 2:** `POST /auth/reset-password`.

- Recibir el token y la nueva contraseña.
- Validar la expiración del token.
- Actualizar la contraseña del usuario.

## 2 Frontend con Next.js App Router

**Subtotal por tareas: 29 h.** La referencia especifica Next.js 14 o superior y se enfoca en seguridad del cliente y experiencia de uso.

### FE-AUTH-01 Configuración del cliente HTTP — 4 h

- Crear una instancia de Axios configurada con `baseURL`; el título original contempla Axios o Fetch.
- Configurar un interceptor de solicitudes para inyectar el Bearer Token desde cookies o LocalStorage, según la alternativa que se seleccione.
- Configurar un interceptor de respuestas para manejar `401`: intentar usar el `refresh_token` o redirigir al login.

### FE-AUTH-02 Store de autenticación — 6 h

- Crear el estado global `useAuthStore` mediante Zustand o Context.
- Implementar las acciones `login`, `logout` y `register`.
- Implementar persistencia de sesión y el estado de carga `isLoading`.

### FE-AUTH-03 Formulario de registro — 6 h

- Diseñar la interfaz con Tailwind CSS.
- Implementar un selector visual de rol con el texto del ejemplo: “¿Eres Jugador o Dueño de Cancha?”.
- Validar el formulario con Zod y React Hook Form: coincidencia de contraseñas y formato del email.
- Mostrar mensajes de error.

### FE-AUTH-04 Formulario de login — 4 h

- Crear una interfaz centrada.
- Integrar el formulario con el store de autenticación.
- Redirigir según los roles de referencia: `OWNER` a `/dashboard` y `PLAYER` a `/home`.

### FE-AUTH-05 Protección de rutas — 4 h

- Crear `middleware.ts`.
- Proteger `/dashboard/*` para que solo entren usuarios con rol `OWNER`, según el ejemplo original.
- Proteger `/profile/*` para usuarios autenticados.
- Redirigir a `/login` si no hay un token válido.

### FE-AUTH-06 Flujo de recuperación de contraseña — 5 h

- Crear la página para solicitar el email de recuperación.
- Crear la página para ingresar la nueva contraseña, recibiendo el token como parámetro de la URL.

## 3 Estimación de complejidad del documento original

| Tarea | Complejidad | Notas técnicas de referencia |
|---|---|---|
| Backend core: modelos y JWT | M | Base del módulo; requiere especial cuidado. |
| Endpoints de backend | S | Implementación prevista como rápida con FastAPI. |
| Recuperación de contraseña | M | Requiere lógica de tokens y un servicio de email, aunque sea simulado. |
| Lógica de autenticación del frontend | L | Manejo de refresh tokens y protección de rutas con App Router. |
| Formularios del frontend | S | Se apoya en Tailwind y componentes reutilizables. |

Las categorías S, M y L se conservan del original; el documento no establece una conversión de estas categorías a horas.

## 4 Puntos pendientes de adaptación a Casabra

- Sustituir los roles y pantallas de jugadores/dueños de cancha por los actores del proyecto.
- Definir la asignación de roles internos: el ejemplo permite recibir el rol en el registro, pero Casabra necesita distinguir el alta pública del propietario de la asignación autorizada de roles del equipo.
- Cerrar las alternativas que el original deja abiertas: librerías de JWT, manejo de sesión, almacenamiento de tokens, servicio de email y persistencia de tokens de recuperación.
- Definir criterios de aceptación verificables, incluidos rechazo de credenciales inválidas, acceso sin permiso y expiración de tokens.
- Desglosar el trabajo de TDD, pruebas, configuración AWS, observabilidad y despliegue antes de usar las 65 h como cotización completa.
