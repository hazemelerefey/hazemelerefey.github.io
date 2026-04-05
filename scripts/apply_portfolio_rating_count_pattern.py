from pathlib import Path

path = Path(r'D:\hazemelerefy website\index.html')
text = path.read_text(encoding='utf-8')

keys = ['kanban', 'realestate', 'healthcare', 'global_sales', 'churn', 'ecommerce']
for key in keys:
    old = f'''                                    <div class="flex items-center gap-1">
                                        <span x-text="ratings.{key}.average"
                                            class="text-white font-bold text-sm mr-2"></span>
                                        <template x-for="star in 5">
                                            <i class="fas fa-star text-xs transition-transform hover:scale-125 cursor-pointer"
                                                :class="(ratings.{key}.hoverScore >= star || (!ratings.{key}.hoverScore && ratings.{key}.score >= star)) ? 'text-amber-400' : 'text-gray-600'"
                                                @mouseenter="hoverStar('{key}', star)"
                                                @mouseleave="resetHover('{key}')"
                                                @click="setRating('{key}', star)"></i>
                                        </template>
                                    </div>'''
    new = f'''                                    <div class="flex items-center gap-2">
                                        <span class="text-white font-bold text-sm" x-text="ratings.{key}.average"></span>
                                        <span class="text-xs text-textMuted" x-text="`(${ {''} }ratings.{key}.totalVotes)`"></span>
                                        <div class="flex items-center gap-1 ml-1">
                                            <template x-for="star in 5">
                                                <i class="fas fa-star text-xs transition-transform hover:scale-125 cursor-pointer"
                                                    :class="(ratings.{key}.hoverScore >= star || (!ratings.{key}.hoverScore && ratings.{key}.score >= star)) ? 'text-amber-400' : 'text-gray-600'"
                                                    @mouseenter="hoverStar('{key}', star)"
                                                    @mouseleave="resetHover('{key}')"
                                                    @click="setRating('{key}', star)"></i>
                                            </template>
                                        </div>
                                    </div>'''.replace("${ {''} }", "${")
    if old not in text:
        raise SystemExit(f'missing block for {key}')
    text = text.replace(old, new, 1)

path.write_text(text, encoding='utf-8')
print('applied rating count pattern to remaining portfolio cards')
