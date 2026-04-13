import codecs

new_content = """<!-- Telemetry Data Grid (Rare Portfolio Stats) -->
                    <div class="grid grid-cols-1 md:grid-cols-12 gap-4 lg:gap-6 mt-16 lg:mt-24 mb-6 relative z-10 w-full px-4 max-w-6xl mx-auto"
                        x-data="{ shown: false }" x-init="$nextTick(() => { shown = true })" x-intersect.once="shown = true">
                        
                        <style>
                            @keyframes traverse-line {
                                0% { left: 2%; opacity: 0; transform: scale(0.5) translateY(-50%); }
                                10% { opacity: 1; transform: scale(1) translateY(-50%); }
                                90% { opacity: 1; transform: scale(1) translateY(-50%); }
                                100% { left: 98%; opacity: 0; transform: scale(0.5) translateY(-50%); }
                            }
                            .animate-traverse {
                                animation: traverse-line 3s cubic-bezier(0.4, 0, 0.2, 1) infinite;
                            }
                        </style>

                        <!-- Widget 1: Projects (Line Chart) -->
                        <div data-aos="fade-up" data-aos-delay="400"
                            class="md:col-span-7 lg:col-span-5 group relative bg-gradient-to-br from-white/[0.04] to-transparent backdrop-blur-2xl border border-white/[0.08] p-6 rounded-3xl overflow-hidden hover:border-cyan-500/40 transition-all duration-500 min-h-[160px] flex flex-col justify-end shadow-lg cursor-default">
                            <!-- Curved Line Chart Background -->
                            <div class="absolute inset-0 opacity-30 group-hover:opacity-70 transition-opacity duration-700 pointer-events-none mix-blend-screen">
                                <svg viewBox="0 0 200 100" class="w-full h-full" preserveAspectRatio="none">
                                    <path d="M0,25 L200,25 M0,50 L200,50 M0,75 L200,75" stroke="rgba(255,255,255,0.05)" stroke-width="1" stroke-dasharray="4 4" />
                                    <path d="M -10,110 L 0,80 Q 40,90 60,50 T 130,40 T 210,10 L 210,110 Z" fill="url(#cyan-glow)" opacity="0.3"/>
                                    <path d="M -10,80 Q 40,90 60,50 T 130,40 T 210,10" fill="none" stroke="#22d3ee" stroke-width="2.5" stroke-linecap="round" />
                                    <defs>
                                        <linearGradient id="cyan-glow" x1="0" y1="0" x2="0" y2="1">
                                            <stop offset="0%" stop-color="#22d3ee" stop-opacity="0.8" />
                                            <stop offset="100%" stop-color="#22d3ee" stop-opacity="0" />
                                        </linearGradient>
                                    </defs>
                                </svg>
                            </div>
                            
                            <div class="relative z-10 flex items-end justify-between">
                                <div>
                                    <div class="text-[10px] font-black uppercase tracking-[0.25em] text-cyan-400 mb-1 drop-shadow-[0_0_5px_rgba(34,211,238,0.5)]">Delivered</div>
                                    <div class="text-5xl md:text-6xl font-black text-white tracking-tighter leading-none mb-1">
                                        <span x-show="shown" x-transition data-count="60" data-suffix="+">0</span>
                                    </div>
                                    <div class="text-white/40 text-sm font-semibold tracking-wide">Data-driven Projects</div>
                                </div>
                                <div class="w-12 h-12 rounded-2xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-cyan-400 backdrop-blur-md shadow-[0_0_20px_rgba(34,211,238,0.2)] group-hover:scale-110 group-hover:bg-cyan-500/20 transition-all duration-300">
                                    <i class="fas fa-layer-group text-xl"></i>
                                </div>
                            </div>
                        </div>

                        <!-- Widget 2: Clients (Radial Chart) -->
                        <div data-aos="fade-up" data-aos-delay="500"
                            class="md:col-span-5 lg:col-span-3 group relative bg-gradient-to-br from-white/[0.04] to-transparent backdrop-blur-2xl border border-white/[0.08] p-6 rounded-3xl overflow-hidden hover:border-pink-500/40 transition-all duration-500 min-h-[160px] flex flex-col justify-end shadow-lg cursor-default">
                            <!-- Radial Gauge Background -->
                            <div class="absolute -right-8 -top-8 w-40 h-40 opacity-20 group-hover:opacity-60 group-hover:rotate-45 transition-all duration-1000 ease-out pointer-events-none mix-blend-screen">
                                <svg viewBox="0 0 100 100" class="w-full h-full transform -rotate-90">
                                    <circle cx="50" cy="50" r="40" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="8" stroke-dasharray="4 2"/>
                                    <circle cx="50" cy="50" r="40" fill="none" stroke="#ec4899" stroke-width="8" stroke-dasharray="251.2" stroke-dashoffset="100" class="group-hover:stroke-dashoffset-[50] transition-all duration-1000 ease-out"/>
                                    <circle cx="50" cy="50" r="25" fill="none" stroke="rgba(236,72,153,0.4)" stroke-width="2" stroke-dasharray="5 5" class="animate-[spin_10s_linear_infinite]"/>
                                </svg>
                            </div>
                            
                            <div class="relative z-10">
                                <div class="text-[10px] font-black uppercase tracking-[0.25em] text-pink-400 mb-1 drop-shadow-[0_0_5px_rgba(236,72,153,0.5)]">Satisfied</div>
                                <div class="text-5xl md:text-6xl font-black text-white tracking-tighter leading-none mb-1">
                                    <span x-show="shown" x-transition data-count="20" data-suffix="+">0</span>
                                </div>
                                <div class="text-white/40 text-sm font-semibold tracking-wide">Global Clients</div>
                            </div>
                        </div>

                        <!-- Widget 3: Years (Equalizer) -->
                        <div data-aos="fade-up" data-aos-delay="600"
                            class="md:col-span-12 lg:col-span-4 group relative bg-gradient-to-br from-white/[0.04] to-transparent backdrop-blur-2xl border border-white/[0.08] p-6 rounded-3xl overflow-hidden hover:border-purple-500/40 transition-all duration-500 min-h-[160px] flex flex-col justify-end shadow-lg cursor-default">
                            <!-- Equalizer Background -->
                            <div class="absolute inset-x-6 bottom-0 flex items-end justify-between gap-1.5 opacity-20 group-hover:opacity-60 transition-opacity duration-700 pointer-events-none h-3/4">
                                <div class="w-full bg-purple-500/40 rounded-t-sm transition-all duration-700 h-[20%] group-hover:h-[40%]"></div>
                                <div class="w-full bg-purple-500/60 rounded-t-sm transition-all duration-700 delay-75 h-[40%] group-hover:h-[65%]"></div>
                                <div class="w-full bg-purple-500/80 rounded-t-sm transition-all duration-700 delay-150 h-[30%] group-hover:h-[50%]"></div>
                                <div class="w-full bg-purple-400 rounded-t-sm transition-all duration-700 delay-200 h-[60%] group-hover:h-[100%] shadow-[0_0_15px_rgba(168,85,247,0.8)]"></div>
                                <div class="w-full bg-purple-500/50 rounded-t-sm transition-all duration-700 delay-300 h-[35%] group-hover:h-[70%]"></div>
                                <div class="w-full bg-purple-500/30 rounded-t-sm transition-all duration-700 delay-100 h-[15%] group-hover:h-[30%]"></div>
                                <div class="w-full bg-purple-500/70 rounded-t-sm transition-all duration-700 delay-200 h-[45%] group-hover:h-[80%]"></div>
                            </div>
                            
                            <div class="relative z-10 flex flex-row lg:flex-col lg:items-start items-end justify-between">
                                <div class="mb-0 lg:mb-2">
                                    <div class="text-[10px] font-black uppercase tracking-[0.25em] text-purple-400 mb-1 drop-shadow-[0_0_5px_rgba(168,85,247,0.5)]">Expertise</div>
                                    <div class="text-5xl md:text-6xl font-black text-white tracking-tighter leading-none mb-1">
                                        <span x-show="shown" x-transition data-count="6" data-suffix="+">0</span>
                                    </div>
                                </div>
                                <div class="text-white/40 text-sm font-semibold tracking-wide bg-darkBase/50 px-3 py-1 rounded-full backdrop-blur-sm border border-white/5">Years Experience</div>
                            </div>
                        </div>

                        <!-- Widget 4: Platforms (Network Nodes) -->
                        <div data-aos="fade-up" data-aos-delay="700"
                            class="md:col-span-12 group relative bg-gradient-to-r from-white/[0.04] via-transparent to-white/[0.02] backdrop-blur-2xl border border-white/[0.08] p-5 rounded-3xl overflow-hidden hover:border-amber-500/40 transition-all duration-500 flex flex-col sm:flex-row items-start sm:items-center justify-between shadow-lg cursor-default">
                            
                            <!-- Info -->
                            <div class="relative z-10 flex items-center gap-5 w-full sm:w-auto mb-6 sm:mb-0">
                                <div class="w-14 h-14 rounded-2xl bg-amber-500/10 border border-amber-500/20 flex flex-shrink-0 items-center justify-center text-amber-400 relative overflow-hidden group-hover:shadow-[0_0_20px_rgba(245,158,11,0.2)] transition-shadow">
                                    <div class="absolute inset-0 bg-amber-400/20 opacity-0 group-hover:opacity-100 group-hover:animate-pulse transition-opacity"></div>
                                    <i class="fas fa-network-wired text-xl relative z-10"></i>
                                </div>
                                <div>
                                    <div class="flex items-baseline gap-3 mb-0.5">
                                        <div class="text-3xl md:text-4xl font-black text-white tracking-tighter leading-none">
                                            <span x-show="shown" x-transition data-count="5" data-suffix="">0</span>
                                        </div>
                                        <div class="text-[10px] font-black uppercase tracking-[0.25em] text-amber-400 drop-shadow-[0_0_5px_rgba(245,158,11,0.5)]">Active Systems</div>
                                    </div>
                                    <div class="text-white/40 text-sm font-semibold tracking-wide">Cross-Platform Integrations</div>
                                </div>
                            </div>
                            
                            <!-- Network Nodes Visual -->
                            <div class="relative z-10 w-full sm:w-1/2 lg:w-[45%] h-12 flex items-center justify-between px-2 opacity-60 group-hover:opacity-100 transition-opacity duration-500">
                                <!-- Connecting Line -->
                                <div class="absolute left-4 right-4 h-[1px] bg-gradient-to-r from-amber-500/0 via-amber-500/50 to-amber-500/0 top-1/2 -translate-y-1/2"></div>
                                <!-- Animated pulsing dot traversing the line -->
                                <div class="absolute h-1.5 w-1.5 rounded-full bg-amber-400 shadow-[0_0_12px_#fbbf24] top-1/2 -translate-y-1/2 animate-traverse pointer-events-none mix-blend-screen"></div>
                                
                                <!-- Nodes -->
                                <div class="w-2.5 h-2.5 rounded-full bg-[#0B0B0F] border-2 border-amber-500 relative z-10 group-hover:scale-150 group-hover:bg-amber-400 transition-all duration-300 shadow-[0_0_10px_rgba(245,158,11,0.3)]"></div>
                                <div class="w-1.5 h-1.5 rounded-full bg-[#0B0B0F] border border-amber-500 relative z-10 group-hover:scale-150 group-hover:bg-amber-400 transition-all duration-300 delay-75 shadow-[0_0_8px_rgba(245,158,11,0.3)]"></div>
                                <div class="w-3 h-3 rounded-full bg-[#0B0B0F] border-2 border-amber-500 relative z-10 group-hover:scale-150 group-hover:shadow-[0_0_15px_#fbbf24] transition-all duration-300 delay-150"></div>
                                <div class="w-1.5 h-1.5 rounded-full bg-[#0B0B0F] border border-amber-500 relative z-10 group-hover:scale-150 group-hover:bg-amber-400 transition-all duration-300 delay-200"></div>
                                <div class="w-4 h-4 rounded-full bg-[#0B0B0F] border-2 border-amber-400 relative z-10 group-hover:scale-125 transition-all duration-300 delay-300 flex items-center justify-center shadow-[0_0_15px_rgba(245,158,11,0.6)]">
                                    <div class="w-1.5 h-1.5 bg-amber-300 rounded-full group-hover:animate-ping"></div>
                                </div>
                            </div>
                        </div>
                        
                    </div>
"""

with codecs.open('index.html', 'r', 'utf-8') as f:
    t = f.read()

start_idx = t.find('<!-- Floating Stats Cloud -->')
end_idx = t.find('<!-- Scroll Down Indicator -->', start_idx)

if start_idx != -1 and end_idx != -1:
    t = t[:start_idx] + new_content + "\n                    " + t[end_idx:]
    with codecs.open('index.html', 'w', 'utf-8') as f:
        f.write(t)
    print("Successfully replaced stats widget.")
else:
    print("Could not find replacement boundaries.")
