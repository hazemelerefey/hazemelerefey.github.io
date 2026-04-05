from pathlib import Path

out_dir = Path(r'D:\hazemelerefy website\images')
out_dir.mkdir(parents=True, exist_ok=True)

files = {}

files['kanban-project.svg'] = '''<svg width="1200" height="720" viewBox="0 0 1200 720" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="1200" height="720" rx="36" fill="#0B1020"/>
<rect x="0" y="0" width="1200" height="720" rx="36" fill="url(#g1)"/>
<defs>
  <linearGradient id="g1" x1="90" y1="80" x2="1110" y2="660" gradientUnits="userSpaceOnUse">
    <stop stop-color="#0F172A"/>
    <stop offset="1" stop-color="#111827"/>
  </linearGradient>
</defs>
<text x="64" y="96" fill="#22D3EE" font-family="Arial" font-size="22" font-weight="700">KANBAN WORKFLOW</text>
<text x="64" y="154" fill="#F8FAFC" font-family="Arial" font-size="52" font-weight="700">Frontend Kanban Board</text>
<text x="64" y="198" fill="#94A3B8" font-family="Arial" font-size="24">Drag-and-drop task movement with clear lane structure</text>
<rect x="62" y="250" width="300" height="360" rx="28" fill="#111827" stroke="#334155"/>
<rect x="382" y="250" width="300" height="360" rx="28" fill="#0F172A" stroke="#22D3EE" stroke-opacity="0.35"/>
<rect x="702" y="250" width="300" height="360" rx="28" fill="#111827" stroke="#334155"/>
<text x="92" y="294" fill="#CBD5E1" font-family="Arial" font-size="24" font-weight="700">Backlog</text>
<text x="412" y="294" fill="#CFFAFE" font-family="Arial" font-size="24" font-weight="700">In Progress</text>
<text x="732" y="294" fill="#CBD5E1" font-family="Arial" font-size="24" font-weight="700">Done</text>
<rect x="92" y="326" width="240" height="72" rx="18" fill="#1E293B"/>
<rect x="92" y="416" width="210" height="72" rx="18" fill="#1E293B"/>
<rect x="412" y="326" width="240" height="96" rx="18" fill="#155E75" fill-opacity="0.55" stroke="#22D3EE"/>
<rect x="412" y="442" width="220" height="72" rx="18" fill="#4C1D95" fill-opacity="0.55" stroke="#A78BFA"/>
<rect x="732" y="326" width="224" height="72" rx="18" fill="#1E293B"/>
<rect x="732" y="416" width="200" height="72" rx="18" fill="#1E293B"/>
<circle cx="1070" cy="138" r="74" fill="#22D3EE" fill-opacity="0.12"/>
<text x="432" y="362" fill="#F8FAFC" font-family="Arial" font-size="20" font-weight="700">Sprint planning</text>
<text x="432" y="390" fill="#CFFAFE" font-family="Arial" font-size="16">Priority board with movement states</text>
</svg>'''

