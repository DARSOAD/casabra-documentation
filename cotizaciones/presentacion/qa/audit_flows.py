"""Independent behavioral checks against the rendered local demo, without app edits."""
import json
from pathlib import Path
from datetime import datetime, timezone
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa"
SHOTS = OUT / "capturas"


def main():
    SHOTS.mkdir(exist_ok=True)
    results = {"at_utc": datetime.now(timezone.utc).isoformat(), "url": (ROOT / "index.html").as_uri(), "checks": [], "errors": [], "failed_requests": [], "network_requests": [], "dialog_viewports": []}

    def check(name, condition, detail=None):
        item = {"name": name, "passed": bool(condition)}
        if detail is not None:
            item["detail"] = detail
        results["checks"].append(item)
        if not condition:
            print("FAIL: " + name, flush=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe", headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 960}, reduced_motion="reduce")
        page.on("pageerror", lambda error: results["errors"].append(str(error)))
        page.on("requestfailed", lambda request: results["failed_requests"].append({"url": request.url, "failure": request.failure}))
        page.on("request", lambda request: results["network_requests"].append(request.url) if request.url.startswith(("http:", "https:")) else None)

        def state():
            return page.locator("#module-dialog .record .status").inner_text()

        def role(value):
            page.locator("#demo-role").select_option(value)

        def snap(name):
            page.screenshot(path=str(SHOTS / (name + ".png")), full_page=True)

        def register():
            page.locator('input[name="consent"]').check()
            page.locator('#onboarding-form button[type="submit"]').click()

        def open_module(key):
            if page.locator("#module-dialog").evaluate("e=>e.open"):
                nested = page.locator(f'#module-dialog [data-module="{key}"]:visible')
                if nested.count():
                    nested.first.click()
                    return
                page.keyboard.press("Escape")
            page.locator(f'[data-module="{key}"]:visible').first.click()

        try:
            page.goto(results["url"], wait_until="load")
            page.locator("#tab-vision").focus()
            page.keyboard.press("ArrowRight")
            check("Flecha derecha activa mapa y mueve foco", page.locator("#tab-evolution").get_attribute("aria-selected") == "true" and page.evaluate("document.activeElement.id") == "tab-evolution")
            page.keyboard.press("Home")
            check("Home activa visión", page.locator("#vision").is_visible())
            page.keyboard.press("End")
            check("End activa mapa", page.locator("#evolution").is_visible())
            page.keyboard.press("ArrowLeft")
            check("Flecha izquierda vuelve a visión", page.locator("#vision").is_visible())

            trigger = page.locator('#vision [data-module="onboarding"]').first
            trigger.scroll_into_view_if_needed()
            trigger.focus()
            origin_scroll = page.evaluate("scrollY")
            page.keyboard.press("Enter")
            check("Enter abre detalle y enfoca título", page.locator("#module-dialog").evaluate("e=>e.open") and page.evaluate("document.activeElement.id") == "module-title")
            for _ in range(25):
                page.keyboard.press("Tab")
                check("Foco permanece dentro del diálogo", page.evaluate("document.querySelector('#module-dialog').contains(document.activeElement)"), page.evaluate("({tag:document.activeElement.tagName,id:document.activeElement.id,text:document.activeElement.innerText.slice(0,100)})"))
            for _ in range(15):
                page.keyboard.press("Shift+Tab")
                check("Foco inverso permanece dentro del diálogo", page.evaluate("document.querySelector('#module-dialog').contains(document.activeElement)"))
            page.keyboard.press("Escape")
            page.wait_for_timeout(50)
            check("Escape cierra detalle", not page.locator("#module-dialog").evaluate("e=>e.open"))
            check("Cierre devuelve foco al disparador", trigger.evaluate("e=>e===document.activeElement"))
            check("Cierre conserva scroll de origen", abs(page.evaluate("scrollY") - origin_scroll) < 2, {"before": origin_scroll, "after": page.evaluate("scrollY")})

            open_module("onboarding")
            page.locator('#onboarding-form button[type="submit"]').click()
            check("Consentimiento impide registro vacío", page.locator("#demo-feedback").inner_text().startswith("La autorización") and page.locator("#onboarding-form").is_visible())
            register()
            check("Registro recibe la misma persona e inmueble", "Laura Méndez" in page.locator(".record").inner_text() and "CAS-024" in page.locator(".record").inner_text())
            check("Registro no adquiere inmueble", state() == "Documentación faltante")
            page.locator('#identity-form select').select_option(label="Pendiente de revisión")
            page.locator('#identity-form button').click()
            check("Identidad pendiente visible sin aprobación", "Resultado: Pendiente de revisión" in page.locator("#module-dialog").inner_text() and "No se considera aprobado" in page.locator("#module-dialog").inner_text())
            page.locator('#identity-form select').select_option(label="Proveedor no disponible")
            page.locator('#identity-form button').click()
            check("Identidad fallida ofrece reintento", "Reintento controlado" in page.locator("#module-dialog").inner_text())
            page.locator('#identity-form select').select_option(label="Sin coincidencias reportadas")
            page.locator('#identity-form button').click()
            snap("flujo-01-registro-identidad")

            open_module("crm")
            page.locator('#activity-form input[name="note"]').fill("QA: Laura confirma su expediente CAS-024")
            page.locator('#activity-form button').click()
            check("Actividad guardada vinculada a misma persona", "QA: Laura confirma su expediente CAS-024" in page.locator("#module-dialog").inner_text() and "Laura Méndez" in page.locator(".record").inner_text())
            page.locator('#commitment-form input[name="title"]').fill("QA: Revisar expediente CAS-024")
            page.locator('#commitment-form button').click()
            check("Compromiso con fecha y responsable", "QA: Revisar expediente CAS-024" in page.locator("#module-dialog").inner_text() and "2026-11-20" in page.locator("#module-dialog").inner_text())
            page.locator('[data-action="completeCommitment"]').click()
            check("Compromiso puede completarse", "Completada" in page.locator("#module-dialog").inner_text())
            page.locator('#stage-form select').select_option(label="Contrato firmado")
            page.locator('#stage-form button').click()
            check("Etapa comercial no altera adquisición", state() == "Documentación faltante")
            snap("flujo-02-crm-contexto")

            open_module("acquisition")
            role("gerente")
            check("Gerencia no completa documentos del propietario", page.locator('[data-action="documents"]').is_disabled())
            role("propietaria")
            page.locator('[data-action="documents"]').click()
            check("Documentación completa inicia En estudio", state() == "En estudio")
            check("Propietaria no registra estudio jurídico", page.locator('[data-action="study"]').is_disabled())
            role("abogada")
            page.locator('[data-action="study"]').click()
            check("Estudio conserva actor autorizado", "Registrado por Valentina Ruiz" in page.locator("#module-dialog").inner_text())
            role("asesor")
            page.locator('[data-action="offer"]').click()
            check("Asesor envía propuesta", state() == "Propuesta enviada")
            check("Asesor no acepta oferta del propietario", page.locator('[data-action="accept"]').is_disabled())
            role("propietaria")
            page.locator('[data-action="accept"]').click()
            check("Aceptación solo inicia compra", state() == "En proceso de compra")
            role("gerente")
            check("Gerencia no confirma compra ni asigna ruta antes de adquisición", page.locator('[data-action="acquire"]').is_disabled() and page.locator("#route-form").count() == 0)
            snap("flujo-03-oferta-aceptada-compra-pendiente")
            role("abogada")
            page.locator('[data-action="acquire"]').click()
            check("Abogada confirma adquisición", state() == "Adquirido")
            check("Abogada no asigna ruta gerencial", page.locator("#route-form button").is_disabled())
            role("gerente")
            page.locator('#route-form select').select_option(label="Venta")
            page.locator('#route-form input[name="works"]').check()
            page.locator('#route-form button').click()
            check("Gerencia asigna Venta con adecuaciones tras compra", "Activo de Casabra · Ruta Venta" in page.locator("#module-dialog").inner_text() and "con adecuaciones previas" in page.locator("#module-dialog").inner_text())
            page.locator(".history-list").evaluate("e=>e.open=true")
            history = page.locator(".history-list").inner_text()
            check("Historial conserva estados y responsables", all(word in history for word in ["Documentación faltante", "En estudio", "Propuesta enviada", "En proceso de compra", "Adquirido", "Valentina Ruiz", "Camila Torres"]))
            snap("flujo-04-adquirido-ruta-historial")
            page.locator('[data-action="go-map"]').click()
            page.wait_for_timeout(100)
            check("Ruta completada permite seguir al mapa de operación", page.locator("#evolution").is_visible() and not page.locator("#module-dialog").evaluate("e=>e.open"))
            open_module("external")
            for status in ["Recibido por proveedor", "Pendiente de revisión", "Proveedor no disponible", "Respuesta recibida"]:
                page.locator('#external-form select').select_option(label=status)
                page.locator('#external-form button').click()
                check("LeanCore simula " + status, "Estado simulado: " + status in page.locator("#module-dialog").inner_text())
                check("LeanCore no altera adquisición en " + status, state() == "Adquirido")
                if status == "Pendiente de revisión":
                    check("Pendiente no representa aprobación/desembolso", "No representa aprobación ni desembolso" in page.locator("#module-dialog").inner_text())
                if status == "Proveedor no disponible":
                    check("Fallo financiero permite reintento sin aprobar", "Puede simular un reintento" in page.locator("#module-dialog").inner_text())
                    snap("flujo-05-proveedor-fallo-reintento")
            page.keyboard.press("Escape")

            optional = ["works", "contracts", "rent", "sale", "portal", "payments", "financial"]
            hours = ["520", "430", "900", "820", "500", "730", "100"]
            for key, hours_value in zip(optional, hours):
                open_module(key)
                text = page.locator("#module-dialog").inner_text()
                check("Detalle opcional " + key + " conserva horas/alcance/dependencia", hours_value + " horas estimadas" in text and "Alcance propuesto" in text and "Dependencias" in text)
                page.locator("#toggle-scenario").click()
                check("Selección opcional " + key + " accesible y reversa", page.locator("#toggle-scenario").get_attribute("aria-pressed") == "true")
                snap("opcional-" + key)
                page.keyboard.press("Escape")
            check("Los7 opcionales se agregan sin alterar cotización base", "7 módulos" in page.locator("#scenario-summary").inner_text() and "1.460" in page.locator(".phase-1 .pill").inner_text() and "4.000" in page.locator(".phase-2 .pill").inner_text())
            open_module("works")
            page.locator("#toggle-scenario").click()
            check("Selección se puede quitar", page.locator("#toggle-scenario").get_attribute("aria-pressed") == "false")
            page.keyboard.press("Escape")
            check("Fase3 sin precio/horas y costos correctamente contextualizados", all(word in page.locator(".phase-3").inner_text() for word in ["USD 1.500", "USD 18.000", "no un ahorro neto", "no asigna horas ni presupuesto"]))

            for width in [375, 768, 1024, 1440]:
                page.set_viewport_size({"width": width, "height": 960})
                for key in ["onboarding", "crm", "acquisition", "external", "rent"]:
                    open_module(key)
                    dimensions = page.locator("#module-dialog").evaluate("e=>({width:e.clientWidth,scrollWidth:e.scrollWidth,left:e.getBoundingClientRect().left,right:e.getBoundingClientRect().right})")
                    okay = dimensions["scrollWidth"] <= dimensions["width"] + 1 and dimensions["left"] >= 0 and dimensions["right"] <= width + 1
                    results["dialog_viewports"].append({"viewport": width, "module": key, "passed": okay, **dimensions})
                    check(f"Panel {key} cabe a{width}px", okay, dimensions)
                    if width == 375:
                        snap("movil-" + key)
                    page.keyboard.press("Escape")

            page.set_viewport_size({"width": 1440, "height": 960})
            open_module("onboarding")
            page.locator('[data-action="reset"]').click()
            register()
            open_module("acquisition")
            role("propietaria")
            page.locator('[data-action="documents"]').click()
            role("abogada")
            page.locator('[data-action="study"]').click()
            role("asesor")
            page.locator('[data-action="offer"]').click()
            role("propietaria")
            page.locator('[data-action="reject"]').click()
            check("Propietaria puede rechazar propuesta", state() == "Rechazado")
            snap("flujo-06-propuesta-rechazada")

            page.locator('[data-action="reset"]').first.click()
            open_module("onboarding")
            register()
            open_module("acquisition")
            role("propietaria")
            page.locator('[data-action="documents"]').click()
            role("abogada")
            page.locator("#company-reject-form").evaluate("e=>e.closest('details').open=true")
            check("Abogada no rechaza como compañía sin rol asesor", page.locator("#company-reject-form button").is_disabled())
            role("asesor")
            page.locator("#company-reject-form").evaluate("e=>e.closest('details').open=true")
            page.locator('#company-reject-form input').fill("")
            page.locator('#company-reject-form button').click()
            check("Rechazo compañía exige motivo", state() == "En estudio" and not page.locator('#company-reject-form input').evaluate("e=>e.validity.valid"))
            page.locator('#company-reject-form input').fill("QA: decisión de la compañía con motivo documentado")
            page.locator('#company-reject-form button').click()
            check("Asesor rechaza inmueble durante estudio", state() == "Rechazado")
            page.locator(".history-list").evaluate("e=>e.open=true")
            check("Rechazo empresa conserva motivo y autor", "QA: decisión de la compañía con motivo documentado" in page.locator(".history-list").inner_text() and "Santiago Ríos" in page.locator(".history-list").inner_text())
            snap("flujo-07-rechazo-compania")
            page.locator("#close-dialog").click()
            page.wait_for_timeout(50)
            check("Botón Cerrar devuelve a la página sin panel", not page.locator("#module-dialog").evaluate("e=>e.open") and page.locator("#evolution").is_visible())

        except Exception as error:
            results["fatal"] = str(error)
            snap("fallo-auditoria")
        finally:
            browser.close()
    check("Sin errores JavaScript", not results["errors"], results["errors"])
    check("Sin recursos fallidos", not results["failed_requests"], results["failed_requests"])
    check("Sin solicitudes externas", not results["network_requests"], results["network_requests"])
    results["summary"] = {"passed": sum(item["passed"] for item in results["checks"]), "failed": sum(not item["passed"] for item in results["checks"]), "total": len(results["checks"])}
    (OUT / "flujos-resultados.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"summary": results["summary"], "fatal": results.get("fatal"), "failures": [item for item in results["checks"] if not item["passed"]]}, ensure_ascii=False, indent=2))
    if results.get("fatal") or results["summary"]["failed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
