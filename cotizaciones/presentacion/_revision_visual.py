from pathlib import Path
from playwright.sync_api import sync_playwright
p = Path('cotizaciones/presentacion/index.html').resolve().as_uri()
out = Path('cotizaciones/presentacion/_revision'); out.mkdir(exist_ok=True)
with sync_playwright() as pw:
 b = pw.chromium.launch(executable_path=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe', headless=True)
 for width,height,name in [(1440,900,'portada'),(375,812,'movil')]:
  page=b.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
  page.goto(p,wait_until='load'); page.screenshot(path=str(out / (name+'.png')),full_page=False)
  print(name,page.title(),page.evaluate('document.documentElement.scrollWidth'),width)
  page.close()
 b.close()
