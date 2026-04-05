import re

file_path = r'd:\hazemelerefy website\my website\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# We want to transform the "block bg-cardBase rounded-2xl p-6 border border-cardBorder hover:border-cyan-500/50 transition-colors group relative overflow-hidden" 
# to the noise wrapper.

# Regex to find each card:
# <a href="(.*?)" target="_blank"\s+class="block bg-cardBase rounded-2xl p-6 border border-cardBorder hover:border-.*?-500/50 transition-colors group relative overflow-hidden">
#   <div class="absolute top-0 right-0 w-32 h-32 bg-.*?-500/10 rounded-full blur-\[40px\] group-hover:bg-.*?-500/20 transition-all">\s*</div>
#   <div class="flex justify-between items-start mb-4">
#   ...
#   </div>
# </a>

pattern = r'(<a href="[^"]*"\s+target="_blank"\s+)class="block bg-cardBase rounded-2xl p-6 border border-cardBorder hover:border-([a-z]+)-500/50 transition-colors group relative overflow-hidden">\s*<div\s*class="absolute top-0 right-0 w-32 h-32 bg-\2-500/10 rounded-full blur-\[40px\] group-hover:bg-\2-500/20 transition-all">\s*</div>'

def replace_func(m):
    start_tag = m.group(1)
    color = m.group(2) # cyan or pink
    
    # We replace the anchor tag classes and inner container
    return (start_tag + 'class="noise-card-wrapper block">\n' +
            '                <div class="noise-layer noise-gradient-1"></div>\n' +
            '                <div class="noise-layer noise-gradient-2"></div>\n' +
            '                <div class="noise-layer noise-gradient-3"></div>\n' +
            '                <div class="noise-strip"></div>\n' +
            '                <div class="noise-overlay"></div>\n' +
            f'                <div class="noise-card-inner p-6 border-transparent hover:border-{color}-500/50 transition-colors duration-500 group relative">')

# But we also need to close the `noise-card-inner` `</div>` before `</a>`
# To do this safely, we can just find the closing tags of the blocks.
# Let's just do a simpler string replacement for the opening of the card:

new_html = re.sub(pattern, replace_func, html)

# Now we have unclosed <div class="noise-card-inner">! We must add an extra </div> before each </a> in that grid section.
# How to know which </a>?
# All <a> in the workspace blocks have: 
#                     <span class="flex items-center gap-1"><i class="fas fa-code-branch"></i> \d+</span>
#                 </div>
#             </a>
# We can regex that too:
new_html = re.sub(r'(<span class="flex items-center gap-1"><i class="fas fa-code-branch"></i> \d+</span>\s*</div>)', r'\1\n                </div>', new_html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("HTML cards transformed successfully!")
