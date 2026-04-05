from pathlib import Path

path = Path(r'D:\hazemelerefy website\index.html')
text = path.read_text(encoding='utf-8')

old_open = '''                        <a x-show="portfolioFilter === 'all' || portfolioFilter === 'frontend'"
                            x-transition:enter="transition-all duration-500"
                            x-transition:enter-start="opacity-0 translate-y-8"
                            x-transition:enter-end="opacity-100 translate-y-0"
                            href="https://github.com/hazemelerefey/jobpulse" target="_blank" rel="noopener noreferrer"
                            class="group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(34,211,238,0.18)] hover:border-cyan-500/50 transition-all duration-500 flex flex-col h-full">'''

new_open = '''                        <div x-show="portfolioFilter === 'all' || portfolioFilter === 'frontend'"
                            x-transition:enter="transition-all duration-500"
                            x-transition:enter-start="opacity-0 translate-y-8"
                            x-transition:enter-end="opacity-100 translate-y-0"
                            class="group bg-cardBase border border-cardBorder rounded-3xl overflow-hidden shadow-xl hover:shadow-[0_0_30px_rgba(34,211,238,0.18)] hover:border-cyan-500/50 transition-all duration-500 flex flex-col h-full">'''

old_footer = '''                                <div
                                    class="flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0">
                                    <div class="flex items-center gap-1">
                                        <span x-text="ratings.jobpulse.average"
                                            class="text-white font-bold text-sm mr-2"></span>
                                        <template x-for="star in 5">
                                            <i class="fas fa-star text-xs transition-transform hover:scale-125 cursor-pointer"
                                                :class="(ratings.jobpulse.hoverScore >= star || (!ratings.jobpulse.hoverScore && ratings.jobpulse.score >= star)) ? 'text-amber-400' : 'text-gray-600'"
                                                @mouseenter="hoverStar('jobpulse', star)"
                                                @mouseleave="resetHover('jobpulse')"
                                                @click="setRating('jobpulse', star)"></i>
                                        </template>
                                    </div>
                                </div>
                            </div>
                        </a>'''

new_footer = '''                                <div
                                    class="flex flex-col sm:flex-row items-start sm:items-center justify-between pt-4 border-t border-cardBorder/50 mt-auto gap-4 sm:gap-0">
                                    <div class="flex items-center gap-1">
                                        <span x-text="ratings.jobpulse.average"
                                            class="text-white font-bold text-sm mr-2"></span>
                                        <template x-for="star in 5">
                                            <i class="fas fa-star text-xs transition-transform hover:scale-125 cursor-pointer"
                                                :class="(ratings.jobpulse.hoverScore >= star || (!ratings.jobpulse.hoverScore && ratings.jobpulse.score >= star)) ? 'text-amber-400' : 'text-gray-600'"
                                                @mouseenter="hoverStar('jobpulse', star)"
                                                @mouseleave="resetHover('jobpulse')"
                                                @click="setRating('jobpulse', star)"></i>
                                        </template>
                                    </div>

                                    <a href="https://github.com/hazemelerefey/jobpulse" target="_blank" rel="noopener noreferrer"
                                        class="inline-flex items-center gap-2 px-4 py-2 rounded-xl border border-cyan-500/25 text-cyan-400 hover:text-white hover:bg-cyan-500/10 transition-all duration-300 text-sm font-semibold">
                                        <i class="fab fa-github"></i>
                                        <span>GitHub</span>
                                    </a>
                                </div>
                            </div>
                        </div>'''

if old_open not in text:
    raise SystemExit('JobPulse open block not found')
if old_footer not in text:
    raise SystemExit('JobPulse footer block not found')

text = text.replace(old_open, new_open, 1)
text = text.replace(old_footer, new_footer, 1)
path.write_text(text, encoding='utf-8')
print('jobpulse safe fix applied')
