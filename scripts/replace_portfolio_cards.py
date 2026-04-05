from pathlib import Path

path = Path(r'D:\hazemelerefy website\index.html')
text = path.read_text(encoding='utf-8')

repls = []
repls.append(("""                        <!-- Project 2: SaaS Task Management (Frontend) -->
                        <div x-show=\"portfolioFilter === 'all' || portfolioFilter === 'frontend'\"
                            x-transition:enter=\"transition-all duration-500\"
                            x-transition:enter-start=\"opacity-0 translate-y-8\"
                            x-transition:enter-end=\"opacity-100 translate-y-0\"
                            class=\"group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(6,182,212,0.15)] hover:border-cyan-500/50 transition-all duration-500 flex flex-col h-full\">

                            <div class=\"h-56 overflow-hidden relative border-b border-cardBorder cursor-pointer\"
                                @click=\"zoomedImageSrc = 'images/saas-dashboard.png'; zoomModalOpen = true; document.body.style.overflow = 'hidden';\">
                                <img src=\"images/saas-dashboard.png\" alt=\"SaaS Task Management\"
                                    class=\"w-full h-full object-cover group-hover:scale-105 transition-transform duration-700\">
                                <div class=\"absolute inset-0 bg-gradient-to-t from-darkBase/90 to-transparent\"></div>

                                <div class=\"absolute top-4 left-4 flex gap-2\">
                                    <span
                                        class=\"bg-cyan-500/20 text-cyan-400 border border-cyan-500/30 text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">SaaS</span>
                                    <span
                                        class=\"bg-darkBase/60 text-white border border-cardBorder text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">React</span>
                                </div>

                                <div
                                    class=\"absolute inset-0 bg-cyan-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center\">
                                    <i class=\"fas fa-search-plus text-3xl text-white drop-shadow-lg\"></i>
                                </div>
                            </div>

                            <div class=\"p-6 flex-1 flex flex-col\">
                                <h3
                                    class=\"text-xl font-bold text-white mb-2 group-hover:text-cyan-400 transition-colors\">
                                    SaaS Task Management</h3>
                                <p class=\"text-textMuted text-sm mb-6 flex-1 line-clamp-3\">A premium productivity
                                    dashboard featuring deep state management for complex Kanban boards, progress
                                    analytics, and team collaboration views with glowing neon accents.</p>

                                <div
                                    class=\"flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0\">
                                    <div class=\"flex items-center gap-1\">
                                        <span x-text=\"ratings.saas.average\"
                                            class=\"text-white font-bold text-sm mr-2\"></span>
                                        <template x-for=\"star in 5\">
                                            <i class=\"fas fa-star text-xs transition-transform hover:scale-125 cursor-pointer\"
                                                :class=\"(ratings.saas.hoverScore >= star || (!ratings.saas.hoverScore && ratings.saas.score >= star)) ? 'text-amber-400' : 'text-gray-600'\"
                                                @mouseenter=\"hoverStar('saas', star)\" @mouseleave=\"resetHover('saas')\"
                                                @click=\"setRating('saas', star)\"></i>
                                        </template>
                                    </div>
                                    <button
                                        class=\"text-cyan-400 hover:text-white text-sm font-bold flex items-center gap-1 transition-colors group/btn\">
                                        Details <i
                                            class=\"fas fa-arrow-right group-hover/btn:translate-x-1 transition-transform\"></i>
                                    </button>
                                </div>
                            </div>
                        </div>""", """                        <!-- Project 2: Frontend Kanban Board (Frontend) -->
                        <a x-show=\"portfolioFilter === 'all' || portfolioFilter === 'frontend'\"
                            x-transition:enter=\"transition-all duration-500\"
                            x-transition:enter-start=\"opacity-0 translate-y-8\"
                            x-transition:enter-end=\"opacity-100 translate-y-0\"
                            href=\"https://github.com/hazemelerefey/frontend-kanban-board\" target=\"_blank\" rel=\"noopener noreferrer\"
                            class=\"group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(6,182,212,0.15)] hover:border-cyan-500/50 transition-all duration-500 flex flex-col h-full\">

                            <div class=\"h-56 overflow-hidden relative border-b border-cardBorder cursor-pointer\"
                                @click.prevent=\"zoomedImageSrc = 'images/saas-dashboard.png'; zoomModalOpen = true; document.body.style.overflow = 'hidden';\">
                                <img src=\"images/saas-dashboard.png\" alt=\"Frontend Kanban Board\"
                                    class=\"w-full h-full object-cover group-hover:scale-105 transition-transform duration-700\">
                                <div class=\"absolute inset-0 bg-gradient-to-t from-darkBase/90 to-transparent\"></div>

                                <div class=\"absolute top-4 left-4 flex gap-2 flex-wrap\">
                                    <span
                                        class=\"bg-cyan-500/20 text-cyan-400 border border-cyan-500/30 text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">Kanban UI</span>
                                    <span
                                        class=\"bg-darkBase/60 text-white border border-cardBorder text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">Frontend</span>
                                </div>

                                <div
                                    class=\"absolute inset-0 bg-cyan-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center\">
                                    <i class=\"fas fa-search-plus text-3xl text-white drop-shadow-lg\"></i>
                                </div>
                            </div>

                            <div class=\"p-6 flex-1 flex flex-col\">
                                <h3
                                    class=\"text-xl font-bold text-white mb-2 group-hover:text-cyan-400 transition-colors\">
                                    Frontend Kanban Board</h3>
                                <p class=\"text-textMuted text-sm mb-6 flex-1 line-clamp-3\">A real product-style task management interface focused on drag-and-drop workflow, board clarity, and polished admin-style UI composition for productivity use cases.</p>

                                <div
                                    class=\"flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0\">
                                    <div class=\"flex items-center gap-2 text-xs text-textMuted font-medium\">
                                        <span class=\"flex items-center gap-1\"><i class=\"fas fa-columns text-cyan-400\"></i> Workflow UI</span>
                                        <span class=\"flex items-center gap-1\"><i class=\"fab fa-github text-white\"></i> Real repo</span>
                                    </div>
                                    <span
                                        class=\"text-cyan-400 hover:text-white text-sm font-bold flex items-center gap-1 transition-colors group/btn\">
                                        Open Project <i
                                            class=\"fas fa-arrow-right group-hover/btn:translate-x-1 transition-transform\"></i>
                                    </span>
                                </div>
                            </div>
                        </a>"""))
