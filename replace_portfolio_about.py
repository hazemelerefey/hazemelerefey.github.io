import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    text = f.read()

start_marker = '<!-- ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ  PREMIUM ABOUT ME'
end_marker = '<!-- ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ ظـ  PORTFOLIO SKILLS (CV INTEGRATION)'

start_idx = text.find('<!--') # Let me just find the markers dynamically without hardcoding weird characters.
# The user's repo has weird Arabic characters in comments.
# Let's search by section id
start_idx = text.find('<section id="portfolio-about"')
end_idx = text.find('<section class="py-16 px-6 md:px-12 max-w-7xl mx-auto border-t border-cardBorder relative z-40">')

# Wait, finding end_idx might be tricky. Let's find '<!--' before PORTFOLIO SKILLS
portfolio_skills_idx = text.find('PORTFOLIO SKILLS (CV INTEGRATION)')
if portfolio_skills_idx != -1:
    end_idx = text.rfind('<!--', 0, portfolio_skills_idx)


new_about_me = """<section id="portfolio-about" class="py-32 px-6 md:px-12 max-w-7xl mx-auto relative z-30">
                <!-- Massive Typography Background -->
                <div class="absolute inset-0 flex items-center justify-center opacity-[0.02] pointer-events-none overflow-hidden select-none">
                    <h2 class="text-[15vw] font-black text-white whitespace-nowrap">VISIONARY</h2>
                </div>

                <div class="relative z-10 flex flex-col items-center text-center">
                    
                    <div data-aos="fade-up" data-aos-duration="1000">
                        <span class="px-4 py-2 rounded-full border border-pink-500/30 bg-pink-500/10 text-pink-400 text-xs font-bold tracking-[0.2em] uppercase mb-8 inline-block shadow-[0_0_20px_rgba(236,72,153,0.15)]">The Philosophy</span>
                    </div>

                    <h3 data-aos="fade-up" data-aos-duration="1000" data-aos-delay="100" class="text-4xl md:text-6xl font-black text-white leading-tight max-w-4xl mb-12">
                        I bridge the gap between <span class="text-gradient-cyan-pink">Deep Analytics</span> and <span class="text-gradient-cyan-pink">Pixel-Perfect Interfaces</span>.
                    </h3>

                    <!-- Bento-Style Feature Row instead of heavy text -->
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-5xl mt-8">
                        
                        <!-- Block 1 -->
                        <div data-aos="fade-up" data-aos-duration="1000" data-aos-delay="200" class="bg-gradient-to-b from-white/[0.04] to-transparent border border-white/10 rounded-3xl p-8 hover:border-cyan-500/30 transition-all duration-500 group relative overflow-hidden backdrop-blur-xl">
                            <div class="absolute top-0 right-0 w-32 h-32 bg-cyan-500/10 rounded-full blur-[50px] group-hover:bg-cyan-500/20 transition-all duration-700"></div>
                            <div class="w-12 h-12 bg-cyan-500/10 border border-cyan-500/20 rounded-2xl flex items-center justify-center text-cyan-400 text-xl mx-auto mb-6 group-hover:scale-110 transition-transform duration-500">
                                <i class="fas fa-database"></i>
                            </div>
                            <h4 class="text-white font-bold text-xl mb-3">Analytical Rigor</h4>
                            <p class="text-white/50 text-sm leading-relaxed">Extracting deep insights from raw data using advanced SQL, Python, and statistical intelligence.</p>
                        </div>

                        <!-- Block 2 -->
                        <div data-aos="fade-up" data-aos-duration="1000" data-aos-delay="300" class="bg-gradient-to-b from-white/[0.04] to-transparent border border-white/10 rounded-3xl p-8 hover:border-purple-500/30 transition-all duration-500 group relative overflow-hidden backdrop-blur-xl md:-translate-y-8">
                            <div class="absolute top-0 right-0 w-32 h-32 bg-purple-500/10 rounded-full blur-[50px] group-hover:bg-purple-500/20 transition-all duration-700"></div>
                            <div class="w-12 h-12 bg-purple-500/10 border border-purple-500/20 rounded-2xl flex items-center justify-center text-purple-400 text-xl mx-auto mb-6 group-hover:scale-110 transition-transform duration-500">
                                <i class="fas fa-layer-group"></i>
                            </div>
                            <h4 class="text-white font-bold text-xl mb-3">Structural Clarity</h4>
                            <p class="text-white/50 text-sm leading-relaxed">Designing reporting architecture that transforms overwhelming metrics into intuitive, actionable narratives.</p>
                        </div>

                        <!-- Block 3 -->
                        <div data-aos="fade-up" data-aos-duration="1000" data-aos-delay="400" class="bg-gradient-to-b from-white/[0.04] to-transparent border border-white/10 rounded-3xl p-8 hover:border-pink-500/30 transition-all duration-500 group relative overflow-hidden backdrop-blur-xl">
                            <div class="absolute top-0 right-0 w-32 h-32 bg-pink-500/10 rounded-full blur-[50px] group-hover:bg-pink-500/20 transition-all duration-700"></div>
                            <div class="w-12 h-12 bg-pink-500/10 border border-pink-500/20 rounded-2xl flex items-center justify-center text-pink-400 text-xl mx-auto mb-6 group-hover:scale-110 transition-transform duration-500">
                                <i class="fas fa-paint-brush"></i>
                            </div>
                            <h4 class="text-white font-bold text-xl mb-3">Frontend Mastery</h4>
                            <p class="text-white/50 text-sm leading-relaxed">Deploying complex insights within pixel-perfect, premium web interfaces that demand attention.</p>
                        </div>

                    </div>
                </div>
            </section>
            
            """

if start_idx != -1 and end_idx != -1:
    # rewind to the exact comment block start for portfolio-about
    actual_start = text.rfind('<!--', 0, start_idx)
    if actual_start != -1:
        start_idx = actual_start
        
    final_text = text[:start_idx] + new_about_me + text[end_idx:]
    with codecs.open('index.html', 'w', 'utf-8') as f:
        f.write(final_text)
    print("SUCCESS: Replaced Portfolio About me")
else:
    print("FAIL: Could not find markers. start=", start_idx, "end=", end_idx)
