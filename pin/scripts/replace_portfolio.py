import os
import re
import subprocess

current_html_path = r'd:\hazemelerefy website\my website\index.html'

# 1. Get the pristine original index.html from Git
try:
    pristine_html = subprocess.check_output(['git', 'show', 'HEAD:index.html'], cwd=os.path.dirname(current_html_path)).decode('utf-8')
except subprocess.CalledProcessError:
    print("Git show failed!")
    exit(1)

# 2. Extract the pristine Workspace section from original HTML
# The Workspace section contains: <section class="py-20 px-6 ..."> ... <div x-show="workspaceTab === 'frontend'"> ... </section>
# Let's extract the two grids: frontend and analytics
# We will use regex to find all the <a> tags inside the projects-grid divs.

def transform_card(match):
    anchor_opening = match.group(1) # e.g. <a href="..." target="_blank" class "...">
    inner_html = match.group(2) # inner contents of the anchor tag
    
    # We strip the original classes and substitute our Aceternity Wrapper classes.
    # We'll just grab the href
    href_match = re.search(r'href="([^"]+)"', anchor_opening)
    href = href_match.group(1) if href_match else "#"
    
    # The new fully native Tailwind Aceternity Bento Card:
    return f"""<a href="{href}" target="_blank" class="group relative overflow-hidden rounded-2xl bg-[#1e293b] p-[2px] transition-all duration-300 hover:scale-[1.02] shadow-[0px_1px_10px_rgba(0,0,0,0.5)] block">
                <!-- Aceternity Animated Gradient Border layers -->
                <div class="absolute inset-0 z-0 bg-gradient-to-br from-pink-500 via-indigo-500 to-cyan-500 opacity-60"></div>
                <div class="absolute inset-0 z-0 animate-[pulse_5s_ease-in-out_infinite] bg-gradient-to-tr from-cyan-400 via-purple-500 to-yellow-400 opacity-40"></div>
                
                <!-- Noise Overlay Layer -->
                <div class="absolute inset-0 z-0 bg-[url('https://assets.aceternity.com/noise.webp')] opacity-20 mix-blend-overlay"></div>

                <!-- Internal Card Content -->
                <div class="relative z-10 flex h-full min-h-[320px] flex-col overflow-hidden rounded-xl bg-cardBase dark:bg-[#15151D] p-6 text-left transition-colors duration-500 group-hover:bg-[#101018]">
                    {inner_html.strip()}
                </div>
            </a>"""

# In the pristine HTML, let's find the entire <div class="projects-grid"> blocks
grid_pattern = r'(<div class="projects-grid">\s*)(.*?)(\s*</div>\s*</div>\s*<!-- Analytics Tab -->)'
frontend_match = re.search(grid_pattern, pristine_html, re.DOTALL)

if not frontend_match:
    print("Could not find frontend grid in pristine HTML!")
else:
    frontend_inner = frontend_match.group(2)
    new_frontend_inner = re.sub(r'(<a\s+href="[^"]*"\s+target="_blank"[^>]*>)(.*?)(</a>)', transform_card, frontend_inner, flags=re.DOTALL)
    pristine_html = pristine_html.replace(frontend_inner, new_frontend_inner)

analytics_pattern = r'(<!-- Analytics Tab -->\s*<div x-show="workspaceTab === \'analytics\'".*?<div class="projects-grid">\s*)(.*?)(\s*</div>\s*</div>\s*</section>)'
analytics_match = re.search(analytics_pattern, pristine_html, re.DOTALL)

if not analytics_match:
    print("Could not find analytics grid in pristine HTML!")
else:
    analytics_inner = analytics_match.group(2)
    new_analytics_inner = re.sub(r'(<a\s+href="[^"]*"\s+target="_blank"[^>]*>)(.*?)(</a>)', transform_card, analytics_inner, flags=re.DOTALL)
    pristine_html = pristine_html.replace(analytics_inner, new_analytics_inner)

# 3. Read Current HTML
with open(current_html_path, 'r', encoding='utf-8') as f:
    current_html = f.read()

# Replace the broken workspace section in current HTML with the newly built pristine workspace section
# The workspace section starts at <!-- My Workspace Section --> and ends at <!-- ═══════════════════ QUICK CTA BANNER ═══════════════════ -->
workspace_re = r'(<!-- My Workspace Section -->.*?</section>\s*)(?=<!-- ═══════════════════ QUICK CTA BANNER ═══════════════════ -->)'
current_workspace_match = re.search(workspace_re, current_html, re.DOTALL)
pristine_workspace_match = re.search(workspace_re, pristine_html, re.DOTALL)

if current_workspace_match and pristine_workspace_match:
    new_html = current_html.replace(current_workspace_match.group(1), pristine_workspace_match.group(1))
    with open(current_html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully injected the new Aceternity Bento Cards!")
else:
    print("Regex failed to locate workspace boundaries!")
