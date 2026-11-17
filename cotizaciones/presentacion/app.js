'use strict';

function createDemo() {
  return { registered: false, name: 'Laura Méndez', email: 'laura.mendez@example.com', city: 'Bogotá', property: 'CAS-024 · Apartamento Cedro', consent: null, identity: 'Sin consultar', crmStage: 'Nuevo contacto', activities: [], commitments: [], acquisition: 'Documentación faltante', study: false, route: null, works: false, history: [], external: 'Sin enviar', externalReference: null };
}

function advance(demo, action, payload = {}) {
  const record = (before, after, actor, detail) => demo.history.push({ before, after, actor, detail, date: new Date().toLocaleString('es-CO', { timeZone: 'America/Bogota' }) });
  const requireState = (state) => { if (demo.acquisition !== state) throw new Error(`Esta acción requiere el estado ${state}.`); };
  const requireRole = (role, label) => { if (payload.role !== role) throw new Error(`Esta acción corresponde a ${label}.`); };
  if (action === 'register') {
    if (!payload.consent) throw new Error('La autorización de tratamiento de datos es necesaria para continuar.');
    if (demo.registered) throw new Error('Laura ya tiene un registro; no se creará un duplicado.');
    demo.registered = true;
    demo.name = payload.name || demo.name;
    demo.email = payload.email || demo.email;
    demo.consent = { version: 'DEMO-01', date: new Date().toISOString(), subject: demo.name, evidence: 'Aceptación expresa en demostración local' };
    record('Sin registro', 'Registro recibido', demo.name, 'Cuenta e intención de venta vinculadas; el inmueble aún no pertenece a Casabra.');
  } else if (action === 'identity') {
    if (!demo.registered) throw new Error('Complete primero el registro.');
    demo.identity = payload.status;
  } else if (action === 'crmStage') {
    if (!demo.registered) throw new Error('Complete primero el registro de Laura.');
    const before = demo.crmStage;
    demo.crmStage = payload.stage;
    record(before, payload.stage, 'Santiago Ríos', 'Cambio de etapa comercial; no modifica el estado de adquisición.');
  } else if (action === 'activity') {
    if (!payload.note?.trim()) throw new Error('Indique el resultado de la interacción.');
    demo.activities.push({ type: payload.type, note: payload.note.trim(), author: 'Santiago Ríos', date: new Date().toLocaleDateString('es-CO') });
  } else if (action === 'commitment') {
    if (!payload.title?.trim() || !payload.date) throw new Error('Indique el compromiso y su fecha.');
    demo.commitments.push({ title: payload.title.trim(), date: payload.date, owner: 'Santiago Ríos', completed: false });
  } else if (action === 'completeCommitment') {
    if (demo.commitments[payload.index]) demo.commitments[payload.index].completed = true;
  } else if (action === 'documents') {
    if (!demo.registered) throw new Error('Complete primero el registro.');
    requireState('Documentación faltante');
    requireRole('propietaria', 'Laura, la propietaria');
    demo.acquisition = 'En estudio';
    record('Documentación faltante', demo.acquisition, demo.name, 'Requisitos de muestra completados; la lista definitiva se configura en el levantamiento.');
  } else if (action === 'study') {
    requireState('En estudio');
    requireRole('abogada', 'Valentina, la abogada');
    demo.study = true;
    record('En estudio', 'En estudio', 'Valentina Ruiz', 'Estudio jurídico ilustrativo registrado con conclusión y alertas de muestra.');
  } else if (action === 'offer') {
    requireState('En estudio');
    requireRole('asesor', 'Santiago, el asesor');
    demo.acquisition = 'Propuesta enviada';
    record('En estudio', demo.acquisition, 'Santiago Ríos', 'Oferta de demostración: COP 420.000.000; no es un valor de la cotización.');
  } else if (action === 'rejectCompany') {
    requireState('En estudio');
    requireRole('asesor', 'Santiago, el asesor');
    if (!payload.reason?.trim()) throw new Error('Indique el motivo del rechazo por la compañía.');
    demo.acquisition = 'Rechazado';
    record('En estudio', 'Rechazado', 'Santiago Ríos', `Rechazo por la compañía: ${payload.reason.trim()}`);
  } else if (action === 'accept' || action === 'reject') {
    requireState('Propuesta enviada');
    requireRole('propietaria', 'Laura, la propietaria');
    demo.acquisition = action === 'accept' ? 'En proceso de compra' : 'Rechazado';
    record('Propuesta enviada', demo.acquisition, demo.name, action === 'accept' ? 'Oferta aceptada; compra pendiente de formalización.' : 'Oferta rechazada por la propietaria.');
  } else if (action === 'acquire') {
    requireState('En proceso de compra');
    requireRole('abogada', 'Valentina, la abogada');
    demo.acquisition = 'Adquirido';
    record('En proceso de compra', 'Adquirido', 'Valentina Ruiz', 'Compra completada y titularidad formalizada, simuladas. Alta en inventario de Casabra.');
  } else if (action === 'route') {
    requireState('Adquirido');
    requireRole('gerente', 'Camila, la gerente');
    if (!['Arriendo', 'Venta'].includes(payload.route)) throw new Error('Seleccione Arriendo o Venta.');
    if (demo.route) throw new Error('La ruta ya está asignada en este recorrido. Reinicie para explorar otra.');
    demo.route = payload.route;
    demo.works = Boolean(payload.works);
    record('Adquirido', 'Adquirido', 'Camila Torres', `Ruta ${demo.route}; ${demo.works ? 'con' : 'sin'} adecuaciones.`);
  } else if (action === 'external') {
    if (!demo.registered) throw new Error('Complete primero el registro para compartir un contexto simulado.');
    demo.external = payload.status;
    demo.externalReference = 'LC-DEMO-024';
  } else throw new Error('Acción de demostración desconocida.');
  return demo;
}

