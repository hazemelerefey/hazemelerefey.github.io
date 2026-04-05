from pathlib import Path

path = Path(r'D:\hazemelerefy website\index.html')
text = path.read_text(encoding='utf-8')

repls = [
    ("""                <h3 class=\"text-xl font-bold text-white mb-2 group-hover:text-pink-400 transition-colors\">JobPulse</h3>
                <p class=\"text-textMuted text-sm mb-6\">Premium job market intelligence dashboard focused on role demand, salary signals, and skill momentum through a polished frontend product experience.</p>
                <div class=\"flex items-center justify-between gap-4 text-xs text-textMuted font-medium\">""",
     """                <h3 class=\"text-xl font-bold text-white mb-2 group-hover:text-pink-400 transition-colors\">JobPulse</h3>
                <p class=\"text-[11px] uppercase tracking-[0.18em] text-pink-400/70 mb-3\">hazemelerefey/jobpulse</p>
                <p class=\"text-textMuted text-sm mb-6\">Premium job market intelligence dashboard focused on role demand, salary signals, and skill momentum through a polished frontend product experience.</p>
                <div class=\"flex items-center justify-between gap-4 text-xs text-textMuted font-medium\">"""),
    ("""                <h3 class=\"text-xl font-bold text-white mb-2 group-hover:text-pink-400 transition-colors\">Frontend E-Commerce Dashboard
                </h3>
                <p class=\"text-textMuted text-sm mb-6\">A modern admin dashboard frontend for tracking sales, orders, and user activity with responsive layout and chart-driven UI.</p>
                <div class=\"flex items-center justify-between gap-4 text-xs text-textMuted font-medium\">""",
     """                <h3 class=\"text-xl font-bold text-white mb-2 group-hover:text-pink-400 transition-colors\">Frontend E-Commerce Dashboard
                </h3>
                <p class=\"text-[11px] uppercase tracking-[0.18em] text-pink-400/70 mb-3\">hazemelerefey/frontend-ecommerce-dashboard</p>
                <p class=\"text-textMuted text-sm mb-6\">A modern admin dashboard frontend for tracking sales, orders, and user activity with responsive layout and chart-driven UI.</p>
                <div class=\"flex items-center justify-between gap-4 text-xs text-textMuted font-medium\">"""),
    ("""                <h3 class=\"text-xl font-bold text-white mb-2 group-hover:text-pink-400 transition-colors\">Frontend Kanban Board
                </h3>
                <p class=\"text-textMuted text-sm mb-6\">A drag-and-drop task management interface focused on board clarity, workflow movement, and polished product-style interactions.</p>
                <div class=\"flex items-center justify-between gap-4 text-xs text-textMuted font-medium\">""",
     """                <h3 class=\"text-xl font-bold text-white mb-2 group-hover:text-pink-400 transition-colors\">Frontend Kanban Board
                </h3>
                <p class=\"text-[11px] uppercase tracking-[0.18em] text-pink-400/70 mb-3\">hazemelerefey/frontend-kanban-board</p>
                <p class=\"text-textMuted text-sm mb-6\">A drag-and-drop task management interface focused on board clarity, workflow movement, and polished product-style interactions.</p>
                <div class=\"flex items-center justify-between gap-4 text-xs text-textMuted font-medium\">"""),
    ("""                <h3 class=\"text-xl font-bold text-white mb-2 group-hover:text-cyan-400 transition-colors\">Customer Churn Prediction</h3>
                <p class=\"text-textMuted text-sm mb-6\">Retention-focused predictive analytics project using machine learning to identify churn risk patterns and support smarter customer strategy.</p>
                <div class=\"flex items-center justify-between gap-4 text-xs text-textMuted font-medium\">""",
     """                <h3 class=\"text-xl font-bold text-white mb-2 group-hover:text-cyan-400 transition-colors\">Customer Churn Prediction</h3>
                <p class=\"text-[11px] uppercase tracking-[0.18em] text-cyan-400/70 mb-3\">hazemelerefey/analytics-churn-prediction</p>
                <p class=\"text-textMuted text-sm mb-6\">Retention-focused predictive analytics project using machine learning to identify churn risk patterns and support smarter customer strategy.</p>
                <div class=\"flex items-center justify-between gap-4 text-xs text-textMuted font-medium\">"""),
    ("""                <h3 class=\"text-xl font-bold text-white mb-2 group-hover:text-cyan-400 transition-colors\">Analytics Sales Forecasting</h3>
                <p class=\"text-textMuted text-sm mb-6\">Time-series forecasting project built to analyze historical sales movement and support better planning through ARIMA-based predictive reporting.</p>
                <div class=\"flex items-center justify-between gap-4 text-xs text-textMuted font-medium\">""",
     """                <h3 class=\"text-xl font-bold text-white mb-2 group-hover:text-cyan-400 transition-colors\">Analytics Sales Forecasting</h3>
                <p class=\"text-[11px] uppercase tracking-[0.18em] text-cyan-400/70 mb-3\">hazemelerefey/analytics-sales-forecasting</p>
                <p class=\"text-textMuted text-sm mb-6\">Time-series forecasting project built to analyze historical sales movement and support better planning through ARIMA-based predictive reporting.</p>
                <div class=\"flex items-center justify-between gap-4 text-xs text-textMuted font-medium\">"""),
    ("""                <h3 class=\"text-xl font-bold text-white mb-2 group-hover:text-cyan-400 transition-colors\">Global E-Commerce Sales Tracker</h3>
                <p class=\"text-textMuted text-sm mb-6\">Interactive business intelligence dashboard for tracking revenue, profit, orders, and regional performance across a global e-commerce dataset.</p>
                <div class=\"flex items-center justify-between gap-4 text-xs text-textMuted font-medium\">""",
     """                <h3 class=\"text-xl font-bold text-white mb-2 group-hover:text-cyan-400 transition-colors\">Global E-Commerce Sales Tracker</h3>
                <p class=\"text-[11px] uppercase tracking-[0.18em] text-cyan-400/70 mb-3\">hazemelerefey/global-ecommerce-sales-tracker</p>
                <p class=\"text-textMuted text-sm mb-6\">Interactive business intelligence dashboard for tracking revenue, profit, orders, and regional performance across a global e-commerce dataset.</p>
                <div class=\"flex items-center justify-between gap-4 text-xs text-textMuted font-medium\">"""),
]

