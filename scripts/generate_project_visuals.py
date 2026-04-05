from pathlib import Path

out_dir = Path(r'D:\hazemelerefy website\images')
out_dir.mkdir(parents=True, exist_ok=True)

projects = [
    {
        'file': 'kanban-project.svg',
        'title': 'Frontend Kanban Board',
        'subtitle': 'Drag-and-drop workflow • Redux Toolkit • React UI',
        'bg1': '#0b1220', 'bg2': '#111827', 'glow': '#22d3ee', 'accent': '#7c3aed',
        'chip1': 'Workflow UI', 'chip2': 'React', 'chip3': 'Redux Toolkit',
        'panelTitle': 'Board lanes', 'panelMetric': '24 tasks', 'metric2': '3 priorities',
        'list1': 'Backlog', 'list2': 'In Progress', 'list3': 'Done'
    },
    {
        'file': 'realestate-project.svg',
        'title': 'Frontend Real Estate Finder',
        'subtitle': 'Listing discovery • Filters • Map-based browsing',
        'bg1': '#08111b', 'bg2': '#10233b', 'glow': '#a855f7', 'accent': '#14b8a6',
        'chip1': 'Search UX', 'chip2': 'Next.js', 'chip3': 'Maps',
        'panelTitle': 'Listings', 'panelMetric': '128 homes', 'metric2': '12 filters',
        'list1': 'City view', 'list2': 'Map sync', 'list3': 'Detail card'
    },
    {
        'file': 'ecommerce-admin-project.svg',
        'title': 'Frontend E-Commerce Dashboard',
        'subtitle': 'Admin analytics • Orders • Sales activity',
        'bg1': '#0a1425', 'bg2': '#0f172a', 'glow': '#38bdf8', 'accent': '#2563eb',
        'chip1': 'Admin UI', 'chip2': 'React', 'chip3': 'Recharts',
        'panelTitle': 'Commerce summary', 'panelMetric': '$84.2k', 'metric2': '1,284 orders',
        'list1': 'Revenue', 'list2': 'Orders', 'list3': 'Users'
    },
    {
        'file': 'churn-project.svg',
        'title': 'Customer Churn Prediction',
        'subtitle': 'Retention analytics • ML signals • Risk scoring',
        'bg1': '#170b1f', 'bg2': '#0f172a', 'glow': '#ef4444', 'accent': '#ec4899',
        'chip1': 'Predictive Analytics', 'chip2': 'Python', 'chip3': 'Scikit-learn',
        'panelTitle': 'Risk monitor', 'panelMetric': '18.4% churn', 'metric2': 'AUC 0.87',
        'list1': 'High risk', 'list2': 'Feature impact', 'list3': 'Retention focus'
    },
    {
        'file': 'forecasting-project.svg',
        'title': 'Analytics Sales Forecasting',
        'subtitle': 'ARIMA time-series analysis • Trend forecasting',
        'bg1': '#0b1120', 'bg2': '#172554', 'glow': '#60a5fa', 'accent': '#7c3aed',
        'chip1': 'Forecasting', 'chip2': 'Python', 'chip3': 'ARIMA',
        'panelTitle': 'Forecast horizon', 'panelMetric': '+12.8%', 'metric2': '6 months',
        'list1': 'Trend', 'list2': 'Seasonality', 'list3': 'Projection'
    },
    {
        'file': 'global-sales-project.svg',
        'title': 'Global E-Commerce Sales Tracker',
        'subtitle': 'Revenue • Profit • Regional commercial performance',
        'bg1': '#111827', 'bg2': '#3b0764', 'glow': '#f59e0b', 'accent': '#ec4899',
        'chip1': 'Commercial BI', 'chip2': 'Power BI', 'chip3': 'DAX',
        'panelTitle': 'Regional summary', 'panelMetric': '$2.4M', 'metric2': '37 markets',
        'list1': 'Revenue', 'list2': 'Profit', 'list3': 'Regions'
    },
]

