import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    t = f.read()

# 1. Remove the outer @click handler from the portfolio cards
t = t.replace(
    " hover:outline-red-500/30': project.color === 'red'\n                                }\"\n                                @click=\"openStory(project)\">",
    " hover:outline-red-500/30': project.color === 'red'\n                                }\">"
)

# 2. Add type="button" to the trigger
t = t.replace(
    '<button @click.stop="openStory(project)" class="w-full relative overflow-hidden group/btn rounded-2xl bg-white/[0.03] border border-white/10 hover:border-white/30 backdrop-blur-xl transition-all duration-500 p-4 flex items-center justify-between shadow-[0_10px_30px_rgba(0,0,0,0.5)]">',
    '<button type="button" @click.stop="openStory(project)" class="w-full relative cursor-pointer overflow-hidden group/btn rounded-2xl bg-white/[0.03] border border-white/10 hover:border-white/30 backdrop-blur-xl transition-all duration-500 p-4 flex items-center justify-between shadow-[0_10px_30px_rgba(0,0,0,0.5)] pointer-events-auto">'
)

# 3. Elevate z-index and add pointer-events-auto to the modal wrapper
t = t.replace(
    'class="fixed inset-0 z-[200] flex items-center justify-center p-0 md:p-6"',
    'class="fixed inset-0 z-[999] flex items-center justify-center p-0 md:p-6 pointer-events-auto"'
)

# 4. Add type="button" to the modal close button
t = t.replace(
    '<button @click="closeStory()" \n                class="absolute top-6 right-6 z-50 w-12 h-12 rounded-full bg-black/40 border border-white/20 backdrop-blur-xl flex items-center justify-center text-white/70 hover:text-white hover:bg-white/10 hover:scale-105 transition-all duration-300">',
    '<button type="button" @click="closeStory()" \n                class="absolute top-6 right-6 z-50 w-12 h-12 rounded-full bg-black/40 border border-white/20 backdrop-blur-xl flex items-center justify-center text-white/70 hover:text-white hover:bg-white/10 hover:scale-105 transition-all duration-300 cursor-pointer pointer-events-auto">'
)

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(t)
    print('index.html safely updated with popup bugfixes.')
