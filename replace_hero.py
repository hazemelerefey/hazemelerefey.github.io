import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    text = f.read()

# Find the portfolio hero section
start_marker = '<!-- Hero Section -->\r\n            <header id="portfolio-hero"'
end_marker = '</header>\r\n\r\n            <!-- PREMIUM ABOUT ME'

idx_start = text.find(start_marker)
idx_end = text.find(end_marker)

if idx_start == -1:
    # Try without \r\n
    start_marker = '<!-- Hero Section -->\n            <header id="portfolio-hero"'
    idx_start = text.find(start_marker)

if idx_end == -1:
    end_marker = '</header>\n\n            <!-- PREMIUM ABOUT ME'
    idx_end = text.find(end_marker)

new_hero = """<!-- Hero Section -->
            <header id="portfolio-hero"
                class="relative min-h-[85vh] pt-40 pb-24 md:pt-48 md:pb-32 flex flex-col items-center justify-center text-center px-6 overflow-hidden">

                <!-- ================================================ -->
                <!-- PREMIUM CODED BACKGROUND                        -->
                <!-- ================================================ -->
                <div class="absolute inset-0 z-0 overflow-hidden pointer-events-none">
                    <!-- Base gradient -->
                    <div class="absolute inset-0 bg-gradient-to-br from-[#030014] via-[#0a0a1a] to-[#030014]"></div>

                    <!-- Animated grid lines -->
                    <div class="absolute inset-0 opacity-[0.04]" style="background-image: linear-gradient(rgba(6,182,212,0.3) 1px, transparent 1px), linear-gradient(90deg, rgba(6,182,212,0.3) 1px, transparent 1px); background-size: 60px 60px;"></div>
                    
                    <!-- Floating orbital glows -->
                    <div class="absolute top-[15%] left-[20%] w-[500px] h-[500px] bg-cyan-500/8 rounded-full blur-[150px] animate-pulse" style="animation-duration: 6s;"></div>
                    <div class="absolute bottom-[10%] right-[15%] w-[400px] h-[400px] bg-pink-500/8 rounded-full blur-[120px] animate-pulse" style="animation-duration: 8s;"></div>
                    <div class="absolute top-[50%] left-[60%] w-[300px] h-[300px] bg-purple-500/5 rounded-full blur-[100px] animate-pulse" style="animation-duration: 10s;"></div>

                    <!-- Diagonal accent lines -->
                    <div class="absolute top-0 left-0 w-full h-full overflow-hidden">
                        <div class="absolute -top-[50%] -left-[10%] w-[1px] h-[200%] bg-gradient-to-b from-transparent via-cyan-500/20 to-transparent rotate-[25deg]"></div>
                        <div class="absolute -top-[50%] left-[30%] w-[1px] h-[200%] bg-gradient-to-b from-transparent via-pink-500/10 to-transparent rotate-[25deg]"></div>
                        <div class="absolute -top-[50%] right-[20%] w-[1px] h-[200%] bg-gradient-to-b from-transparent via-purple-500/10 to-transparent rotate-[25deg]"></div>
                    </div>

                    <!-- Code rain decoration (static CSS dots) -->
                    <div class="absolute inset-0 opacity-[0.03]" style="background-image: radial-gradient(circle, rgba(255,255,255,0.8) 1px, transparent 1px); background-size: 30px 30px;"></div>

                    <!-- Top/Bottom fade to maintain clean transitions -->
                    <div class="absolute inset-x-0 top-0 h-32 bg-gradient-to-b from-[#030014] to-transparent"></div>
                    <div class="absolute inset-x-0 bottom-0 h-40 bg-gradient-to-t from-darkBase via-darkBase/90 to-transparent"></div>
                </div>

                <!-- ================================================ -->
                <!-- HERO CONTENT                                     -->
                <!-- ================================================ -->
                <div class="relative z-10 max-w-6xl mx-auto flex flex-col md:flex-row items-center gap-12 md:gap-16">
                    
                    <!-- Profile Picture Column -->
                    <div data-aos="fade-right" data-aos-duration="1200" class="md:w-[38%] flex justify-center order-2 md:order-1">
                        <div class="relative group cursor-pointer">
                            <!-- Outer glow ring -->
                            <div class="absolute -inset-3 bg-gradient-to-tr from-cyan-500 via-purple-500 to-pink-500 rounded-3xl opacity-30 blur-xl group-hover:opacity-60 transition-opacity duration-700"></div>
                            
                            <!-- Photo container -->
                            <div class="relative w-64 h-80 md:w-72 md:h-[22rem] rounded-2xl p-[3px] bg-gradient-to-tr from-cyan-500 via-purple-500 to-pink-500 shadow-2xl group-hover:shadow-[0_0_60px_rgba(168,85,247,0.4)] transition-shadow duration-700">
                                <img src="images/profile.jpg" alt="Hazem Khaled Ezat - Data Analyst"
                                    class="w-full h-full object-cover rounded-[13px] grayscale-[20%] group-hover:grayscale-0 transition-all duration-700">
                            </div>
                            
                            <!-- Floating status badge -->
                            <div class="absolute -bottom-4 left-1/2 -translate-x-1/2 bg-[#0a0a1a]/90 backdrop-blur-xl border border-white/10 px-5 py-2 rounded-full flex items-center gap-2 shadow-[0_10px_30px_rgba(0,0,0,0.5)]">
                                <div class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse shadow-[0_0_8px_rgba(52,211,153,0.6)]"></div>
                                <span class="text-white/80 text-xs font-bold tracking-wider uppercase">Available for hire</span>
                            </div>
                        </div>
                    </div>

                    <!-- Text Column -->
                    <div class="md:w-[62%] text-center md:text-left order-1 md:order-2 flex flex-col items-center md:items-start">

                        <!-- Intro Label -->
                        <div data-aos="fade-up" data-aos-duration="1000" class="mb-5">
                            <span class="inline-flex items-center gap-2 uppercase tracking-[0.2em] text-cyan-400 text-[11px] font-bold bg-cyan-500/10 px-5 py-2.5 rounded-full border border-cyan-500/20 shadow-[0_0_20px_rgba(6,182,212,0.1)]">
                                <i class="fas fa-chart-line text-[10px]"></i>
                                Data Analyst
                                <span class="w-1 h-1 rounded-full bg-white/30"></span>
                                Frontend Background
                            </span>
                        </div>

                        <!-- Main Headline -->
                        <h1 data-aos="fade-up" data-aos-duration="1000" data-aos-delay="100"
                            class="text-4xl md:text-6xl lg:text-7xl font-black text-white mb-5 leading-[1.1] tracking-tight">
                            Hazem <br/><span class="text-gradient-cyan-pink">Khaled Ezat</span>
                        </h1>

                        <!-- Tagline -->
                        <p data-aos="fade-up" data-aos-duration="1000" data-aos-delay="200" class="text-lg md:text-xl text-white/50 max-w-xl leading-relaxed mb-8 font-light">
                            Translating complex data into <strong class="text-white/80 font-semibold">pixel-perfect dashboards</strong> and premium digital experiences.
                        </p>

                        <!-- CTA Row -->
                        <div data-aos="fade-up" data-aos-duration="1000" data-aos-delay="300"
                            class="flex flex-col sm:flex-row gap-4 mt-2">
                            <!-- Download CV -->
                            <a href="assets/Hazemelerefy CV.pdf" download="Hazemelerefy_CV.pdf" @click.prevent="
                            fetch($el.href)
                                .then(res => res.blob())
                                .then(blob => {
                                    const url = window.URL.createObjectURL(blob);
                                    const a = document.createElement('a');
                                    a.style.display = 'none';
                                    a.href = url;
                                    a.download = $el.getAttribute('download');
                                    document.body.appendChild(a);
                                    a.click();
                                    window.URL.revokeObjectURL(url);
                                })
                                .catch(() => window.open($el.href, '_blank'));
                        " class="btn-pill relative group shadow-[0_0_30px_rgba(6,182,212,0.3)] hover:shadow-[0_0_50px_rgba(236,72,153,0.5)] !bg-gradient-to-r from-pink-500 to-cyan-500 !text-white border-none transition-all duration-300 cursor-pointer">
                                <span class="relative z-10 flex items-center font-bold tracking-wide">
                                    <i class="fas fa-file-download mr-2 text-lg"></i> Download CV
                                </span>
                                <div class="absolute inset-0 bg-white opacity-0 group-hover:opacity-20 transition-opacity rounded-full"></div>
                            </a>
                            <!-- Contact + Socials -->
                            <div class="flex items-center gap-3">
                                <a href="#contact"
                                    class="btn-pill !bg-white/5 backdrop-blur-md !text-white !border-white/10 hover:!border-white/30 hover:!bg-white/10 transition-all duration-300 cursor-pointer">
                                    Contact Me
                                </a>
                                <a href="https://github.com/hazemelerefey" target="_blank" rel="noopener noreferrer" aria-label="GitHub"
                                    class="w-[48px] h-[48px] rounded-full border border-white/10 bg-white/5 backdrop-blur-md flex items-center justify-center text-white/50 hover:text-white hover:border-white/30 hover:bg-white/10 transition-all duration-300 cursor-pointer">
                                    <i class="fab fa-github text-xl"></i>
                                </a>
                                <a href="https://www.linkedin.com/in/hazemelerefy" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn"
                                    class="w-[48px] h-[48px] rounded-full border border-white/10 bg-white/5 backdrop-blur-md flex items-center justify-center text-white/50 hover:text-[#0A66C2] hover:border-[#0A66C2]/50 hover:bg-[#0A66C2]/10 transition-all duration-300 cursor-pointer">
                                    <i class="fab fa-linkedin-in text-lg"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </header>

            """

if idx_start != -1 and idx_end != -1:
    # idx_end points to start of '</header>', we need to skip past </header>\r\n\r\n
    # Actually idx_end includes '</header>\r\n\r\n            ', we want to cut up to just before '<!-- PREMIUM ABOUT ME'
    text = text[:idx_start] + new_hero + text[idx_end + len(end_marker) - len('<!-- PREMIUM ABOUT ME'):]
    with codecs.open('index.html', 'w', 'utf-8') as f:
        f.write(text)
    print("SUCCESS")
else:
    print("FAIL: start=", idx_start, "end=", idx_end)
    # Debug: show what's around the markers
    if idx_start == -1:
        # Find portfolio-hero at all
        test = text.find('portfolio-hero')
        print("portfolio-hero found at:", test)
        if test != -1:
            print("Context:", repr(text[test-80:test+80]))
    if idx_end == -1:
        test2 = text.find('PREMIUM ABOUT ME')
        print("PREMIUM ABOUT ME found at:", test2)
        if test2 != -1:
            print("Context:", repr(text[test2-80:test2+80]))
