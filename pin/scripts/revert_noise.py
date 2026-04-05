import os
import shutil

html_bak = r'd:\hazemelerefy website\my website\index.html.bak'
html_main = r'd:\hazemelerefy website\my website\index.html'

if os.path.exists(html_bak):
    shutil.copy2(html_bak, html_main)
    print("Restored index.html from backup!")
else:
    print("No backup found!")

css_path = r'd:\hazemelerefy website\my website\css\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

split_token = '/* ═══════════════════ ACETERNITY NOISE CARDS ═══════════════════ */'
if split_token in css:
    css = css.split(split_token)[0].strip()
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css + '\n')
    print("Cleaned style.css")
else:
    print("CSS token not found.")
