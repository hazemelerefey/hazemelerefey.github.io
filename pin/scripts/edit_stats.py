import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add CSS animations
css_to_add = """
        .animate-marquee-left {
            animation: marquee-left 30s linear infinite !important;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-15px); }
        }
        .animate-float-1 { animation: float 6s ease-in-out infinite; }
        .animate-float-2 { animation: float 7s ease-in-out infinite 1s; }
        .animate-float-3 { animation: float 5s ease-in-out infinite 2s; }
        .animate-float-4 { animation: float 8s ease-in-out infinite 0.5s; }
    </style>"""

html = html.replace("""
        .animate-marquee-left {
            animation: marquee-left 30s linear infinite !important;
        }
    </style>""", css_to_add)

# 2. Add Floating Cloud at bottom of header
cloud_html = """
                    <!-- Floating Stats Cloud -->
                    <div class="flex flex-wrap justify-center items-center gap-4 md:gap-8 mt-16 lg:mt-24 mb-6 relative z-10 w-full px-4" x-data="{ shown: false }" x-intersect.once="shown = true">
                        
                        <!-- Stat 1: Projects -->
                        <div class="animate-float-1 transform md:-translate-y-6" data-aos="fade-up" data-aos-delay="400">
                            <div class="group relative bg-cardBase/60 backdrop-blur-xl border border-cardBorder p-4 md:p-5 rounded-2xl hover:scale-105 transition-transform shadow-lg flex items-center gap-4">
                                <div class="absolute inset-0 bg-cyan-500/5 rounded-2xl blur-xl group-hover:bg-cyan-500/10 transition-all"></div>
                                <div class="w-10 h-10 md:w-12 md:h-12 rounded-xl bg-cyan-500/10 flex items-center justify-center border border-cyan-500/20 shadow-[0_0_10px_rgba(6,182,212,0.2)]">
                                    <i class="fas fa-project-diagram text-cyan-400 text-lg md:text-xl group-hover:scale-110 transition-transform"></i>
                                </div>
                                <div>
                                    <div class="text-2xl md:text-3xl font-black text-white leading-none mb-1">
                                        <span x-text="shown ? '50+' : '0'" class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500" :class="shown && 'transition-all duration-1000'"></span>
                                    </div>
                                    <div class="text-textMuted text-[10px] md:text-xs font-bold uppercase tracking-[0.2em] leading-none">Projects</div>
                                </div>
                            </div>
                        </div>

                        <!-- Stat 2: Clients -->
                        <div class="animate-float-2 transform md:translate-y-4" data-aos="fade-up" data-aos-delay="500">
                            <div class="group relative bg-cardBase/60 backdrop-blur-xl border border-cardBorder p-4 md:p-5 rounded-2xl hover:scale-105 transition-transform shadow-lg flex items-center gap-4">
                                <div class="absolute inset-0 bg-pink-500/5 rounded-2xl blur-xl group-hover:bg-pink-500/10 transition-all"></div>
                                <div class="w-10 h-10 md:w-12 md:h-12 rounded-xl bg-pink-500/10 flex items-center justify-center border border-pink-500/20 shadow-[0_0_10px_rgba(236,72,153,0.2)]">
                                    <i class="fas fa-smile-beam text-pink-400 text-lg md:text-xl group-hover:scale-110 transition-transform"></i>
                                </div>
                                <div>
                                    <div class="text-2xl md:text-3xl font-black text-white leading-none mb-1">
                                        <span x-text="shown ? '30+' : '0'" class="text-transparent bg-clip-text bg-gradient-to-r from-pink-400 to-rose-500" :class="shown && 'transition-all duration-1000'"></span>
                                    </div>
                                    <div class="text-textMuted text-[10px] md:text-xs font-bold uppercase tracking-[0.2em] leading-none">Clients</div>
                                </div>
                            </div>
                        </div>

                        <!-- Stat 3: Experience -->
                        <div class="animate-float-3 transform md:-translate-y-2" data-aos="fade-up" data-aos-delay="600">
                            <div class="group relative bg-cardBase/60 backdrop-blur-xl border border-cardBorder p-4 md:p-5 rounded-2xl hover:scale-105 transition-transform shadow-lg flex items-center gap-4">
                                <div class="absolute inset-0 bg-purple-500/5 rounded-2xl blur-xl group-hover:bg-purple-500/10 transition-all"></div>
                                <div class="w-10 h-10 md:w-12 md:h-12 rounded-xl bg-purple-500/10 flex items-center justify-center border border-purple-500/20 shadow-[0_0_10px_rgba(168,85,247,0.2)]">
                                    <i class="fas fa-crown text-purple-400 text-lg md:text-xl group-hover:scale-110 transition-transform"></i>
                                </div>
                                <div>
                                    <div class="text-2xl md:text-3xl font-black text-white leading-none mb-1">
                                        <span x-text="shown ? '3+' : '0'" class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-indigo-500" :class="shown && 'transition-all duration-1000'"></span>
                                    </div>
                                    <div class="text-textMuted text-[10px] md:text-xs font-bold uppercase tracking-[0.2em] leading-none">Years</div>
                                </div>
                            </div>
                        </div>

                        <!-- Stat 4: Platforms -->
                        <div class="animate-float-4 transform md:translate-y-6" data-aos="fade-up" data-aos-delay="700">
                            <div class="group relative bg-cardBase/60 backdrop-blur-xl border border-cardBorder p-4 md:p-5 rounded-2xl hover:scale-105 transition-transform shadow-lg flex items-center gap-4">
                                <div class="absolute inset-0 bg-amber-500/5 rounded-2xl blur-xl group-hover:bg-amber-500/10 transition-all"></div>
                                <div class="w-10 h-10 md:w-12 md:h-12 rounded-xl bg-amber-500/10 flex items-center justify-center border border-amber-500/20 shadow-[0_0_10px_rgba(245,158,11,0.2)]">
                                    <i class="fas fa-globe text-amber-400 text-lg md:text-xl group-hover:scale-110 transition-transform"></i>
                                </div>
                                <div>
                                    <div class="text-2xl md:text-3xl font-black text-white leading-none mb-1">
                                        <span x-text="shown ? '5' : '0'" class="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-orange-500" :class="shown && 'transition-all duration-1000'"></span>
                                    </div>
                                    <div class="text-textMuted text-[10px] md:text-xs font-bold uppercase tracking-[0.2em] leading-none">Platforms</div>
                                </div>
                            </div>
                        </div>

                    </div>

                    <!-- Scroll Down Indicator -->
                    <div data-aos="fade-up" data-aos-delay="800" class="mt-8 animate-bounce w-full text-center">
                        <i class="fas fa-chevron-down text-textMuted text-2xl opacity-50"></i>
                    </div>
                </div>
            </header>"""

# Replace the scroll down indicator and header end
html = re.sub(
    r'<!-- Scroll Down Indicator -->\s*<div data-aos="fade-up" data-aos-delay="600" class="mt-16 animate-bounce">\s*<i class="fas fa-chevron-down text-textMuted text-2xl opacity-50"></i>\s*</div>\s*</div>\s*</header>',
    cloud_html,
    html
)

# 3. Remove old Stats Bar
# Use regex to find and remove the whole section starting with <!-- ══ STATS BAR ══ -->
# up to the next section tag closing
old_stat_bar_pattern = r'<!-- ═══════════════════ STATS BAR ═══════════════════ -->.*?</section>'
html = re.sub(old_stat_bar_pattern, '', html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html successfully.")
