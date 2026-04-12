import codecs
import sys

with codecs.open('index.html', 'r', 'utf-8') as f:
    text = f.read()

bento_start = '<!-- ABOUT ME / EXPERIENCE BENTO GRID -->'
bento_end = '<!-- Work Process Section (Moved to end of Portfolio) -->'

start_idx = text.find(bento_start)
end_idx = text.find(bento_end)

if start_idx != -1 and end_idx != -1:
    bento_section = text[start_idx:end_idx]
    text_without_bento = text[:start_idx] + text[end_idx:]
    
    insert_marker = '<section id="expertise-home"'
    insert_idx = text_without_bento.find(insert_marker)
    
    if insert_idx != -1:
        final_text = text_without_bento[:insert_idx] + bento_section + '\n\n            ' + text_without_bento[insert_idx:]
        with codecs.open('index.html', 'w', 'utf-8') as f:
            f.write(final_text)
        print('SUCCESS')
    else:
        print('FAIL: Could not find insert_marker')
else:
    print('FAIL: Could not find start/end')
