# Historias de Usuario del Proyecto

---

## Fase 1: Base

### Módulo 1. Onboarding del cliente
* **HU-01:** **COMO** propietario, **QUIERO** registrarme desde mi celular e indicar qué inmueble quiero venderle a la compañía, **PARA** iniciar el proceso de evaluación de compra sin desplazarme ni llenar papeles.
* **HU-02:** **COMO** propietario, **QUIERO** aceptar de forma clara cómo se usarán mis datos personales, **PARA** tener certeza de que mi información está protegida y de que mi autorización es consciente.
* **HU-03:** **COMO** oficial de cumplimiento, **QUIERO** que el sistema verifique la identidad del cliente y consulte listas restrictivas al registrarse, **PARA** prevenir riesgos de lavado de activos.


### Módulo 2. Adquisición de inmuebles

[Épica técnica y estimación](epicas%20y%20tiempos/ficha-inmueble-epica.md) · [Criterios mínimos de aceptación en Gherkin](epicas%20y%20tiempos/adquisicion-inmuebles-criterios-aceptacion.md).

* **HU-04:** **COMO** propietario, **QUIERO** subir los documentos del inmueble y los míos (escritura, certificado de tradición y libertad, cédula) desde la app, **PARA** no entregar los mismos papeles varias veces.
* **HU-05:** **COMO** asesor comercial, **QUIERO** ver la ficha de cada inmueble con sus datos, fotos y documentos legales, **PARA** tener un expediente completo en un solo lugar.
* **HU-06:** **COMO** abogado de la empresa, **QUIERO** registrar el estudio de títulos y las alertas (gravámenes, embargos, falta de licencias), **PARA** decidir si el inmueble se puede tomar antes de invertir.
* **HU-07:** **COMO** gerente, **QUIERO** asignar a cada inmueble adquirido la ruta de arriendo o venta y definir si requiere adecuaciones, **PARA** que pase al flujo operativo correspondiente.
* **HU-08:** **COMO** propietario, **QUIERO** ver en qué paso va mi solicitud, **PARA** saber qué falta y cuándo recibiré respuesta.

### Cumplimiento (transversal)

* **HU-09:** **COMO** oficial de cumplimiento, **QUIERO** registrar el origen de los fondos y marcar operaciones inusuales, **PARA** poder reportarlas a tiempo si es necesario.
* **HU-10:** **COMO** administrador, **QUIERO** que cada autorización, firma y verificación quede guardada con fecha y usuario, **PARA** demostrar el cumplimiento ante una auditoría.
* **HU-11:** **COMO** titular de datos, **QUIERO** poder consultar, corregir o pedir la eliminación de mis datos, **PARA** ejercer mis derechos sin trámites complicados.

### Módulo 5. CRM
* **HU-12:** **COMO** asesor comercial, **QUIERO** ver en una ficha el estado de cada cliente (contactado, en evaluación, contrato firmado), **PARA** saber a quién darle seguimiento hoy.
* **HU-13:** **COMO** asesor comercial, **QUIERO** registrar llamadas, visitas y compromisos con el cliente, **PARA** que cualquier compañero pueda continuar la conversación sin perder contexto.
* **HU-14:** **COMO** asesor comercial, **QUIERO** recibir recordatorios de seguimientos pendientes, **PARA** no perder oportunidades por olvido.
* **HU-15:** **COMO** gerente, **QUIERO** un tablero con clientes por etapa e inmuebles captados, **PARA** medir el avance comercial y decidir dónde enfocar al equipo.

---

## Fase 2: Operación

### Módulo 6. Proyectos de obra
* **HU-16:** **COMO** jefe de obra, **QUIERO** crear un proyecto con presupuesto, cronograma y responsables, **PARA** planear la remodelación antes de empezar.
* **HU-17:** **COMO** jefe de obra, **QUIERO** subir fotos y registrar el avance semanal desde el sitio, **PARA** mantener el proyecto actualizado sin trabajo doble en oficina.
* **HU-18:** **COMO** jefe de obra, **QUIERO** adjuntar las licencias y permisos del proyecto, **PARA** tener a la mano lo exigido si llega una inspección.
* **HU-19:** **COMO** gerente, **QUIERO** ver qué proyectos van retrasados o sobre presupuesto, **PARA** intervenir a tiempo.

### Módulo 7. Contratos y firma electrónica
* **HU-20:** **COMO** abogado de la empresa, **QUIERO** manejar plantillas de contrato para adquirir, arrendar y vender inmuebles, **PARA** que cada operación tenga un estándar legal consistente.
* **HU-21:** **COMO** contraparte de una operación, **QUIERO** revisar y firmar el contrato correspondiente desde el celular, **PARA** formalizar la operación sin ir a una oficina.
* **HU-22:** **COMO** administrador, **QUIERO** que los contratos firmados queden archivados con su trazabilidad, **PARA** poder probar su validez si hay un conflicto.

