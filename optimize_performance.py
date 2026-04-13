"""
Performance Optimization Script
Applies the 4 optimization rules from the user's cheat sheet:
1. Hardware Acceleration (GPU-only animations)
2. Debounce/Throttle JS events
3. Strategic will-change usage
4. prefers-reduced-motion accessibility
"""
import codecs

# ═══════════════════════════════════════════════
# PART 1: OPTIMIZE extreme.js
# ═══════════════════════════════════════════════
with codecs.open('js/extreme.js', 'r', 'utf-8') as f:
    js = f.read()

# --- FIX 1: Add throttling to 3D Tilt Cards mousemove (initTiltCards) ---
# Currently fires on EVERY mousemove with no throttle
old_tilt = """  function initTiltCards() {
    const cards = document.querySelectorAll('.card-3d');
    const MAX_TILT = 10; // degrees

    cards.forEach((card) => {
      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const cx   = rect.left + rect.width  / 2;
        const cy   = rect.top  + rect.height / 2;
        const dx   = (e.clientX - cx) / (rect.width  / 2);
        const dy   = (e.clientY - cy) / (rect.height / 2);

        const rx =  -dy * MAX_TILT;
        const ry =   dx * MAX_TILT;

        card.style.setProperty('--rx', rx.toFixed(2) + 'deg');
        card.style.setProperty('--ry', ry.toFixed(2) + 'deg');

        // Mouse position for highlight
        const mx = ((e.clientX - rect.left) / rect.width  * 100).toFixed(1) + '%';
        const my = ((e.clientY - rect.top ) / rect.height * 100).toFixed(1) + '%';
        card.style.setProperty('--mx', mx);
        card.style.setProperty('--my', my);

        card.style.transform = `perspective(1000px) rotateX(${rx}deg) rotateY(${ry}deg) translateZ(4px)`;
      });

      card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateZ(0)';
        card.style.setProperty('--mx', '50%');
        card.style.setProperty('--my', '50%');
      });
    });
  }"""

new_tilt = """  function initTiltCards() {
    const cards = document.querySelectorAll('.card-3d');
    const MAX_TILT = 10; // degrees

    cards.forEach((card) => {
      let tiltTicking = false;
      card.addEventListener('mousemove', (e) => {
        if (tiltTicking) return;
        tiltTicking = true;
        requestAnimationFrame(() => {
          const rect = card.getBoundingClientRect();
          const cx   = rect.left + rect.width  / 2;
          const cy   = rect.top  + rect.height / 2;
          const dx   = (e.clientX - cx) / (rect.width  / 2);
          const dy   = (e.clientY - cy) / (rect.height / 2);

          const rx =  -dy * MAX_TILT;
          const ry =   dx * MAX_TILT;

          card.style.setProperty('--rx', rx.toFixed(2) + 'deg');
          card.style.setProperty('--ry', ry.toFixed(2) + 'deg');

          const mx = ((e.clientX - rect.left) / rect.width  * 100).toFixed(1) + '%';
          const my = ((e.clientY - rect.top ) / rect.height * 100).toFixed(1) + '%';
          card.style.setProperty('--mx', mx);
          card.style.setProperty('--my', my);

          card.style.transform = `perspective(1000px) rotateX(${rx}deg) rotateY(${ry}deg) translateZ(4px)`;
          tiltTicking = false;
        });
      });

      card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateZ(0)';
        card.style.setProperty('--mx', '50%');
        card.style.setProperty('--my', '50%');
      });

      // will-change: add on mouseenter, remove on mouseleave
      card.addEventListener('mouseenter', () => {
        card.style.willChange = 'transform';
      });
      card.addEventListener('mouseleave', () => {
        card.style.willChange = 'auto';
      });
    });
  }"""

js = js.replace(old_tilt, new_tilt)

# --- FIX 2: Add rAF throttle to Card Spotlight mousemove ---
old_spotlight_cards = """  function initCardSpotlight() {
    const cards = document.querySelectorAll('.expertise-card, .glass-extreme, .project-card-extreme');

    cards.forEach((card) => {
      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = ((e.clientX - rect.left) / rect.width  * 100).toFixed(1) + '%';
        const y = ((e.clientY - rect.top ) / rect.height * 100).toFixed(1) + '%';
        card.style.setProperty('--mx', x);
        card.style.setProperty('--my', y);
      });
    });
  }"""

