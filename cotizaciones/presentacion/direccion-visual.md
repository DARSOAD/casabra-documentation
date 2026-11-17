# Dirección visual — presentación CASABRA

## Criterios de la guía

El PDF de referencia presenta UI/UX Pro Max, Taste Skill, Frontend Design, Impeccable y Emil Design Eng, junto con herramientas complementarias de auditoría y navegador. No figuran en el catálogo de skills disponibles de esta sesión; se toma el PDF como guía de diseño, sin afirmar que se hayan instalado o ejecutado. Sus aportes aplicables son: definir pocos tokens, evitar composiciones genéricas repetidas, jerarquía clara, contraste, revisión responsive, movimiento breve y respeto a `prefers-reduced-motion`.

La referencia local de Sites para presentaciones propone una secuencia narrativa, demostraciones concretas y contenido fiel a las fuentes. Los datos de muestra deben identificarse como ilustrativos.

## Concepto

**Una plataforma, un recorrido.** Una presentación editorial sobria y contemporánea: tipografía amplia, reglas finas, numeración y espacios generosos. El mapa presenta una evolución legible de arriba abajo, desde el alcance inicial hasta un posible core propio. Las áreas del producto se ven como partes de un mismo sistema, no como productos o propuestas independientes.

## Marca y tokens

El único recurso de marca suministrado es `disenos/casabra-logo-provisional-negro.png`: wordmark negro sobre blanco con espacio blanco propio. Usarlo sin alterar ni recortar, con ancho proporcional y `height: auto`; mostrarlo sobre fondo blanco. No afirmar que los colores adicionales sean oficiales: son decisiones de presentación.

- Tinta `#17201d`: texto principal y superficies oscuras.
- Papel `#f6f5ef`: fondo cálido y claro.
- Blanco `#ffffff`: superficies y marca.
- Verde bosque `#285c4a`: acento, enlaces y elementos activos.
- Salvia `#dce8df`: énfasis suave y estados de fase base.
- Ámbar `#a25c28`: indicador de opción, con texto oscuro para asegurar contraste.
- Línea `#cbd2c9`: divisores y límites.

Tipografía sin red: Georgia para títulos editoriales; `Segoe UI`, sans-serif para lectura e interfaz. Tamaños fluidos con `clamp`, interlineado cómodo y ancho de texto limitado. Evitar animación decorativa larga y fotografías genéricas.

## Composición y alcance

- Cabecera limpia con logo y dos pestañas accesibles: **Visión y propuesta inicial** y **Mapa de evolución**.
- Primera pestaña: portada con titular, intención de la plataforma y una visualización arquitectónica abstracta; progresión hacia base de Onboarding, CRM y Adquisición y las condiciones comerciales procedentes de la fuente.
- Segunda pestaña: mapa vertical, numerado y con conectores; diferenciar base, opciones, dependencia externa y futuro mediante etiquetas y texto, además de color. Fase 2 solo describe las opciones señaladas en el documento comercial; fase 3 muestra el concepto de core propio.
- Los prototipos interactivos se limitan a la base y al intercambio conceptual con Leancore. En diálogos, todos comparten barra, navegación y estilos de una misma plataforma. Son demostraciones con datos ficticios, no funcionalidades existentes ni una integración ya implementada.
- Preferir trazos, bloques tipográficos y maquetas de interfaz a una cuadrícula continua de tarjetas. La navegación debe permitir volver al mapa sin perder contexto.

## Accesibilidad y adaptación

Usar HTML semántico, pestañas con estado y control por teclado, diálogo accesible con foco visible, etiquetas en controles, contraste mínimo AA y texto que no dependa solo del color. Evitar efectos necesarios para entender el contenido; respetar movimiento reducido. En móvil, apilar columnas y convertir el mapa a un eje lineal sin desplazamiento horizontal; verificar 375, 768, 1024 y 1440 px. La presentación debe funcionar localmente sin fuentes ni dependencias de red.