repls.append(("""                        <!-- Project 3: Real Estate Booking (Frontend) -->
                        <div x-show=\"portfolioFilter === 'all' || portfolioFilter === 'frontend'\"
                            x-transition:enter=\"transition-all duration-500\"
                            x-transition:enter-start=\"opacity-0 translate-y-8\"
                            x-transition:enter-end=\"opacity-100 translate-y-0\"
                            class=\"group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(168,85,247,0.15)] hover:border-purple-500/50 transition-all duration-500 flex flex-col h-full\">

                            <div class=\"h-56 overflow-hidden relative border-b border-cardBorder cursor-pointer\"
                                @click=\"zoomedImageSrc = 'images/real-estate.png'; zoomModalOpen = true; document.body.style.overflow = 'hidden';\">
                                <img src=\"images/real-estate.png\" alt=\"Real Estate Booking\"
                                    class=\"w-full h-full object-cover group-hover:scale-105 transition-transform duration-700\">
                                <div class=\"absolute inset-0 bg-gradient-to-t from-darkBase/90 to-transparent\"></div>

                                <div class=\"absolute top-4 left-4 flex gap-2\">
                                    <span
                                        class=\"bg-purple-500/20 text-purple-400 border border-purple-500/30 text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">Web
                                        App</span>
                                    <span
                                        class=\"bg-darkBase/60 text-white border border-cardBorder text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">Vue.js</span>
                                </div>

                                <div
                                    class=\"absolute inset-0 bg-purple-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center\">
                                    <i class=\"fas fa-search-plus text-3xl text-white drop-shadow-lg\"></i>
                                </div>
                            </div>

                            <div class=\"p-6 flex-1 flex flex-col\">
                                <h3
                                    class=\"text-xl font-bold text-white mb-2 group-hover:text-purple-400 transition-colors\">
                                    Real Estate Booking</h3>
                                <p class=\"text-textMuted text-sm mb-6 flex-1 line-clamp-3\">A highly interactive property
                                    booking system showcasing complex API integrations for dynamic search filters,
                                    map-based layouts, and real-time pricing calculations.</p>

                                <div
                                    class=\"flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0\">
                                    <div class=\"flex items-center gap-1\">
                                        <span x-text=\"ratings.real_estate.average\"
                                            class=\"text-white font-bold text-sm mr-2\"></span>
                                        <template x-for=\"star in 5\">
                                            <i class=\"fas fa-star text-xs transition-transform hover:scale-125 cursor-pointer\"
                                                :class=\"(ratings.real_estate.hoverScore >= star || (!ratings.real_estate.hoverScore && ratings.real_estate.score >= star)) ? 'text-amber-400' : 'text-gray-600'\"
                                                @mouseenter=\"hoverStar('real_estate', star)\"
                                                @mouseleave=\"resetHover('real_estate')\"
                                                @click=\"setRating('real_estate', star)\"></i>
                                        </template>
                                    </div>
                                    <button
                                        class=\"text-purple-400 hover:text-white text-sm font-bold flex items-center gap-1 transition-colors group/btn\">
                                        Details <i
                                            class=\"fas fa-arrow-right group-hover/btn:translate-x-1 transition-transform\"></i>
                                    </button>
                                </div>
                            </div>
                        </div>""", """                        <!-- Project 3: Frontend Real Estate Finder (Frontend) -->
                        <a x-show=\"portfolioFilter === 'all' || portfolioFilter === 'frontend'\"
                            x-transition:enter=\"transition-all duration-500\"
                            x-transition:enter-start=\"opacity-0 translate-y-8\"
                            x-transition:enter-end=\"opacity-100 translate-y-0\"
                            href=\"https://github.com/hazemelerefey/frontend-realestate-finder\" target=\"_blank\" rel=\"noopener noreferrer\"
                            class=\"group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(168,85,247,0.15)] hover:border-purple-500/50 transition-all duration-500 flex flex-col h-full\">

                            <div class=\"h-56 overflow-hidden relative border-b border-cardBorder cursor-pointer\"
                                @click.prevent=\"zoomedImageSrc = 'images/real-estate.png'; zoomModalOpen = true; document.body.style.overflow = 'hidden';\">
                                <img src=\"images/real-estate.png\" alt=\"Frontend Real Estate Finder\"
                                    class=\"w-full h-full object-cover group-hover:scale-105 transition-transform duration-700\">
                                <div class=\"absolute inset-0 bg-gradient-to-t from-darkBase/90 to-transparent\"></div>

                                <div class=\"absolute top-4 left-4 flex gap-2 flex-wrap\">
                                    <span
                                        class=\"bg-purple-500/20 text-purple-400 border border-purple-500/30 text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">Real Estate UI</span>
                                    <span
                                        class=\"bg-darkBase/60 text-white border border-cardBorder text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">Frontend</span>
                                </div>

                                <div
                                    class=\"absolute inset-0 bg-purple-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center\">
                                    <i class=\"fas fa-search-plus text-3xl text-white drop-shadow-lg\"></i>
                                </div>
                            </div>

                            <div class=\"p-6 flex-1 flex flex-col\">
                                <h3
                                    class=\"text-xl font-bold text-white mb-2 group-hover:text-purple-400 transition-colors\">
                                    Frontend Real Estate Finder</h3>
                                <p class=\"text-textMuted text-sm mb-6 flex-1 line-clamp-3\">A real estate search interface built around advanced filtering, listing discovery, and product-style browsing patterns for property exploration and comparison.</p>

                                <div
                                    class=\"flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0\">
                                    <div class=\"flex items-center gap-2 text-xs text-textMuted font-medium\">
                                        <span class=\"flex items-center gap-1\"><i class=\"fas fa-house text-purple-400\"></i> Search UX</span>
                                        <span class=\"flex items-center gap-1\"><i class=\"fab fa-github text-white\"></i> Real repo</span>
                                    </div>
                                    <span
                                        class=\"text-purple-400 hover:text-white text-sm font-bold flex items-center gap-1 transition-colors group/btn\">
                                        Open Project <i
                                            class=\"fas fa-arrow-right group-hover/btn:translate-x-1 transition-transform\"></i>
                                    </span>
                                </div>
                            </div>
                        </a>"""))
