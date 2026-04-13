import codecs, re

with codecs.open('index.html', 'r', 'utf-8') as f:
    text = f.read()

changes = []

# ====================================================
# 1. REPLACE ALL hazemkhaled53@gmail.com -> hazemelerefy@gmail.com
# ====================================================
old_email = 'hazemkhaled53@gmail.com'
new_email = 'hazemelerefy@gmail.com'
count_email = text.count(old_email)
text = text.replace(old_email, new_email)
changes.append(f"Replaced {count_email} email references")

# Also fix khamsat link
text = text.replace('hazemkhaled53', 'hazemelerefy')
changes.append("Fixed khamsat username too")

# ====================================================
# 2. REMOVE OLD CTA BANNER "Ready to bring your ideas to life?"
# Lines 772-797 area
# ====================================================
cta_start_marker = '\r\n            <!-- \u0638\u0640\u0638\u0640\u0638\u0640\u0638\u0640\u0638\u0640\u0638\u0640\u0638\u0640\u0638\u0640\u0638\u0640\u0638\u0640\u0638\u0640\u0638\u0640\u0638\u0640\u0638\u0640\u0638\u0640\u0638\u0640\u0638\u0640\u0638\u0640\u0638\u0640 QUICK CTA BANNER'
cta_end = '\r\n            </section>\r\n\r\n        </div>\r\n'
cta_end_replace = '\r\n        </div>\r\n'

idx_cta = text.find(cta_start_marker)
if idx_cta != -1:
    # Find the section end
    idx_cta_end = text.find('</section>\r\n\r\n        </div>\r\n', idx_cta)
    if idx_cta_end != -1:
        end_pos = idx_cta_end + len('</section>\r\n')
        text = text[:idx_cta] + text[end_pos:]
        changes.append("Removed old Quick CTA Banner")
    else:
        changes.append("WARN: Could not find CTA end marker")
else:
    changes.append("WARN: Could not find CTA start marker")

# ====================================================
# 3. REPLACE FEATURED PROJECTS (home page)
# Both projects navigate to portfolio, no GitHub links
# ====================================================
feat_start = text.find('FEATURED PROJECTS')
if feat_start == -1:
    changes.append("WARN: Could not find FEATURED PROJECTS")
else:
    # Find section start
    section_start = text.rfind('<section', 0, feat_start)
    # Find section end
    section_end = text.find('</section>', feat_start)
    if section_start != -1 and section_end != -1:
        section_end += len('</section>\r\n')
        new_featured = """<section class="py-24 px-6 md:px-12 max-w-7xl mx-auto border-t border-cardBorder relative z-10">
                <div class="text-center mb-16" data-aos="fade-up">
                    <span class="uppercase tracking-[0.3em] text-cyan-400 text-[10px] font-bold mb-4 block">Featured Work</span>
                    <h2 class="text-4xl md:text-5xl font-bold text-white">Recent <span class="text-gradient-cyan-pink">Projects</span></h2>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <!-- Project 1: JobPulse -->
                    <div data-aos="fade-up" @click="navTo('portfolio')"
                        class="group relative rounded-3xl overflow-hidden bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] hover:border-cyan-500/30 transition-all duration-500 cursor-pointer backdrop-blur-xl">
                        <div class="absolute top-0 right-0 w-48 h-48 bg-cyan-500/5 rounded-full blur-[80px] group-hover:bg-cyan-500/15 transition-all duration-700"></div>
                        <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-cyan-500/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                        <div class="p-6 relative z-10">
                            <div class="rounded-2xl overflow-hidden mb-6 border border-white/[0.06] shadow-xl bg-[#020617]">
                                <img src="images/jobpulse-hero.svg" alt="JobPulse Dashboard" loading="lazy"
                                    class="w-full h-48 object-cover transform group-hover:scale-105 transition-transform duration-700">
                            </div>
                            <div class="flex items-center gap-2 mb-3 flex-wrap">
                                <span class="text-[9px] font-black uppercase tracking-widest text-cyan-400/70 bg-cyan-500/10 border border-cyan-500/10 px-3 py-1 rounded-full">Next.js</span>
                                <span class="text-[9px] font-black uppercase tracking-widest text-emerald-400/70 bg-emerald-500/10 border border-emerald-500/10 px-3 py-1 rounded-full">Intelligence</span>
                                <span class="text-[9px] font-black uppercase tracking-widest text-pink-400/70 bg-pink-500/10 border border-pink-500/10 px-3 py-1 rounded-full">Flagship</span>
                            </div>
                            <h3 class="text-lg font-bold text-white mb-2 group-hover:text-cyan-400 transition-colors">JobPulse</h3>
                            <p class="text-white/35 text-sm leading-relaxed">A premium job market intelligence product that turns hiring data into readable signals around role demand, salary movement, and skill momentum.</p>
                            <div class="mt-4 flex items-center text-sm font-bold text-cyan-400/60 gap-2 group-hover:text-cyan-400 group-hover:translate-x-1 transition-all">
                                View Project <i class="fas fa-arrow-right text-[10px]"></i>
                            </div>
                        </div>
                    </div>

                    <!-- Project 2: Global Sales -->
                    <div data-aos="fade-up" data-aos-delay="100" @click="navTo('portfolio')"
                        class="group relative rounded-3xl overflow-hidden bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] hover:border-purple-500/30 transition-all duration-500 cursor-pointer backdrop-blur-xl">
                        <div class="absolute top-0 right-0 w-48 h-48 bg-purple-500/5 rounded-full blur-[80px] group-hover:bg-purple-500/15 transition-all duration-700"></div>
                        <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-purple-500/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                        <div class="p-6 relative z-10">
                            <div class="rounded-2xl overflow-hidden mb-6 border border-white/[0.06] shadow-xl">
                                <img src="images/global-sales-dashboard.png" alt="Global Sales Dashboard" loading="lazy"
                                    class="w-full h-48 object-cover transform group-hover:scale-105 transition-transform duration-700">
                            </div>
                            <div class="flex items-center gap-2 mb-3">
                                <span class="text-[9px] font-black uppercase tracking-widest text-purple-400/70 bg-purple-500/10 border border-purple-500/10 px-3 py-1 rounded-full">Power BI</span>
                                <span class="text-[9px] font-black uppercase tracking-widest text-amber-400/70 bg-amber-500/10 border border-amber-500/10 px-3 py-1 rounded-full">Finance</span>
                            </div>
                            <h3 class="text-lg font-bold text-white mb-2 group-hover:text-purple-400 transition-colors">Global Sales Performance</h3>
                            <p class="text-white/35 text-sm leading-relaxed">Executive-level dashboard overseeing global market performance with geographic drill-downs and financial mapping.</p>
                            <div class="mt-4 flex items-center text-sm font-bold text-purple-400/60 gap-2 group-hover:text-purple-400 group-hover:translate-x-1 transition-all">
                                View Project <i class="fas fa-arrow-right text-[10px]"></i>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
"""
        text = text[:section_start] + new_featured + text[section_end:]
        changes.append("Rebuilt Featured Projects with premium glassmorphic cards (navigate to portfolio)")