### Módulo 8. Arriendo de inmuebles adquiridos
* **HU-34:** **COMO** gerente de activos, **QUIERO** asignar a arriendo un inmueble cuya adquisición ya fue completada, **PARA** iniciar su ciclo de explotación como activo de la compañía.
* **HU-35:** **COMO** administrador de inmuebles, **QUIERO** registrar el estado de alistamiento, adecuaciones, disponibilidad, canon objetivo y condiciones del inmueble, **PARA** prepararlo para su publicación.
* **HU-36:** **COMO** asesor de arriendos, **QUIERO** administrar la ficha comercial, fotografías, anuncios y canales de publicación de cada inmueble disponible, **PARA** atraer interesados y mantener actualizada la oferta.
* **HU-37:** **COMO** asesor de arriendos, **QUIERO** registrar interesados, solicitudes, documentos, visitas y resultado de la evaluación de cada candidato, **PARA** dar seguimiento y recomendar un arrendatario.
* **HU-38:** **COMO** administrador, **QUIERO** generar y formalizar el contrato de arrendamiento aprobado, **PARA** dejar claras las condiciones, fechas, obligaciones y garantías antes de entregar el inmueble.
* **HU-39:** **COMO** administrador de inmuebles, **QUIERO** registrar el inventario, la entrega, las novedades y la devolución del inmueble, **PARA** mantener trazabilidad de su estado durante todo el arrendamiento.
* **HU-46:** **COMO** administrador, **QUIERO** controlar cánones, pagos, mora, reajustes, vencimientos, renovaciones y terminaciones, **PARA** gestionar el contrato durante toda su vigencia.
* **HU-47:** **COMO** gerente de activos, **QUIERO** consultar ocupación, ingresos, vacancia y estado contractual de los inmuebles en arriendo, **PARA** medir el desempeño de esta línea de negocio.

### Módulo 9. Venta de inmuebles adquiridos
* **HU-40:** **COMO** gerente de activos, **QUIERO** asignar a venta un inmueble cuya adquisición ya fue completada y registrar el precio objetivo, **PARA** iniciar su proceso de comercialización.
* **HU-41:** **COMO** asesor de ventas, **QUIERO** preparar la ficha comercial con descripción, fotografías, precio, documentos disponibles y estado de alistamiento, **PARA** publicar una oferta completa y consistente.
* **HU-42:** **COMO** asesor de ventas, **QUIERO** publicar y actualizar el inmueble en los canales comerciales definidos, **PARA** generar oportunidades y mantener vigente la información.
* **HU-43:** **COMO** asesor de ventas, **QUIERO** registrar cada prospecto, su origen, intereses, interacciones, tareas y próximos seguimientos en el CRM, **PARA** gestionar el embudo comercial sin perder oportunidades.
* **HU-44:** **COMO** asesor de ventas, **QUIERO** coordinar visitas y registrar comentarios y nivel de interés de cada prospecto, **PARA** dar seguimiento informado a cada oportunidad.
* **HU-45:** **COMO** gerente comercial, **QUIERO** registrar y comparar ofertas, contraofertas y aprobaciones de precio, **PARA** negociar dentro de los parámetros autorizados.
* **HU-48:** **COMO** abogado, **QUIERO** preparar y revisar los documentos de compraventa y verificar las condiciones para el cierre, **PARA** formalizar correctamente la transacción.
* **HU-49:** **COMO** administrador, **QUIERO** registrar firma, pago, entrega y cierre de la venta, **PARA** actualizar el inventario y conservar la trazabilidad del negocio.
* **HU-50:** **COMO** gerente comercial, **QUIERO** consultar el embudo, tiempos de cierre, ofertas y ventas realizadas, **PARA** evaluar los resultados de la línea de venta.

---

## Fase 3: Crecimiento

### Módulo 10. Pagos y utilidades
* **HU-27:** **COMO** contador, **QUIERO** registrar los costos y los ingresos de cada inmueble o proyecto, **PARA** conocer la rentabilidad real de cada negocio.
* **HU-28:** **COMO** gerente, **QUIERO** calcular y registrar el retorno y la rentabilidad de cada inmueble según sus costos e ingresos, **PARA** evaluar el resultado de cada ruta de negocio.
* **HU-29:** **COMO** contador, **QUIERO** generar facturas y soportes para la DIAN desde el mismo sistema, **PARA** no digitar la información dos veces.

### Módulo 11. Portal del cliente
* **HU-30:** **COMO** propietario, **QUIERO** ver el avance de la obra, mis documentos y mis resultados en un panel propio, **PARA** confiar en que mi inmueble está bien gestionado sin tener que llamar.
* **HU-31:** **COMO** propietario, **QUIERO** recibir notificaciones cuando haya un hito importante (obra terminada, inmueble arrendado o vendido, pago realizado), **PARA** estar informado sin tener que preguntar.
* **HU-32:** **COMO** gerente, **QUIERO** reportes consolidados de ingresos, ocupación y rentabilidad, **PARA** tomar decisiones de inversión con datos.

---

## Administración (transversal)
* **HU-33:** **COMO** administrador del sistema, **QUIERO** asignar permisos por rol (asesor, abogado, contador, gerente, cliente), **PARA** que cada persona vea solo la información que necesita.