files['realestate-project.svg'] = '''<svg width="1200" height="720" viewBox="0 0 1200 720" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="1200" height="720" rx="36" fill="#08111B"/>
<rect width="1200" height="720" rx="36" fill="url(#g)"/>
<defs>
  <linearGradient id="g" x1="120" y1="60" x2="1090" y2="650" gradientUnits="userSpaceOnUse">
    <stop stop-color="#0F172A"/>
    <stop offset="1" stop-color="#12324A"/>
  </linearGradient>
</defs>
<text x="64" y="96" fill="#A78BFA" font-family="Arial" font-size="22" font-weight="700">PROPERTY SEARCH EXPERIENCE</text>
<text x="64" y="154" fill="#F8FAFC" font-family="Arial" font-size="52" font-weight="700">Frontend Real Estate Finder</text>
<text x="64" y="198" fill="#94A3B8" font-family="Arial" font-size="24">Listing discovery, filters, map context, and detail browsing</text>
<rect x="60" y="248" width="460" height="390" rx="28" fill="#0F172A" stroke="#334155"/>
<rect x="548" y="248" width="592" height="390" rx="28" fill="#10263C" stroke="#14B8A6" stroke-opacity="0.35"/>
<rect x="92" y="284" width="170" height="42" rx="18" fill="#1E293B"/>
<rect x="276" y="284" width="120" height="42" rx="18" fill="#1E293B"/>
<rect x="92" y="352" width="396" height="112" rx="24" fill="#172554"/>
<rect x="92" y="484" width="396" height="112" rx="24" fill="#1E293B"/>
<text x="114" y="392" fill="#F8FAFC" font-family="Arial" font-size="24" font-weight="700">Modern apartment</text>
<text x="114" y="422" fill="#CBD5E1" font-family="Arial" font-size="18">3 beds • 2 baths • New Cairo</text>
<path d="M580 314H1110V608H580V314Z" fill="#0B1B2D"/>
<path d="M640 350C690 380 720 430 772 454C832 482 882 466 934 508C968 534 1012 550 1080 520" stroke="#14B8A6" stroke-width="10" stroke-linecap="round"/>
<circle cx="772" cy="454" r="16" fill="#A78BFA"/>
<circle cx="934" cy="508" r="16" fill="#22D3EE"/>
<circle cx="1080" cy="520" r="16" fill="#F8FAFC"/>
<text x="610" y="584" fill="#E2E8F0" font-family="Arial" font-size="20">Map-driven discovery flow</text>
</svg>'''

files['ecommerce-admin-project.svg'] = '''<svg width="1200" height="720" viewBox="0 0 1200 720" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="1200" height="720" rx="36" fill="#081225"/>
<rect width="1200" height="720" rx="36" fill="url(#g)"/>
<defs><linearGradient id="g" x1="80" y1="60" x2="1120" y2="660" gradientUnits="userSpaceOnUse"><stop stop-color="#0F172A"/><stop offset="1" stop-color="#0B3B70"/></linearGradient></defs>
<text x="64" y="96" fill="#38BDF8" font-family="Arial" font-size="22" font-weight="700">ADMIN DASHBOARD UI</text>
<text x="64" y="154" fill="#F8FAFC" font-family="Arial" font-size="52" font-weight="700">Frontend E-Commerce Dashboard</text>
<text x="64" y="198" fill="#94A3B8" font-family="Arial" font-size="24">Sales overview, orders table, and product-style analytics layout</text>
<rect x="64" y="248" width="220" height="390" rx="28" fill="#0F172A" stroke="#334155"/>
<rect x="310" y="248" width="826" height="390" rx="28" fill="#111827" stroke="#38BDF8" stroke-opacity="0.35"/>
<rect x="342" y="284" width="230" height="110" rx="24" fill="#172554"/>
<rect x="592" y="284" width="230" height="110" rx="24" fill="#0F766E" fill-opacity="0.7"/>
<rect x="842" y="284" width="260" height="110" rx="24" fill="#1E293B"/>
<rect x="342" y="420" width="760" height="40" rx="12" fill="#1E293B"/>
<rect x="342" y="476" width="760" height="40" rx="12" fill="#1E293B"/>
<rect x="342" y="532" width="760" height="40" rx="12" fill="#1E293B"/>
<text x="374" y="350" fill="#F8FAFC" font-family="Arial" font-size="28" font-weight="700">Revenue</text>
<text x="374" y="382" fill="#CBD5E1" font-family="Arial" font-size="20">$84,200</text>
<text x="624" y="350" fill="#F8FAFC" font-family="Arial" font-size="28" font-weight="700">Orders</text>
<text x="624" y="382" fill="#D1FAE5" font-family="Arial" font-size="20">1,284</text>
<text x="878" y="350" fill="#F8FAFC" font-family="Arial" font-size="28" font-weight="700">Users</text>
<text x="878" y="382" fill="#CBD5E1" font-family="Arial" font-size="20">9,420</text>
</svg>'''

