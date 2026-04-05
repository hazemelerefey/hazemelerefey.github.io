from pathlib import Path

path = Path(r'D:\hazemelerefy website\index.html')
text = path.read_text(encoding='utf-8')

projects = [
    ('jobpulse', 'https://github.com/hazemelerefey/jobpulse', 'text-cyan-400', 'border-cyan-500/30', 'hover:bg-cyan-500/10'),
    ('frontend-kanban-board', 'https://github.com/hazemelerefey/frontend-kanban-board', 'text-cyan-400', 'border-cyan-500/30', 'hover:bg-cyan-500/10'),
    ('frontend-realestate-finder', 'https://github.com/hazemelerefey/frontend-realestate-finder', 'text-purple-400', 'border-purple-500/30', 'hover:bg-purple-500/10'),
    ('healthcare-operations-waitlist-dashboard', 'https://github.com/hazemelerefey/healthcare-operations-waitlist-dashboard', 'text-emerald-400', 'border-emerald-500/30', 'hover:bg-emerald-500/10'),
    ('global-ecommerce-sales-tracker', 'https://github.com/hazemelerefey/global-ecommerce-sales-tracker', 'text-amber-400', 'border-amber-500/30', 'hover:bg-amber-500/10'),
    ('analytics-churn-prediction', 'https://github.com/hazemelerefey/analytics-churn-prediction', 'text-red-400', 'border-red-500/30', 'hover:bg-red-500/10'),
    ('frontend-ecommerce-dashboard', 'https://github.com/hazemelerefey/frontend-ecommerce-dashboard', 'text-cyan-400', 'border-cyan-500/30', 'hover:bg-cyan-500/10'),
]

# convert opening and closing anchors for portfolio cards only
for slug, url, color, border, hoverbg in projects:
    text = text.replace(f'href="{url}" target="_blank" rel="noopener noreferrer"\n                            class="group', f'class="group', 1)
    text = text.replace('                        </a>', '                        </div>', 1)

# add button block after each rating footer block sequentially
button_templates = [
    ('jobpulse', 'text-cyan-400', 'border-cyan-500/30', 'hover:bg-cyan-500/10'),
    ('kanban', 'text-cyan-400', 'border-cyan-500/30', 'hover:bg-cyan-500/10'),
    ('realestate', 'text-purple-400', 'border-purple-500/30', 'hover:bg-purple-500/10'),
    ('healthcare', 'text-emerald-400', 'border-emerald-500/30', 'hover:bg-emerald-500/10'),
    ('global_sales', 'text-amber-400', 'border-amber-500/30', 'hover:bg-amber-500/10'),
    ('churn', 'text-red-400', 'border-red-500/30', 'hover:bg-red-500/10'),
    ('ecommerce', 'text-cyan-400', 'border-cyan-500/30', 'hover:bg-cyan-500/10'),
]
urls = {
    'jobpulse': 'https://github.com/hazemelerefey/jobpulse',
    'kanban': 'https://github.com/hazemelerefey/frontend-kanban-board',
    'realestate': 'https://github.com/hazemelerefey/frontend-realestate-finder',
    'healthcare': 'https://github.com/hazemelerefey/healthcare-operations-waitlist-dashboard',
    'global_sales': 'https://github.com/hazemelerefey/global-ecommerce-sales-tracker',
    'churn': 'https://github.com/hazemelerefey/analytics-churn-prediction',
    'ecommerce': 'https://github.com/hazemelerefey/frontend-ecommerce-dashboard',
}

for key, color, border, hoverbg in button_templates:
    target = '''                                </div>
                            </div>'''
    replacement = f'''                                </div>

                                <div class="mt-4 pt-4 border-t border-cardBorder/40">
                                    <a href="{urls[key]}" target="_blank" rel="noopener noreferrer"
                                        class="inline-flex items-center gap-2 px-4 py-2 rounded-xl border {border} {color} bg-white/0 {hoverbg} transition-all duration-300 text-sm font-semibold">
                                        <i class="fab fa-github"></i>
                                        <span>View GitHub</span>
                                        <i class="fas fa-arrow-up-right-from-square text-xs"></i>
                                    </a>
                                </div>
                            </div>'''
    text = text.replace(target, replacement, 1)

path.write_text(text, encoding='utf-8')
print('portfolio github button fix applied')
