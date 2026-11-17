# Presentación local de Casabra

Abra `index.html` directamente en un navegador moderno. Funciona mediante `file://`, sin instalación, servidor, conexión a internet, CDN, tipografías remotas ni dependencias externas. Entregable local: no se ha publicado.

Extraiga `CASABRA-presentacion.zip` en una carpeta y abra `index.html`. El paquete contiene la presentación, el logotipo y sus notas. El [inventario de fuentes](fuentes-propuesta.md) resume el PDF comercial y los criterios del proyecto. Sus enlaces a los originales y a la evidencia de trabajo corresponden a la copia del repositorio.

## Uso

- Las pestañas superiores separan la propuesta inicial del mapa de evolución. Se pueden recorrer con las flechas izquierda/derecha y con Inicio/Fin.
- Cada módulo abre un panel amplio. `Escape` o **Cerrar** devuelve al botón de origen y conserva el contexto y la posición de la página.
- **Ir al recorrido interactivo** lleva al prototipo del módulo base.
- **Reiniciar demo** devuelve los datos ficticios al inicio. Los cambios viven en memoria mientras esta página permanece abierta; al recargar se reinician. No se utiliza almacenamiento local ni se envía información.
- La selección de módulos de fase 2 es un escenario de conversación; no recalcula precios ni representa contratación. Esas vistas no contienen prototipos.

## Recorrido sugerido

1. En Onboarding, registre a **Laura Méndez**, acepte la autorización de muestra y simule un resultado de identidad. Sin autorización se impide el alta; un proveedor no disponible no equivale a verificación satisfactoria.
2. Continúe en CRM. Cambie la etapa comercial, registre una llamada y programe un compromiso de **Santiago Ríos**. La etapa CRM no cambia el estado del inmueble.
3. Continúe en Adquisición con **CAS-024 · Apartamento Cedro, Bogotá**. Como Laura, complete los requisitos de muestra. Cambie a **Valentina Ruiz** para registrar el estudio jurídico, a Santiago para enviar la propuesta y a Laura para aceptarla. El resultado es **En proceso de compra**.
4. Cambie a Valentina para confirmar la compra completada. Solo entonces el estado es **Adquirido** y **Camila Torres**, gerente, puede asignar Arriendo o Venta e indicar adecuaciones.
5. En la conexión conceptual con **LeanCore**, simule un intercambio, un caso pendiente o un proveedor no disponible. La respuesta externa no cambia el estado de adquisición ni constituye aprobación de crédito.

## Fuentes y límites

- Fuente comercial: `../Cotización CASABRA V2.pdf`, de 17/11/2026. Inventario auditado: [fuentes-propuesta.md](fuentes-propuesta.md). Se reproducen sus módulos, horas estimadas y condiciones; no se inventa una tarifa ni un precio de desarrollo en COP.
- Fase 1: 600 h Onboarding + 460 h CRM + 400 h Adquisición = **1.460 h**. Fase 2: 520 + 430 + 900 + 820 + 500 + 730 + 100 = **4.000 h**. Son sumas de estimaciones, no duración de calendario. Fase 3 no tiene horas ni presupuesto definidos en el PDF.
- Pagos sobre el valor acordado por módulo: **40 / 20 / 20 / 20 %**, con entregas al 50 %, 75 % y 100 %; acumulados 40 / 60 / 80 / 100 %. Garantía y soporte bajo las condiciones acordadas, sin inventar meses ni SLA.
- LeanCore: cargo mínimo mensual **USD 1.500**; administración de cada crédito **USD 0,30**. El PDF no define la periodicidad del cargo por crédito ni su relación con el mínimo. **USD 18.000/año** es únicamente 1.500 × 12; no representa ahorro neto. El costo de un core propio incluye desarrollo, infraestructura, operación, mantenimiento, soporte y controles, todavía por estimar.
- La conexión se muestra en la arquitectura inicial por solicitud del usuario; sus **100 h siguen cotizadas en fase 2**. Adelantarla exige acordar alcance y cronograma. No existen endpoints, llamadas de red ni credenciales.
- La secuencia de adquisición se basa en los [criterios aprobados](../../epicas%20y%20tiempos/adquisicion-inmuebles-criterios-aceptacion.md), [contexto](../../contexto.md) y [memoria](../../docs/MEMORY.md). Los [criterios de onboarding](../../epicas%20y%20tiempos/onboarding-cliente-criterios-aceptacion.md) y [CRM](../../epicas%20y%20tiempos/crm-criterios-aceptacion.md) son propuestas pendientes de validación; no se presentan como aprobados.
- Los nombres, correo `example.com`, inmueble, oferta de **COP 420.000.000**, documentos, estudios y respuestas del proveedor son datos de demostración. No son una lista definitiva de requisitos ni un concepto jurídico o financiero.
- Las dependencias de fase 2 y el recorrido planificación → migración → validación son explicaciones propuestas para conversar sobre implementación; deben validarse en el levantamiento. Consumo AWS y otros servicios se consideran por separado, sin asignar un importe que no aparece en el PDF.
- Logo provisional local: `assets/casabra-logo-provisional-negro.png`, copia proporcional del recurso de `disenos`.

## Verificación

El [informe de verificación](qa/RESULTADOS.md) recoge los resultados del navegador y de Node.js. La [validación visual](validacion-visual.md) describe la inspección de escritorio y móvil. Los scripts y las capturas de trabajo están en la copia del repositorio.

Para repetir las pruebas desde la raíz del repositorio, use Node.js y Python con Playwright y Chrome instalados.

```powershell
node --test cotizaciones/presentacion/demo.test.js
node --check cotizaciones/presentacion/app.js
python cotizaciones/presentacion/qa/probe_browser.py --flows
python cotizaciones/presentacion/qa/probe_browser.py
```