files['churn-project.svg'] = '''<svg width="1200" height="720" viewBox="0 0 1200 720" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="1200" height="720" rx="36" fill="#130B18"/>
<rect width="1200" height="720" rx="36" fill="url(#g)"/>
<defs><linearGradient id="g" x1="80" y1="70" x2="1110" y2="650" gradientUnits="userSpaceOnUse"><stop stop-color="#1E1B4B"/><stop offset="1" stop-color="#3F0D1F"/></linearGradient></defs>
<text x="64" y="96" fill="#FB7185" font-family="Arial" font-size="22" font-weight="700">RETENTION ANALYTICS</text>
<text x="64" y="154" fill="#F8FAFC" font-family="Arial" font-size="52" font-weight="700">Customer Churn Prediction</text>
<text x="64" y="198" fill="#CBD5E1" font-family="Arial" font-size="24">Risk segmentation, feature signals, and model-led retention focus</text>
<circle cx="280" cy="418" r="150" fill="#EF4444" fill-opacity="0.14"/>
<circle cx="280" cy="418" r="104" fill="#EF4444" fill-opacity="0.22"/>
<circle cx="280" cy="418" r="62" fill="#EF4444" fill-opacity="0.34"/>
<text x="210" y="412" fill="#F8FAFC" font-family="Arial" font-size="28" font-weight="700">18.4%</text>
<text x="196" y="444" fill="#FCA5A5" font-family="Arial" font-size="18">churn risk</text>
<rect x="500" y="270" width="620" height="320" rx="30" fill="#111827" stroke="#FB7185" stroke-opacity="0.3"/>
<text x="536" y="316" fill="#F8FAFC" font-family="Arial" font-size="28" font-weight="700">Feature impact</text>
<rect x="540" y="346" width="420" height="28" rx="14" fill="#1E293B"/>
<rect x="540" y="400" width="320" height="28" rx="14" fill="#1E293B"/>
<rect x="540" y="454" width="250" height="28" rx="14" fill="#1E293B"/>
<rect x="540" y="346" width="360" height="28" rx="14" fill="#EF4444" fill-opacity="0.76"/>
<rect x="540" y="400" width="250" height="28" rx="14" fill="#F59E0B" fill-opacity="0.76"/>
<rect x="540" y="454" width="180" height="28" rx="14" fill="#A855F7" fill-opacity="0.76"/>
<text x="974" y="366" fill="#E2E8F0" font-family="Arial" font-size="18">Contract type</text>
<text x="874" y="420" fill="#E2E8F0" font-family="Arial" font-size="18">Tenure</text>
<text x="804" y="474" fill="#E2E8F0" font-family="Arial" font-size="18">Support calls</text>
</svg>'''

files['forecasting-project.svg'] = '''<svg width="1200" height="720" viewBox="0 0 1200 720" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="1200" height="720" rx="36" fill="#0B1020"/>
<rect width="1200" height="720" rx="36" fill="url(#g)"/>
<defs><linearGradient id="g" x1="70" y1="60" x2="1110" y2="650" gradientUnits="userSpaceOnUse"><stop stop-color="#172554"/><stop offset="1" stop-color="#1E1B4B"/></linearGradient></defs>
<text x="64" y="96" fill="#60A5FA" font-family="Arial" font-size="22" font-weight="700">TIME-SERIES FORECASTING</text>
<text x="64" y="154" fill="#F8FAFC" font-family="Arial" font-size="52" font-weight="700">Analytics Sales Forecasting</text>
<text x="64" y="198" fill="#CBD5E1" font-family="Arial" font-size="24">ARIMA-based trend analysis and future sales projection</text>
<rect x="80" y="260" width="1040" height="340" rx="28" fill="#111827" stroke="#60A5FA" stroke-opacity="0.35"/>
<path d="M136 512C206 490 240 454 308 446C378 438 422 384 492 392C564 400 604 334 678 344C752 354 796 274 870 286C938 296 1000 238 1062 224" stroke="#60A5FA" stroke-width="8" stroke-linecap="round"/>
<path d="M136 544C206 528 240 504 308 496C378 488 422 454 492 458C564 462 604 414 678 422C752 430 796 372 870 380C938 388 1000 338 1062 320" stroke="#A855F7" stroke-width="8" stroke-dasharray="18 16" stroke-linecap="round"/>
<text x="140" y="594" fill="#CBD5E1" font-family="Arial" font-size="20">Historical trend</text>
<text x="340" y="594" fill="#C4B5FD" font-family="Arial" font-size="20">Forecast projection</text>
</svg>'''

for name, content in files.items():
    (out_dir / name).write_text(content, encoding='utf-8')

print('generated distinct visuals:', len(files))