repls.append(("""                        <!-- Project 5: Global Sales Performance (Analytics) -->
                        <div x-show=\"portfolioFilter === 'all' || portfolioFilter === 'analytics'\"
                            x-transition:enter=\"transition-all duration-500\"
                            x-transition:enter-start=\"opacity-0 translate-y-8\"
                            x-transition:enter-end=\"opacity-100 translate-y-0\"
                            class=\"group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(245,158,11,0.15)] hover:border-amber-500/50 transition-all duration-500 flex flex-col h-full\">

                            <div class=\"h-56 overflow-hidden relative border-b border-cardBorder cursor-pointer\"
                                @click=\"zoomedImageSrc = 'images/global-sales-dashboard.png'; zoomModalOpen = true; document.body.style.overflow = 'hidden';\">
                                <img src=\"images/global-sales-dashboard.png\" alt=\"Global Sales Dashboard\"
                                    class=\"w-full h-full object-cover group-hover:scale-105 transition-transform duration-700\">
                                <div class=\"absolute inset-0 bg-gradient-to-t from-darkBase/90 to-transparent\"></div>

                                <div class=\"absolute top-4 left-4 flex gap-2\">
                                    <span
                                        class=\"bg-amber-500/20 text-amber-400 border border-amber-500/30 text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">Executive</span>
                                    <span
                                        class=\"bg-darkBase/60 text-white border border-cardBorder text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">SQL
                                        & DAX</span>
                                </div>

                                <div
                                    class=\"absolute inset-0 bg-amber-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center\">
                                    <i class=\"fas fa-search-plus text-3xl text-white drop-shadow-lg\"></i>
                                </div>
                            </div>

                            <div class=\"p-6 flex-1 flex flex-col\">
                                <h3
                                    class=\"text-xl font-bold text-white mb-2 group-hover:text-amber-400 transition-colors\">
                                    Global Sales Oversight</h3>
                                <p class=\"text-textMuted text-sm mb-6 flex-1 line-clamp-3\">An executive-level tool
                                    overseeing global market performance. Built through rigorous data integration and
                                    geographic normalization to enable instant spatial drill-downs without lag.</p>

                                <div
                                    class=\"flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0\">
                                    <div class=\"flex items-center gap-1\">
                                        <span x-text=\"ratings.global_sales.average\"
                                            class=\"text-white font-bold text-sm mr-2\"></span>
                                        <template x-for=\"star in 5\">
                                            <i class=\"fas fa-star text-xs transition-transform hover:scale-125 cursor-pointer\"
                                                :class=\"(ratings.global_sales.hoverScore >= star || (!ratings.global_sales.hoverScore && ratings.global_sales.score >= star)) ? 'text-amber-400' : 'text-gray-600'\"
                                                @mouseenter=\"hoverStar('global_sales', star)\"
                                                @mouseleave=\"resetHover('global_sales')\"
                                                @click=\"setRating('global_sales', star)\"></i>
                                        </template>
                                    </div>
                                    <button @click=\"openDashboard('global_sales')\"
                                        class=\"text-amber-400 hover:text-white text-sm font-bold flex items-center gap-1 transition-colors group/btn\">
                                        Open App <i
                                            class=\"fas fa-arrow-right group-hover/btn:translate-x-1 transition-transform\"></i>
                                    </button>
                                </div>
                            </div>
                        </div>""", """                        <!-- Project 5: Global E-Commerce Sales Tracker (Analytics) -->
                        <a x-show=\"portfolioFilter === 'all' || portfolioFilter === 'analytics'\"
                            x-transition:enter=\"transition-all duration-500\"
                            x-transition:enter-start=\"opacity-0 translate-y-8\"
                            x-transition:enter-end=\"opacity-100 translate-y-0\"
                            href=\"https://github.com/hazemelerefey/global-ecommerce-sales-tracker\" target=\"_blank\" rel=\"noopener noreferrer\"
                            class=\"group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(245,158,11,0.15)] hover:border-amber-500/50 transition-all duration-500 flex flex-col h-full\">

                            <div class=\"h-56 overflow-hidden relative border-b border-cardBorder cursor-pointer\"
                                @click.prevent=\"zoomedImageSrc = 'images/global-sales-dashboard.png'; zoomModalOpen = true; document.body.style.overflow = 'hidden';\">
                                <img src=\"images/global-sales-dashboard.png\" alt=\"Global E-Commerce Sales Tracker\"
                                    class=\"w-full h-full object-cover group-hover:scale-105 transition-transform duration-700\">
                                <div class=\"absolute inset-0 bg-gradient-to-t from-darkBase/90 to-transparent\"></div>

                                <div class=\"absolute top-4 left-4 flex gap-2 flex-wrap\">
                                    <span
                                        class=\"bg-amber-500/20 text-amber-400 border border-amber-500/30 text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">Commercial BI</span>
                                    <span
                                        class=\"bg-darkBase/60 text-white border border-cardBorder text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">Power BI</span>
                                </div>

                                <div
                                    class=\"absolute inset-0 bg-amber-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center\">
                                    <i class=\"fas fa-search-plus text-3xl text-white drop-shadow-lg\"></i>
                                </div>
                            </div>

                            <div class=\"p-6 flex-1 flex flex-col\">
                                <h3
                                    class=\"text-xl font-bold text-white mb-2 group-hover:text-amber-400 transition-colors\">
                                    Global E-Commerce Sales Tracker</h3>
                                <p class=\"text-textMuted text-sm mb-6 flex-1 line-clamp-3\">An interactive business intelligence dashboard for tracking revenue, profit, orders, and regional commercial performance across a multi-country e-commerce dataset.</p>

                                <div
                                    class=\"flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0\">
                                    <div class=\"flex items-center gap-2 text-xs text-textMuted font-medium\">
                                        <span class=\"flex items-center gap-1\"><i class=\"fas fa-chart-line text-amber-400\"></i> KPI reporting</span>
                                        <span class=\"flex items-center gap-1\"><i class=\"fab fa-github text-white\"></i> Real repo</span>
                                    </div>
                                    <span
                                        class=\"text-amber-400 hover:text-white text-sm font-bold flex items-center gap-1 transition-colors group/btn\">
                                        Open Project <i
                                            class=\"fas fa-arrow-right group-hover/btn:translate-x-1 transition-transform\"></i>
                                    </span>
                                </div>
                            </div>
                        </a>"""))
