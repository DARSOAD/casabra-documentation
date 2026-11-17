from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path('cotizaciones/presentacion/index.html').resolve().as_uri(); out=Path('cotizaciones/presentacion/_revision')
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',headless=True)
 for w,h,n in [(1440,900,'desktop'),(375,812,'movil')]:
  page=b.new_page(viewport={'width':w,'height':h}); page.goto(p); page.locator('[data-module=onboarding]').first.click(); page.locator('[name=consent]').check(); page.locator('#onboarding-form button[type=submit]').click(); page.locator('#close-dialog').click()
  page.locator('[data-module=acquisition]').first.click(); page.screenshot(path=str(out/(n+'-acceso-recorrido.png')))
  page.locator('[data-action=demo-scroll]').click(); page.get_by_text('Ficha y documentos del expediente',exact=True).click(); page.locator('.demo-table').scroll_into_view_if_needed(); page.screenshot(path=str(out/(n+'-tabla.png')))
  print(n,'table',page.locator('.demo-table').is_visible(),'document width',page.evaluate('document.documentElement.scrollWidth'),'table',page.locator('.table-wrap').evaluate('(e)=>[e.clientWidth,e.scrollWidth]')); page.close()
 b.close()
