from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path('cotizaciones/presentacion/index.html').resolve().as_uri()
out=Path('cotizaciones/presentacion/_revision')
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',headless=True)
 page=b.new_page(viewport={'width':1440,'height':900},device_scale_factor=1)
 page.goto(p); page.evaluate("document.querySelector('#vision').hidden=true;document.querySelector('#evolution').hidden=false")
 page.screenshot(path=str(out/'mapa-preliminar.png'),full_page=True)
 print('mapa',page.evaluate('document.documentElement.scrollWidth'))
 b.close()