repls.append(("""                        <!-- Project 6: Predictive Customer Churn (Analytics) -->
                        <div x-show=\"portfolioFilter === 'all' || portfolioFilter === 'analytics'\"
                            x-transition:enter=\"transition-all duration-500\"
                            x-transition:enter-start=\"opacity-0 translate-y-8\"
                            x-transition:enter-end=\"opacity-100 translate-y-0\"
                            class=\"group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(239,68,68,0.15)] hover:border-red-500/50 transition-all duration-500 flex flex-col h-full\">

                            <div class=\"h-56 overflow-hidden relative border-b border-cardBorder cursor-pointer\"
                                @click=\"zoomedImageSrc = 'images/customer-churn.png'; zoomModalOpen = true; document.body.style.overflow = 'hidden';\">
                                <img src=\"images/customer-churn.png\" alt=\"Predictive ML Model\"
                                    class=\"w-full h-full object-cover group-hover:scale-105 transition-transform duration-700\">
                                <div class=\"absolute inset-0 bg-gradient-to-t from-darkBase/90 to-transparent\"></div>

                                <div class=\"absolute top-4 left-4 flex gap-2\">
                                    <span
                                        class=\"bg-red-500/20 text-red-400 border border-red-500/30 text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">Machine
                                        Learning</span>
                                    <span
                                        class=\"bg-darkBase/60 text-white border border-cardBorder text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">Python</span>
                                </div>

                                <div
                                    class=\"absolute inset-0 bg-red-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center\">
                                    <i class=\"fas fa-search-plus text-3xl text-white drop-shadow-lg\"></i>
                                </div>
                            </div>

                            <div class=\"p-6 flex-1 flex flex-col\">
                                <h3
                                    class=\"text-xl font-bold text-white mb-2 group-hover:text-red-400 transition-colors\">
                                    Predictive Churn Model</h3>
                                <p class=\"text-textMuted text-sm mb-6 flex-1 line-clamp-3\">A sci-kit learn predictive
                                    classification model that identifies at-risk telecom customers. Visualized via
                                    interactive SHAP value charts identifying key predictive factors.</p>

                                <div
                                    class=\"flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0\">
                                    <div class=\"flex items-center gap-1\">
                                        <span x-text=\"ratings.churn.average\"
                                            class=\"text-white font-bold text-sm mr-2\"></span>
                                        <template x-for=\"star in 5\">
                                            <i class=\"fas fa-star text-xs transition-transform hover:scale-125 cursor-pointer\"
                                                :class=\"(ratings.churn.hoverScore >= star || (!ratings.churn.hoverScore && ratings.churn.score >= star)) ? 'text-amber-400' : 'text-gray-600'\"
                                                @mouseenter=\"hoverStar('churn', star)\" @mouseleave=\"resetHover('churn')\"
                                                @click=\"setRating('churn', star)\"></i>
                                        </template>
                                    </div>
                                    <button
                                        class=\"text-red-400 hover:text-white text-sm font-bold flex items-center gap-1 transition-colors group/btn\">
                                        Details <i
                                            class=\"fas fa-arrow-right group-hover/btn:translate-x-1 transition-transform\"></i>
                                    </button>
                                </div>
                            </div>
                        </div>""", """                        <!-- Project 6: Customer Churn Prediction (Analytics) -->
                        <a x-show=\"portfolioFilter === 'all' || portfolioFilter === 'analytics'\"
                            x-transition:enter=\"transition-all duration-500\"
                            x-transition:enter-start=\"opacity-0 translate-y-8\"
                            x-transition:enter-end=\"opacity-100 translate-y-0\"
                            href=\"https://github.com/hazemelerefey/analytics-churn-prediction\" target=\"_blank\" rel=\"noopener noreferrer\"
                            class=\"group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(239,68,68,0.15)] hover:border-red-500/50 transition-all duration-500 flex flex-col h-full\">

                            <div class=\"h-56 overflow-hidden relative border-b border-cardBorder cursor-pointer\"
                                @click.prevent=\"zoomedImageSrc = 'images/customer-churn.png'; zoomModalOpen = true; document.body.style.overflow = 'hidden';\">
                                <img src=\"images/customer-churn.png\" alt=\"Customer Churn Prediction\"
                                    class=\"w-full h-full object-cover group-hover:scale-105 transition-transform duration-700\">
                                <div class=\"absolute inset-0 bg-gradient-to-t from-darkBase/90 to-transparent\"></div>

                                <div class=\"absolute top-4 left-4 flex gap-2 flex-wrap\">
                                    <span
                                        class=\"bg-red-500/20 text-red-400 border border-red-500/30 text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">Machine Learning</span>
                                    <span
                                        class=\"bg-darkBase/60 text-white border border-cardBorder text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">Python</span>
                                </div>

                                <div
                                    class=\"absolute inset-0 bg-red-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center\">
                                    <i class=\"fas fa-search-plus text-3xl text-white drop-shadow-lg\"></i>
                                </div>
                            </div>

                            <div class=\"p-6 flex-1 flex flex-col\">
                                <h3
                                    class=\"text-xl font-bold text-white mb-2 group-hover:text-red-400 transition-colors\">
                                    Customer Churn Prediction</h3>
                                <p class=\"text-textMuted text-sm mb-6 flex-1 line-clamp-3\">A retention-focused predictive analytics project built to identify churn risk patterns, highlight important features, and support stronger customer retention decisions through machine learning.</p>

                                <div
                                    class=\"flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0\">
                                    <div class=\"flex items-center gap-2 text-xs text-textMuted font-medium\">
                                        <span class=\"flex items-center gap-1\"><i class=\"fas fa-brain text-red-400\"></i> Predictive analytics</span>
                                        <span class=\"flex items-center gap-1\"><i class=\"fab fa-github text-white\"></i> Real repo</span>
                                    </div>
                                    <span
                                        class=\"text-red-400 hover:text-white text-sm font-bold flex items-center gap-1 transition-colors group/btn\">
                                        Open Project <i
                                            class=\"fas fa-arrow-right group-hover/btn:translate-x-1 transition-transform\"></i>
                                    </span>
                                </div>
                            </div>
                        </a>"""))
