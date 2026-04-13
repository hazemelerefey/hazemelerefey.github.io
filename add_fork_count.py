import codecs
with codecs.open('index.html', 'r', 'utf-8') as f:
    text = f.read()

old = 'fas fa-star text-[8px] text-yellow-500/60"></i> 0</span>'
new = 'fas fa-star text-[8px] text-yellow-500/60"></i> 0</span><span class="flex items-center gap-1.5 text-xs text-white/30"><i class="fas fa-code-branch text-[8px] text-white/30"></i> 0</span>'

count = text.count(old)
text = text.replace(old, new)
with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(text)
print(f'Replaced {count} instances')