if (typeof module !== 'undefined' && module.exports) module.exports = { createDemo, advance };

if (typeof document !== 'undefined') {
  const $ = (selector) => document.querySelector(selector);
  const $$ = (selector) => [...document.querySelectorAll(selector)];
  const safe = (value) => String(value).replace(/[&<>"']/g, (char) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[char]));
  let demo = createDemo();
  let activeModule = null;
  let returnFocus = null;
  let returnScroll = 0;
  let selectedRole = 'propietaria';
  const scenarios = new Set();
  const tabScroll = { vision: 0, evolution: 0 };
  let currentTab = 'vision';
  const dialog = $('#module-dialog');

  const modules = {
    onboarding: { title: 'Onboarding', kicker: '01 · Identificar y vincular', hours: '600', benefit: 'Comenzar la relación con información inicial confiable y una autorización de datos trazable.', users: 'Laura Méndez, propietaria; equipo autorizado y oficial de cumplimiento.', scope: ['Registro y conocimiento inicial del cliente.', 'Autorizaciones de tratamiento de información.', 'Verificación de identidad y consulta de listas mediante el proveedor acordado.', 'Controles de acceso, trazabilidad y gestión de información.'], receives: 'Datos de la propietaria, autorización e información inicial del inmueble.', delivers: 'Cliente identificado e intención de venta vinculada al inmueble, disponibles para seguimiento y evaluación.', note: 'Los criterios de onboarding son una propuesta para cotización, pendiente de validación. Proveedor, política de revisión y requisitos exactos se acuerdan antes del desarrollo.' },
    crm: { title: 'CRM', kicker: '02 · Mantener la continuidad', hours: '460', benefit: 'Que cada conversación se convierta en contexto y cada compromiso tenga un responsable.', users: 'Santiago Ríos, asesor comercial; Camila Torres, gerente.', scope: ['Seguimiento comercial de la relación con cada cliente.', 'Ficha y etapa del cliente, interacciones y compromisos.', 'Recordatorios de seguimiento dentro de la app.', 'Visibilidad gerencial del avance comercial.'], receives: 'Cliente e inmueble vinculados desde onboarding; contexto del proceso de adquisición.', delivers: 'Historial comercial, siguiente compromiso y visibilidad para el equipo autorizado.', note: 'Los criterios de CRM son propuestos, pendientes de validación. La etapa comercial del cliente es independiente del estado de adquisición del inmueble.' },
    acquisition: { title: 'Adquisición de inmueble', kicker: '03 · Evaluar, decidir y formalizar', hours: '400', benefit: 'Conservar un expediente completo y una trazabilidad clara desde la presentación del inmueble hasta su adquisición o rechazo.', users: 'Laura Méndez, propietaria; Santiago Ríos, asesor; Valentina Ruiz, abogada; Camila Torres, gerente.', scope: ['Expediente documental y ficha del inmueble.', 'Estudio jurídico con conclusión y alertas.', 'Propuesta económica y respuesta de la propietaria.', 'Confirmación de compra y asignación posterior de Arriendo o Venta.', 'Seguimiento del estado y trazabilidad de decisiones.'], receives: 'Intención de venta, información del cliente y seguimiento comercial.', delivers: 'Decisión documentada. Solo una compra completada habilita el activo de Casabra y su ruta operativa.', note: 'Reglas de roles y estados según criterios aprobados HU-04 a HU-08. Requisitos documentales exactos por definir; los documentos de esta demo son ilustrativos.' },
    works: { title: 'Proyectos de obra', hours: '520', benefit: 'Dar visibilidad al presupuesto, responsables y avance de cada intervención.', scope: ['Presupuestos, cronogramas y responsables.', 'Fotografías y avances.', 'Permisos y alertas de desviación.'], dependencies: 'Inmueble adquirido; ruta y necesidad de adecuaciones definidas por la gerencia.' },
    contracts: { title: 'Contratos y firma electrónica', hours: '430', benefit: 'Formalizar acuerdos con documentos accesibles y trazables.', scope: ['Plantillas acordadas.', 'Revisión y firma desde el celular.', 'Archivo y trazabilidad.'], dependencies: 'Plantillas, participantes y proveedor de firma por acordar; información del inmueble y del negocio.' },
    rent: { title: 'Arriendo de inmuebles adquiridos', hours: '900', benefit: 'Conectar la comercialización del activo con su administración y el autoservicio del arrendatario.', scope: ['Alistamiento, oferta comercial e interesados.', 'Contratación y entrega.', 'Obligaciones, pagos y cartera.', 'Autoservicio del arrendatario.'], dependencies: 'Activo de Casabra con ruta Arriendo; adecuaciones cuando correspondan; contratos y proveedores que se acuerden.' },
    sale: { title: 'Venta de inmuebles adquiridos', hours: '820', benefit: 'Dar continuidad al proceso comercial hasta registrar el cierre.', scope: ['Preparación comercial y canales definidos.', 'Prospectos, visitas y ofertas.', 'Negociación, documentos y cierre.'], dependencies: 'Activo de Casabra con ruta Venta; preparación comercial, CRM y formalización según alcance acordado.' },
    portal: { title: 'Portal del cliente', hours: '500', benefit: 'Hacer visible la información autorizada y facilitar la lectura gerencial.', scope: ['Consulta de información e hitos autorizados para el propietario original.', 'Reportes gerenciales.'], dependencies: 'Información generada por módulos disponibles; definición de permisos, hitos y reportes autorizados.' },
    payments: { title: 'Pagos y utilidades', hours: '730', benefit: 'Relacionar los resultados económicos con el inmueble o proyecto que los origina.', scope: ['Costos e ingresos por inmueble o proyecto.', 'Rentabilidad.', 'Facturación mediante el servicio que se acuerde.'], dependencies: 'Movimientos disponibles de la operación; reglas económicas y servicio de facturación por acordar.' },
    financial: { title: 'Conexión con proveedor financiero', hours: '100', benefit: 'Usar funciones financieras de un tercero mientras Casabra adquiere experiencia operativa.', scope: ['Uso de las funciones financieras contratadas con un tercero.', 'Recorrido acordado para Casabra.', 'Propuesta de conexión con LeanCore: creación, administración y recaudo de créditos.'], dependencies: 'Contrato y capacidades habilitadas por el proveedor; alcance, responsabilidades y condiciones por acordar.' }
  };
  const optionalKeys = ['works', 'contracts', 'rent', 'sale', 'portal', 'payments', 'financial'];
  $('#optional-modules').innerHTML = optionalKeys.map((key, index) => `<button class="module-node optional" data-module="${key}"><span>${String(index + 1).padStart(2, '0')} · ${modules[key].title}</span><small>${modules[key].hours} h estimadas <span id="selected-${key}"></span></small><b aria-hidden="true">↗</b></button>`).join('');

  function changeTab(id, focus = true) {
    if (!['vision', 'evolution'].includes(id)) return;
    tabScroll[currentTab] = window.scrollY;
    currentTab = id;
    $$('.tab').forEach((tab) => { const active = tab.id === `tab-${id}`; tab.setAttribute('aria-selected', active); tab.tabIndex = active ? 0 : -1; });
    $$('.panel').forEach((panel) => { panel.hidden = panel.id !== id; });
    window.scrollTo({ top: tabScroll[id], behavior: 'instant' });
    if (focus) $(`#tab-${id}`).focus({ preventScroll: true });
  }

  function openModule(key, trigger) {
    if (!dialog.open) { returnFocus = trigger || document.activeElement; returnScroll = window.scrollY; }
    activeModule = key;
    renderModule();
    if (!dialog.open) { dialog.showModal(); document.body.classList.add('dialog-open'); }
    dialog.scrollTop = 0;
    $('#module-title').focus({ preventScroll: true });
  }

  function closeModule() {
    dialog.close();
  }

  dialog.addEventListener('close', () => {
    document.body.classList.remove('dialog-open');
    window.scrollTo({ top: returnScroll, behavior: 'instant' });
    returnFocus?.focus({ preventScroll: true });
    activeModule = null;
  });
  $('#close-dialog').addEventListener('click', closeModule);
  dialog.addEventListener('click', (event) => { if (event.target === dialog) { const r = dialog.getBoundingClientRect(); if (event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) closeModule(); } });
  document.addEventListener('keydown', (event) => {
    if (!dialog.open || event.key !== 'Tab') return;
    const controls = [...dialog.querySelectorAll('button, a[href], input, select, textarea, summary, [tabindex]')].filter((element) => element.tabIndex >= 0 && !element.disabled && element.getClientRects().length > 0 && getComputedStyle(element).visibility !== 'hidden');
    if (!controls.length) { event.preventDefault(); $('#module-title').focus(); return; }
    const first = controls[0];
    const last = controls[controls.length - 1];
    if (!dialog.contains(document.activeElement)) { event.preventDefault(); (event.shiftKey ? last : first).focus(); }
    else if (!controls.includes(document.activeElement)) {
      const position = event.shiftKey ? Node.DOCUMENT_POSITION_PRECEDING : Node.DOCUMENT_POSITION_FOLLOWING;
      const candidates = controls.filter((control) => document.activeElement.compareDocumentPosition(control) & position);
      event.preventDefault();
      (event.shiftKey ? candidates.at(-1) || last : candidates[0] || first).focus();
    }
    else if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
    else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
  });

  function scope(items) { return `<ul class="scope-list">${items.map((item) => `<li>${item}</li>`).join('')}</ul>`; }
  function recordHeader() { return `<div class="record"><div class="person"><span class="avatar">LM</span><div><strong>${safe(demo.name)}</strong><small>Propietaria original · ${safe(demo.email)}</small></div></div><div><strong>CAS-024 · Apartamento Cedro</strong><small>Bogotá · Inmueble de demostración</small></div><span class="status">${safe(demo.acquisition)}</span></div>`; }
  function feedback() { return '<p class="demo-feedback" id="demo-feedback" role="status" tabindex="-1">Los cambios solo afectan esta demostración.</p>'; }
  function missingRegistration() { return `<div class="notice"><h3>El recorrido comienza con Laura</h3><p>Registre primero a la propietaria para conservar el mismo contacto e inmueble entre los tres módulos.</p><button class="button primary" data-module="onboarding">Ir a Onboarding →</button></div>`; }

  function renderModule() {
    if (activeModule === 'external') { renderExternal(); return; }
    const m = modules[activeModule];
    const isOptional = optionalKeys.includes(activeModule);
    $('#dialog-kicker').textContent = isOptional ? 'Fase 02 · Módulo opcional / por priorizar' : m.kicker;
    $('#dialog-content').innerHTML = `<div class="module-overview"><div><h2 id="module-title" tabindex="-1">${m.title}</h2><p class="module-benefit">${m.benefit}</p>${isOptional ? '' : '<button class="button secondary" data-action="demo-scroll">Ir al recorrido interactivo ↓</button>'}</div><span class="pill ${isOptional ? 'optional' : ''}">${m.hours} horas estimadas</span></div><div class="detail-grid"><div><h3>Alcance propuesto</h3>${scope(m.scope)}</div><div><h3>${isOptional ? 'Dependencias' : 'Quiénes participan'}</h3><p>${isOptional ? m.dependencies : m.users}</p>${isOptional ? '' : `<div class="handoff"><p><strong>Recibe</strong><br>${m.receives}</p><p><strong>Entrega</strong><br>${m.delivers}</p></div>`}</div></div>${isOptional ? optionalView(activeModule) : `<p class="notice">${m.note}</p><section class="prototype" tabindex="-1" aria-label="Prototipo funcional de ${m.title}"><div class="prototype-toolbar"><span><b>Recorrido interactivo</b> · Datos ficticios</span><button class="button text" data-action="reset">Reiniciar demo</button></div>${recordHeader()}${activeModule === 'onboarding' ? onboardingView() : activeModule === 'crm' ? crmView() : acquisitionView()}${feedback()}</section>`}<p class="muted source-note">Alcance y horas: Cotización CASABRA V2. Tiempos aproximados; se precisarán en el levantamiento de requerimientos de cada módulo antes de iniciar su desarrollo.</p>`;
  }

  function optionalView(key) {
    return `<div class="scenario-toggle"><h3>Explorar un escenario de evolución</h3><p>Marque este módulo para conversar sobre una posible prioridad. La selección no altera precios ni representa una contratación.</p><button class="button ${scenarios.has(key) ? 'primary' : 'secondary'}" id="toggle-scenario" data-action="scenario" aria-pressed="${scenarios.has(key)}">${scenarios.has(key) ? 'Quitar del escenario' : 'Añadir al escenario'}</button></div><p class="notice">Vista informativa de fase 2, sin prototipo. ${key === 'financial' ? 'La arquitectura muestra la conexión desde la fase 1 para explicar la continuidad; sus 100 h están cotizadas en fase 2. Adelantarla requiere acordar alcance y cronograma.' : 'El alcance detallado y el orden de ejecución se validarán por módulo.'}</p>`;
  }

  function onboardingView() {
    if (!demo.registered) return `<div class="prototype-screen"><aside class="prototype-sidebar"><span class="eyebrow">LAURA · PROPIETARIA</span><h3>El primer contacto.</h3><p>Un registro que conecta a la persona con su intención de venta.</p><ol><li>Datos iniciales</li><li>Autorización expresa</li><li>Control de identidad</li></ol></aside><div class="prototype-body"><h3>Bienvenida, Laura</h3><p>Complete este ejemplo para presentar Apartamento Cedro a evaluación.</p><form id="onboarding-form"><div class="form-grid"><label class="field">Nombre completo<input name="name" value="Laura Méndez" required autocomplete="off"></label><label class="field">Correo electrónico<input name="email" value="laura.mendez@example.com" type="email" required autocomplete="off"></label><label class="field">Inmueble<input value="CAS-024 · Apartamento Cedro" readonly></label><label class="field">Ciudad<input value="Bogotá" readonly></label></div><details><summary>Consultar autorización de muestra</summary><p>Texto ilustrativo DEMO-01: autorizo el tratamiento de estos datos ficticios para simular el registro y el seguimiento de mi intención de venta. El texto legal definitivo deberá acordarse.</p></details><label class="check-row"><input name="consent" type="checkbox"> Acepto expresamente la autorización de tratamiento de datos de muestra.</label><button class="button primary" type="submit">Crear registro e intención de venta →</button></form></div></div>`;
    return `<div class="prototype-screen"><aside class="prototype-sidebar"><span class="eyebrow">REGISTRO RECIBIDO</span><h3>Una relación conectada.</h3><p>La cuenta de Laura y la intención de venta están vinculadas. Casabra aún no adquirió el inmueble.</p><span class="status">Autorización registrada</span></aside><div class="prototype-body"><h3>Control inicial de identidad</h3><p>Simule la respuesta del proveedor. Una coincidencia o una falla requiere revisión; nunca equivale a aprobación automática.</p><form id="identity-form"><label class="field">Respuesta simulada<select name="status"><option>Sin coincidencias reportadas</option><option>Pendiente de revisión</option><option>Proveedor no disponible</option></select></label><button class="button secondary">Simular consulta</button></form><div class="notice"><strong>Resultado: ${safe(demo.identity)}</strong><p>${demo.identity === 'Proveedor no disponible' ? 'Consulta sin respuesta satisfactoria. Reintento controlado disponible con el mismo botón.' : demo.identity === 'Pendiente de revisión' ? 'Caso pendiente del oficial de cumplimiento. No se considera aprobado.' : demo.identity === 'Sin consultar' ? 'Aún no se ha consultado al proveedor de muestra.' : 'Resultado de muestra disponible para personal autorizado; no sustituye la decisión de cumplimiento.'}</p></div><details><summary>Ver evidencia de autorización</summary><p>Versión ${demo.consent.version} · Sujeto: ${safe(demo.consent.subject)} · Fecha: ${safe(demo.consent.date)} · Aceptación expresa.</p></details><div class="demo-actions"><button class="button primary" data-module="crm">Continuar en CRM →</button><button class="button secondary" data-module="acquisition">Ver expediente</button></div></div></div>`;
  }

  function crmView() {
    if (!demo.registered) return missingRegistration();
    const activities = demo.activities.length ? `<ul class="activity-list">${demo.activities.map((a) => `<li><strong>${safe(a.type)}</strong> · ${safe(a.date)}<p>${safe(a.note)}</p><small>${safe(a.author)} · Nota interna</small></li>`).join('')}</ul>` : '<p class="muted">Todavía no hay interacciones. Registre la primera llamada.</p>';
    const commitments = demo.commitments.length ? `<ul class="activity-list">${demo.commitments.map((c, i) => `<li><strong>${safe(c.title)}</strong><p>${safe(c.date)} · ${c.owner} · ${c.completed ? 'Completada' : 'Pendiente'}</p>${c.completed ? '' : `<button class="button text" data-action="completeCommitment" data-index="${i}">Marcar completada</button>`}</li>`).join('')}</ul>` : '<p class="muted">No hay compromisos programados.</p>';
    return `<div class="prototype-screen"><aside class="prototype-sidebar"><span class="eyebrow">SANTIAGO · ASESOR</span><h3>Conservar el contexto.</h3><p>La ficha comercial reúne actividades y compromisos del mismo contacto.</p><form id="stage-form"><label class="field">Etapa del cliente<select name="stage">${['Nuevo contacto', 'En evaluación', 'Contrato firmado'].map((s) => `<option${demo.crmStage === s ? ' selected' : ''}>${s}</option>`).join('')}</select></label><button class="button secondary">Guardar etapa</button></form><p class="notice">Cambiar esta etapa no cambia el estado del inmueble.</p><div class="metric"><span>Tablero gerencial ilustrativo</span><strong>1 cliente · 1 inmueble presentado</strong><small>Captado no significa adquirido. ${demo.acquisition === 'Adquirido' ? '1' : '0'} adquiridos.</small></div></aside><div class="prototype-body"><h3>Interacciones y siguiente paso</h3><form id="activity-form"><div class="form-grid"><label class="field">Interacción<select name="type"><option>Llamada</option><option>Visita</option></select></label><label class="field">Resultado<input name="note" value="Laura confirma interés y acuerda completar su expediente." required maxlength="250"></label></div><button class="button secondary">Registrar interacción</button></form>${activities}<h3>Agenda de Santiago</h3><form id="commitment-form"><div class="form-grid"><label class="field">Compromiso<input name="title" value="Revisar expediente de Apartamento Cedro" required maxlength="150"></label><label class="field">Fecha de seguimiento<input name="date" type="date" value="2026-11-20" required></label></div><button class="button secondary">Programar compromiso</button></form>${commitments}<p class="muted">Agenda y aviso ilustrativos dentro de la app; no se envían correos ni notificaciones reales.</p><button class="button primary" data-module="acquisition">Continuar en Adquisición →</button></div></div>`;
  }

  function acquisitionView() {
    if (!demo.registered) return missingRegistration();
    const state = demo.acquisition;
    let action = '';
    if (state === 'Documentación faltante') action = `<h3>Completar el expediente</h3><p>Laura revisa los requisitos pendientes y aporta la información necesaria. La lista definitiva se acordará y configurará; esta demo utiliza un requisito de muestra.</p><div class="document-sample"><strong>Requisito de muestra</strong><p>Información y documento ilustrativos del inmueble · Pendiente</p></div><button class="button primary" data-action="documents"${selectedRole !== 'propietaria' ? ' disabled' : ''}>Completar requisitos de muestra →</button><p class="muted">Actúa como Laura, propietaria. No se carga ningún archivo real.</p>`;
    if (state === 'En estudio') action = `<h3>Evaluar y decidir</h3><p>Valentina registra el estudio jurídico y Santiago consulta el resultado para decidir una propuesta.</p><div class="notice"><strong>Estudio jurídico: ${demo.study ? 'Registrado por Valentina Ruiz' : 'Pendiente'}</strong><p>${demo.study ? 'Conclusión y alertas de muestra conservadas. No constituye un concepto jurídico real.' : 'Registre una conclusión ilustrativa antes de recorrer la propuesta.'}</p></div><div class="demo-actions"><button class="button secondary" data-action="study"${selectedRole !== 'abogada' || demo.study ? ' disabled' : ''}>Registrar estudio de muestra</button><button class="button primary" data-action="offer"${selectedRole !== 'asesor' || !demo.study ? ' disabled' : ''}>Enviar propuesta económica →</button></div><p class="muted">Oferta ficticia del inmueble: COP 420.000.000. Es un dato de demostración, no el precio del desarrollo.</p><details><summary>La compañía decide no continuar</summary><form id="company-reject-form"><label class="field">Motivo del rechazo<input name="reason" value="La compañía decide no continuar en este ejemplo." required maxlength="250"></label><button class="button secondary"${selectedRole !== 'asesor' ? ' disabled' : ''}>Rechazar inmueble como asesor</button></form></details>`;
    if (state === 'Propuesta enviada') action = `<h3>Laura decide sobre su oferta</h3><p class="big-number">COP 420.000.000</p><p>Valor ficticio ofrecido por Casabra para este inmueble de muestra.</p><div class="demo-actions"><button class="button primary" data-action="accept"${selectedRole !== 'propietaria' ? ' disabled' : ''}>Aceptar oferta →</button><button class="button secondary" data-action="reject"${selectedRole !== 'propietaria' ? ' disabled' : ''}>Rechazar oferta</button></div><p class="notice">Aceptar la oferta inicia el proceso de compra. Aún no convierte el inmueble en un activo de Casabra.</p>`;
    if (state === 'En proceso de compra') action = `<h3>Formalizar la adquisición</h3><p>La oferta está aceptada. La compra y la formalización de titularidad deben completarse antes de confirmar el alta en el inventario de Casabra.</p><button class="button primary" data-action="acquire"${selectedRole !== 'abogada' ? ' disabled' : ''}>Confirmar compra completada →</button><p class="notice">Actúa como Valentina, abogada. La gerencia todavía no puede asignar Arriendo o Venta.</p>`;
    if (state === 'Adquirido') action = demo.route ? `<h3>Activo de Casabra · Ruta ${safe(demo.route)}</h3><p>Camila asignó ${safe(demo.route)} ${demo.works ? 'con adecuaciones previas' : 'sin adecuaciones previas'}. El inmueble está habilitado para el flujo operativo correspondiente.</p><span class="status">Recorrido completado</span><p class="muted">Los módulos operativos de fase 2 se presentan en el mapa de evolución, sin prototipos.</p><button class="button secondary" data-action="go-map">Explorar los módulos de operación →</button>` : `<h3>Camila define la ruta del activo</h3><p>La compra está completada. Ahora la gerente puede decidir el destino y si requiere adecuaciones.</p><form id="route-form"><label class="field">Ruta<select name="route"><option>Arriendo</option><option>Venta</option></select></label><label class="check-row"><input type="checkbox" name="works"> Requiere adecuaciones</label><button class="button primary"${selectedRole !== 'gerente' ? ' disabled' : ''}>Asignar ruta operativa →</button></form>`;
    if (state === 'Rechazado') action = '<h3>Solicitud rechazada</h3><p>La decisión y su responsable permanecen en el historial. Reinicie la demo si desea explorar la aceptación y la compra.</p><button class="button secondary" data-action="reset">Reiniciar recorrido</button>';
    return `<div class="prototype-screen"><aside class="prototype-sidebar"><span class="eyebrow">EXPEDIENTE CAS-024</span><h3>Una decisión a la vez.</h3><label class="field">Actuar como<select id="demo-role"><option value="propietaria"${selectedRole === 'propietaria' ? ' selected' : ''}>Laura · Propietaria</option><option value="asesor"${selectedRole === 'asesor' ? ' selected' : ''}>Santiago · Asesor</option><option value="abogada"${selectedRole === 'abogada' ? ' selected' : ''}>Valentina · Abogada</option><option value="gerente"${selectedRole === 'gerente' ? ' selected' : ''}>Camila · Gerente</option></select></label><p class="muted">El selector ilustra responsabilidades, no es un sistema de autenticación.</p><ol class="state-track">${['Documentación faltante', 'En estudio', 'Propuesta enviada', 'En proceso de compra', 'Adquirido'].map((s) => `<li${s === state ? ' aria-current="step" class="current"' : ''}>${s}</li>`).join('')}</ol><p>Respuesta estimada: <strong>Por confirmar</strong></p></aside><div class="prototype-body">${action}<details><summary>Ficha y documentos del expediente</summary><div class="table-wrap"><table class="demo-table"><caption>Ejemplo de expediente · No define requisitos documentales obligatorios</caption><thead><tr><th scope="col">Elemento</th><th scope="col">Información de muestra</th><th scope="col">Situación</th></tr></thead><tbody><tr><th scope="row">Ficha del inmueble</th><td>Apartamento Cedro · Bogotá</td><td>CAS-024</td></tr><tr><th scope="row">Propietaria original</th><td>${safe(demo.name)}</td><td>Contacto vinculado</td></tr><tr><th scope="row">Documento de muestra</th><td>Referencia documental ilustrativa</td><td>${state === 'Documentación faltante' ? 'Pendiente' : 'Vinculado al expediente'}</td></tr><tr><th scope="row">Estudio jurídico</th><td>Valentina Ruiz</td><td>${demo.study ? 'Registrado' : 'Pendiente'}</td></tr></tbody></table></div></details><details class="history-list"><summary>Ver historial de decisiones (${demo.history.length})</summary>${demo.history.map((h) => `<article><strong>${safe(h.before)} → ${safe(h.after)}</strong><p>${safe(h.detail)}</p><small>${safe(h.actor)} · ${safe(h.date)}</small></article>`).join('')}</details></div></div>`;
  }

  function renderExternal() {
    $('#dialog-kicker').textContent = 'Proveedor externo · Intercambio conceptual';
    $('#dialog-content').innerHTML = `<div class="module-overview"><h2 id="module-title" tabindex="-1">Casabra ↔ LeanCore</h2><span class="pill external">Simulación sin conexión</span></div><p class="module-benefit">Conectar la experiencia de Casabra con funciones financieras contratadas a un tercero, conservando responsabilidades claras.</p><div class="detail-grid"><div><h3>Información propia de Casabra</h3>${scope(['Identidad y autorizaciones del cliente.', 'Inmueble, expediente y relación comercial.', 'Operación inmobiliaria y trazabilidad de decisiones.'])}</div><div><h3>Capacidad del proveedor</h3>${scope(['Creación y administración de créditos.', 'Recaudo de créditos.', 'Funciones efectivamente contratadas con LeanCore.'])}</div></div><p class="notice">Conexión mostrada desde el inicio; cotizada en fase 2 (100 horas). Adelantarla requiere acordar alcance y cronograma. Los datos compartidos, permisos, capacidades y responsabilidades siguen por definir.</p><section class="prototype"><div class="prototype-toolbar"><b>Simulación de intercambio</b><span>Sin API, credenciales ni transmisión de datos</span></div>${recordHeader()}<div class="prototype-body">${demo.registered ? `<h3>Contexto simulado de Laura y CAS-024</h3><p>Referencia local: ${demo.externalReference || 'Aún no generada'} · El estado financiero externo no cambia el estado de adquisición.</p><form id="external-form"><label class="field">Respuesta de muestra<select name="status">${['Recibido por proveedor', 'Pendiente de revisión', 'Proveedor no disponible', 'Respuesta recibida'].map((s) => `<option${demo.external === s ? ' selected' : ''}>${s}</option>`).join('')}</select></label><button class="button primary">Simular intercambio →</button></form><div class="notice"><strong>Estado simulado: ${safe(demo.external)}</strong><p>${demo.external === 'Proveedor no disponible' ? 'No existe respuesta confirmada. Puede simular un reintento; una falla nunca se muestra como aprobación.' : demo.external === 'Pendiente de revisión' ? 'Pendiente visible para revisión. No representa aprobación ni desembolso.' : 'Solo representa el estado de un intercambio de muestra; no crea ni aprueba créditos.'}</p></div>` : missingRegistration()}${feedback()}</div></section><details><summary>Costos de referencia del proveedor</summary><p>Cargo mínimo mensual: USD 1.500. Administración de cada crédito: USD 0,30. Periodicidad del cargo por crédito y relación con el mínimo: por validar con el proveedor. El mínimo anualizado es USD 18.000 (1.500 × 12), sin asumir ahorro neto.</p></details>`;
  }

  function refresh(message, focusId) {
    const top = dialog.scrollTop;
    renderModule();
    dialog.scrollTop = top;
    const feedbackElement = $('#demo-feedback');
    if (feedbackElement && message) feedbackElement.textContent = message;
    const target = focusId ? document.getElementById(focusId) : feedbackElement;
    target?.focus({ preventScroll: true });
  }

  function showToast(message) {
    $('#toast').textContent = message;
    $('#toast').classList.add('visible');
    window.setTimeout(() => { $('#toast').classList.remove('visible'); $('#toast').textContent = ''; }, 4000);
  }

  function resetDemo() {
    demo = createDemo(); selectedRole = 'propietaria';
    if (dialog.open) refresh('La demostración volvió al inicio. Puede registrar a Laura nuevamente.');
    showToast('Demo reiniciada. Los datos ficticios volvieron al inicio.');
  }

  function scenarioSummary() {
    $('#scenario-summary').textContent = scenarios.size ? `${scenarios.size} módulo${scenarios.size === 1 ? '' : 's'} para conversar: ${[...scenarios].map((key) => modules[key].title).join(', ')}.` : 'Ningún módulo seleccionado para el escenario.';
    optionalKeys.forEach((key) => { $(`#selected-${key}`).textContent = scenarios.has(key) ? '· En escenario' : ''; });
  }

  document.addEventListener('click', (event) => {
    const moduleButton = event.target.closest('[data-module]');
    if (moduleButton) { openModule(moduleButton.dataset.module, moduleButton); return; }
    const tabButton = event.target.closest('[data-tab]');
    if (tabButton) { changeTab(tabButton.dataset.tab); return; }
    const scrollButton = event.target.closest('[data-scroll]');
    if (scrollButton) { const target = document.getElementById(scrollButton.dataset.scroll); target.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' }); return; }
    const actionButton = event.target.closest('[data-action]');
    if (!actionButton) return;
    const action = actionButton.dataset.action;
    if (action === 'demo-scroll') { const prototype = dialog.querySelector('.prototype'); prototype.scrollIntoView({ behavior: 'instant', block: 'start' }); prototype.focus({ preventScroll: true }); return; }
    if (action === 'reset') { resetDemo(); return; }
    if (action === 'scenario') { if (scenarios.has(activeModule)) scenarios.delete(activeModule); else scenarios.add(activeModule); scenarioSummary(); refresh('', 'toggle-scenario'); return; }
    if (action === 'go-map') { dialog.close(); changeTab('evolution'); window.setTimeout(() => document.querySelector('.phase-2').scrollIntoView({ behavior: 'instant', block: 'start' }), 0); return; }
    try {
      advance(demo, action, { role: selectedRole, index: Number(actionButton.dataset.index) });
      const message = action === 'accept' ? 'Oferta aceptada: En proceso de compra. El inmueble aún no está adquirido.' : action === 'acquire' ? 'Valentina confirmó la compra: Adquirido. Camila ya puede asignar la ruta.' : action === 'study' ? 'Valentina registró el estudio. Cambie a Santiago para enviar la propuesta.' : action === 'documents' ? 'Expediente En estudio. Cambie a Valentina para registrar el estudio jurídico.' : action === 'offer' ? 'Propuesta enviada. Cambie a Laura para responder a la oferta.' : 'Cambio registrado en esta demostración.';
      refresh(message);
    } catch (error) { $('#demo-feedback').textContent = error.message; $('#demo-feedback').focus({ preventScroll: true }); }
  });

  document.addEventListener('submit', (event) => {
    if (!dialog.contains(event.target)) return;
    event.preventDefault();
    const form = event.target;
    const data = Object.fromEntries(new FormData(form));
    const actions = { 'onboarding-form': 'register', 'identity-form': 'identity', 'stage-form': 'crmStage', 'activity-form': 'activity', 'commitment-form': 'commitment', 'route-form': 'route', 'external-form': 'external', 'company-reject-form': 'rejectCompany' };
    if (!actions[form.id]) return;
    try {
      advance(demo, actions[form.id], { ...data, consent: data.consent === 'on', works: data.works === 'on', role: selectedRole });
      refresh(form.id === 'onboarding-form' ? 'Laura y su intención de venta quedaron registradas. Puede simular el control de identidad y continuar en CRM.' : form.id === 'route-form' ? 'Camila asignó la ruta operativa. Recorrido completado.' : 'Información de muestra registrada.');
    } catch (error) { $('#demo-feedback').textContent = error.message; $('#demo-feedback').focus({ preventScroll: true }); }
  });

  document.addEventListener('change', (event) => {
    if (event.target.id === 'demo-role') { selectedRole = event.target.value; refresh(`Actuando como ${event.target.options[event.target.selectedIndex].text}.`, 'demo-role'); }
  });
  $$('.tab').forEach((tab) => {
    tab.addEventListener('click', () => changeTab(tab.id.replace('tab-', '')));
    tab.addEventListener('keydown', (event) => {
      if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
      event.preventDefault();
      const id = event.key === 'Home' ? 'vision' : event.key === 'End' ? 'evolution' : currentTab === 'vision' ? 'evolution' : 'vision';
      changeTab(id);
    });
  });
  $('.brand').addEventListener('click', (event) => { event.preventDefault(); changeTab('vision'); window.scrollTo({ top: 0, behavior: 'instant' }); });
  $('#reset-demo').addEventListener('click', resetDemo);
}

