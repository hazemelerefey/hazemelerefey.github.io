from pathlib import Path

path = Path(r'D:\hazemelerefy website\index.html')
text = path.read_text(encoding='utf-8')

text = text.replace(
'''                <div class="flex items-center gap-4 text-xs text-textMuted font-medium">
                    <span class="flex items-center gap-1"><i class="fas fa-star text-yellow-500"></i> 0</span>
                    <span class="flex items-center gap-1"><i class="fas fa-code-branch"></i> 0</span>
                </div>''',
'''                <div class="flex items-center justify-between gap-4 text-xs text-textMuted font-medium">
                    <div class="flex items-center gap-4">
                        <span class="flex items-center gap-1"><i class="fas fa-star text-yellow-500"></i> 0</span>
                        <span class="flex items-center gap-1"><i class="fas fa-code-branch"></i> 0</span>
                    </div>
                    <span class="text-[11px] uppercase tracking-[0.18em] text-pink-400/90">Live GitHub Stats</span>
                </div>''', 3)

text = text.replace(
'''                <div class="flex items-center gap-4 text-xs text-textMuted font-medium">
                    <span class="flex items-center gap-1"><i class="fas fa-star text-yellow-500"></i> 0</span>
                    <span class="flex items-center gap-1"><i class="fas fa-code-branch"></i> 0</span>
                </div>''',
'''                <div class="flex items-center justify-between gap-4 text-xs text-textMuted font-medium">
                    <div class="flex items-center gap-4">
                        <span class="flex items-center gap-1"><i class="fas fa-star text-yellow-500"></i> 0</span>
                        <span class="flex items-center gap-1"><i class="fas fa-code-branch"></i> 0</span>
                    </div>
                    <span class="text-[11px] uppercase tracking-[0.18em] text-cyan-400/90">Live GitHub Stats</span>
                </div>''', 3)

text = text.replace('>React</span>', '>React Admin UI</span>', 1)
text = text.replace('>React</span>', '>Workflow UI</span>', 1)
text = text.replace('>ARIMA</span>', '>ARIMA / Python</span>', 1)
text = text.replace('>Power BI</span>', '>Power BI / DAX</span>', 1)

path.write_text(text, encoding='utf-8')
print('workspace enhanced')
