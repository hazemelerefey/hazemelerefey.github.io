import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    text = f.read()

start_marker = '<!-- SERVICES VIEW CONTENT -->\r\n'
end_marker = '</div> <!-- END SERVICES VIEW -->\r\n'

idx_start = text.find(start_marker)
idx_end = text.find(end_marker)

if idx_start == -1:
    start_marker = '<!-- SERVICES VIEW CONTENT -->\n'
    idx_start = text.find(start_marker)
if idx_end == -1:
    end_marker = '</div> <!-- END SERVICES VIEW -->\n'
    idx_end = text.find(end_marker)

new_services = r"""<!-- SERVICES VIEW CONTENT -->
    <div x-show="activeView === 'services'" x-cloak x-transition:enter="transition ease-out duration-500 delay-100"
        x-transition:enter-start="opacity-0 transform translate-y-8"
        x-transition:enter-end="opacity-100 transform translate-y-0"
        class="pt-32 pb-20 px-6 md:px-12 max-w-7xl mx-auto min-h-screen">

        <!-- ============================================== -->
        <!-- SECTION 1: CINEMATIC SERVICES HERO             -->
        <!-- ============================================== -->
        <div class="text-center mb-20 relative">
            <div class="absolute inset-0 flex items-center justify-center opacity-[0.015] pointer-events-none overflow-hidden select-none">
                <h2 class="text-[12vw] font-black text-white whitespace-nowrap tracking-tighter">SERVICES</h2>
            </div>
            <div class="relative z-10">
                <span class="uppercase tracking-[0.3em] text-cyan-400 text-[10px] font-bold mb-4 block" data-aos="fade-up">Available For Hire</span>
                <h1 class="text-5xl md:text-6xl lg:text-7xl font-black text-white mb-6 leading-tight" data-aos="fade-up" data-aos-delay="100">
                    Professional <span class="text-gradient-cyan-pink">Services</span>
                </h1>
                <p class="text-white/40 max-w-2xl mx-auto text-lg leading-relaxed font-light" data-aos="fade-up" data-aos-delay="200">
                    From pixel-perfect dashboards to full-stack web experiences. Let's turn your vision into a premium digital reality.
                </p>
            </div>
        </div>

        <!-- ============================================== -->
        <!-- SECTION 2: WHAT I DELIVER (SERVICES GRID)      -->
        <!-- ============================================== -->
        <div class="mb-28" x-data="{ activeServiceTab: 'analytics' }">
            <div class="flex items-center gap-4 mb-10" data-aos="fade-up">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-500/20 to-pink-500/20 border border-white/10 flex items-center justify-center">
                    <i class="fas fa-cubes text-white/70 text-sm"></i>
                </div>
                <h2 class="text-2xl font-bold text-white">What I <span class="text-gradient-cyan-pink">Deliver</span></h2>
                <div class="h-[1px] flex-1 bg-gradient-to-r from-white/10 to-transparent"></div>
            </div>

            <!-- Services Tab Switcher -->
            <div class="flex justify-center mb-10" data-aos="fade-up" data-aos-delay="100">
                <div class="inline-flex items-center bg-white/[0.02] p-1.5 rounded-2xl border border-white/[0.08] shadow-lg backdrop-blur-xl w-full max-w-md mx-auto">
                    <button @click="activeServiceTab = 'analytics'"
                        :class="{'bg-gradient-to-r from-cyan-500 to-cyan-600 text-white shadow-[0_4px_20px_rgba(6,182,212,0.3)]': activeServiceTab === 'analytics', 'text-white/40 hover:text-white': activeServiceTab !== 'analytics'}"
                        class="flex-1 py-3 px-6 rounded-xl font-bold text-sm transition-all duration-300 cursor-pointer">
                        <i class="fas fa-chart-line mr-2"></i> Analytics
                    </button>
                    <button @click="activeServiceTab = 'frontend'"
                        :class="{'bg-gradient-to-r from-pink-500 to-pink-600 text-white shadow-[0_4px_20px_rgba(236,72,153,0.3)]': activeServiceTab === 'frontend', 'text-white/40 hover:text-white': activeServiceTab !== 'frontend'}"
                        class="flex-1 py-3 px-6 rounded-xl font-bold text-sm transition-all duration-300 cursor-pointer">
                        <i class="fas fa-paint-brush mr-2"></i> Frontend
                    </button>
                </div>
            </div>

            <!-- Analytics Services -->
            <div x-show="activeServiceTab === 'analytics'" class="grid grid-cols-1 md:grid-cols-2 gap-6"
                x-transition:enter="transition ease-in-out duration-300"
                x-transition:enter-start="opacity-0 translate-y-4" x-transition:enter-end="opacity-100 translate-y-0">

                <!-- Service 1 -->
                <div data-aos="fade-up" class="bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-8 relative overflow-hidden group hover:border-cyan-500/30 transition-all duration-500 backdrop-blur-xl cursor-default">
                    <div class="absolute top-0 right-0 w-48 h-48 bg-cyan-500/8 rounded-full blur-[80px] group-hover:bg-cyan-500/15 transition-all duration-700"></div>
                    <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-cyan-500/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="relative z-10 flex gap-6">
                        <div class="w-14 h-14 shrink-0 rounded-2xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center shadow-[0_0_20px_rgba(6,182,212,0.15)]">
                            <i class="fas fa-database text-cyan-400 text-xl"></i>
                        </div>
                        <div>
                            <h3 class="text-lg font-bold text-white mb-2">Data Warehousing & SQL</h3>
                            <p class="text-white/40 text-sm leading-relaxed mb-4">Structuring enormous datasets, architecting clean pipelines, and optimizing complex queries for speed and accuracy.</p>
                            <div class="flex flex-wrap gap-2">
                                <span class="text-[9px] font-bold uppercase tracking-widest text-cyan-400/60 bg-cyan-500/10 border border-cyan-500/10 px-3 py-1 rounded-full">PostgreSQL</span>
                                <span class="text-[9px] font-bold uppercase tracking-widest text-cyan-400/60 bg-cyan-500/10 border border-cyan-500/10 px-3 py-1 rounded-full">MySQL</span>
                                <span class="text-[9px] font-bold uppercase tracking-widest text-cyan-400/60 bg-cyan-500/10 border border-cyan-500/10 px-3 py-1 rounded-full">ETL</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Service 2 -->
                <div data-aos="fade-up" data-aos-delay="100" class="bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-8 relative overflow-hidden group hover:border-emerald-500/30 transition-all duration-500 backdrop-blur-xl cursor-default">
                    <div class="absolute top-0 right-0 w-48 h-48 bg-emerald-500/8 rounded-full blur-[80px] group-hover:bg-emerald-500/15 transition-all duration-700"></div>
                    <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-emerald-500/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="relative z-10 flex gap-6">
                        <div class="w-14 h-14 shrink-0 rounded-2xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center shadow-[0_0_20px_rgba(52,211,153,0.15)]">
                            <i class="fas fa-chart-pie text-emerald-400 text-xl"></i>
                        </div>
                        <div>
                            <h3 class="text-lg font-bold text-white mb-2">Interactive Dashboards</h3>
                            <p class="text-white/40 text-sm leading-relaxed mb-4">Crafting executive-level, real-time dashboards using Power BI to visually narrate business intelligence with stunning clarity.</p>
                            <div class="flex flex-wrap gap-2">
                                <span class="text-[9px] font-bold uppercase tracking-widest text-emerald-400/60 bg-emerald-500/10 border border-emerald-500/10 px-3 py-1 rounded-full">Power BI</span>
                                <span class="text-[9px] font-bold uppercase tracking-widest text-emerald-400/60 bg-emerald-500/10 border border-emerald-500/10 px-3 py-1 rounded-full">DAX</span>
                                <span class="text-[9px] font-bold uppercase tracking-widest text-emerald-400/60 bg-emerald-500/10 border border-emerald-500/10 px-3 py-1 rounded-full">KPI Design</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Service 3 -->
                <div data-aos="fade-up" data-aos-delay="200" class="bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-8 relative overflow-hidden group hover:border-purple-500/30 transition-all duration-500 backdrop-blur-xl cursor-default">
                    <div class="absolute top-0 right-0 w-48 h-48 bg-purple-500/8 rounded-full blur-[80px] group-hover:bg-purple-500/15 transition-all duration-700"></div>
                    <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-purple-500/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="relative z-10 flex gap-6">
                        <div class="w-14 h-14 shrink-0 rounded-2xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center shadow-[0_0_20px_rgba(168,85,247,0.15)]">
                            <i class="fas fa-brain text-purple-400 text-xl"></i>
                        </div>
                        <div>
                            <h3 class="text-lg font-bold text-white mb-2">Predictive ML Models</h3>
                            <p class="text-white/40 text-sm leading-relaxed mb-4">Developing AI algorithms for forecasting, churn prediction, and deep analytical insights that drive business strategy.</p>
                            <div class="flex flex-wrap gap-2">
                                <span class="text-[9px] font-bold uppercase tracking-widest text-purple-400/60 bg-purple-500/10 border border-purple-500/10 px-3 py-1 rounded-full">Scikit-learn</span>
                                <span class="text-[9px] font-bold uppercase tracking-widest text-purple-400/60 bg-purple-500/10 border border-purple-500/10 px-3 py-1 rounded-full">Python</span>
                                <span class="text-[9px] font-bold uppercase tracking-widest text-purple-400/60 bg-purple-500/10 border border-purple-500/10 px-3 py-1 rounded-full">ARIMA</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Service 4 -->
                <div data-aos="fade-up" data-aos-delay="300" class="bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-8 relative overflow-hidden group hover:border-amber-500/30 transition-all duration-500 backdrop-blur-xl cursor-default">
                    <div class="absolute top-0 right-0 w-48 h-48 bg-amber-500/8 rounded-full blur-[80px] group-hover:bg-amber-500/15 transition-all duration-700"></div>
                    <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-amber-500/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="relative z-10 flex gap-6">
                        <div class="w-14 h-14 shrink-0 rounded-2xl bg-amber-500/10 border border-amber-500/20 flex items-center justify-center shadow-[0_0_20px_rgba(245,158,11,0.15)]">
                            <i class="fas fa-microscope text-amber-400 text-xl"></i>
                        </div>
                        <div>
                            <h3 class="text-lg font-bold text-white mb-2">Statistical Analysis</h3>
                            <p class="text-white/40 text-sm leading-relaxed mb-4">Deploying rigorous data cleaning, validation, and reporting to uncover hidden trends and actionable business intelligence.</p>
                            <div class="flex flex-wrap gap-2">
                                <span class="text-[9px] font-bold uppercase tracking-widest text-amber-400/60 bg-amber-500/10 border border-amber-500/10 px-3 py-1 rounded-full">Pandas</span>
                                <span class="text-[9px] font-bold uppercase tracking-widest text-amber-400/60 bg-amber-500/10 border border-amber-500/10 px-3 py-1 rounded-full">NumPy</span>
                                <span class="text-[9px] font-bold uppercase tracking-widest text-amber-400/60 bg-amber-500/10 border border-amber-500/10 px-3 py-1 rounded-full">Excel</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Frontend Services -->
            <div x-show="activeServiceTab === 'frontend'" x-cloak class="grid grid-cols-1 md:grid-cols-2 gap-6"
                x-transition:enter="transition ease-in-out duration-300"
                x-transition:enter-start="opacity-0 translate-y-4" x-transition:enter-end="opacity-100 translate-y-0">

                <!-- Service 5 -->
                <div data-aos="fade-up" class="bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-8 relative overflow-hidden group hover:border-pink-500/30 transition-all duration-500 backdrop-blur-xl cursor-default">
                    <div class="absolute top-0 right-0 w-48 h-48 bg-pink-500/8 rounded-full blur-[80px] group-hover:bg-pink-500/15 transition-all duration-700"></div>
                    <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-pink-500/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="relative z-10 flex gap-6">
                        <div class="w-14 h-14 shrink-0 rounded-2xl bg-pink-500/10 border border-pink-500/20 flex items-center justify-center shadow-[0_0_20px_rgba(236,72,153,0.15)]">
                            <i class="fas fa-id-card text-pink-400 text-xl"></i>
                        </div>
                        <div>
                            <h3 class="text-lg font-bold text-white mb-2">Portfolio Website Development</h3>
                            <p class="text-white/40 text-sm leading-relaxed mb-4">Creating fluid, animated, high-performance personal and corporate portfolios that make an unforgettable first impression.</p>
                            <div class="flex flex-wrap gap-2">
                                <span class="text-[9px] font-bold uppercase tracking-widest text-pink-400/60 bg-pink-500/10 border border-pink-500/10 px-3 py-1 rounded-full">HTML/CSS</span>
                                <span class="text-[9px] font-bold uppercase tracking-widest text-pink-400/60 bg-pink-500/10 border border-pink-500/10 px-3 py-1 rounded-full">Tailwind</span>
                                <span class="text-[9px] font-bold uppercase tracking-widest text-pink-400/60 bg-pink-500/10 border border-pink-500/10 px-3 py-1 rounded-full">Alpine.js</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Service 6 -->
                <div data-aos="fade-up" data-aos-delay="100" class="bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-8 relative overflow-hidden group hover:border-cyan-500/30 transition-all duration-500 backdrop-blur-xl cursor-default">
                    <div class="absolute top-0 right-0 w-48 h-48 bg-cyan-500/8 rounded-full blur-[80px] group-hover:bg-cyan-500/15 transition-all duration-700"></div>
                    <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-cyan-500/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="relative z-10 flex gap-6">
                        <div class="w-14 h-14 shrink-0 rounded-2xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center shadow-[0_0_20px_rgba(6,182,212,0.15)]">
                            <i class="fas fa-layer-group text-cyan-400 text-xl"></i>
                        </div>
                        <div>
                            <h3 class="text-lg font-bold text-white mb-2">Custom Web App Architecture</h3>
                            <p class="text-white/40 text-sm leading-relaxed mb-4">Engineering robust web apps from scratch using React, Next.js, and Tailwind with dynamic functionality ready for production.</p>
                            <div class="flex flex-wrap gap-2">
                                <span class="text-[9px] font-bold uppercase tracking-widest text-cyan-400/60 bg-cyan-500/10 border border-cyan-500/10 px-3 py-1 rounded-full">React</span>
                                <span class="text-[9px] font-bold uppercase tracking-widest text-cyan-400/60 bg-cyan-500/10 border border-cyan-500/10 px-3 py-1 rounded-full">Next.js</span>
                                <span class="text-[9px] font-bold uppercase tracking-widest text-cyan-400/60 bg-cyan-500/10 border border-cyan-500/10 px-3 py-1 rounded-full">API</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Service 7 -->
                <div data-aos="fade-up" data-aos-delay="200" class="md:col-span-2 bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-8 relative overflow-hidden group hover:border-purple-500/30 transition-all duration-500 backdrop-blur-xl cursor-default">
                    <div class="absolute top-0 right-0 w-48 h-48 bg-purple-500/8 rounded-full blur-[80px] group-hover:bg-purple-500/15 transition-all duration-700"></div>
                    <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-purple-500/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="relative z-10 flex gap-6">
                        <div class="w-14 h-14 shrink-0 rounded-2xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center shadow-[0_0_20px_rgba(168,85,247,0.15)]">
                            <i class="fab fa-figma text-purple-400 text-xl"></i>
                        </div>
                        <div>
                            <h3 class="text-lg font-bold text-white mb-2">UI/UX Design Mockups</h3>
                            <p class="text-white/40 text-sm leading-relaxed mb-4">Designing beautiful, modern interfaces using Figma focused on seamless user journeys, conversion optimization, and premium visual composition.</p>
                            <div class="flex flex-wrap gap-2">
                                <span class="text-[9px] font-bold uppercase tracking-widest text-purple-400/60 bg-purple-500/10 border border-purple-500/10 px-3 py-1 rounded-full">Figma</span>
                                <span class="text-[9px] font-bold uppercase tracking-widest text-purple-400/60 bg-purple-500/10 border border-purple-500/10 px-3 py-1 rounded-full">Prototyping</span>
                                <span class="text-[9px] font-bold uppercase tracking-widest text-purple-400/60 bg-purple-500/10 border border-purple-500/10 px-3 py-1 rounded-full">Wireframing</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- ============================================== -->
        <!-- SECTION 3: HIRE ME PLATFORMS                    -->
        <!-- ============================================== -->
        <div class="mb-28">
            <div class="flex items-center gap-4 mb-10" data-aos="fade-up">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-emerald-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center">
                    <i class="fas fa-globe text-white/70 text-sm"></i>
                </div>
                <h2 class="text-2xl font-bold text-white">Hire Me <span class="text-gradient-cyan-pink">Across Platforms</span></h2>
                <div class="h-[1px] flex-1 bg-gradient-to-r from-white/10 to-transparent"></div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
                <!-- Upwork -->
                <a href="https://www.upwork.com/freelancers/~01095d37046356f7d5?mp_source=share" target="_blank" rel="noopener noreferrer" data-aos="fade-up"
                    class="block bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-7 relative overflow-hidden group hover:border-[#14A800]/40 transition-all duration-500 backdrop-blur-xl cursor-pointer">
                    <div class="absolute top-0 right-0 w-40 h-40 bg-[#14A800]/5 rounded-full blur-[60px] group-hover:bg-[#14A800]/15 transition-all duration-700"></div>
                    <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-[#14A800]/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="relative z-10">
                        <div class="flex justify-between items-center mb-5">
                            <div class="w-11 h-11 rounded-2xl bg-[#14A800]/10 border border-[#14A800]/20 flex items-center justify-center">
                                <i class="fas fa-briefcase text-[#14A800] text-lg"></i>
                            </div>
                            <span class="text-[9px] font-black uppercase tracking-[0.15em] text-[#14A800] bg-[#14A800]/10 border border-[#14A800]/20 px-3 py-1.5 rounded-full">Top Rated</span>
                        </div>
                        <h3 class="text-lg font-bold text-white mb-1 group-hover:text-[#14A800] transition-colors">Upwork</h3>
                        <p class="text-white/35 text-sm mb-5">Main platform for frontend builds, dashboards, and data-focused freelance work.</p>
                        <span class="text-[#14A800]/60 text-xs font-bold uppercase tracking-wider group-hover:text-[#14A800] transition-colors flex items-center gap-1.5">Hire Me <i class="fas fa-arrow-right text-[10px] group-hover:translate-x-1 transition-transform"></i></span>
                    </div>
                </a>

                <!-- Freelancer -->
                <a href="https://www.freelancer.com/u/hazemawed53?frm=hazemawed53&sb=t" target="_blank" rel="noopener noreferrer" data-aos="fade-up" data-aos-delay="50"
                    class="block bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-7 relative overflow-hidden group hover:border-[#29B2FE]/40 transition-all duration-500 backdrop-blur-xl cursor-pointer">
                    <div class="absolute top-0 right-0 w-40 h-40 bg-[#29B2FE]/5 rounded-full blur-[60px] group-hover:bg-[#29B2FE]/15 transition-all duration-700"></div>
                    <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-[#29B2FE]/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="relative z-10">
                        <div class="flex justify-between items-center mb-5">
                            <div class="w-11 h-11 rounded-2xl bg-[#29B2FE]/10 border border-[#29B2FE]/20 flex items-center justify-center">
                                <i class="fas fa-paper-plane text-[#29B2FE] text-lg"></i>
                            </div>
                        </div>
                        <h3 class="text-lg font-bold text-white mb-1 group-hover:text-[#29B2FE] transition-colors">Freelancer.com</h3>
                        <p class="text-white/35 text-sm mb-5">Fast-turnaround web development and shorter project milestones.</p>
                        <span class="text-[#29B2FE]/60 text-xs font-bold uppercase tracking-wider group-hover:text-[#29B2FE] transition-colors flex items-center gap-1.5">Hire Me <i class="fas fa-arrow-right text-[10px] group-hover:translate-x-1 transition-transform"></i></span>
                    </div>
                </a>

                <!-- PeoplePerHour -->
                <a href="https://pph.me/hazemelerefy" target="_blank" rel="noopener noreferrer" data-aos="fade-up" data-aos-delay="100"
                    class="block bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-7 relative overflow-hidden group hover:border-[#FF7300]/40 transition-all duration-500 backdrop-blur-xl cursor-pointer">
                    <div class="absolute top-0 right-0 w-40 h-40 bg-[#FF7300]/5 rounded-full blur-[60px] group-hover:bg-[#FF7300]/15 transition-all duration-700"></div>
                    <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-[#FF7300]/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="relative z-10">
                        <div class="flex justify-between items-center mb-5">
                            <div class="w-11 h-11 rounded-2xl bg-[#FF7300]/10 border border-[#FF7300]/20 flex items-center justify-center">
                                <i class="fas fa-hourglass-half text-[#FF7300] text-lg"></i>
                            </div>
                        </div>
                        <h3 class="text-lg font-bold text-white mb-1 group-hover:text-[#FF7300] transition-colors">PeoplePerHour</h3>
                        <p class="text-white/35 text-sm mb-5">Custom data automation scripts and UI/UX design hourly offers.</p>
                        <span class="text-[#FF7300]/60 text-xs font-bold uppercase tracking-wider group-hover:text-[#FF7300] transition-colors flex items-center gap-1.5">Hire Me <i class="fas fa-arrow-right text-[10px] group-hover:translate-x-1 transition-transform"></i></span>
                    </div>
                </a>

                <!-- Mostaql -->
                <a href="https://mostaql.com/u/zoo_ma" target="_blank" rel="noopener noreferrer" data-aos="fade-up" data-aos-delay="150"
                    class="block bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-7 relative overflow-hidden group hover:border-[#2386c8]/40 transition-all duration-500 backdrop-blur-xl cursor-pointer">
                    <div class="absolute top-0 right-0 w-40 h-40 bg-[#2386c8]/5 rounded-full blur-[60px] group-hover:bg-[#2386c8]/15 transition-all duration-700"></div>
                    <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-[#2386c8]/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="relative z-10">
                        <div class="flex justify-between items-center mb-5">
                            <div class="w-11 h-11 rounded-2xl bg-[#2386c8]/10 border border-[#2386c8]/20 flex items-center justify-center">
                                <i class="fas fa-star text-[#2386c8] text-lg"></i>
                            </div>
                        </div>
                        <h3 class="text-lg font-bold text-white mb-1 group-hover:text-[#2386c8] transition-colors">Mostaql</h3>
                        <p class="text-white/35 text-sm mb-5">High-quality projects serving clients across the MENA region.</p>
                        <span class="text-[#2386c8]/60 text-xs font-bold uppercase tracking-wider group-hover:text-[#2386c8] transition-colors flex items-center gap-1.5">Hire Me <i class="fas fa-arrow-right text-[10px] group-hover:translate-x-1 transition-transform"></i></span>
                    </div>
                </a>

                <!-- Khamsat -->
                <a href="https://khamsat.com/user/hazemkhaled53" target="_blank" rel="noopener noreferrer" data-aos="fade-up" data-aos-delay="200"
                    class="block bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-7 relative overflow-hidden group hover:border-[#20af5a]/40 transition-all duration-500 backdrop-blur-xl cursor-pointer">
                    <div class="absolute top-0 right-0 w-40 h-40 bg-[#20af5a]/5 rounded-full blur-[60px] group-hover:bg-[#20af5a]/15 transition-all duration-700"></div>
                    <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-[#20af5a]/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="relative z-10">
                        <div class="flex justify-between items-center mb-5">
                            <div class="w-11 h-11 rounded-2xl bg-[#20af5a]/10 border border-[#20af5a]/20 flex items-center justify-center">
                                <i class="fas fa-shopping-cart text-[#20af5a] text-lg"></i>
                            </div>
                        </div>
                        <h3 class="text-lg font-bold text-white mb-1 group-hover:text-[#20af5a] transition-colors">Khamsat</h3>
                        <p class="text-white/35 text-sm mb-5">Mini-services, bug fixing, and quick tech consultations.</p>
                        <span class="text-[#20af5a]/60 text-xs font-bold uppercase tracking-wider group-hover:text-[#20af5a] transition-colors flex items-center gap-1.5">Hire Me <i class="fas fa-arrow-right text-[10px] group-hover:translate-x-1 transition-transform"></i></span>
                    </div>
                </a>
            </div>
        </div>

        <!-- ============================================== -->
        <!-- SECTION 4: PROJECT REQUEST FORM                -->
        <!-- ============================================== -->
        <div id="request-service" class="scroll-mt-32">
            <div class="flex items-center gap-4 mb-10" data-aos="fade-up">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-pink-500/20 to-purple-500/20 border border-white/10 flex items-center justify-center">
                    <i class="fas fa-paper-plane text-white/70 text-sm"></i>
                </div>
                <h2 class="text-2xl font-bold text-white">Start a <span class="text-gradient-cyan-pink">Project</span></h2>
                <div class="h-[1px] flex-1 bg-gradient-to-r from-white/10 to-transparent"></div>
            </div>

            <div data-aos="fade-up" data-aos-delay="100" class="bg-gradient-to-br from-white/[0.03] to-transparent border border-white/[0.08] rounded-3xl p-8 md:p-12 relative overflow-hidden backdrop-blur-xl">
                <div class="absolute -top-40 -right-40 w-96 h-96 bg-cyan-500/5 rounded-full blur-[120px] pointer-events-none"></div>
                <div class="absolute -bottom-40 -left-40 w-96 h-96 bg-pink-500/5 rounded-full blur-[120px] pointer-events-none"></div>

                <div class="relative z-10 flex flex-col md:flex-row gap-12">
                    <div class="md:w-1/2">
                        <h3 class="text-2xl md:text-3xl font-bold text-white mb-4">Start your project with a <span class="text-gradient-cyan-pink">clear brief</span></h3>
                        <p class="text-white/40 mb-8 leading-relaxed">Tell me what you need, your timeline, and the result you want. I will review and reply with the best delivery approach.</p>

                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-8">
                            <div class="rounded-2xl border border-white/[0.08] bg-white/[0.02] p-5">
                                <div class="text-[10px] font-black text-cyan-400 uppercase tracking-[0.2em] mb-2">Best for</div>
                                <p class="text-sm text-white/40">Portfolios, frontends, dashboards, freelance requests, and brand improvements.</p>
                            </div>
                            <div class="rounded-2xl border border-white/[0.08] bg-white/[0.02] p-5">
                                <div class="text-[10px] font-black text-pink-400 uppercase tracking-[0.2em] mb-2">Fastest path</div>
                                <p class="text-sm text-white/40">Send the form, then continue by email with references and repo links.</p>
                            </div>
                        </div>

                        <div class="space-y-4">
                            <a href="mailto:hazemkhaled53@gmail.com" class="flex items-center gap-4 text-white/40 hover:text-white transition-colors group cursor-pointer">
                                <div class="w-12 h-12 rounded-2xl bg-white/[0.03] border border-white/[0.08] flex items-center justify-center group-hover:border-cyan-400/30 transition-colors">
                                    <i class="fas fa-envelope text-cyan-400"></i>
                                </div>
                                <div>
                                    <div class="text-[10px] font-black text-cyan-400 uppercase tracking-[0.2em]">Email Me</div>
                                    <div class="text-sm">Click to email me directly</div>
                                </div>
                            </a>
                            <div class="flex items-center gap-4 text-white/40">
                                <div class="w-12 h-12 rounded-2xl bg-white/[0.03] border border-white/[0.08] flex items-center justify-center">
                                    <i class="fab fa-whatsapp text-green-400"></i>
                                </div>
                                <div>
                                    <div class="text-[10px] font-black text-green-400 uppercase tracking-[0.2em]">WhatsApp</div>
                                    <div class="text-sm">Available upon request after initial contact</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="md:w-1/2">
                        <form class="space-y-4" @submit.prevent="submitProjectRequest($event)">
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                <div>
                                    <label class="block text-[10px] font-black text-white/30 uppercase tracking-[0.2em] mb-2">Name</label>
                                    <input type="text" name="name" required
                                        class="w-full bg-white/[0.03] border border-white/[0.08] rounded-xl px-4 py-3 text-white focus:outline-none focus:border-cyan-500/50 focus:ring-1 focus:ring-cyan-500/30 hover:border-white/15 transition-all placeholder-white/20 text-sm"
                                        placeholder="John Doe">
                                </div>
                                <div>
                                    <label class="block text-[10px] font-black text-white/30 uppercase tracking-[0.2em] mb-2">Email</label>
                                    <input type="email" name="email" required
                                        class="w-full bg-white/[0.03] border border-white/[0.08] rounded-xl px-4 py-3 text-white focus:outline-none focus:border-cyan-500/50 focus:ring-1 focus:ring-cyan-500/30 hover:border-white/15 transition-all placeholder-white/20 text-sm"
                                        placeholder="john@company.com">
                                </div>
                            </div>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                <div>
                                    <label class="block text-[10px] font-black text-white/30 uppercase tracking-[0.2em] mb-2">Budget Range</label>
                                    <input type="text" name="budget"
                                        class="w-full bg-white/[0.03] border border-white/[0.08] rounded-xl px-4 py-3 text-white focus:outline-none focus:border-cyan-500/50 focus:ring-1 focus:ring-cyan-500/30 hover:border-white/15 transition-all placeholder-white/20 text-sm"
                                        placeholder="e.g., $100 - $300">
                                </div>
                                <div>
                                    <label class="block text-[10px] font-black text-white/30 uppercase tracking-[0.2em] mb-2">Timeline</label>
                                    <input type="text" name="timeline"
                                        class="w-full bg-white/[0.03] border border-white/[0.08] rounded-xl px-4 py-3 text-white focus:outline-none focus:border-cyan-500/50 focus:ring-1 focus:ring-cyan-500/30 hover:border-white/15 transition-all placeholder-white/20 text-sm"
                                        placeholder="e.g., 1-2 weeks">
                                </div>
                            </div>

                            <!-- Service Selector -->
                            <div x-data="{ open: false }" class="relative z-50">
                                <label class="block text-[10px] font-black text-white/30 uppercase tracking-[0.2em] mb-2">Service Needed</label>
                                <div @click="open = !open" @click.away="open = false"
                                    class="w-full bg-white/[0.03] border border-white/[0.08] rounded-xl px-4 py-3 text-white hover:border-white/15 transition-all cursor-pointer flex justify-between items-center group">
                                    <span x-text="serviceRequest.selected || 'Select a service...'"
                                        :class="serviceRequest.selected ? 'text-white' : 'text-white/20'" class="text-sm"></span>
                                    <i class="fas fa-chevron-down text-white/20 text-xs transition-transform duration-300 group-hover:text-white/40"
                                        :class="open ? 'rotate-180' : ''"></i>
                                </div>
                                <div x-show="open" x-transition:enter="transition ease-out duration-200"
                                    x-transition:enter-start="opacity-0 translate-y-2"
                                    x-transition:enter-end="opacity-100 translate-y-0"
                                    x-transition:leave="transition ease-in duration-150"
                                    x-transition:leave-start="opacity-100" x-transition:leave-end="opacity-0 translate-y-2" x-cloak
                                    class="absolute top-full left-0 w-full mt-2 bg-[#0B0B0F]/98 backdrop-blur-2xl border border-white/[0.08] rounded-2xl shadow-[0_20px_60px_rgba(0,0,0,0.8)] p-6 ring-1 ring-white/5">
                                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                                        <div>
                                            <h4 class="text-pink-400 font-black mb-3 uppercase text-[9px] tracking-[0.2em] border-b border-white/5 pb-2">Frontend Services</h4>
                                            <div class="space-y-2">
                                                <div @click="serviceRequest.selected = 'UI/UX Design Mockups'; open = false" class="text-sm text-white/40 hover:text-white cursor-pointer transition-all hover:translate-x-1 py-1">UI/UX Design Mockups</div>
                                                <div @click="serviceRequest.selected = 'Website Portfolio Development'; open = false" class="text-sm text-white/40 hover:text-white cursor-pointer transition-all hover:translate-x-1 py-1">Website Portfolio Development</div>
                                                <div @click="serviceRequest.selected = 'Custom Website Architecture'; open = false" class="text-sm text-white/40 hover:text-white cursor-pointer transition-all hover:translate-x-1 py-1">Custom Website Architecture</div>
                                            </div>
                                        </div>
                                        <div>
                                            <h4 class="text-cyan-400 font-black mb-3 uppercase text-[9px] tracking-[0.2em] border-b border-white/5 pb-2">Analytics Services</h4>
                                            <div class="space-y-2">
                                                <div @click="serviceRequest.selected = 'Data Warehousing & SQL'; open = false" class="text-sm text-white/40 hover:text-white cursor-pointer transition-all hover:translate-x-1 py-1">Data Warehousing & SQL</div>
                                                <div @click="serviceRequest.selected = 'Interactive Data Dashboards'; open = false" class="text-sm text-white/40 hover:text-white cursor-pointer transition-all hover:translate-x-1 py-1">Interactive Data Dashboards</div>
                                                <div @click="serviceRequest.selected = 'Predictive ML Models'; open = false" class="text-sm text-white/40 hover:text-white cursor-pointer transition-all hover:translate-x-1 py-1">Predictive ML Models</div>
                                                <div @click="serviceRequest.selected = 'Statistical Analysis'; open = false" class="text-sm text-white/40 hover:text-white cursor-pointer transition-all hover:translate-x-1 py-1">Statistical Analysis</div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="mt-4 pt-3 border-t border-white/5 text-center">
                                        <div @click="serviceRequest.selected = 'Other Inquiry'; open = false" class="text-sm text-white/30 hover:text-white cursor-pointer transition-colors italic">Got another idea? Click here.</div>
                                    </div>
                                </div>
                                <input type="hidden" name="service" :value="serviceRequest.selected" required>
                            </div>

                            <style>h4+.space-y-2>div:hover>div{opacity:1;}</style>

                            <div class="relative z-0">
                                <label class="block text-[10px] font-black text-white/30 uppercase tracking-[0.2em] mb-2">Project Details</label>
                                <textarea name="details" required rows="5"
                                    class="w-full bg-white/[0.03] border border-white/[0.08] rounded-xl px-4 py-3 text-white focus:outline-none focus:border-cyan-500/50 focus:ring-1 focus:ring-cyan-500/30 hover:border-white/15 transition-all placeholder-white/20 resize-none text-sm"
                                    placeholder="Tell me about your project, goals, references, and what success looks like..."></textarea>
                            </div>

                            <div class="rounded-2xl border border-white/[0.05] bg-white/[0.02] p-4 text-sm text-white/30">
                                After you submit, your email app will open with a pre-filled project brief so you can send it directly.
                            </div>

                            <button type="submit"
                                class="w-full btn-pill !bg-gradient-to-r from-cyan-500 to-pink-500 !text-white border-none mt-2 shadow-[0_0_30px_rgba(6,182,212,0.2)] hover:shadow-[0_0_40px_rgba(236,72,153,0.4)] transition-all flex justify-center py-4 text-lg cursor-pointer">
                                Send Project Brief <i class="fas fa-paper-plane ml-2 mt-1"></i>
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

    </div> <!-- END SERVICES VIEW -->
"""

if idx_start != -1 and idx_end != -1:
    text = text[:idx_start] + new_services + text[idx_end + len(end_marker):]
    with codecs.open('index.html', 'w', 'utf-8') as f:
        f.write(text)
    print("SUCCESS")
else:
    print("FAIL: start=", idx_start, "end=", idx_end)
