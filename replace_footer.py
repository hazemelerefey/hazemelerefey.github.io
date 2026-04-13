import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    text = f.read()

# Find the old footer/CTA block
old_start = '    <!-- Global Footer / CTA -->\r\n'
old_end = '    </div>\r\n\r\n    <!-- MY WORK'

idx_start = text.find(old_start)
if idx_start == -1:
    old_start = '    <!-- Global Footer / CTA -->\n'
    idx_start = text.find(old_start)

idx_end = text.find(old_end)
if idx_end == -1:
    old_end = '    </div>\n\n    <!-- MY WORK'
    idx_end = text.find(old_end)

print(f"Start: {idx_start}, End: {idx_end}")

if idx_start == -1 or idx_end == -1:
    print("FAIL: Could not find markers")
    exit(1)

# We want to end right at "</div>\n" (the closing of the footer wrapper)
# Find the actual end of </div> after idx_end's start
close_end = text.find('\n', idx_end) + 1

new_content = """    <!-- ============================================== -->
    <!-- PREMIUM CTA SECTION (Home/Portfolio only)       -->
    <!-- ============================================== -->
    <div x-show="activeView !== 'workspace' && activeView !== 'services'" x-transition>
        <section class="relative py-24 px-6 overflow-hidden">
            <!-- Background ambient -->
            <div class="absolute inset-0 pointer-events-none">
                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[300px] bg-gradient-to-r from-cyan-500/8 via-purple-500/8 to-pink-500/8 rounded-full blur-[120px]"></div>
            </div>
            <div class="max-w-4xl mx-auto text-center relative z-10" data-aos="fade-up">
                <div class="inline-flex items-center gap-2 bg-white/[0.03] border border-white/[0.08] rounded-full px-5 py-2 mb-8">
                    <div class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></div>
                    <span class="text-[10px] font-black uppercase tracking-[0.2em] text-white/40">Available for new projects</span>
                </div>
                <h2 class="text-4xl md:text-5xl lg:text-6xl font-black text-white mb-6 leading-tight">
                    Let's build something<br><span class="text-gradient-cyan-pink">extraordinary</span> together
                </h2>
                <p class="text-white/35 text-lg max-w-2xl mx-auto mb-10 leading-relaxed font-light">
                    Whether it's a stunning portfolio, an interactive dashboard, or a data-driven web app — I'm ready to turn your vision into reality.
                </p>
                <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
                    <a href="mailto:hazemkhaled53@gmail.com"
                        class="group relative inline-flex items-center gap-3 bg-gradient-to-r from-cyan-500 to-pink-500 text-white font-bold text-lg px-10 py-4 rounded-full shadow-[0_0_30px_rgba(6,182,212,0.25)] hover:shadow-[0_0_50px_rgba(236,72,153,0.35)] transition-all duration-500 cursor-pointer overflow-hidden">
                        <span class="relative z-10">Send me an email</span>
                        <i class="fas fa-arrow-right relative z-10 group-hover:translate-x-1 transition-transform"></i>
                        <div class="absolute inset-0 bg-gradient-to-r from-pink-500 to-cyan-500 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                    </a>
                    <a href="#" @click.prevent="navTo('services')"
                        class="inline-flex items-center gap-2 text-white/40 hover:text-white font-medium text-sm px-6 py-4 rounded-full border border-white/[0.08] hover:border-white/20 transition-all duration-300 cursor-pointer">
                        <i class="fas fa-briefcase text-xs"></i> View Services
                    </a>
                </div>
            </div>
        </section>
    </div>

    <!-- ============================================== -->
    <!-- GLOBAL PROFESSIONAL FOOTER                      -->
    <!-- ============================================== -->
    <footer class="relative border-t border-white/[0.05] bg-[#050508]">
        <!-- Top gradient line -->
        <div class="absolute inset-x-0 top-0 h-[1px] bg-gradient-to-r from-transparent via-white/10 to-transparent"></div>

        <div class="max-w-7xl mx-auto px-6 md:px-12 pt-16 pb-8">
            <!-- Footer Grid -->
            <div class="grid grid-cols-1 md:grid-cols-4 gap-12 mb-14">
                <!-- Brand Column -->
                <div class="md:col-span-2">
                    <a href="#" @click.prevent="navTo('home')" class="group inline-flex items-center gap-3 mb-5">
                        <svg width="44" height="22" viewBox="0 0 60 30" fill="none" xmlns="http://www.w3.org/2000/svg"
                            class="transform transition-transform duration-300 group-hover:scale-110 group-hover:drop-shadow-[0_0_8px_rgba(6,182,212,0.8)]">
                            <text x="0" y="24" font-family="'Plus Jakarta Sans', Arial, sans-serif" font-weight="900"
                                font-size="28" fill="url(#hey-gradient-ft)" letter-spacing="-1">HEY</text>
                            <defs>
                                <linearGradient id="hey-gradient-ft" x1="0" y1="0" x2="60" y2="30" gradientUnits="userSpaceOnUse">
                                    <stop stop-color="#06B6D4" />
                                    <stop offset="0.5" stop-color="#A855F7" />
                                    <stop offset="1" stop-color="#EC4899" />
                                </linearGradient>
                            </defs>
                        </svg>
                    </a>
                    <p class="text-white/25 text-sm leading-relaxed max-w-sm mb-6">
                        Data Analyst & Frontend Developer crafting premium digital experiences — from interactive dashboards to pixel-perfect web interfaces.
                    </p>
                    <div class="flex gap-3">
                        <a href="https://github.com/hazemelerefey" target="_blank" rel="noopener noreferrer" aria-label="GitHub"
                            class="w-10 h-10 rounded-xl bg-white/[0.03] border border-white/[0.06] flex items-center justify-center text-white/25 hover:text-white hover:border-white/20 hover:bg-white/[0.06] transition-all duration-300 cursor-pointer">
                            <i class="fab fa-github text-sm"></i>
                        </a>
                        <a href="https://linkedin.com/in/hazemelerefy" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn"
                            class="w-10 h-10 rounded-xl bg-white/[0.03] border border-white/[0.06] flex items-center justify-center text-white/25 hover:text-white hover:border-[#0A66C2]/40 hover:bg-[#0A66C2]/10 transition-all duration-300 cursor-pointer">
                            <i class="fab fa-linkedin-in text-sm"></i>
                        </a>
                        <a href="https://www.upwork.com/freelancers/~01095d37046356f7d5" target="_blank" rel="noopener noreferrer" aria-label="Upwork"
                            class="w-10 h-10 rounded-xl bg-white/[0.03] border border-white/[0.06] flex items-center justify-center text-white/25 hover:text-white hover:border-[#14A800]/40 hover:bg-[#14A800]/10 transition-all duration-300 cursor-pointer">
                            <i class="fas fa-briefcase text-sm"></i>
                        </a>
                    </div>
                </div>

                <!-- Quick Links -->
                <div>
                    <h4 class="text-[10px] font-black uppercase tracking-[0.25em] text-white/30 mb-5">Navigate</h4>
                    <ul class="space-y-3">
                        <li><a href="#" @click.prevent="navTo('home')" class="text-sm text-white/25 hover:text-white transition-colors cursor-pointer">Home</a></li>
                        <li><a href="#" @click.prevent="navTo('portfolio')" class="text-sm text-white/25 hover:text-white transition-colors cursor-pointer">Portfolio</a></li>
                        <li><a href="#" @click.prevent="navTo('workspace')" class="text-sm text-white/25 hover:text-white transition-colors cursor-pointer">Workspace</a></li>
                        <li><a href="#" @click.prevent="navTo('services')" class="text-sm text-white/25 hover:text-white transition-colors cursor-pointer">Services</a></li>
                    </ul>
                </div>

                <!-- Contact -->
                <div>
                    <h4 class="text-[10px] font-black uppercase tracking-[0.25em] text-white/30 mb-5">Get in Touch</h4>
                    <ul class="space-y-3">
                        <li>
                            <a href="mailto:hazemkhaled53@gmail.com" class="text-sm text-white/25 hover:text-white transition-colors flex items-center gap-2 cursor-pointer">
                                <i class="fas fa-envelope text-[10px] text-cyan-400/40"></i> hazemkhaled53@gmail.com
                            </a>
                        </li>
                        <li>
                            <a href="https://www.upwork.com/freelancers/~01095d37046356f7d5" target="_blank" rel="noopener noreferrer" class="text-sm text-white/25 hover:text-white transition-colors flex items-center gap-2 cursor-pointer">
                                <i class="fas fa-briefcase text-[10px] text-[#14A800]/60"></i> Hire on Upwork
                            </a>
                        </li>
                        <li>
                            <a href="https://github.com/hazemelerefey" target="_blank" rel="noopener noreferrer" class="text-sm text-white/25 hover:text-white transition-colors flex items-center gap-2 cursor-pointer">
                                <i class="fab fa-github text-[10px] text-white/30"></i> GitHub Profile
                            </a>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Bottom Bar -->
            <div class="pt-6 border-t border-white/[0.04] flex flex-col md:flex-row justify-between items-center gap-4">
                <p class="text-white/15 text-xs">&copy; 2026 Hazem Khaled Ezat. All Rights Reserved.</p>
                <p class="text-white/10 text-[10px] uppercase tracking-[0.2em]">Designed & Built with passion</p>
            </div>
        </div>
    </footer>

"""

text = text[:idx_start] + new_content + text[close_end:]

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(text)
print("SUCCESS")
