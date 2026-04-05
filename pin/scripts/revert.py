import sys

with open('d:/hazemelerefy website/my website/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Convert to 0-indexed line numbers for Python slicing
# Exp: 406-536 (inclusive) -> lines[405:536]
# Ecom card: 1225-1327 (inclusive) -> lines[1224:1327]
# Ecom modal: 2394-2496 (inclusive) -> lines[2393:2496]

# But note that deleting lines shifts the indices! It's better to recreate the file by skipping those ranges.
# Let's use the provided content line by line.

output_lines = []
for i, line in enumerate(lines):
    line_num = i + 1
    if 406 <= line_num <= 536: continue
    if 1225 <= line_num <= 1327: continue
    if 2394 <= line_num <= 2496: continue
    output_lines.append(line)

with open('d:/hazemelerefy website/my website/index.html', 'w', encoding='utf-8') as f:
    f.writelines(output_lines)

# Also revert app.js changes manually since they are small
with open('d:/hazemelerefy website/my website/js/app.js', 'r', encoding='utf-8') as f:
    app_lines = f.readlines()

new_app_lines = []
skip = False
for line in app_lines:
    if 'ecommerce: {' in line:
        skip = True
    if skip and '}' in line and 'ecommerce' not in line: # simplistic tracking, wait, safer to just replace
        pass

# let's write a safer app.js replace
with open('d:/hazemelerefy website/my website/js/app.js', 'r', encoding='utf-8') as f:
    app_content = f.read()

app_content = app_content.replace("""                    },
                    ecommerce: {
                        score: 0,
                        hoverScore: 0,
                        totalVotes: 245,
                        average: 4.9
                    }""", """                    }""")

with open('d:/hazemelerefy website/my website/js/app.js', 'w', encoding='utf-8') as f:
    f.write(app_content)

print("Reverted successfully")
