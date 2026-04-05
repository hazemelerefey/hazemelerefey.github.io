from pathlib import Path

out_dir = Path(r'D:\hazemelerefy website\images')
out_dir.mkdir(parents=True, exist_ok=True)

files = {}

files['kanban-project.svg'] = '''<svg width="1200" height="720" viewBox="0 0 1200 720" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="1200" height="720" rx="28" fill="#0b1020"/>
<rect x="24" y="24" width="1152" height="672" rx="24" fill="#0f172a" stroke="#263244"/>
<rect x="24" y="24" width="1152" height="56" rx="24" fill="#111827"/>
<circle cx="58" cy="52" r="7" fill="#ef4444"/><circle cx="82" cy="52" r="7" fill="#f59e0b"/><circle cx="106" cy="52" r="7" fill="#22c55e"/>
<rect x="136" y="40" width="220" height="24" rx="12" fill="#1f2937"/>
<rect x="56" y="110" width="320" height="560" rx="22" fill="#101826" stroke="#223145"/>
<rect x="390" y="110" width="320" height="560" rx="22" fill="#0f1c2d" stroke="#22d3ee" stroke-opacity="0.28"/>
<rect x="724" y="110" width="320" height="560" rx="22" fill="#101826" stroke="#223145"/>
<text x="84" y="148" fill="#cbd5e1" font-family="Arial" font-size="22" font-weight="700">Backlog</text>
<text x="418" y="148" fill="#cffafe" font-family="Arial" font-size="22" font-weight="700">In Progress</text>
<text x="752" y="148" fill="#cbd5e1" font-family="Arial" font-size="22" font-weight="700">Done</text>
<rect x="84" y="176" width="74" height="18" rx="9" fill="#1f2937"/><rect x="418" y="176" width="74" height="18" rx="9" fill="#164e63"/><rect x="752" y="176" width="74" height="18" rx="9" fill="#1f2937"/>
<rect x="84" y="222" width="264" height="118" rx="18" fill="#172233"/><rect x="84" y="356" width="232" height="104" rx="18" fill="#172233"/><rect x="84" y="476" width="250" height="96" rx="18" fill="#172233"/>
<rect x="418" y="222" width="264" height="144" rx="18" fill="#155e75" fill-opacity="0.35" stroke="#22d3ee"/><rect x="418" y="382" width="230" height="110" rx="18" fill="#4c1d95" fill-opacity="0.35" stroke="#a78bfa"/>
<rect x="752" y="222" width="240" height="92" rx="18" fill="#172233"/><rect x="752" y="330" width="212" height="88" rx="18" fill="#172233"/><rect x="752" y="434" width="236" height="92" rx="18" fill="#172233"/>
<rect x="106" y="244" width="160" height="12" rx="6" fill="#e2e8f0"/><rect x="106" y="266" width="110" height="10" rx="5" fill="#64748b"/>
<rect x="440" y="244" width="178" height="12" rx="6" fill="#f8fafc"/><rect x="440" y="268" width="134" height="10" rx="5" fill="#bae6fd"/>
<rect x="774" y="244" width="134" height="12" rx="6" fill="#e2e8f0"/><rect x="774" y="266" width="102" height="10" rx="5" fill="#64748b"/>
</svg>'''

files['realestate-project.svg'] = '''<svg width="1200" height="720" viewBox="0 0 1200 720" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="1200" height="720" rx="28" fill="#08111b"/>
<rect x="24" y="24" width="1152" height="672" rx="24" fill="#0f172a" stroke="#223145"/>
<rect x="24" y="24" width="1152" height="56" rx="24" fill="#101826"/>
<circle cx="58" cy="52" r="7" fill="#ef4444"/><circle cx="82" cy="52" r="7" fill="#f59e0b"/><circle cx="106" cy="52" r="7" fill="#22c55e"/>
<rect x="136" y="40" width="240" height="24" rx="12" fill="#1f2937"/>
<rect x="56" y="108" width="340" height="72" rx="22" fill="#111827" stroke="#334155"/>
<rect x="70" y="126" width="120" height="34" rx="16" fill="#172554"/><rect x="202" y="126" width="76" height="34" rx="16" fill="#1f2937"/><rect x="290" y="126" width="86" height="34" rx="16" fill="#1f2937"/>
<rect x="56" y="204" width="430" height="466" rx="24" fill="#111827" stroke="#334155"/>
<rect x="510" y="108" width="610" height="562" rx="24" fill="#0b1b2d" stroke="#14b8a6" stroke-opacity="0.3"/>
<rect x="82" y="230" width="378" height="152" rx="20" fill="#172554"/>
<rect x="82" y="398" width="378" height="116" rx="20" fill="#162230"/>
<rect x="82" y="530" width="378" height="116" rx="20" fill="#162230"/>
<text x="104" y="270" fill="#f8fafc" font-family="Arial" font-size="28" font-weight="700">Modern apartment</text>
<text x="104" y="304" fill="#cbd5e1" font-family="Arial" font-size="18">3 beds • 2 baths • New Cairo</text>
<text x="104" y="338" fill="#99f6e4" font-family="Arial" font-size="20" font-weight="700">EGP 5,200,000</text>
<path d="M552 160H1078V624H552V160Z" fill="#0e2235"/>
<path d="M612 220L686 264L736 238L814 308L908 284L982 360L1050 332" stroke="#22d3ee" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="736" cy="238" r="14" fill="#a78bfa"/><circle cx="908" cy="284" r="14" fill="#14b8a6"/><circle cx="1050" cy="332" r="14" fill="#f8fafc"/>
</svg>'''

