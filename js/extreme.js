/**
 * ╔══════════════════════════════════════════════════════════════╗
 * ║       HAZEM PORTFOLIO — EXTREME UI/UX ENGINE v1.0           ║
 * ║  Custom Cursor · Mouse Spotlight · 3D Tilt Cards            ║
 * ║  Scroll Reveal · Skill Bars · Counter Animation             ║
 * ╚══════════════════════════════════════════════════════════════╝
 */

(function () {
  'use strict';

  /* ─── 1. INJECT DOM ELEMENTS ─────────────────────────────────── */
  function injectElements() {
    // Spotlight div
    const spotlight = document.createElement('div');
    spotlight.id = 'spotlight';
    document.body.prepend(spotlight);

    // Custom cursor elements
    const dot = document.createElement('div');
    dot.id = 'cursor-dot';
    const ring = document.createElement('div');
    ring.id = 'cursor-ring';
    document.body.appendChild(dot);
    document.body.appendChild(ring);

    // Ambient grid bg class on body
    document.body.classList.add('extreme-grid-bg');
  }

  /* ─── 2. CUSTOM CURSOR ─────────────────────────────────────────── */
  function initCursor() {
    const dot  = document.getElementById('cursor-dot');
    const ring = document.getElementById('cursor-ring');
    if (!dot || !ring) return;

    let mouseX = 0, mouseY = 0;
    let ringX = 0, ringY = 0;
    let rafRunning = false;

    document.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;

      dot.style.left  = mouseX + 'px';
      dot.style.top   = mouseY + 'px';

      if (!rafRunning) {
        rafRunning = true;
        requestAnimationFrame(animateRing);
      }
    });

    function animateRing() {
      ringX += (mouseX - ringX) * 0.12;
      ringY += (mouseY - ringY) * 0.12;
      ring.style.left = ringX + 'px';
      ring.style.top  = ringY + 'px';

      if (Math.abs(mouseX - ringX) > 0.1 || Math.abs(mouseY - ringY) > 0.1) {
        requestAnimationFrame(animateRing);
      } else {
        rafRunning = false;
      }
    }

    // Hover state
    const interactables = 'a, button, [role="button"], input, textarea, select, label, .expertise-card, .project-card-extreme, .glass-extreme, .platform-card, .card-3d';

    document.addEventListener('mouseover', (e) => {
      if (e.target.closest(interactables)) {
        document.body.classList.add('cursor-hover');
      }
    });

    document.addEventListener('mouseout', (e) => {
      if (e.target.closest(interactables)) {
        document.body.classList.remove('cursor-hover');
      }
    });

    // Hide on mouse leave
    document.addEventListener('mouseleave', () => {
      dot.style.opacity  = '0';
      ring.style.opacity = '0';
    });
    document.addEventListener('mouseenter', () => {
      dot.style.opacity  = '1';
      ring.style.opacity = '1';
    });
  }

  /* ─── 3. MOUSE SPOTLIGHT TRACKER ──────────────────────────────── */
  function initSpotlight() {
    const el = document.getElementById('spotlight');
    if (!el) return;

    let ticking = false;
    document.addEventListener('mousemove', (e) => {
      if (!ticking) {
        requestAnimationFrame(() => {
          const x = (e.clientX / window.innerWidth  * 100).toFixed(2) + '%';
          const y = (e.clientY / window.innerHeight * 100).toFixed(2) + '%';
          el.style.setProperty('--mx', x);
          el.style.setProperty('--my', y);
          el.style.background = `radial-gradient(
            600px circle at ${x} ${y},
            rgba(0,245,255,0.045) 0%,
            rgba(0,245,255,0.01) 35%,
            transparent 70%
          )`;
          ticking = false;
        });
        ticking = true;
      }
    });
  }

  /* ─── 4. SCROLL REVEAL (Intersection Observer) ────────────────── */
  function initScrollReveal() {
    const targets = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
    if (!targets.length) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('revealed');
            observer.unobserve(entry.target); // fire once
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );

    targets.forEach((el) => observer.observe(el));
  }

  /* ─── 5. 3D TILT CARDS ─────────────────────────────────────────── */
  function initTiltCards() {
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
  }

  /* ─── 6. CARD SPOTLIGHT HOVER (neon cards) ─────────────────────── */
  function initCardSpotlight() {
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
  }

  /* ─── 7. SKILL BAR ANIMATION ───────────────────────────────────── */
  function initSkillBars() {
    const bars = document.querySelectorAll('.skill-bar-fill');
    if (!bars.length) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('animated');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.3 }
    );

    bars.forEach((b) => observer.observe(b));
  }

  /* ─── 8. COUNT-UP ANIMATION ────────────────────────────────────── */
  function initCounters() {
    const counters = document.querySelectorAll('[data-count]');
    if (!counters.length) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const el     = entry.target;
          const target = parseInt(el.getAttribute('data-count'), 10);
          const suffix = el.getAttribute('data-suffix') || '';
          const duration = 1600;
          let start = null;

          function step(ts) {
            if (!start) start = ts;
            const progress = Math.min((ts - start) / duration, 1);
            const eased    = 1 - Math.pow(1 - progress, 3); // ease-out-cubic
            el.textContent = Math.floor(eased * target) + suffix;
            if (progress < 1) requestAnimationFrame(step);
          }

          requestAnimationFrame(step);
          observer.unobserve(el);
        });
      },
      { threshold: 0.5 }
    );

    counters.forEach((c) => observer.observe(c));
  }

  /* ─── 9. AUTO-APPLY REVEAL CLASSES ─────────────────────────────── */
  function applyRevealClasses() {
    // Section headings
    document.querySelectorAll('section > div > h2, section > div > h1').forEach((el, i) => {
      if (!el.classList.contains('reveal')) {
        el.classList.add('reveal');
      }
    });

    // Card grids — staggered reveal
    document.querySelectorAll('.expertise-card').forEach((card, i) => {
      if (!card.classList.contains('reveal')) {
        card.classList.add('reveal', 'card-3d');
        if (i % 3 === 1) card.classList.add('reveal-delay-2');
        if (i % 3 === 2) card.classList.add('reveal-delay-3');
      }
    });

    // Stats row
    document.querySelectorAll('[class*="stat"]').forEach((el, i) => {
      if (!el.classList.contains('reveal')) {
        el.classList.add('reveal', 'reveal-delay-' + Math.min(i + 1, 6));
      }
    });
  }

  /* ─── 10. MARQUEE PAUSE ON HOVER ───────────────────────────────── */
  function initMarqueePause() {
    document.querySelectorAll('.animate-marquee-left, .animate-marquee-right').forEach((el) => {
      el.parentElement.addEventListener('mouseenter', () => {
        el.style.animationPlayState = 'paused';
      });
      el.parentElement.addEventListener('mouseleave', () => {
        el.style.animationPlayState = 'running';
      });
    });
  }

  /* ─── 11. SCROLL PROGRESS BAR ──────────────────────────────────── */
  function initScrollProgress() {
    const bar = document.createElement('div');
    bar.style.cssText = [
      'position:fixed',
      'top:0', 'left:0',
      'height:2px',
      'width:0%',
      'background:linear-gradient(90deg,#00f5ff,#ff2e97)',
      'z-index:99999',
      'pointer-events:none',
      'box-shadow:0 0 8px rgba(0,245,255,0.6)',
      'transition:width 0.1s linear'
    ].join(';');
    document.body.appendChild(bar);

    window.addEventListener('scroll', () => {
      const total   = document.documentElement.scrollHeight - window.innerHeight;
      const current = window.scrollY;
      bar.style.width = ((current / total) * 100).toFixed(2) + '%';
    }, { passive: true });
  }

  /* ─── 12. KINETIC BLOB PARALLAX ────────────────────────────────── */
  function initBlobParallax() {
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
  }

  /* ─── 13. ADD SCAN LINES TO HERO CARDS ─────────────────────────── */
  function initScanLines() {
    document.querySelectorAll('.expertise-card').forEach((card) => {
      const scan = document.createElement('div');
      scan.className = 'scan-line';
      card.appendChild(scan);
    });
  }

  /* ─── BOOT ──────────────────────────────────────────────────────── */
  function boot() {
    injectElements();
    initCursor();
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

    console.log('%c⚡ EXTREME UI/UX ENGINE LOADED', 'color:#00f5ff;font-weight:900;font-size:14px;text-shadow:0 0 10px #00f5ff;');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }

})();
