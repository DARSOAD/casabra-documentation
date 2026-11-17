"""Read-only browser probe for the local presentation; run after app.js is ready."""
import json
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa"
SHOTS = OUT / "capturas"


def main():
    SHOTS.mkdir(exist_ok=True)
    report = {"url": (ROOT / "index.html").as_uri(), "errors": [], "failed_requests": [], "network_requests": [], "viewports": []}
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe",
            headless=True,
        )
        page = browser.new_page(viewport={"width": 1440, "height": 960}, reduced_motion="reduce")
        page.on("pageerror", lambda error: report["errors"].append(str(error)))
        page.on("requestfailed", lambda request: report["failed_requests"].append({"url": request.url, "failure": request.failure}))
        page.on("request", lambda request: report["network_requests"].append(request.url) if request.url.startswith(("http:", "https:")) else None)
        page.goto(report["url"], wait_until="load")
        report["title"] = page.title()
        for width in [375, 768, 1024, 1440]:
            page.set_viewport_size({"width": width, "height": 960})
            page.screenshot(path=str(SHOTS / f"vision-{width}.png"), full_page=True)
            report["viewports"].append({"width": width, "tab": "vision", **page.evaluate("({viewport:innerWidth,scrollWidth:document.documentElement.scrollWidth,bodyWidth:document.body.scrollWidth})")})
            page.locator("#tab-evolution").click()
            page.screenshot(path=str(SHOTS / f"mapa-{width}.png"), full_page=True)
            report["viewports"].append({"width": width, "tab": "evolution", **page.evaluate("({viewport:innerWidth,scrollWidth:document.documentElement.scrollWidth,bodyWidth:document.body.scrollWidth})")})
            page.locator("#tab-vision").click()
        page.set_viewport_size({"width": 1440, "height": 960})
        report["dialogs"] = []
        for key in ["onboarding", "crm", "acquisition", "external"]:
            if key == "external":
                page.locator("#tab-evolution").click()
            trigger = page.locator(f'[data-module="{key}"]:visible').first
            trigger.click()
            report["dialogs"].append({"key": key, "text": page.locator("#module-dialog").inner_text(), "html": page.locator("#dialog-content").inner_html()})
            page.screenshot(path=str(SHOTS / f"modulo-{key}.png"), full_page=True)
            page.keyboard.press("Escape")
        browser.close()
    (OUT / "probe-resultados.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"errors": report["errors"], "failed_requests": report["failed_requests"], "network_requests": report["network_requests"], "viewports": report["viewports"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if "--flows" in sys.argv:
        from audit_flows import main as audit_flows
        audit_flows()
    else:
        main()
