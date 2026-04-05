import re
import sys

# The issue is that the portfolio block replacement deleted the closing div tags from the header
# and possibly wrapped the grid in a flex layout unintentionally because of unclosed tags in the hero section.

with open('d:/hazemelerefy website/my website/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's check exactly what the hero section closing looks like
match = text.find('        </div>\n\n        <!-- PORTFOLIO VIEW CONTENT -->')

if match != -1:
    print("Found PORTFOLIO VIEW CONTENT marker")
else:
    print("Could not find PORTFOLIO VIEW CONTENT marker, checking for Work/Projects Pipeline Section")

# The problem is here:
# 861:                         </div>
# 862:                     </div>
# 863:                 </div>
# 864:             </header>
# 866:             <!-- Work/Projects Pipeline Section -->

# Wait, the structure in the HTML is:
#         <!-- PORTFOLIO VIEW CONTENT -->
#         <div x-show="activeView === 'portfolio'">
#             <!-- Hero Section -->
#             <header id="portfolio-hero" ... > ... </header>
#             <section id="work" ... >
#               <div class="mb-32 ..."> ... </div>
#               <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 relative z-50 overflow-visible">
#                   <!-- Portfolio Filter Options -->

# Ah! The filter options are inside the global grid! 
# Line 878: <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 relative z-50 overflow-visible">
# And then on Line 882: <div class="flex justify-center mb-12" data-aos="fade-up">

# This means the filter options and the inner 6-card grid are all placed INSIDE the outer 3-column grid. 
# That's why everything is compressed into one tiny column!

# We need to close the first grid or remove it entirely if it's redundant.

# Let's fix this using exact string replacement.
bad_html = """                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 relative z-50 overflow-visible">
                    
                    
                    <!-- Portfolio Filter Options -->"""

good_html = """                <div class="relative z-50 overflow-visible w-full">
                    
                    
                    <!-- Portfolio Filter Options -->"""


if bad_html in text:
    new_text = text.replace(bad_html, good_html)
    with open('d:/hazemelerefy website/my website/index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Fixed layout bug: replaced outer grid with full width div.")
else:
    print("Could not find the bad html.")

# Also remove the trailing stray text at the end of the grid:
# \2 (Moved to end of Portfolio) -->

# Let's just find and remove that specific string if it exists.
stray_text = r"\2 (Moved to end of Portfolio) -->"
if stray_text in text:
    text = text.replace(stray_text, "")
    with open('d:/hazemelerefy website/my website/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Removed stray \\2 text.")