# ====================================================
# 4. REPLACE "How I Work" section in Portfolio
# ====================================================
how_start = text.find('How I Work')
if how_start == -1:
    changes.append("WARN: How I Work not found")
else:
    process_start = text.rfind('<section id="process"', 0, how_start)
    process_end = text.find('</section>\r\n', how_start)
    if process_start != -1 and process_end != -1:
        process_end += len('</section>\r\n')
        new_process = """<section class="py-24 px-6 md:px-12 max-w-7xl mx-auto border-t border-white/[0.05]">
                        <div class="text-center mb-16" data-aos="fade-up">
                            <span class="uppercase tracking-[0.3em] text-purple-400 text-[10px] font-bold mb-4 block">My Process</span>
                            <h2 class="text-4xl md:text-5xl font-bold text-white">How I <span class="text-gradient-cyan-pink">Work</span></h2>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6" data-aos="fade-up" data-aos-delay="100">
                            <!-- Step 1 -->
                            <div class="relative group">
                                <div class="bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-7 hover:border-cyan-500/30 transition-all duration-500 backdrop-blur-xl h-full">
                                    <div class="absolute top-0 right-0 w-32 h-32 bg-cyan-500/5 rounded-full blur-[60px] group-hover:bg-cyan-500/15 transition-all duration-700"></div>
                                    <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-cyan-500/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                                    <div class="relative z-10">
                                        <div class="text-[10px] font-black text-cyan-400/40 uppercase tracking-[0.3em] mb-4">Step 01</div>
                                        <div class="w-12 h-12 rounded-2xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center mb-5 shadow-[0_0_15px_rgba(6,182,212,0.1)]">
                                            <i class="fas fa-comments text-cyan-400 text-lg"></i>
                                        </div>
                                        <h3 class="text-lg font-bold text-white mb-2">Discovery & Planning</h3>
                                        <p class="text-white/30 text-sm leading-relaxed">Understanding your vision, goals, and requirements through collaborative research and strategic planning.</p>
                                    </div>
                                </div>
                                <div class="hidden lg:block absolute top-1/2 -right-3 w-6 h-[1px] bg-gradient-to-r from-white/10 to-transparent"></div>
                            </div>

                            <!-- Step 2 -->
                            <div class="relative group">
                                <div class="bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-7 hover:border-purple-500/30 transition-all duration-500 backdrop-blur-xl h-full">
                                    <div class="absolute top-0 right-0 w-32 h-32 bg-purple-500/5 rounded-full blur-[60px] group-hover:bg-purple-500/15 transition-all duration-700"></div>
                                    <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-purple-500/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                                    <div class="relative z-10">
                                        <div class="text-[10px] font-black text-purple-400/40 uppercase tracking-[0.3em] mb-4">Step 02</div>
                                        <div class="w-12 h-12 rounded-2xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center mb-5 shadow-[0_0_15px_rgba(168,85,247,0.1)]">
                                            <i class="fab fa-figma text-purple-400 text-lg"></i>
                                        </div>
                                        <h3 class="text-lg font-bold text-white mb-2">Design & Prototyping</h3>
                                        <p class="text-white/30 text-sm leading-relaxed">Creating high-fidelity Figma designs focusing on modern aesthetics, glassmorphism, and intuitive user journeys.</p>
                                    </div>
                                </div>
                                <div class="hidden lg:block absolute top-1/2 -right-3 w-6 h-[1px] bg-gradient-to-r from-white/10 to-transparent"></div>
                            </div>

                            <!-- Step 3 -->
                            <div class="relative group">
                                <div class="bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-7 hover:border-pink-500/30 transition-all duration-500 backdrop-blur-xl h-full">
                                    <div class="absolute top-0 right-0 w-32 h-32 bg-pink-500/5 rounded-full blur-[60px] group-hover:bg-pink-500/15 transition-all duration-700"></div>
                                    <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-pink-500/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                                    <div class="relative z-10">
                                        <div class="text-[10px] font-black text-pink-400/40 uppercase tracking-[0.3em] mb-4">Step 03</div>
                                        <div class="w-12 h-12 rounded-2xl bg-pink-500/10 border border-pink-500/20 flex items-center justify-center mb-5 shadow-[0_0_15px_rgba(236,72,153,0.1)]">
                                            <i class="fas fa-code text-pink-400 text-lg"></i>
                                        </div>
                                        <h3 class="text-lg font-bold text-white mb-2">Development & Data</h3>
                                        <p class="text-white/30 text-sm leading-relaxed">Building the frontend with React/Tailwind and connecting it to scalable databases or ML pipelines.</p>
                                    </div>
                                </div>
                                <div class="hidden lg:block absolute top-1/2 -right-3 w-6 h-[1px] bg-gradient-to-r from-white/10 to-transparent"></div>
                            </div>

                            <!-- Step 4 -->
                            <div class="relative group">
                                <div class="bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-7 hover:border-emerald-500/30 transition-all duration-500 backdrop-blur-xl h-full">
                                    <div class="absolute top-0 right-0 w-32 h-32 bg-emerald-500/5 rounded-full blur-[60px] group-hover:bg-emerald-500/15 transition-all duration-700"></div>
                                    <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-emerald-500/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                                    <div class="relative z-10">
                                        <div class="text-[10px] font-black text-emerald-400/40 uppercase tracking-[0.3em] mb-4">Step 04</div>
                                        <div class="w-12 h-12 rounded-2xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center mb-5 shadow-[0_0_15px_rgba(52,211,153,0.1)]">
                                            <i class="fas fa-rocket text-emerald-400 text-lg"></i>
                                        </div>
                                        <h3 class="text-lg font-bold text-white mb-2">Testing & Deployment</h3>
                                        <p class="text-white/30 text-sm leading-relaxed">Ensuring optimal performance across all devices and deploying with CI/CD for seamless updates.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
"""
        text = text[:process_start] + new_process + text[process_end:]
        changes.append("Rebuilt How I Work as premium 4-column card grid")