repls.append(("""                        <!-- Project 7: Personal Portfolio (Frontend) -->
                        <div x-show=\"portfolioFilter === 'all' || portfolioFilter === 'frontend'\"
                            x-transition:enter=\"transition-all duration-500\"
                            x-transition:enter-start=\"opacity-0 translate-y-8\"
                            x-transition:enter-end=\"opacity-100 translate-y-0\"
                            class=\"group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(6,182,212,0.15)] hover:border-cyan-500/50 transition-all duration-500 flex flex-col h-full\">

                            <div class=\"h-56 overflow-hidden relative border-b border-cardBorder cursor-pointer\"
                                @click=\"zoomedImageSrc = 'images/hero_banner.png'; zoomModalOpen = true; document.body.style.overflow = 'hidden';\">
                                <img src=\"images/hero_banner.png\" alt=\"Personal Portfolio & Professional Services\"
                                    class=\"w-full h-full object-cover group-hover:scale-105 transition-transform duration-700\">
                                <div class=\"absolute inset-0 bg-gradient-to-t from-darkBase/90 to-transparent\"></div>

                                <div class=\"absolute top-4 left-4 flex gap-2\">
                                    <span
                                        class=\"bg-cyan-500/20 text-cyan-400 border border-cyan-500/30 text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">UI/UX</span>
                                    <span
                                        class=\"bg-darkBase/60 text-white border border-cardBorder text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">Alpine.js</span>
                                </div>

                                <div
                                    class=\"absolute inset-0 bg-cyan-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center\">
                                    <i class=\"fas fa-search-plus text-3xl text-white drop-shadow-lg\"></i>
                                </div>
                            </div>

                            <div class=\"p-6 flex-1 flex flex-col\">
                                <h3
                                    class=\"text-xl font-bold text-white mb-2 group-hover:text-cyan-400 transition-colors\">
                                    Premium Portfolio Platform</h3>
                                <p class=\"text-textMuted text-sm mb-6 flex-1 line-clamp-3\">Designed and developed a
                                    premium, high-performance portfolio website to showcase data analytics and front-end
                                    capabilities with responsive animations, dynamic UI/UX, and SEO architecture.</p>

                                <div
                                    class=\"flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0\">
                                    <div class=\"flex items-center gap-1\">
                                        <span x-text=\"ratings.portfolio.average\"
                                            class=\"text-white font-bold text-sm mr-2\"></span>
                                        <template x-for=\"star in 5\">
                                            <i class=\"fas fa-star text-xs transition-transform hover:scale-125 cursor-pointer\"
                                                :class=\"(ratings.portfolio.hoverScore >= star || (!ratings.portfolio.hoverScore && ratings.portfolio.score >= star)) ? 'text-amber-400' : 'text-gray-600'\"
                                                @mouseenter=\"hoverStar('portfolio', star)\"
                                                @mouseleave=\"resetHover('portfolio')\"
                                                @click=\"setRating('portfolio', star)\"></i>
                                        </template>
                                    </div>
                                    <button
                                        class=\"text-cyan-400 hover:text-white text-sm font-bold flex items-center gap-1 transition-colors group/btn\">
                                        Details <i
                                            class=\"fas fa-arrow-right group-hover/btn:translate-x-1 transition-transform\"></i>
                                    </button>
                                </div>
                            </div>
                        </div>""", """                        <!-- Project 7: Frontend E-Commerce Dashboard (Frontend) -->
                        <a x-show=\"portfolioFilter === 'all' || portfolioFilter === 'frontend'\"
                            x-transition:enter=\"transition-all duration-500\"
                            x-transition:enter-start=\"opacity-0 translate-y-8\"
                            x-transition:enter-end=\"opacity-100 translate-y-0\"
                            href=\"https://github.com/hazemelerefey/frontend-ecommerce-dashboard\" target=\"_blank\" rel=\"noopener noreferrer\"
                            class=\"group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(6,182,212,0.15)] hover:border-cyan-500/50 transition-all duration-500 flex flex-col h-full\">

                            <div class=\"h-56 overflow-hidden relative border-b border-cardBorder cursor-pointer\"
                                @click.prevent=\"zoomedImageSrc = 'images/ecommerce-dashboard.png'; zoomModalOpen = true; document.body.style.overflow = 'hidden';\">
                                <img src=\"images/ecommerce-dashboard.png\" alt=\"Frontend E-Commerce Dashboard\"
                                    class=\"w-full h-full object-cover group-hover:scale-105 transition-transform duration-700\">
                                <div class=\"absolute inset-0 bg-gradient-to-t from-darkBase/90 to-transparent\"></div>

                                <div class=\"absolute top-4 left-4 flex gap-2 flex-wrap\">
                                    <span
                                        class=\"bg-cyan-500/20 text-cyan-400 border border-cyan-500/30 text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">React Admin UI</span>
                                    <span
                                        class=\"bg-darkBase/60 text-white border border-cardBorder text-[10px] sm:text-xs font-bold px-3 py-1 rounded-full backdrop-blur-sm\">Frontend</span>
                                </div>

                                <div
                                    class=\"absolute inset-0 bg-cyan-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center\">
                                    <i class=\"fas fa-search-plus text-3xl text-white drop-shadow-lg\"></i>
                                </div>
                            </div>

                            <div class=\"p-6 flex-1 flex flex-col\">
                                <h3
                                    class=\"text-xl font-bold text-white mb-2 group-hover:text-cyan-400 transition-colors\">
                                    Frontend E-Commerce Dashboard</h3>
                                <p class=\"text-textMuted text-sm mb-6 flex-1 line-clamp-3\">A modern admin dashboard interface built to monitor sales, orders, and user activity through a clean responsive frontend experience with product-ready layout and chart integration.</p>

                                <div
                                    class=\"flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0\">
                                    <div class=\"flex items-center gap-2 text-xs text-textMuted font-medium\">
                                        <span class=\"flex items-center gap-1\"><i class=\"fas fa-cart-shopping text-cyan-400\"></i> Admin dashboard</span>
                                        <span class=\"flex items-center gap-1\"><i class=\"fab fa-github text-white\"></i> Real repo</span>
                                    </div>
                                    <span
                                        class=\"text-cyan-400 hover:text-white text-sm font-bold flex items-center gap-1 transition-colors group/btn\">
                                        Open Project <i
                                            class=\"fas fa-arrow-right group-hover/btn:translate-x-1 transition-transform\"></i>
                                    </span>
                                </div>
                            </div>
                        </a>"""))

for old, new in repls:
    if old not in text:
        raise SystemExit('Target block not found for replacement')
    text = text.replace(old, new, 1)

path.write_text(text, encoding='utf-8')
print('ok')
