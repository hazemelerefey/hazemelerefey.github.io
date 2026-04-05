import re

with open('d:/hazemelerefy website/my website/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# I see in the screenshot the text "\2 (Moved to end of Portfolio) -->"
# It seems my previous regex replacement used `\2` as a backreference.
# Let's fix this heavily mutated file. We need to find the start of the portfolio section
# and the start of the methodology section, and replace everything in between.

def get_clean_html():
    return """
                    <!-- Portfolio Filter Options -->
                    <div class="flex justify-center mb-12" data-aos="fade-up">
                        <div class="inline-flex bg-darkBase/80 backdrop-blur-sm border border-cardBorder p-1.5 rounded-full shadow-[0_0_20px_rgba(0,0,0,0.5)] flex-wrap justify-center gap-2">
                            <button @click="portfolioFilter = 'all'" 
                                    :class="portfolioFilter === 'all' ? 'bg-cyan-500/20 text-cyan-400 border-cyan-500/30' : 'text-textMuted hover:text-white border-transparent'"
                                    class="px-6 py-2.5 rounded-full text-sm font-bold tracking-wide transition-all duration-300 border flex items-center gap-2">
                                <i class="fas fa-layer-group"></i> All Projects
                            </button>
                            <button @click="portfolioFilter = 'frontend'" 
                                    :class="portfolioFilter === 'frontend' ? 'bg-pink-500/20 text-pink-400 border-pink-500/30' : 'text-textMuted hover:text-white border-transparent'"
                                    class="px-6 py-2.5 rounded-full text-sm font-bold tracking-wide transition-all duration-300 border flex items-center gap-2">
                                <i class="fas fa-code"></i> Frontend
                            </button>
                            <button @click="portfolioFilter = 'analytics'" 
                                    :class="portfolioFilter === 'analytics' ? 'bg-purple-500/20 text-purple-400 border-purple-500/30' : 'text-textMuted hover:text-white border-transparent'"
                                    class="px-6 py-2.5 rounded-full text-sm font-bold tracking-wide transition-all duration-300 border flex items-center gap-2">
                                <i class="fas fa-chart-line"></i> Analytics
                            </button>
                        </div>
                    </div>

                    <!-- 6 Unified Project Cards Grid -->
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-24 relative z-20">

                        <!-- Project 1: E-Commerce Platform (Frontend) -->
                        <div x-show="portfolioFilter === 'all' || portfolioFilter === 'frontend'" 
                             x-transition:enter="transition-all duration-500"
                             x-transition:enter-start="opacity-0 translate-y-8"
                             x-transition:enter-end="opacity-100 translate-y-0"
                             class="group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(236,72,153,0.15)] hover:border-pink-500/50 transition-all duration-500 flex flex-col h-full">
                            
                            <!-- Image Container with Zoom -->
                            <div class="h-56 overflow-hidden relative border-b border-cardBorder cursor-pointer"
                                 @click="zoomedImageSrc = 'images/ecommerce-dashboard.png'; zoomModalOpen = true; document.body.style.overflow = 'hidden';">
                                <img src="images/ecommerce-dashboard.png" alt="E-Commerce Platform" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                                <div class="absolute inset-0 bg-gradient-to-t from-darkBase/90 to-transparent"></div>
                                
                                <div class="absolute top-4 left-4 flex gap-2">
                                    <span class="bg-pink-500/20 text-pink-400 border border-pink-500/30 text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm">UI/UX</span>
                                    <span class="bg-darkBase/60 text-white border border-cardBorder text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm">Next.js</span>
                                </div>
                                
                                <div class="absolute inset-0 bg-pink-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                                    <i class="fas fa-search-plus text-3xl text-white drop-shadow-lg"></i>
                                </div>
                            </div>
                            
                            <!-- Card Content -->
                            <div class="p-6 flex-1 flex flex-col">
                                <h3 class="text-xl font-bold text-white mb-2 group-hover:text-pink-400 transition-colors">Enterprise E-Commerce</h3>
                                <p class="text-textMuted text-sm mb-6 flex-1 line-clamp-3">A high-performance modern storefront built with React, Next.js, and TailwindCSS. Features complex cart state, responsive product grids, and sleek glassmorphism UI components.</p>
                                
                                <!-- Rating footer -->
                                <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0">
                                    <div class="flex items-center gap-1">
                                        <span x-text="ratings.ecommerce.average" class="text-white font-bold text-sm mr-2"></span>
                                        <template x-for="star in 5">
                                            <i class="fas fa-star text-xs transition-transform hover:scale-125 cursor-pointer"
                                                :class="(ratings.ecommerce.hoverScore >= star || (!ratings.ecommerce.hoverScore && ratings.ecommerce.score >= star)) ? 'text-amber-400' : 'text-gray-600'"
                                                @mouseenter="hoverStar('ecommerce', star)" @mouseleave="resetHover('ecommerce')" @click="setRating('ecommerce', star)"></i>
                                        </template>
                                    </div>
                                    <button class="text-pink-400 hover:text-white text-sm font-bold flex items-center gap-1 transition-colors group/btn">
                                        Details <i class="fas fa-arrow-right group-hover/btn:translate-x-1 transition-transform"></i>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <!-- Project 2: SaaS Task Management (Frontend) -->
                        <div x-show="portfolioFilter === 'all' || portfolioFilter === 'frontend'" 
                             x-transition:enter="transition-all duration-500"
                             x-transition:enter-start="opacity-0 translate-y-8"
                             x-transition:enter-end="opacity-100 translate-y-0"
                             class="group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(6,182,212,0.15)] hover:border-cyan-500/50 transition-all duration-500 flex flex-col h-full">
                            
                            <div class="h-56 overflow-hidden relative border-b border-cardBorder cursor-pointer"
                                 @click="zoomedImageSrc = 'images/saas-dashboard.png'; zoomModalOpen = true; document.body.style.overflow = 'hidden';">
                                <img src="images/saas-dashboard.png" alt="SaaS Task Management" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                                <div class="absolute inset-0 bg-gradient-to-t from-darkBase/90 to-transparent"></div>
                                
                                <div class="absolute top-4 left-4 flex gap-2">
                                    <span class="bg-cyan-500/20 text-cyan-400 border border-cyan-500/30 text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm">SaaS</span>
                                    <span class="bg-darkBase/60 text-white border border-cardBorder text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm">React</span>
                                </div>
                                
                                <div class="absolute inset-0 bg-cyan-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                                    <i class="fas fa-search-plus text-3xl text-white drop-shadow-lg"></i>
                                </div>
                            </div>
                            
                            <div class="p-6 flex-1 flex flex-col">
                                <h3 class="text-xl font-bold text-white mb-2 group-hover:text-cyan-400 transition-colors">SaaS Task Management</h3>
                                <p class="text-textMuted text-sm mb-6 flex-1 line-clamp-3">A premium productivity dashboard featuring deep state management for complex Kanban boards, progress analytics, and team collaboration views with glowing neon accents.</p>
                                
                                <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0">
                                    <div class="flex items-center gap-1">
                                        <span x-text="ratings.saas.average" class="text-white font-bold text-sm mr-2"></span>
                                        <template x-for="star in 5">
                                            <i class="fas fa-star text-xs transition-transform hover:scale-125 cursor-pointer"
                                                :class="(ratings.saas.hoverScore >= star || (!ratings.saas.hoverScore && ratings.saas.score >= star)) ? 'text-amber-400' : 'text-gray-600'"
                                                @mouseenter="hoverStar('saas', star)" @mouseleave="resetHover('saas')" @click="setRating('saas', star)"></i>
                                        </template>
                                    </div>
                                    <button class="text-cyan-400 hover:text-white text-sm font-bold flex items-center gap-1 transition-colors group/btn">
                                        Details <i class="fas fa-arrow-right group-hover/btn:translate-x-1 transition-transform"></i>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <!-- Project 3: Real Estate Booking (Frontend) -->
                        <div x-show="portfolioFilter === 'all' || portfolioFilter === 'frontend'" 
                             x-transition:enter="transition-all duration-500"
                             x-transition:enter-start="opacity-0 translate-y-8"
                             x-transition:enter-end="opacity-100 translate-y-0"
                             class="group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(168,85,247,0.15)] hover:border-purple-500/50 transition-all duration-500 flex flex-col h-full">
                            
                            <div class="h-56 overflow-hidden relative border-b border-cardBorder cursor-pointer"
                                 @click="zoomedImageSrc = 'images/real-estate.png'; zoomModalOpen = true; document.body.style.overflow = 'hidden';">
                                <img src="images/real-estate.png" alt="Real Estate Booking" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                                <div class="absolute inset-0 bg-gradient-to-t from-darkBase/90 to-transparent"></div>
                                
                                <div class="absolute top-4 left-4 flex gap-2">
                                    <span class="bg-purple-500/20 text-purple-400 border border-purple-500/30 text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm">Web App</span>
                                    <span class="bg-darkBase/60 text-white border border-cardBorder text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm">Vue.js</span>
                                </div>
                                
                                <div class="absolute inset-0 bg-purple-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                                    <i class="fas fa-search-plus text-3xl text-white drop-shadow-lg"></i>
                                </div>
                            </div>
                            
                            <div class="p-6 flex-1 flex flex-col">
                                <h3 class="text-xl font-bold text-white mb-2 group-hover:text-purple-400 transition-colors">Real Estate Booking</h3>
                                <p class="text-textMuted text-sm mb-6 flex-1 line-clamp-3">A highly interactive property booking system showcasing complex API integrations for dynamic search filters, map-based layouts, and real-time pricing calculations.</p>
                                
                                <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0">
                                    <div class="flex items-center gap-1">
                                        <span x-text="ratings.real_estate.average" class="text-white font-bold text-sm mr-2"></span>
                                        <template x-for="star in 5">
                                            <i class="fas fa-star text-xs transition-transform hover:scale-125 cursor-pointer"
                                                :class="(ratings.real_estate.hoverScore >= star || (!ratings.real_estate.hoverScore && ratings.real_estate.score >= star)) ? 'text-amber-400' : 'text-gray-600'"
                                                @mouseenter="hoverStar('real_estate', star)" @mouseleave="resetHover('real_estate')" @click="setRating('real_estate', star)"></i>
                                        </template>
                                    </div>
                                    <button class="text-purple-400 hover:text-white text-sm font-bold flex items-center gap-1 transition-colors group/btn">
                                        Details <i class="fas fa-arrow-right group-hover/btn:translate-x-1 transition-transform"></i>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <!-- Project 4: Healthcare Analytics (Analytics) -->
                        <div x-show="portfolioFilter === 'all' || portfolioFilter === 'analytics'" 
                             x-transition:enter="transition-all duration-500"
                             x-transition:enter-start="opacity-0 translate-y-8"
                             x-transition:enter-end="opacity-100 translate-y-0"
                             class="group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(16,185,129,0.15)] hover:border-emerald-500/50 transition-all duration-500 flex flex-col h-full">
                            
                            <div class="h-56 overflow-hidden relative border-b border-cardBorder cursor-pointer"
                                 @click="zoomedImageSrc = 'images/healthcare-dashboard.png'; zoomModalOpen = true; document.body.style.overflow = 'hidden';">
                                <img src="images/healthcare-dashboard.png" alt="Healthcare Analytics" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                                <div class="absolute inset-0 bg-gradient-to-t from-darkBase/90 to-transparent"></div>
                                
                                <div class="absolute top-4 left-4 flex gap-2">
                                    <span class="bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm">BI Dashboard</span>
                                    <span class="bg-darkBase/60 text-white border border-cardBorder text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm">Power BI</span>
                                </div>
                                
                                <div class="absolute inset-0 bg-emerald-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                                    <i class="fas fa-search-plus text-3xl text-white drop-shadow-lg"></i>
                                </div>
                            </div>
                            
                            <div class="p-6 flex-1 flex flex-col">
                                <h3 class="text-xl font-bold text-white mb-2 group-hover:text-emerald-400 transition-colors">Healthcare Analytics</h3>
                                <p class="text-textMuted text-sm mb-6 flex-1 line-clamp-3">A comprehensive dashboard tracking patient flow, operational efficiency, and waitlist trends. Covers full data lifecycle: extraction, Star Schema modeling, and advanced DAX.</p>
                                
                                <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0">
                                    <div class="flex items-center gap-1">
                                        <span x-text="ratings.healthcare.average" class="text-white font-bold text-sm mr-2"></span>
                                        <template x-for="star in 5">
                                            <i class="fas fa-star text-xs transition-transform hover:scale-125 cursor-pointer"
                                                :class="(ratings.healthcare.hoverScore >= star || (!ratings.healthcare.hoverScore && ratings.healthcare.score >= star)) ? 'text-amber-400' : 'text-gray-600'"
                                                @mouseenter="hoverStar('healthcare', star)" @mouseleave="resetHover('healthcare')" @click="setRating('healthcare', star)"></i>
                                        </template>
                                    </div>
                                    <button @click="openDashboard('healthcare')" class="text-emerald-400 hover:text-white text-sm font-bold flex items-center gap-1 transition-colors group/btn">
                                        Open App <i class="fas fa-arrow-right group-hover/btn:translate-x-1 transition-transform"></i>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <!-- Project 5: Global Sales Performance (Analytics) -->
                        <div x-show="portfolioFilter === 'all' || portfolioFilter === 'analytics'" 
                             x-transition:enter="transition-all duration-500"
                             x-transition:enter-start="opacity-0 translate-y-8"
                             x-transition:enter-end="opacity-100 translate-y-0"
                             class="group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(245,158,11,0.15)] hover:border-amber-500/50 transition-all duration-500 flex flex-col h-full">
                            
                            <div class="h-56 overflow-hidden relative border-b border-cardBorder cursor-pointer"
                                 @click="zoomedImageSrc = 'images/global-sales-dashboard.png'; zoomModalOpen = true; document.body.style.overflow = 'hidden';">
                                <img src="images/global-sales-dashboard.png" alt="Global Sales Dashboard" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                                <div class="absolute inset-0 bg-gradient-to-t from-darkBase/90 to-transparent"></div>
                                
                                <div class="absolute top-4 left-4 flex gap-2">
                                    <span class="bg-amber-500/20 text-amber-400 border border-amber-500/30 text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm">Executive</span>
                                    <span class="bg-darkBase/60 text-white border border-cardBorder text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm">SQL & DAX</span>
                                </div>
                                
                                <div class="absolute inset-0 bg-amber-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                                    <i class="fas fa-search-plus text-3xl text-white drop-shadow-lg"></i>
                                </div>
                            </div>
                            
                            <div class="p-6 flex-1 flex flex-col">
                                <h3 class="text-xl font-bold text-white mb-2 group-hover:text-amber-400 transition-colors">Global Sales Oversight</h3>
                                <p class="text-textMuted text-sm mb-6 flex-1 line-clamp-3">An executive-level tool overseeing global market performance. Built through rigorous data integration and geographic normalization to enable instant spatial drill-downs without lag.</p>
                                
                                <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0">
                                    <div class="flex items-center gap-1">
                                        <span x-text="ratings.global_sales.average" class="text-white font-bold text-sm mr-2"></span>
                                        <template x-for="star in 5">
                                            <i class="fas fa-star text-xs transition-transform hover:scale-125 cursor-pointer"
                                                :class="(ratings.global_sales.hoverScore >= star || (!ratings.global_sales.hoverScore && ratings.global_sales.score >= star)) ? 'text-amber-400' : 'text-gray-600'"
                                                @mouseenter="hoverStar('global_sales', star)" @mouseleave="resetHover('global_sales')" @click="setRating('global_sales', star)"></i>
                                        </template>
                                    </div>
                                    <button @click="openDashboard('global_sales')" class="text-amber-400 hover:text-white text-sm font-bold flex items-center gap-1 transition-colors group/btn">
                                        Open App <i class="fas fa-arrow-right group-hover/btn:translate-x-1 transition-transform"></i>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <!-- Project 6: Predictive Customer Churn (Analytics) -->
                        <div x-show="portfolioFilter === 'all' || portfolioFilter === 'analytics'" 
                             x-transition:enter="transition-all duration-500"
                             x-transition:enter-start="opacity-0 translate-y-8"
                             x-transition:enter-end="opacity-100 translate-y-0"
                             class="group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(239,68,68,0.15)] hover:border-red-500/50 transition-all duration-500 flex flex-col h-full">
                            
                            <div class="h-56 overflow-hidden relative border-b border-cardBorder cursor-pointer"
                                 @click="zoomedImageSrc = 'images/customer-churn.png'; zoomModalOpen = true; document.body.style.overflow = 'hidden';">
                                <img src="images/customer-churn.png" alt="Predictive ML Model" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                                <div class="absolute inset-0 bg-gradient-to-t from-darkBase/90 to-transparent"></div>
                                
                                <div class="absolute top-4 left-4 flex gap-2">
                                    <span class="bg-red-500/20 text-red-400 border border-red-500/30 text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm">Machine Learning</span>
                                    <span class="bg-darkBase/60 text-white border border-cardBorder text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm">Python</span>
                                </div>
                                
                                <div class="absolute inset-0 bg-red-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                                    <i class="fas fa-search-plus text-3xl text-white drop-shadow-lg"></i>
                                </div>
                            </div>
                            
                            <div class="p-6 flex-1 flex flex-col">
                                <h3 class="text-xl font-bold text-white mb-2 group-hover:text-red-400 transition-colors">Predictive Churn Model</h3>
                                <p class="text-textMuted text-sm mb-6 flex-1 line-clamp-3">A sci-kit learn predictive classification model that identifies at-risk telecom customers. Visualized via interactive SHAP value charts identifying key predictive factors.</p>
                                
                                <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0">
                                    <div class="flex items-center gap-1">
                                        <span x-text="ratings.churn.average" class="text-white font-bold text-sm mr-2"></span>
                                        <template x-for="star in 5">
                                            <i class="fas fa-star text-xs transition-transform hover:scale-125 cursor-pointer"
                                                :class="(ratings.churn.hoverScore >= star || (!ratings.churn.hoverScore && ratings.churn.score >= star)) ? 'text-amber-400' : 'text-gray-600'"
                                                @mouseenter="hoverStar('churn', star)" @mouseleave="resetHover('churn')" @click="setRating('churn', star)"></i>
                                        </template>
                                    </div>
                                    <button class="text-red-400 hover:text-white text-sm font-bold flex items-center gap-1 transition-colors group/btn">
                                        Details <i class="fas fa-arrow-right group-hover/btn:translate-x-1 transition-transform"></i>
                                    </button>
                                </div>
                            </div>
                        </div>

                    </div> <!-- END PORTFOLIO GRID -->

                    """

# Find Start
pattern_start = re.compile(r'<!-- Portfolio Filter Options -->[\s\S]*?(?=<!-- Portfolio Filter Options -->)')

# Oh I see. We already replaced the text, so the start and end are gone.
# Let's find the current block.
# We look for "<!-- Portfolio Filter Options -->"
# Up to "\2 (Moved to end of Portfolio) -->"

match_start = text.find('<!-- Portfolio Filter Options -->')
match_end = text.find(r'\2 (Moved to end of Portfolio) -->')

if match_start != -1 and match_end != -1:
    print(f"Found broken block at {match_start} to {match_end}")
    
    # We replace from match_start to match_end + len(\2...) with our clean HTML
    end_index = match_end + len(r'\2 (Moved to end of Portfolio) -->')
    
    new_text = text[:match_start] + get_clean_html() + "\n                <!-- Work Process Section (Moved to end of Portfolio) -->" + text[end_index:]
    
    with open('d:/hazemelerefy website/my website/index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    
    print("Fixed broken HTML block.")
else:
    print("Could not find the broken block.")