new_spotlight_cards = """  function initCardSpotlight() {
    const cards = document.querySelectorAll('.expertise-card, .glass-extreme, .project-card-extreme');

    cards.forEach((card) => {
      let spotTicking = false;
      card.addEventListener('mousemove', (e) => {
        if (spotTicking) return;
        spotTicking = true;
        requestAnimationFrame(() => {
          const rect = card.getBoundingClientRect();
          const x = ((e.clientX - rect.left) / rect.width  * 100).toFixed(1) + '%';
          const y = ((e.clientY - rect.top ) / rect.height * 100).toFixed(1) + '%';
          card.style.setProperty('--mx', x);
          card.style.setProperty('--my', y);
          spotTicking = false;
        });
      });
    });
  }"""

js = js.replace(old_spotlight_cards, new_spotlight_cards)

# --- FIX 3: Add rAF throttle to Blob Parallax scroll handler ---
old_blob = """  function initBlobParallax() {
    const blobs = document.querySelectorAll('.animate-blob');
    if (!blobs.length) return;

    window.addEventListener('scroll', () => {
      const scrollY = window.scrollY;
      blobs.forEach((blob, i) => {
        const speed  = 0.08 + (i * 0.04);
        const offset = scrollY * speed;
        blob.style.transform = `translateY(${offset}px)`;
      });
    }, { passive: true });
  }"""

new_blob = """  function initBlobParallax() {
    const blobs = document.querySelectorAll('.animate-blob');
    if (!blobs.length) return;

    let blobTicking = false;
    window.addEventListener('scroll', () => {
      if (blobTicking) return;
      blobTicking = true;
      requestAnimationFrame(() => {
        const scrollY = window.scrollY;
        blobs.forEach((blob, i) => {
          const speed  = 0.08 + (i * 0.04);
          const offset = scrollY * speed;
          blob.style.transform = `translateY(${offset}px)`;
        });
        blobTicking = false;
      });
    }, { passive: true });
  }"""

js = js.replace(old_blob, new_blob)

# --- FIX 4: Add rAF throttle to Scroll Progress bar ---
old_scroll_prog = """    window.addEventListener('scroll', () => {
      const total   = document.documentElement.scrollHeight - window.innerHeight;
      const current = window.scrollY;
      bar.style.width = ((current / total) * 100).toFixed(2) + '%';
    }, { passive: true });"""

new_scroll_prog = """    let scrollProgTicking = false;
    window.addEventListener('scroll', () => {
      if (scrollProgTicking) return;
      scrollProgTicking = true;
      requestAnimationFrame(() => {
        const total   = document.documentElement.scrollHeight - window.innerHeight;
        const current = window.scrollY;
        bar.style.width = ((current / total) * 100).toFixed(2) + '%';
        scrollProgTicking = false;
      });
    }, { passive: true });"""

js = js.replace(old_scroll_prog, new_scroll_prog)

# --- FIX 5: Use transform instead of width for scroll progress bar ---
# width triggers reflow! Use scaleX instead (GPU-accelerated)
old_bar_style = """    bar.style.cssText = [
      'position:fixed',
      'top:0', 'left:0',
      'height:6px',
      'width:0%',
      'background:#0a0a0a',
      'z-index:99999',
      'pointer-events:none',
      'border-bottom: 1px solid rgba(255, 255, 255, 0.1)',
      'box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5)',
      'transition:width 0.1s ease-out'
    ].join(';');"""

new_bar_style = """    bar.style.cssText = [
      'position:fixed',
      'top:0', 'left:0',
      'height:6px',
      'width:100%',
      'background:#0a0a0a',
      'z-index:99999',
      'pointer-events:none',
      'border-bottom: 1px solid rgba(255, 255, 255, 0.1)',
      'box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5)',
      'transform-origin:left',
      'transform:scaleX(0)',
      'will-change:transform'
    ].join(';');"""

js = js.replace(old_bar_style, new_bar_style)

# Update the scroll handler to use scaleX instead of width
js = js.replace(
    "bar.style.width = ((current / total) * 100).toFixed(2) + '%';",
    "bar.style.transform = 'scaleX(' + (current / total).toFixed(4) + ')';"
)

