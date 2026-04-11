"""Patch index.html to inject extreme.css and extreme.js"""

with open("index_original.html", "r", encoding="utf-8") as f:
    content = f.read()

# Inject extreme.css before </head>
css_tag = '    <!-- Extreme UI/UX Layer -->\n    <link rel="stylesheet" href="css/extreme.css">\n'
if 'css/extreme.css' not in content:
    content = content.replace("</head>", css_tag + "</head>", 1)
    print("CSS injected OK")
else:
    print("CSS already present")

# Inject extreme.js before </body>
js_tag = '\n    <!-- Extreme UI/UX Engine -->\n    <script src="js/extreme.js" defer></script>\n'
if 'js/extreme.js' not in content:
    content = content.replace("</body>", js_tag + "</body>", 1)
    print("JS injected OK")
else:
    print("JS already present")

with open("index_patched.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Output: index_patched.html (%d bytes)" % len(content))
