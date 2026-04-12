import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    text = f.read()

start_marker = '<!-- Experience & Education Section -->'
end_marker = '<!-- Work Process Section (Moved to end of Portfolio) -->'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

bento_html = """<!-- ABOUT ME / EXPERIENCE BENTO GRID -->
                    <section id="about-me-bento" class="py-24 max-w-7xl mx-auto border-t border-cardBorder relative z-10 w-full overflow-hidden">
                        
                        <div class="text-center mb-16" data-aos="fade-up">
                            <span class="uppercase tracking-[0.2em] text-cyan-400 text-xs font-bold mb-2 block">Who Am I</span>
                            <h2 class="text-4xl md:text-5xl font-bold text-white">My <span class="text-gradient-cyan-pink">Journey</span></h2>
                        </div>

                        <!-- BENTO GRID CONTAINER -->
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 relative z-10 px-6 lg:px-0">
                            
                            <!-- BENTO BOX 1: BIO (Col Span 2) -->
                            <div data-aos="fade-up" data-aos-duration="800" class="md:col-span-2 group relative bg-[#0a0a0a] border border-white/5 p-8 md:p-10 rounded-[2rem] hover:border-cyan-500/30 transition-all duration-500 shadow-[0_20px_40px_-15px_rgba(0,0,0,0.8)] overflow-hidden">
                                <div class="absolute -top-32 -left-32 w-64 h-64 bg-cyan-500/10 rounded-full blur-[80px] group-hover:bg-cyan-500/20 transition-colors duration-700"></div>
                                <div class="absolute -bottom-32 -right-32 w-64 h-64 bg-purple-500/10 rounded-full blur-[80px] group-hover:bg-purple-500/20 transition-colors duration-700 delay-100"></div>
                                
                                <div class="relative z-10">
                                    <div class="flex items-center gap-4 mb-6">
                                        <div class="w-14 h-14 rounded-[1.2rem] bg-white/5 flex items-center justify-center border border-white/10 shadow-[0_0_15px_rgba(255,255,255,0.05)] group-hover:scale-110 transition-transform duration-500">
                                            <i class="fas fa-fingerprint text-cyan-400 text-2xl"></i>
                                        </div>
                                        <div>
                                            <h3 class="text-2xl font-black text-white tracking-tight">Hazem Elerefy</h3>
                                            <div class="text-sm text-cyan-400 font-medium tracking-wide">Data Analyst & Frontend Dev</div>
                                        </div>
                                    </div>
                                    <p class="text-white/70 text-lg leading-relaxed font-light mb-8">
                                        I bridge the gap between complex data and elegant frontend experiences. My legal background sharpens my analytical thinking, while my active passion for UI/UX drives me to craft pixel-perfect, highly responsive web products. I don't just write code—I architect digital solutions that are intuitively useful and visually unforgettable.
                                    </p>
                                    <div class="flex items-center gap-4">
                                        <a href="mailto:hazemawed53@gmail.com" class="px-6 py-3 rounded-full bg-white text-black font-bold text-sm tracking-wide hover:bg-cyan-400 transition-colors shadow-[0_0_20px_rgba(255,255,255,0.2)]">
                                            <i class="fas fa-paper-plane mr-2"></i> Let's Connect
                                        </a>
                                        <a href="https://github.com/hazemelerefey" target="_blank" class="w-12 h-12 rounded-full border border-white/20 flex items-center justify-center text-white/70 hover:text-white hover:bg-white/10 transition-all">
                                            <i class="fab fa-github text-xl"></i>
                                        </a>
                                        <a href="https://linkedin.com" target="_blank" class="w-12 h-12 rounded-full border border-white/20 flex items-center justify-center text-white/70 hover:text-white hover:bg-blue-500/20 hover:border-blue-500 transition-all">
                                            <i class="fab fa-linkedin-in text-xl"></i>
                                        </a>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- BENTO BOX 2: DATA ANALYST (Col Span 1, Row Span 2) -->
                            <div data-aos="fade-up" data-aos-duration="800" data-aos-delay="100" class="md:col-span-1 md:row-span-2 group relative bg-[#0a0a0a] border border-white/5 p-8 rounded-[2rem] hover:border-pink-500/30 transition-all duration-500 shadow-[0_20px_40px_-15px_rgba(0,0,0,0.8)] overflow-hidden flex flex-col">
                                <div class="absolute top-0 right-0 w-full h-[50%] bg-gradient-to-b from-pink-500/5 to-transparent z-0"></div>
                                <div class="absolute -bottom-20 -right-20 w-48 h-48 bg-pink-500/10 rounded-full blur-[60px] group-hover:bg-pink-500/20 transition-colors duration-700"></div>
                                
                                <div class="relative z-10 flex-1 flex flex-col">
                                    <div class="flex items-center justify-between mb-8">
                                        <div class="w-12 h-12 rounded-[1rem] bg-pink-500/10 flex items-center justify-center border border-pink-500/20 shadow-[0_0_15px_rgba(236,72,153,0.15)] group-hover:scale-110 transition-transform duration-500">
                                            <i class="fas fa-chart-pie text-pink-400 text-xl"></i>
                                        </div>
                                        <span class="text-[10px] font-black uppercase tracking-[0.2em] text-pink-400/80 bg-pink-500/10 px-3 py-1.5 rounded-full border border-pink-500/20">Present</span>
                                    </div>
                                    
                                    <h4 class="text-2xl font-black text-white mb-2 leading-tight">Data Analyst</h4>
                                    <div class="text-sm font-bold text-pink-400 mb-6 bg-pink-500/10 py-1 px-3 rounded-md w-max border border-pink-500/20">Digilians | MCIT</div>
                                    
                                    <ul class="space-y-4 text-white/70 text-sm flex-1">
                                        <li class="flex items-start gap-3">
                                            <i class="fas fa-check-circle text-pink-500 mt-0.5 text-xs"></i> 
                                            <span class="leading-relaxed">Architecting KPI dashboards for deep performance tracking and visualization.</span>
                                        </li>
                                        <li class="flex items-start gap-3">
                                            <i class="fas fa-check-circle text-pink-500 mt-0.5 text-xs"></i> 
                                            <span class="leading-relaxed">Developing sophisticated SQL queries for massive-scale reporting.</span>
                                        </li>
                                        <li class="flex items-start gap-3">
                                            <i class="fas fa-check-circle text-pink-500 mt-0.5 text-xs"></i> 
                                            <span class="leading-relaxed">Applying cutting-edge Prompt Engineering for optimized AI outputs.</span>
                                        </li>
                                        <li class="flex items-start gap-3">
                                            <i class="fas fa-check-circle text-pink-500 mt-0.5 text-xs"></i> 
                                            <span class="leading-relaxed">Producing dynamic, real-time data stories and executive visualizations.</span>
                                        </li>
                                    </ul>
                                </div>
                            </div>

                            <!-- BENTO BOX  3: FRONTEND DEV (Col Span 1) -->
                            <div data-aos="fade-up" data-aos-duration="800" data-aos-delay="200" class="md:col-span-1 group relative bg-[#0a0a0a] border border-white/5 p-8 rounded-[2rem] hover:border-emerald-500/30 transition-all duration-500 shadow-[0_20px_40px_-15px_rgba(0,0,0,0.8)] overflow-hidden">
                                <div class="absolute -top-10 -right-10 w-32 h-32 bg-emerald-500/10 rounded-full blur-[40px] group-hover:bg-emerald-500/20 transition-colors duration-700"></div>
                                
                                <div class="relative z-10">
                                    <div class="flex items-center justify-between mb-6">
                                        <div class="w-12 h-12 rounded-[1rem] bg-emerald-500/10 flex items-center justify-center border border-emerald-500/20 shadow-[0_0_15px_rgba(16,185,129,0.15)] group-hover:scale-110 transition-transform duration-500">
                                            <i class="fas fa-laptop-code text-emerald-400 text-xl"></i>
                                        </div>
                                        <span class="text-[10px] font-black uppercase tracking-[0.2em] text-white/40">2022 - 2023</span>
                                    </div>
                                    <h4 class="text-xl font-black text-white mb-2 leading-tight">Front-End Developer</h4>
                                    <div class="text-xs font-bold text-emerald-400 mb-4 bg-emerald-500/10 py-1 px-3 rounded-md w-max border border-emerald-500/20">Udacity</div>
                                    <p class="text-white/60 text-sm leading-relaxed mb-4">Mastered core Web stack (HTML5, CSS3, JS) to build responsive, high-fidelity web apps interconnected through asynchronous APIs.</p>
                                </div>
                            </div>

                            <!-- BENTO BOX 4: EDUCATION STACK (Col Span 1) -->
                            <div data-aos="fade-up" data-aos-duration="800" data-aos-delay="300" class="md:col-span-1 group flex flex-col gap-4">
                                <!-- Degree 1 -->
                                <div class="relative bg-white/[0.02] border border-white/5 p-6 rounded-[1.5rem] hover:bg-white/[0.04] transition-colors overflow-hidden">
                                    <div class="absolute right-0 top-0 h-full w-1 bg-cyan-500/40 rounded-r-lg"></div>
                                    <span class="text-[10px] font-black uppercase tracking-[0.2em] text-white/40 mb-1 block">2025 - 2026</span>
                                    <h5 class="text-sm font-black text-white mb-1">Applied AI & Analytics Diploma</h5>
                                    <div class="text-xs text-cyan-400 font-bold">Digilians | MCIT</div>
                                </div>
                                <!-- Degree 2 -->
                                <div class="relative bg-white/[0.02] border border-white/5 p-6 rounded-[1.5rem] hover:bg-white/[0.04] transition-colors overflow-hidden">
                                    <div class="absolute right-0 top-0 h-full w-1 bg-emerald-500/40 rounded-r-lg"></div>
                                    <span class="text-[10px] font-black uppercase tracking-[0.2em] text-white/40 mb-1 block">2022 - 2023</span>
                                    <h5 class="text-sm font-black text-white mb-1">Nano Degree (GPA: 4)</h5>
                                    <div class="text-xs text-emerald-400 font-bold">Udacity Front-End</div>
                                </div>
                                <!-- Degree 3 -->
                                <div class="relative bg-white/[0.02] border border-white/5 p-6 rounded-[1.5rem] hover:bg-white/[0.04] transition-colors overflow-hidden">
                                    <div class="absolute right-0 top-0 h-full w-1 bg-purple-500/40 rounded-r-lg"></div>
                                    <span class="text-[10px] font-black uppercase tracking-[0.2em] text-white/40 mb-1 block">2020 - 2024</span>
                                    <h5 class="text-sm font-black text-white mb-1">Bachelor of Laws</h5>
                                    <div class="text-xs text-purple-400 font-bold">Port Said University</div>
                                </div>
                            </div>
                            
                            <!-- BENTO BOX 5: QUICK STATS / PASSION (Col Span 2 or generic block) (Optional, but let's stretch across bottom) -->
                            <div data-aos="fade-up" data-aos-duration="800" data-aos-delay="400" class="md:col-span-3 group relative bg-gradient-to-r from-cardBase via-[#0a0a0a] to-cardBase border border-white/5 p-8 rounded-[2rem] hover:border-white/10 transition-all duration-500 overflow-hidden flex items-center justify-between">
                                <div class="absolute inset-0 z-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iMiIgY3k9IjIiIHI9IjIiIGZpbGw9IiNmZmZmZmYwYyIvPjwvc3ZnPg==')] opacity-[0.15]"></div>
                                <div class="relative z-10 flex flex-col md:flex-row w-full justify-around gap-8 text-center md:text-left">
                                    <div>
                                        <div class="text-[10px] font-black uppercase tracking-[0.2em] text-white/40 mb-2">Core Focus</div>
                                        <h5 class="text-xl font-bold text-white">Commercial & Corporate Alignment</h5>
                                    </div>
                                    <div class="hidden md:block w-px h-12 bg-white/10"></div>
                                    <div>
                                        <div class="text-[10px] font-black uppercase tracking-[0.2em] text-white/40 mb-2">Specialty</div>
                                        <h5 class="text-xl font-bold text-cyan-400">High-Fidelity Dashboarding</h5>
                                    </div>
                                    <div class="hidden md:block w-px h-12 bg-white/10"></div>
                                    <div>
                                        <div class="text-[10px] font-black uppercase tracking-[0.2em] text-white/40 mb-2">Delivery Standard</div>
                                        <h5 class="text-xl font-bold text-pink-400">Pixel-Perfect UI Architecture</h5>
                                    </div>
                                </div>
                            </div>

                        </div>
                    </section>
"""

if start_idx != -1 and end_idx != -1:
    new_text = text[:start_idx] + bento_html + '\n\n                    ' + text[end_idx:]
    with codecs.open('index.html', 'w', 'utf-8') as f:
        f.write(new_text)
    print("Replaced successfully")
else:
    print("Failed to find markers")
