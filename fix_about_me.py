import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    text = f.read()

# 1. REMOVE BENTO FROM HOME PAGE
bento_home_start = '<!-- ABOUT ME / EXPERIENCE BENTO GRID -->'
bento_home_end = '<section id="expertise-home"'

idx_b_start = text.find(bento_home_start)
idx_b_end = text.find(bento_home_end)

if idx_b_start != -1 and idx_b_end != -1:
    text = text[:idx_b_start] + text[idx_b_end:]
    print('REMOVED BENTO FROM HOME')
else:
    print('COULD NOT FIND BENTO IN HOME')

# 2. MATCH THE VISIONARY BLOCK IN PORTFOLIO
vis_start = '<section id="portfolio-about"'
vis_end_marker = 'PORTFOLIO SKILLS (CV INTEGRATION)'

idx_v_start = text.find(vis_start)
idx_v_end_marker = text.find(vis_end_marker)

if idx_v_start != -1 and idx_v_end_marker != -1:
    # Find the actual close of the section
    idx_v_end = text.rfind('<!--', idx_v_start, idx_v_end_marker)
    
    new_about = """<!-- PREMIUM ABOUT ME (PORTFOLIO CV) -->
            <section id="portfolio-about" class="py-24 px-6 md:px-12 max-w-7xl mx-auto relative z-30 border-t border-white/5">
                
                <div class="text-center mb-16" data-aos="fade-up">
                    <span class="uppercase tracking-[0.2em] text-cyan-400 text-xs font-bold mb-2 block">CV & Biography</span>
                    <h2 class="text-4xl md:text-5xl font-black text-white">About <span class="text-gradient-cyan-pink">Me</span></h2>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    
                    <!-- Bio & Identity Area (Takes 2 Columns) -->
                    <div data-aos="fade-right" data-aos-duration="1000" class="lg:col-span-2 bg-gradient-to-br from-white/[0.05] to-transparent border border-white/10 rounded-3xl p-8 md:p-10 relative overflow-hidden backdrop-blur-xl group">
                        <div class="absolute top-0 right-0 w-64 h-64 bg-cyan-500/10 rounded-full blur-[80px] pointer-events-none transition-all duration-700 group-hover:bg-cyan-500/20"></div>
                        
                        <div class="relative z-10">
                            <!-- Small avatar & greeting -->
                            <div class="flex items-center gap-6 mb-8">
                                <div class="w-16 h-16 rounded-2xl overflow-hidden border-2 border-white/10 shadow-[0_0_20px_rgba(255,255,255,0.05)]">
                                    <img src="images/profile.jpg" alt="Hazem Elerefy" class="w-full h-full object-cover">
                                </div>
                                <div>
                                    <h3 class="text-2xl font-bold text-white tracking-tight">Hazem Elerefy</h3>
                                    <div class="text-cyan-400 font-medium tracking-widest text-xs uppercase mt-1">Data Analyst</div>
                                </div>
                            </div>
                            
                            <!-- The actual CV statement -->
                            <div class="space-y-6 text-white/70 leading-relaxed text-[1.05rem]">
                                <p>
                                    I am a <strong class="text-white">Data Analyst</strong> with a robust <strong class="text-pink-400">Front-end Development background</strong>. I specialize in building high-fidelity dashboards, reports, and analytical systems that help stakeholders understand what is happening in the data and what they should focus on next.
                                </p>
                                <p>
                                    My workflow relies on profound technical execution using <strong class="text-cyan-400">SQL, Python, Power BI, and complex analytics workflows</strong>. However, what truly separates my work is my relentless focus on UI clarity. I don't just calculate numbers; I present them in a way that feels clear, practical, and visually irresistible.
                                </p>
                                <p>
                                    Because of my front-end expertise, I possess a refined eye for layout and interaction. This ensures that every dashboard I construct is not only mathematically flawless but functions as a premium digital experience.
                                </p>
                            </div>
                        </div>
                    </div>

                    <!-- Experience Timeline Column -->
                    <div data-aos="fade-left" data-aos-duration="1000" class="lg:col-span-1 bg-gradient-to-b from-white/[0.02] to-white/[0.005] border border-white/10 rounded-3xl p-8 md:p-10 relative overflow-hidden backdrop-blur-xl group">
                        <div class="absolute bottom-0 left-0 w-64 h-64 bg-pink-500/10 rounded-full blur-[80px] pointer-events-none transition-all duration-700 group-hover:bg-pink-500/20"></div>
                        
                        <h4 class="text-xl font-bold text-white mb-8 border-b border-white/10 pb-4">My <span class="text-pink-400">Journey</span></h4>
                        
                        <div class="space-y-8 relative before:absolute before:inset-0 before:ml-2 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-cyan-500 before:via-pink-500 before:to-transparent">
                            
                            <!-- EX 1 -->
                            <div class="relative flex items-start justify-between">
                                <div class="w-10 h-10 mt-1 absolute -left-[1.35rem] rounded-full bg-darkBase border-2 border-cyan-500 flex items-center justify-center text-cyan-400 text-xs shadow-[0_0_15px_rgba(6,182,212,0.4)] z-10">
                                    <i class="fas fa-briefcase"></i>
                                </div>
                                <div class="w-full ml-8">
                                    <div class="text-[10px] font-black uppercase tracking-[0.2em] text-cyan-400 bg-cyan-500/10 inline-block px-3 py-1 rounded-full border border-cyan-500/20 mb-2">Present</div>
                                    <h5 class="text-white font-bold text-lg mb-1">Data Analyst</h5>
                                    <div class="text-white/40 text-sm font-semibold mb-2">Digilians | MCIT</div>
                                    <p class="text-white/60 text-xs leading-relaxed">Architecting KPI dashboards, developing sophisticated SQL reporting queries, and deploying prompt engineering solutions.</p>
                                </div>
                            </div>
                            
                            <!-- EX 2 -->
                            <div class="relative flex items-start justify-between">
                                <div class="w-10 h-10 mt-1 absolute -left-[1.35rem] rounded-full bg-darkBase border-2 border-purple-500 flex items-center justify-center text-purple-400 text-xs shadow-[0_0_15px_rgba(168,85,247,0.4)] z-10">
                                    <i class="fas fa-code"></i>
                                </div>
                                <div class="w-full ml-8">
                                    <div class="text-[10px] font-black uppercase tracking-[0.2em] text-white/30 mb-2">2022 - 2023</div>
                                    <h5 class="text-white font-bold text-lg mb-1">Front-End Dev</h5>
                                    <div class="text-purple-400 font-bold text-xs mb-2">Udacity Nano Degree</div>
                                    <p class="text-white/60 text-xs leading-relaxed">Mastered the core Web stack (HTML5, CSS3, JS) to build responsive, API-integrated web apps. (GPA: 4)</p>
                                </div>
                            </div>
                            
                            <!-- EX 3 -->
                            <div class="relative flex items-start justify-between">
                                <div class="w-10 h-10 mt-1 absolute -left-[1.35rem] rounded-full bg-darkBase border-2 border-pink-500 flex items-center justify-center text-pink-400 text-xs shadow-[0_0_15px_rgba(236,72,153,0.4)] z-10">
                                    <i class="fas fa-graduation-cap"></i>
                                </div>
                                <div class="w-full ml-8">
                                    <div class="text-[10px] font-black uppercase tracking-[0.2em] text-white/30 mb-2">2020 - 2024</div>
                                    <h5 class="text-white font-bold text-lg mb-1">Bachelor of Laws</h5>
                                    <div class="text-pink-400 font-bold text-xs mb-2">Port Said University</div>
                                    <p class="text-white/60 text-xs leading-relaxed">Developed critical thinking, analytical reasoning, and complex logic patterns through Commercial and Corporate Law.</p>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </section>
            
            """
    
    text = text[:idx_v_start] + new_about + text[idx_v_end:]
    print('REPLACED VISIONARY WITH CV ABOUT ME')
else:
    print('COULD NOT FIND VISIONARY BLOCK IN PORTFOLIO')

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(text)
print('COMPLETED')
