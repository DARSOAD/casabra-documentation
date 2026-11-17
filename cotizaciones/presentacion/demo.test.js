const assert = require('node:assert/strict');
const test = require('node:test');
let model = {};
try { model = require('./app.js'); } catch (error) { if (error.code !== 'MODULE_NOT_FOUND') throw error; }

test('el registro necesita consentimiento y la aceptación de oferta no compra el inmueble', () => {
  assert.equal(typeof model.createDemo, 'function', 'el modelo de demostración debe existir');
  const demo = model.createDemo();
  assert.throws(() => model.advance(demo, 'register', { consent: false }), /autorización/);
  model.advance(demo, 'register', { consent: true });
  assert.equal(demo.registered, true);
  assert.equal(demo.acquisition, 'Documentación faltante');
  model.advance(demo, 'documents', { role: 'propietaria' });
  model.advance(demo, 'study', { role: 'abogada' });
  model.advance(demo, 'offer', { role: 'asesor' });
  model.advance(demo, 'accept', { role: 'propietaria' });
  assert.equal(demo.acquisition, 'En proceso de compra');
  assert.throws(() => model.advance(demo, 'route', { route: 'Venta' }), /Adquirido/);
  assert.throws(() => model.advance(demo, 'acquire', { role: 'asesor' }), /abogada/);
  model.advance(demo, 'acquire', { role: 'abogada' });
  assert.equal(demo.acquisition, 'Adquirido');
  model.advance(demo, 'route', { role: 'gerente', route: 'Arriendo', works: true });
  assert.equal(demo.route, 'Arriendo');
  assert.equal(demo.works, true);
  assert.equal(demo.history.at(-1).actor, 'Camila Torres');
});

test('las etapas CRM y los estados externos mantienen separados sus efectos', () => {
  assert.equal(typeof model.createDemo, 'function', 'el modelo de demostración debe existir');
  const demo = model.createDemo();
  model.advance(demo, 'register', { consent: true });
  model.advance(demo, 'crmStage', { stage: 'Contrato firmado' });
  assert.equal(demo.acquisition, 'Documentación faltante');
  model.advance(demo, 'activity', { note: 'Llamada de seguimiento', type: 'Llamada' });
  model.advance(demo, 'commitment', { title: 'Revisar expediente', date: '2026-11-20' });
  assert.equal(demo.activities.length, 1);
  assert.equal(demo.commitments.length, 1);
  model.advance(demo, 'external', { status: 'Pendiente de revisión' });
  assert.equal(demo.external, 'Pendiente de revisión');
  assert.equal(demo.acquisition, 'Documentación faltante');
});

test('el asesor puede rechazar durante el estudio con motivo y responsable conservados', () => {
  const demo = model.createDemo();
  model.advance(demo, 'register', { consent: true });
  model.advance(demo, 'documents', { role: 'propietaria' });
  assert.throws(() => model.advance(demo, 'rejectCompany', { role: 'asesor', reason: '' }), /motivo/);
  assert.throws(() => model.advance(demo, 'rejectCompany', { role: 'propietaria', reason: 'Motivo de muestra' }), /asesor/);
  model.advance(demo, 'rejectCompany', { role: 'asesor', reason: 'La compañía decide no continuar en este ejemplo.' });
  assert.equal(demo.acquisition, 'Rechazado');
  assert.equal(demo.history.at(-1).actor, 'Santiago Ríos');
  assert.match(demo.history.at(-1).detail, /compañía/);
});
