css_code = """
/* ═══════════════════ ACETERNITY NOISE CARDS ═══════════════════ */
.noise-card-wrapper {
    position: relative;
    overflow: hidden;
    border-radius: 1rem; 
    background-color: #15151D; 
    padding: 0.25rem; 
    box-shadow: inset 0px 1px 0px 0px rgba(255, 255, 255, 0.05), inset 0px 0px 10px rgba(0,0,0,0.5);
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    cursor: pointer;
}
.noise-card-wrapper:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5), 0 0 20px rgba(236,72,153,0.1);
}

.noise-layer {
    position: absolute;
    inset: -50%;
    pointer-events: none;
    z-index: 0;
}

/* Gradients that mimic framer-motion random motion */
.noise-gradient-1 {
    background: radial-gradient(circle at 50% 50%, rgba(255, 100, 150, 0.6) 0%, transparent 50%);
    animation: drift 15s ease-in-out infinite alternate;
}
.noise-gradient-2 {
    background: radial-gradient(circle at 30% 70%, rgba(100, 150, 255, 0.5) 0%, transparent 50%);
    animation: drift 23s ease-in-out infinite alternate-reverse;
}
.noise-gradient-3 {
    background: radial-gradient(circle at 70% 30%, rgba(255, 200, 100, 0.45) 0%, transparent 50%);
    animation: drift 19s ease-in-out infinite alternate;
}

@keyframes drift {
    0% { transform: translate(0, 0) scale(1); }
    33% { transform: translate(15%, -15%) scale(1.1); }
    66% { transform: translate(-10%, 20%) scale(0.9); }
    100% { transform: translate(-20%, -10%) scale(1.05); }
}

.noise-strip {
    position: absolute;
    left: 0; right: 0; top: 0;
    height: 4px;
    background: linear-gradient(to right, rgb(255, 100, 150), rgb(100, 150, 255), rgb(255, 200, 100));
    opacity: 0.8;
    filter: blur(3px);
    z-index: 1;
    animation: pulse 4s ease-in-out infinite;
}

.noise-overlay {
    position: absolute;
    inset: 0;
    background-image: url('https://assets.aceternity.com/noise.webp');
    background-size: cover;
    mix-blend-mode: overlay;
    opacity: 0.4;
    z-index: 2;
    pointer-events: none;
}

.noise-card-inner {
    position: relative;
    z-index: 10;
    background-color: #0A0A0F;
    height: 100%;
    display: flex;
    flex-direction: column;
    border-radius: 0.75rem; 
    overflow: hidden;
    text-align: left;
    border: 1px solid rgba(255, 255, 255, 0.05);
    transition: background-color 0.4s ease;
}
.noise-card-wrapper:hover .noise-card-inner {
    background-color: rgba(10, 10, 15, 0.9);
}
"""

with open(r"d:\hazemelerefy website\my website\css\style.css", "a", encoding="utf-8") as f:
    f.write("\n\n" + css_code + "\n")
print("CSS injected successfully!")