# --- FIX 6: Wrap boot() in a reduced-motion check ---
old_boot = """  function boot() {
    injectElements();
    initSpotlight();
    applyRevealClasses();
    initScrollReveal();
    initTiltCards();
    initCardSpotlight();
    initSkillBars();
    initCounters();
    initMarqueePause();
    initScrollProgress();
    initBlobParallax();
    initScanLines();

    console.log('%c\u26a1 EXTREME UI/UX ENGINE LOADED', 'color:#00f5ff;font-weight:900;font-size:14px;text-shadow:0 0 10px #00f5ff;');
  }"""

new_boot = """  function boot() {
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    injectElements();
    initSpotlight();
    applyRevealClasses();
    initScrollReveal();
    initSkillBars();
    initCounters();
    initScrollProgress();

    // Heavy visual effects: skip entirely for reduced-motion users
    if (!prefersReducedMotion) {
      initTiltCards();
      initCardSpotlight();
      initMarqueePause();
      initBlobParallax();
      initScanLines();
    }

    console.log('%c\u26a1 EXTREME UI/UX ENGINE v2.0 \u2014 GPU-Optimized', 'color:#00f5ff;font-weight:900;font-size:14px;text-shadow:0 0 10px #00f5ff;');
  }"""

js = js.replace(old_boot, new_boot)

with codecs.open('js/extreme.js', 'w', 'utf-8') as f:
    f.write(js)
print("[JS] extreme.js optimized successfully.")


# ═══════════════════════════════════════════════
# PART 2: OPTIMIZE extreme.css
# ═══════════════════════════════════════════════
with codecs.open('css/extreme.css', 'r', 'utf-8') as f:
    css = f.read()

# --- FIX 7: Add will-change to animated elements that need it ---
# .reveal already has will-change: transform, opacity — GOOD
# .card-3d already has will-change: transform — GOOD
# Add will-change to other animated cards (only during hover via JS, not static)

# --- FIX 8: Fix scan-line using 'top' property (causes reflow!) ---
old_scan_keyframe = """@keyframes scan-line {
  0%   { top: -2px; opacity: 0; }
  10%  { opacity: 0.6; }
  90%  { opacity: 0.6; }
  100% { top: 100%; opacity: 0; }
}

.scan-line {
  position: absolute;
  left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(0,245,255,0.6), transparent);
  animation: scan-line 3s ease-in-out infinite 1s;
  pointer-events: none;
  z-index: 5;
  transition: opacity 0.3s ease;
}"""

new_scan_keyframe = """@keyframes scan-line {
  0%   { transform: translateY(-2px); opacity: 0; }
  10%  { opacity: 0.6; }
  90%  { opacity: 0.6; }
  100% { transform: translateY(calc(var(--card-h, 200px))); opacity: 0; }
}

.scan-line {
  position: absolute;
  top: 0;
  left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(0,245,255,0.6), transparent);
  animation: scan-line 3s ease-in-out infinite 1s;
  pointer-events: none;
  z-index: 5;
  transition: opacity 0.3s ease;
  will-change: transform, opacity;
}"""

css = css.replace(old_scan_keyframe, new_scan_keyframe)

# --- FIX 9: Upgrade prefers-reduced-motion to be more comprehensive ---
old_reduced_motion = """@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }

  .reveal,
  .reveal-left,
  .reveal-right,
  .reveal-scale {
    opacity: 1 !important;
    transform: none !important;
  }
}"""

new_reduced_motion = """@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }

  .reveal,
  .reveal-left,
  .reveal-right,
  .reveal-scale {
    opacity: 1 !important;
    transform: none !important;
  }

  /* Disable heavy visual effects entirely */
  .scan-line,
  .animate-blob,
  .animate-float,
  .animate-float-up,
  .animate-flicker,
  .animate-cinematic-pan {
    animation: none !important;
  }

  #spotlight {
    display: none !important;
  }

  .card-3d {
    transform: none !important;
    will-change: auto !important;
  }

  .expertise-card:hover,
  .glass-extreme:hover,
  .project-card-extreme:hover,
  .platform-card:hover,
  .card-neon-cyan:hover,
  .card-neon-pink:hover {
    transform: none !important;
  }

  /* Remove will-change globally for memory savings */
  * {
    will-change: auto !important;
  }
}"""

css = css.replace(old_reduced_motion, new_reduced_motion)

