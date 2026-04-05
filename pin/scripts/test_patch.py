import os
import subprocess

html_path = r'd:\hazemelerefy website\my website\index.html'

pristine = subprocess.check_output(['git', 'show', 'HEAD:index.html'], cwd=os.path.dirname(html_path)).decode('utf-8')

start_idx = pristine.find('<!-- My Workspace Section -->')
if start_idx == -1:
    start_idx = pristine.find('My Workspace')
    start_idx = pristine.rfind('<section', 0, start_idx)

end_idx = pristine.find('<!-- ═══════════════════ QUICK CTA BANNER ═══════════════════ -->')
if end_idx == -1:
    end_idx = pristine.find('QUICK CTA BANNER')
    end_idx = pristine.rfind('<!--', 0, end_idx)

original_workspace = pristine[start_idx:end_idx]
print(f"Extracted {len(original_workspace)} chars of original workspace.")

current = open(html_path, 'r', encoding='utf-8').read()
curr_start = current.find('<!-- My Workspace Section -->')
if curr_start == -1:
    curr_start = current.find('My Workspace')
    curr_start = current.rfind('<section', 0, curr_start)

curr_end = current.find('<!-- ═══════════════════ QUICK CTA BANNER ═══════════════════ -->')
if curr_end == -1:
    curr_end = current.find('QUICK CTA BANNER')
    curr_end = current.rfind('<!--', 0, curr_end)

if start_idx != -1 and end_idx != -1 and curr_start != -1 and curr_end != -1:
    # Let's apply the Aceternity modifications specifically to `original_workspace` string!
    # Because original_workspace contains perfectly pristine anchor tags, we can just replace `<a href="..." ... group">`
    import re
    
    def transform_card(match):
        anchor_opening = match.group(1) # e.g. <a href="..." target="_blank"\n class="block bg-cardBase rounded-2xl p-6 ... transition-colors group relative overflow-hidden">
        inner_html = match.group(2) # Inner content
        
        href_match = re.search(r'href="([^"]+)"', anchor_opening)
        href = href_match.group(1) if href_match else "#"
        
        return f"""<a href="{href}" target="_blank" class="group relative overflow-hidden rounded-2xl bg-[#1e293b] p-[2px] transition-all duration-300 hover:scale-[1.02] shadow-[0px_1px_10px_rgba(0,0,0,0.5)] block hover:border-none">
                    <!-- Aceternity Animated Gradient Border layers -->
                    <div class="absolute inset-0 z-0 bg-gradient-to-br from-pink-500 via-indigo-500 to-cyan-500 opacity-70"></div>
                    <div class="absolute inset-0 z-0 animate-[pulse_5s_ease-in-out_infinite] bg-gradient-to-tr from-cyan-400 via-purple-500 to-yellow-400 opacity-50"></div>
                    
                    <!-- Noise Overlay Layer -->
                    <div class="absolute inset-0 z-0 bg-[url('https://assets.aceternity.com/noise.webp')] opacity-20 mix-blend-overlay"></div>

                    <!-- Internal Card Content -->
                    <div class="relative z-10 flex h-full min-h-[320px] flex-col overflow-hidden rounded-xl bg-cardBase dark:bg-[#15151D] p-6 text-left transition-colors duration-500 group-hover:bg-[#101018]">
{inner_html}
                    </div>
                </a>"""

    # We match robustly
    pattern = r'(<a\s+href="[^"]*"\s+target="_blank"(?:[^>]*class="[^"]*bg-cardBase[^"]*")[^>]*>)(.*?)(</a>)'
    new_workspace = re.sub(pattern, transform_card, original_workspace, flags=re.DOTALL)
    
    new_html = current[:curr_start] + new_workspace + current[curr_end:]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESS: HTML injected beautifully!")
else:
    print("Failed to find boundaries in one of the files")