for old, new in repls:
    if old not in text:
        raise SystemExit('pattern not found')
    text = text.replace(old, new, 1)

text = text.replace(
'''                    <span class="text-[11px] uppercase tracking-[0.18em] text-pink-400/90">Live GitHub Stats</span>
                </div>''',
'''                    <span class="text-[11px] uppercase tracking-[0.18em] text-pink-400/90">Live GitHub Stats</span>
                </div>
                <div class="mt-4 flex items-center gap-2 text-[11px] uppercase tracking-[0.18em] text-pink-400/80 group-hover:text-pink-300 transition-colors">
                    <i class="fab fa-github"></i>
                    <span>Open on GitHub</span>
                    <i class="fas fa-arrow-right group-hover:translate-x-1 transition-transform"></i>
                </div>''', 3)

text = text.replace(
'''                    <span class="text-[11px] uppercase tracking-[0.18em] text-cyan-400/90">Live GitHub Stats</span>
                </div>''',
'''                    <span class="text-[11px] uppercase tracking-[0.18em] text-cyan-400/90">Live GitHub Stats</span>
                </div>
                <div class="mt-4 flex items-center gap-2 text-[11px] uppercase tracking-[0.18em] text-cyan-400/80 group-hover:text-cyan-300 transition-colors">
                    <i class="fab fa-github"></i>
                    <span>Open on GitHub</span>
                    <i class="fas fa-arrow-right group-hover:translate-x-1 transition-transform"></i>
                </div>''', 3)

path.write_text(text, encoding='utf-8')
print('workspace card polish applied')