files['ecommerce-admin-project.svg'] = '''<svg width="1200" height="720" viewBox="0 0 1200 720" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="1200" height="720" rx="28" fill="#091423"/>
<rect x="24" y="24" width="1152" height="672" rx="24" fill="#0f172a" stroke="#223145"/>
<rect x="24" y="24" width="1152" height="56" rx="24" fill="#101826"/>
<circle cx="58" cy="52" r="7" fill="#ef4444"/><circle cx="82" cy="52" r="7" fill="#f59e0b"/><circle cx="106" cy="52" r="7" fill="#22c55e"/>
<rect x="56" y="108" width="220" height="560" rx="24" fill="#101826" stroke="#223145"/>
<rect x="300" y="108" width="820" height="560" rx="24" fill="#111827" stroke="#38bdf8" stroke-opacity="0.28"/>
<rect x="332" y="140" width="220" height="110" rx="22" fill="#172554"/>
<rect x="570" y="140" width="220" height="110" rx="22" fill="#0f766e" fill-opacity="0.55"/>
<rect x="808" y="140" width="280" height="110" rx="22" fill="#1e293b"/>
<rect x="332" y="276" width="756" height="156" rx="24" fill="#0f1c2d"/>
<rect x="332" y="454" width="756" height="42" rx="12" fill="#1f2937"/>
<rect x="332" y="512" width="756" height="42" rx="12" fill="#1f2937"/>
<rect x="332" y="570" width="756" height="42" rx="12" fill="#1f2937"/>
<path d="M362 382C420 370 456 330 516 336C582 342 620 286 690 292C760 298 794 258 864 266C934 274 986 238 1052 226" stroke="#38bdf8" stroke-width="8" stroke-linecap="round"/>
<text x="364" y="188" fill="#f8fafc" font-family="Arial" font-size="28" font-weight="700">Revenue</text>
<text x="364" y="220" fill="#cbd5e1" font-family="Arial" font-size="20">$84,200</text>
<text x="602" y="188" fill="#f8fafc" font-family="Arial" font-size="28" font-weight="700">Orders</text>
<text x="602" y="220" fill="#d1fae5" font-family="Arial" font-size="20">1,284</text>
<text x="840" y="188" fill="#f8fafc" font-family="Arial" font-size="28" font-weight="700">Users</text>
<text x="840" y="220" fill="#cbd5e1" font-family="Arial" font-size="20">9,420</text>
</svg>'''

files['churn-project.svg'] = '''<svg width="1200" height="720" viewBox="0 0 1200 720" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="1200" height="720" rx="28" fill="#140c18"/>
<rect x="24" y="24" width="1152" height="672" rx="24" fill="#111827" stroke="#31213d"/>
<rect x="24" y="24" width="1152" height="56" rx="24" fill="#16101d"/>
<circle cx="58" cy="52" r="7" fill="#ef4444"/><circle cx="82" cy="52" r="7" fill="#f59e0b"/><circle cx="106" cy="52" r="7" fill="#22c55e"/>
<rect x="56" y="108" width="320" height="560" rx="24" fill="#16101d" stroke="#3f233e"/>
<rect x="398" y="108" width="722" height="560" rx="24" fill="#111827" stroke="#fb7185" stroke-opacity="0.22"/>
<text x="84" y="156" fill="#f8fafc" font-family="Arial" font-size="24" font-weight="700">Churn risk summary</text>
<circle cx="214" cy="310" r="92" fill="#7f1d1d"/>
<circle cx="214" cy="310" r="66" fill="#ef4444" fill-opacity="0.65"/>
<text x="164" y="306" fill="#fff" font-family="Arial" font-size="30" font-weight="700">18.4%</text>
<text x="168" y="338" fill="#fecaca" font-family="Arial" font-size="18">at risk</text>
<rect x="84" y="450" width="244" height="20" rx="10" fill="#1f2937"/><rect x="84" y="484" width="210" height="20" rx="10" fill="#1f2937"/><rect x="84" y="518" width="182" height="20" rx="10" fill="#1f2937"/>
<text x="430" y="156" fill="#f8fafc" font-family="Arial" font-size="24" font-weight="700">Feature importance</text>
<rect x="430" y="198" width="480" height="26" rx="13" fill="#1f2937"/><rect x="430" y="248" width="390" height="26" rx="13" fill="#1f2937"/><rect x="430" y="298" width="310" height="26" rx="13" fill="#1f2937"/><rect x="430" y="348" width="260" height="26" rx="13" fill="#1f2937"/>
<rect x="430" y="198" width="404" height="26" rx="13" fill="#ef4444" fill-opacity="0.84"/><rect x="430" y="248" width="324" height="26" rx="13" fill="#f59e0b" fill-opacity="0.84"/><rect x="430" y="298" width="246" height="26" rx="13" fill="#a855f7" fill-opacity="0.84"/><rect x="430" y="348" width="190" height="26" rx="13" fill="#38bdf8" fill-opacity="0.84"/>
<text x="936" y="216" fill="#e2e8f0" font-family="Arial" font-size="18">Contract</text><text x="846" y="266" fill="#e2e8f0" font-family="Arial" font-size="18">Tenure</text><text x="768" y="316" fill="#e2e8f0" font-family="Arial" font-size="18">Support calls</text><text x="642" y="366" fill="#e2e8f0" font-family="Arial" font-size="18">Monthly charges</text>
<rect x="430" y="432" width="632" height="166" rx="24" fill="#16101d"/>
<path d="M458 556C520 542 560 516 612 496C674 472 712 430 768 406C826 382 876 384 934 350C972 326 1008 302 1036 286" stroke="#fb7185" stroke-width="8" stroke-linecap="round"/>
</svg>'''

for name, content in files.items():
    (out_dir / name).write_text(content, encoding='utf-8')

print('generated screenshot-like visuals:', len(files))
