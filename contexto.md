# Contexto del negocio y ciclo de vida de los inmuebles

## Modelo de negocio

La compañía compra inmuebles a propietarios para luego explotarlos comercialmente. El propietario se registra en la plataforma, da de alta el inmueble y entrega la información necesaria para que la compañía evalúe una posible compra. El inmueble todavía no pertenece a la compañía mientras la adquisición está en evaluación.

## Ciclo de vida

1. **Registro del propietario:** crea su cuenta, registra sus datos y autoriza el tratamiento de su información.
2. **Presentación del inmueble:** registra características y ubicación, y carga los documentos requeridos para evaluar la propiedad.
3. **Adquisición:** la compañía revisa la información, estudia títulos y riesgos, evalúa el inmueble y toma la decisión de compra. La negociación y formalización de la compra hacen parte de esta etapa.
4. **Alta en el inventario de la compañía:** una vez completada exitosamente la adquisición y formalizada la titularidad, el inmueble pasa a ser un activo de la compañía.
5. **Definición del destino:** para cada inmueble adquirido se define una de dos rutas de negocio: **arriendo** o **venta**. La ruta puede contemplar obras o adecuaciones antes de salir al mercado.
6. **Operación de la ruta elegida:**
   - **Arriendo:** preparar y publicar el inmueble, gestionar interesados y solicitudes, seleccionar arrendatarios, formalizar el contrato, entregar el inmueble, administrar pagos y obligaciones, y gestionar renovaciones, novedades y cierre del arriendo. Durante la vigencia, el arrendatario puede consultar su contrato y estado de cuenta, pagar el canon desde la app y descargar sus recibos; el sistema envía recordatorios y el equipo administra la cartera y la mora desde un tablero.
   - **Venta:** preparar y publicar el inmueble, administrar prospectos y actividades del CRM, coordinar visitas, recibir y evaluar ofertas, negociar, formalizar la compraventa y registrar el cierre.

## Épicas principales del producto

El producto se organiza alrededor de tres superépicas:

1. **Adquisición de inmuebles:** desde el registro de la oportunidad por parte del propietario hasta la decisión, negociación, compra y formalización. Un resultado exitoso habilita el ingreso al inventario de la compañía.
2. **Arriendo:** ciclo operativo y comercial de los inmuebles que la compañía ya adquirió y decidió rentar.
3. **Venta:** ciclo comercial de los inmuebles que la compañía ya adquirió y decidió vender. Incluye CRM de prospectos, seguimiento, visitas, ofertas, negociación y cierre.

## Reglas de interpretación para historias y módulos

- Arriendo y venta son rutas posteriores a la adquisición, no servicios de captación o intermediación para inmuebles de terceros.
- En las etapas de arriendo y venta, el actor propietario del activo es la compañía. El propietario original participa durante la adquisición y puede tener acceso a información según el modelo operativo, pero no es quien autoriza la publicación de un inmueble ya comprado.
- La clasificación comercial se realiza sobre un inmueble adquirido y debe permitir iniciar el flujo correspondiente.
- Las obras y adecuaciones pueden ser una etapa previa a la comercialización; no cambian el destino aprobado del inmueble.
- En arriendo, la compañía administra el activo y el arrendatario es un usuario distinto del propietario original. Los pagos digitales se registran contra el contrato y solo se consideran confirmados cuando el proveedor de pago confirma la transacción; los módulos contables consumen esos movimientos para evitar registros duplicados.
- El CRM de ventas apoya el ciclo de venta de los activos de la compañía. El CRM general también puede dar seguimiento a propietarios y oportunidades durante adquisición, sin confundir ambas etapas.