TEMPLATE = '''<svg width="1200" height="720" viewBox="0 0 1200 720" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="80" y1="40" x2="1120" y2="680" gradientUnits="userSpaceOnUse">
      <stop stop-color="{bg1}"/>
      <stop offset="1" stop-color="{bg2}"/>
    </linearGradient>
    <radialGradient id="glowA" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(240 160) rotate(32) scale(260 240)">
      <stop stop-color="{glow}" stop-opacity="0.28"/>
      <stop offset="1" stop-color="{glow}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glowB" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(980 540) rotate(18) scale(280 220)">
      <stop stop-color="{accent}" stop-opacity="0.22"/>
      <stop offset="1" stop-color="{accent}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="1200" height="720" rx="36" fill="url(#bg)"/>
  <rect width="1200" height="720" rx="36" fill="url(#glowA)"/>
  <rect width="1200" height="720" rx="36" fill="url(#glowB)"/>

  <text x="72" y="120" fill="#E2E8F0" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" letter-spacing="3">PROJECT SHOWCASE</text>
  <text x="72" y="208" fill="#F8FAFC" font-family="Arial, Helvetica, sans-serif" font-size="52" font-weight="700">{title}</text>
  <text x="72" y="260" fill="#94A3B8" font-family="Arial, Helvetica, sans-serif" font-size="26">{subtitle}</text>

  <rect x="72" y="316" width="170" height="40" rx="20" fill="{glow}" fill-opacity="0.14" stroke="{glow}" stroke-opacity="0.4"/>
  <text x="101" y="342" fill="#E5E7EB" font-family="Arial, Helvetica, sans-serif" font-size="18">{chip1}</text>
  <rect x="258" y="316" width="140" height="40" rx="20" fill="#FFFFFF" fill-opacity="0.06" stroke="#FFFFFF" stroke-opacity="0.12"/>
  <text x="300" y="342" fill="#E5E7EB" font-family="Arial, Helvetica, sans-serif" font-size="18">{chip2}</text>
  <rect x="414" y="316" width="180" height="40" rx="20" fill="{accent}" fill-opacity="0.12" stroke="{accent}" stroke-opacity="0.32"/>
  <text x="450" y="342" fill="#F8FAFC" font-family="Arial, Helvetica, sans-serif" font-size="18">{chip3}</text>

  <rect x="650" y="92" width="472" height="536" rx="30" fill="#020617" fill-opacity="0.56" stroke="#FFFFFF" stroke-opacity="0.12"/>
  <rect x="684" y="126" width="180" height="96" rx="22" fill="#FFFFFF" fill-opacity="0.05" stroke="#FFFFFF" stroke-opacity="0.10"/>
  <rect x="882" y="126" width="206" height="96" rx="22" fill="#FFFFFF" fill-opacity="0.05" stroke="#FFFFFF" stroke-opacity="0.10"/>
  <text x="710" y="156" fill="#94A3B8" font-family="Arial, Helvetica, sans-serif" font-size="16">{panelTitle}</text>
  <text x="710" y="198" fill="#F8FAFC" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="700">{panelMetric}</text>
  <text x="908" y="156" fill="#94A3B8" font-family="Arial, Helvetica, sans-serif" font-size="16">Signal</text>
  <text x="908" y="198" fill="#F8FAFC" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="700">{metric2}</text>

  <rect x="684" y="246" width="404" height="154" rx="24" fill="#FFFFFF" fill-opacity="0.04" stroke="#FFFFFF" stroke-opacity="0.08"/>
  <text x="710" y="282" fill="#94A3B8" font-family="Arial, Helvetica, sans-serif" font-size="16">Interface preview</text>
  <path d="M716 360C752 356 776 308 820 314C862 320 896 270 938 278C980 286 1008 236 1056 242" stroke="{glow}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="716" cy="360" r="6" fill="{glow}"/>
  <circle cx="820" cy="314" r="6" fill="{glow}"/>
  <circle cx="938" cy="278" r="6" fill="{glow}"/>
  <circle cx="1056" cy="242" r="6" fill="{glow}"/>
  <rect x="716" y="314" width="116" height="12" rx="6" fill="#FFFFFF" fill-opacity="0.14"/>
  <rect x="716" y="334" width="154" height="12" rx="6" fill="#FFFFFF" fill-opacity="0.10"/>
  <rect x="716" y="382" width="182" height="12" rx="6" fill="#FFFFFF" fill-opacity="0.08"/>

  <rect x="684" y="426" width="404" height="166" rx="24" fill="#FFFFFF" fill-opacity="0.04" stroke="#FFFFFF" stroke-opacity="0.08"/>
  <text x="710" y="462" fill="#94A3B8" font-family="Arial, Helvetica, sans-serif" font-size="16">Key surfaces</text>
  <rect x="716" y="486" width="340" height="28" rx="14" fill="#FFFFFF" fill-opacity="0.05"/>
  <rect x="716" y="526" width="296" height="28" rx="14" fill="#FFFFFF" fill-opacity="0.05"/>
  <rect x="716" y="566" width="248" height="28" rx="14" fill="#FFFFFF" fill-opacity="0.05"/>
  <text x="738" y="505" fill="#E2E8F0" font-family="Arial, Helvetica, sans-serif" font-size="16">{list1}</text>
  <text x="738" y="545" fill="#E2E8F0" font-family="Arial, Helvetica, sans-serif" font-size="16">{list2}</text>
  <text x="738" y="585" fill="#E2E8F0" font-family="Arial, Helvetica, sans-serif" font-size="16">{list3}</text>

  <text x="72" y="420" fill="#CBD5E1" font-family="Arial, Helvetica, sans-serif" font-size="24">Clean project-specific visual based on repo identity</text>
  <text x="72" y="468" fill="#64748B" font-family="Arial, Helvetica, sans-serif" font-size="20">Designed for portfolio presentation without fake placeholder screenshots</text>
</svg>
'''

for project in projects:
    svg = TEMPLATE.format(**project)
    (out_dir / project['file']).write_text(svg, encoding='utf-8')

print('generated', len(projects), 'project visuals')