# --- FIX 10: Add will-change to reveal-left and reveal-right ---
css = css.replace(
    """.reveal-left {
  opacity: 0;
  transform: translateX(-50px);
  transition: opacity 0.7s ease, transform 0.7s cubic-bezier(0.16,1,0.3,1);
}""",
    """.reveal-left {
  opacity: 0;
  transform: translateX(-50px);
  transition: opacity 0.7s ease, transform 0.7s cubic-bezier(0.16,1,0.3,1);
  will-change: transform, opacity;
}"""
)

css = css.replace(
    """.reveal-right {
  opacity: 0;
  transform: translateX(50px);
  transition: opacity 0.7s ease, transform 0.7s cubic-bezier(0.16,1,0.3,1);
}""",
    """.reveal-right {
  opacity: 0;
  transform: translateX(50px);
  transition: opacity 0.7s ease, transform 0.7s cubic-bezier(0.16,1,0.3,1);
  will-change: transform, opacity;
}"""
)

css = css.replace(
    """.reveal-scale {
  opacity: 0;
  transform: scale(0.88);
  transition: opacity 0.6s ease, transform 0.6s cubic-bezier(0.175,0.885,0.32,1.275);
}""",
    """.reveal-scale {
  opacity: 0;
  transform: scale(0.88);
  transition: opacity 0.6s ease, transform 0.6s cubic-bezier(0.175,0.885,0.32,1.275);
  will-change: transform, opacity;
}"""
)

with codecs.open('css/extreme.css', 'w', 'utf-8') as f:
    f.write(css)
print("[CSS] extreme.css optimized successfully.")


# ═══════════════════════════════════════════════
# PART 3: OPTIMIZE style.css
# ═══════════════════════════════════════════════
with codecs.open('css/style.css', 'r', 'utf-8') as f:
    css2 = f.read()

# --- FIX 11: Add will-change to .animate-blob ---
css2 = css2.replace(
    """.animate-blob {
    animation: blob 8s infinite ease-in-out;
}""",
    """.animate-blob {
    animation: blob 8s infinite ease-in-out;
    will-change: transform;
}"""
)

# --- FIX 12: Add will-change to marquee animations ---
css2 = css2.replace(
    """.animate-marquee-left {
    animation: marquee-left 30s linear infinite;
}""",
    """.animate-marquee-left {
    animation: marquee-left 30s linear infinite;
    will-change: transform;
}"""
)

css2 = css2.replace(
    """.animate-marquee-right {
    animation: marquee-right 30s linear infinite;
}""",
    """.animate-marquee-right {
    animation: marquee-right 30s linear infinite;
    will-change: transform;
}"""
)

# --- FIX 13: Add prefers-reduced-motion to style.css ---
css2 += """
/* ─────────────────────────────────────────────
   REDUCED MOTION SAFETY (style.css)
───────────────────────────────────────────── */
@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto !important;
  }

  .animate-blob,
  .animate-float,
  .animate-cinematic-pan,
  .animate-marquee-left,
  .animate-marquee-right,
  .animate-tear,
  .animate-joy-bounce {
    animation: none !important;
    will-change: auto !important;
  }
}
"""

with codecs.open('css/style.css', 'w', 'utf-8') as f:
    f.write(css2)
print("[CSS] style.css optimized successfully.")

print("\n=== ALL OPTIMIZATIONS APPLIED ===")
print("  [1] Hardware Acceleration: scan-line now uses translateY instead of top")
print("  [2] Hardware Acceleration: scroll progress bar uses scaleX instead of width")
print("  [3] Throttle: 3D tilt cards mousemove wrapped in rAF")
print("  [4] Throttle: card spotlight mousemove wrapped in rAF")
print("  [5] Throttle: blob parallax scroll wrapped in rAF")
print("  [6] Throttle: scroll progress bar wrapped in rAF")
print("  [7] will-change: strategic on reveal-left, reveal-right, reveal-scale, scan-line, blobs, marquees")
print("  [8] will-change: dynamic add/remove on 3D tilt cards (mouseenter/mouseleave)")
print("  [9] will-change: scroll progress bar pre-hinted")
print(" [10] Reduced Motion: comprehensive disable for all heavy effects (CSS)")
print(" [11] Reduced Motion: JS boot() skips tilt, spotlight, blob, scan for reduced-motion users")