# ====================================================
# 5. FOOTER: Add LinkedIn to "Get in Touch" 
# ====================================================
get_in_touch_marker = '<h4 class="text-[10px] font-black uppercase tracking-[0.25em] text-white/30 mb-5">Get in Touch</h4>'
linkedin_link = """<li>
                            <a href="https://linkedin.com/in/hazemelerefy" target="_blank" rel="noopener noreferrer" class="text-sm text-white/25 hover:text-white transition-colors flex items-center gap-2 cursor-pointer">
                                <i class="fab fa-linkedin-in text-[10px] text-[#0A66C2]/60"></i> LinkedIn Profile
                            </a>
                        </li>
                        <li>"""

# Find "Get in Touch" and insert LinkedIn after the first <li>
idx_git = text.find(get_in_touch_marker)
if idx_git != -1:
    first_li = text.find('<li>', idx_git)
    if first_li != -1:
        text = text[:first_li] + linkedin_link + text[first_li + len('<li>'):]
        changes.append("Added LinkedIn to Get in Touch footer links")

# ====================================================
# 6. MAKE FOOTER ONLY SHOW on home/portfolio (hide on workspace/services)
# ====================================================
old_footer_tag = '<footer class="relative border-t border-white/[0.05] bg-[#050508]">'
new_footer_tag = '<footer x-show="activeView !== \'workspace\' && activeView !== \'services\'" x-transition class="relative border-t border-white/[0.05] bg-[#050508]">'
if old_footer_tag in text:
    text = text.replace(old_footer_tag, new_footer_tag)
    changes.append("Footer now hidden on Workspace and Services pages")

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(text)

for c in changes:
    print(c)
print("\nDONE - All changes applied")
