import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    text = f.read()

# Find workspace card grids
start_marker = '<!-- Frontend Workspace Content -->'
end_marker = '</div> <!-- END WORKSPACE VIEW -->'

idx_start = text.find(start_marker)
idx_end = text.find(end_marker)

if idx_start == -1:
    # Try without exact spacing
    start_marker = '<!-- Frontend Workspace Content -->\r\n'
    idx_start = text.find(start_marker)

if idx_end == -1:
    end_marker = '</div> <!-- END WORKSPACE VIEW -->\r\n'
    idx_end = text.find(end_marker)

new_workspace_cards = """<!-- Frontend Workspace Content -->
        <div x-show="workspaceTab === 'frontend'" x-transition:enter="transition ease-in-out duration-300"
            x-transition:enter-start="opacity-0 translate-y-4" x-transition:enter-end="opacity-100 translate-y-0"
            class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

            <!-- REPO: JobPulse -->
            <a href="https://github.com/hazemelerefey/jobpulse" target="_blank" data-aos="fade-up" data-aos-delay="0"
                class="block bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-7 relative overflow-hidden group cursor-pointer hover:border-pink-500/40 transition-all duration-500 backdrop-blur-xl">
                <div class="absolute top-0 right-0 w-40 h-40 bg-pink-500/8 rounded-full blur-[60px] group-hover:bg-pink-500/20 transition-all duration-700"></div>
                <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-pink-500/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="relative z-10">
                    <div class="flex justify-between items-start mb-5">
                        <div class="w-11 h-11 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center text-white/70 group-hover:text-white group-hover:border-pink-500/30 transition-all duration-300">
                            <i class="fab fa-github text-xl"></i>
                        </div>
                        <span class="text-[10px] font-black uppercase tracking-[0.15em] text-pink-400 bg-pink-500/10 border border-pink-500/20 px-3 py-1.5 rounded-full">Next.js</span>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-1.5 group-hover:text-pink-400 transition-colors duration-300">JobPulse</h3>
                    <p class="text-[10px] uppercase tracking-[0.2em] text-white/25 font-mono mb-4">hazemelerefey/jobpulse</p>
                    <p class="text-white/50 text-sm leading-relaxed mb-6">Premium job market intelligence dashboard — role demand, salary signals, and skill momentum through a polished product experience.</p>
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <span class="flex items-center gap-1.5 text-xs text-white/30"><i class="fas fa-circle text-[6px] text-yellow-400"></i> JavaScript</span>
                            <span class="flex items-center gap-1.5 text-xs text-white/30"><i class="fas fa-star text-[8px] text-yellow-500/60"></i> 0</span>
                        </div>
                        <span class="text-pink-400/60 text-xs font-bold uppercase tracking-wider group-hover:text-pink-400 transition-colors flex items-center gap-1.5">View <i class="fas fa-arrow-right text-[10px] group-hover:translate-x-1 transition-transform"></i></span>
                    </div>
                </div>
            </a>

            <!-- REPO: E-Commerce Admin UI -->
            <a href="https://github.com/hazemelerefey/frontend-ecommerce-dashboard" target="_blank" data-aos="fade-up" data-aos-delay="100"
                class="block bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-7 relative overflow-hidden group cursor-pointer hover:border-pink-500/40 transition-all duration-500 backdrop-blur-xl">
                <div class="absolute top-0 right-0 w-40 h-40 bg-purple-500/8 rounded-full blur-[60px] group-hover:bg-purple-500/20 transition-all duration-700"></div>
                <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-purple-500/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="relative z-10">
                    <div class="flex justify-between items-start mb-5">
                        <div class="w-11 h-11 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center text-white/70 group-hover:text-white group-hover:border-purple-500/30 transition-all duration-300">
                            <i class="fab fa-github text-xl"></i>
                        </div>
                        <span class="text-[10px] font-black uppercase tracking-[0.15em] text-purple-400 bg-purple-500/10 border border-purple-500/20 px-3 py-1.5 rounded-full">React</span>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-1.5 group-hover:text-purple-400 transition-colors duration-300">E-Commerce Admin UI</h3>
                    <p class="text-[10px] uppercase tracking-[0.2em] text-white/25 font-mono mb-4">hazemelerefey/frontend-ecommerce-dashboard</p>
                    <p class="text-white/50 text-sm leading-relaxed mb-6">Consumer-grade admin dashboard for tracking sales velocity, active orders, and user activity with responsive layout and dynamic charts.</p>
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <span class="flex items-center gap-1.5 text-xs text-white/30"><i class="fas fa-circle text-[6px] text-cyan-400"></i> React</span>
                            <span class="flex items-center gap-1.5 text-xs text-white/30"><i class="fas fa-star text-[8px] text-yellow-500/60"></i> 0</span>
                        </div>
                        <span class="text-purple-400/60 text-xs font-bold uppercase tracking-wider group-hover:text-purple-400 transition-colors flex items-center gap-1.5">View <i class="fas fa-arrow-right text-[10px] group-hover:translate-x-1 transition-transform"></i></span>
                    </div>
                </div>
            </a>

            <!-- REPO: Kanban Board -->
            <a href="https://github.com/hazemelerefey/frontend-kanban-board" target="_blank" data-aos="fade-up" data-aos-delay="200"
                class="block bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-7 relative overflow-hidden group cursor-pointer hover:border-cyan-500/40 transition-all duration-500 backdrop-blur-xl">
                <div class="absolute top-0 right-0 w-40 h-40 bg-cyan-500/8 rounded-full blur-[60px] group-hover:bg-cyan-500/20 transition-all duration-700"></div>
                <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-cyan-500/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="relative z-10">
                    <div class="flex justify-between items-start mb-5">
                        <div class="w-11 h-11 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center text-white/70 group-hover:text-white group-hover:border-cyan-500/30 transition-all duration-300">
                            <i class="fab fa-github text-xl"></i>
                        </div>
                        <span class="text-[10px] font-black uppercase tracking-[0.15em] text-cyan-400 bg-cyan-500/10 border border-cyan-500/20 px-3 py-1.5 rounded-full">Frontend</span>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-1.5 group-hover:text-cyan-400 transition-colors duration-300">Kanban Board</h3>
                    <p class="text-[10px] uppercase tracking-[0.2em] text-white/25 font-mono mb-4">hazemelerefey/frontend-kanban-board</p>
                    <p class="text-white/50 text-sm leading-relaxed mb-6">Fluid drag-and-drop task management interface built for board clarity, workflow movement, and polished product-style interactions.</p>
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <span class="flex items-center gap-1.5 text-xs text-white/30"><i class="fas fa-circle text-[6px] text-yellow-400"></i> JavaScript</span>
                            <span class="flex items-center gap-1.5 text-xs text-white/30"><i class="fas fa-star text-[8px] text-yellow-500/60"></i> 0</span>
                        </div>
                        <span class="text-cyan-400/60 text-xs font-bold uppercase tracking-wider group-hover:text-cyan-400 transition-colors flex items-center gap-1.5">View <i class="fas fa-arrow-right text-[10px] group-hover:translate-x-1 transition-transform"></i></span>
                    </div>
                </div>
            </a>

            <!-- REPO: Real Estate Finder -->
            <a href="https://github.com/hazemelerefey/frontend-realestate-finder" target="_blank" data-aos="fade-up" data-aos-delay="300"
                class="block bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-7 relative overflow-hidden group cursor-pointer hover:border-emerald-500/40 transition-all duration-500 backdrop-blur-xl">
                <div class="absolute top-0 right-0 w-40 h-40 bg-emerald-500/8 rounded-full blur-[60px] group-hover:bg-emerald-500/20 transition-all duration-700"></div>
                <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-emerald-500/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="relative z-10">
                    <div class="flex justify-between items-start mb-5">
                        <div class="w-11 h-11 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center text-white/70 group-hover:text-white group-hover:border-emerald-500/30 transition-all duration-300">
                            <i class="fab fa-github text-xl"></i>
                        </div>
                        <span class="text-[10px] font-black uppercase tracking-[0.15em] text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 px-3 py-1.5 rounded-full">Frontend</span>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-1.5 group-hover:text-emerald-400 transition-colors duration-300">Real Estate Finder</h3>
                    <p class="text-[10px] uppercase tracking-[0.2em] text-white/25 font-mono mb-4">hazemelerefey/frontend-realestate-finder</p>
                    <p class="text-white/50 text-sm leading-relaxed mb-6">Advanced property search interface with filtering architecture, listing discovery map patterns, and a minimal product-style browsing aesthetic.</p>
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <span class="flex items-center gap-1.5 text-xs text-white/30"><i class="fas fa-circle text-[6px] text-yellow-400"></i> JavaScript</span>
                            <span class="flex items-center gap-1.5 text-xs text-white/30"><i class="fas fa-star text-[8px] text-yellow-500/60"></i> 0</span>
                        </div>
                        <span class="text-emerald-400/60 text-xs font-bold uppercase tracking-wider group-hover:text-emerald-400 transition-colors flex items-center gap-1.5">View <i class="fas fa-arrow-right text-[10px] group-hover:translate-x-1 transition-transform"></i></span>
                    </div>
                </div>
            </a>
        </div>

        <!-- Analytics Workspace Content -->
        <div x-show="workspaceTab === 'analytics'" x-cloak x-transition:enter="transition ease-in-out duration-300"
            x-transition:enter-start="opacity-0 translate-y-4" x-transition:enter-end="opacity-100 translate-y-0"
            class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

            <!-- REPO: Healthcare Waitlist Dashboard -->
            <a href="https://github.com/hazemelerefey/healthcare-operations-waitlist-dashboard" target="_blank" data-aos="fade-up" data-aos-delay="0"
                class="block bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-7 relative overflow-hidden group cursor-pointer hover:border-emerald-500/40 transition-all duration-500 backdrop-blur-xl">
                <div class="absolute top-0 right-0 w-40 h-40 bg-emerald-500/8 rounded-full blur-[60px] group-hover:bg-emerald-500/20 transition-all duration-700"></div>
                <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-emerald-500/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="relative z-10">
                    <div class="flex justify-between items-start mb-5">
                        <div class="w-11 h-11 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center text-white/70 group-hover:text-white group-hover:border-emerald-500/30 transition-all duration-300">
                            <i class="fab fa-github text-xl"></i>
                        </div>
                        <span class="text-[10px] font-black uppercase tracking-[0.15em] text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 px-3 py-1.5 rounded-full">Power BI</span>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-1.5 group-hover:text-emerald-400 transition-colors duration-300">Healthcare Waitlist</h3>
                    <p class="text-[10px] uppercase tracking-[0.2em] text-white/25 font-mono mb-4">hazemelerefey/healthcare-operations-waitlist-dashboard</p>
                    <p class="text-white/50 text-sm leading-relaxed mb-6">Executive decision-support dashboard revealing service bottlenecks, specialty backlog patterns, and critical operational healthcare priorities.</p>
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <span class="flex items-center gap-1.5 text-xs text-white/30"><i class="fas fa-circle text-[6px] text-amber-400"></i> DAX</span>
                            <span class="flex items-center gap-1.5 text-xs text-white/30"><i class="fas fa-star text-[8px] text-yellow-500/60"></i> 0</span>
                        </div>
                        <span class="text-emerald-400/60 text-xs font-bold uppercase tracking-wider group-hover:text-emerald-400 transition-colors flex items-center gap-1.5">View <i class="fas fa-arrow-right text-[10px] group-hover:translate-x-1 transition-transform"></i></span>
                    </div>
                </div>
            </a>

            <!-- REPO: Global Sales Tracker -->
            <a href="https://github.com/hazemelerefey/global-ecommerce-sales-tracker" target="_blank" data-aos="fade-up" data-aos-delay="100"
                class="block bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-7 relative overflow-hidden group cursor-pointer hover:border-amber-500/40 transition-all duration-500 backdrop-blur-xl">
                <div class="absolute top-0 right-0 w-40 h-40 bg-amber-500/8 rounded-full blur-[60px] group-hover:bg-amber-500/20 transition-all duration-700"></div>
                <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-amber-500/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="relative z-10">
                    <div class="flex justify-between items-start mb-5">
                        <div class="w-11 h-11 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center text-white/70 group-hover:text-white group-hover:border-amber-500/30 transition-all duration-300">
                            <i class="fab fa-github text-xl"></i>
                        </div>
                        <span class="text-[10px] font-black uppercase tracking-[0.15em] text-amber-400 bg-amber-500/10 border border-amber-500/20 px-3 py-1.5 rounded-full">Power BI</span>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-1.5 group-hover:text-amber-400 transition-colors duration-300">Global Sales Tracker</h3>
                    <p class="text-[10px] uppercase tracking-[0.2em] text-white/25 font-mono mb-4">hazemelerefey/global-ecommerce-sales-tracker</p>
                    <p class="text-white/50 text-sm leading-relaxed mb-6">Central BI command center analyzing multi-region revenue, profit margins, and order fulfillment vectors for enterprise-level sales operations.</p>
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <span class="flex items-center gap-1.5 text-xs text-white/30"><i class="fas fa-circle text-[6px] text-amber-400"></i> DAX</span>
                            <span class="flex items-center gap-1.5 text-xs text-white/30"><i class="fas fa-star text-[8px] text-yellow-500/60"></i> 0</span>
                        </div>
                        <span class="text-amber-400/60 text-xs font-bold uppercase tracking-wider group-hover:text-amber-400 transition-colors flex items-center gap-1.5">View <i class="fas fa-arrow-right text-[10px] group-hover:translate-x-1 transition-transform"></i></span>
                    </div>
                </div>
            </a>

            <!-- REPO: Churn Prediction -->
            <a href="https://github.com/hazemelerefey/analytics-churn-prediction" target="_blank" data-aos="fade-up" data-aos-delay="200"
                class="block bg-gradient-to-br from-white/[0.04] to-transparent border border-white/[0.08] rounded-3xl p-7 relative overflow-hidden group cursor-pointer hover:border-red-500/40 transition-all duration-500 backdrop-blur-xl">
                <div class="absolute top-0 right-0 w-40 h-40 bg-red-500/8 rounded-full blur-[60px] group-hover:bg-red-500/20 transition-all duration-700"></div>
                <div class="absolute inset-x-0 bottom-0 h-[1px] bg-gradient-to-r from-transparent via-red-500/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="relative z-10">
                    <div class="flex justify-between items-start mb-5">
                        <div class="w-11 h-11 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center text-white/70 group-hover:text-white group-hover:border-red-500/30 transition-all duration-300">
                            <i class="fab fa-github text-xl"></i>
                        </div>
                        <span class="text-[10px] font-black uppercase tracking-[0.15em] text-red-400 bg-red-500/10 border border-red-500/20 px-3 py-1.5 rounded-full">Python / ML</span>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-1.5 group-hover:text-red-400 transition-colors duration-300">Churn Prediction</h3>
                    <p class="text-[10px] uppercase tracking-[0.2em] text-white/25 font-mono mb-4">hazemelerefey/analytics-churn-prediction</p>
                    <p class="text-white/50 text-sm leading-relaxed mb-6">Predictive analytics engine identifying subtle churn risk behaviors through machine learning feature importance, enabling proactive customer retention.</p>
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <span class="flex items-center gap-1.5 text-xs text-white/30"><i class="fas fa-circle text-[6px] text-blue-400"></i> Python</span>
                            <span class="flex items-center gap-1.5 text-xs text-white/30"><i class="fas fa-star text-[8px] text-yellow-500/60"></i> 0</span>
                        </div>
                        <span class="text-red-400/60 text-xs font-bold uppercase tracking-wider group-hover:text-red-400 transition-colors flex items-center gap-1.5">View <i class="fas fa-arrow-right text-[10px] group-hover:translate-x-1 transition-transform"></i></span>
                    </div>
                </div>
            </a>
        </div>

    """

if idx_start != -1 and idx_end != -1:
    text = text[:idx_start] + new_workspace_cards + text[idx_end:]
    with codecs.open('index.html', 'w', 'utf-8') as f:
        f.write(text)
    print("SUCCESS")
else:
    print("FAIL: start=", idx_start, "end=", idx_end)
