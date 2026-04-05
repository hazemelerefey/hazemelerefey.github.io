import re

file_path = r'd:\hazemelerefy website\my website\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Make AOS animations twice as fast
html = re.sub(r'data-aos-duration="1000"', 'data-aos-duration="500"', html)
html = re.sub(r'data-aos-duration="800"', 'data-aos-duration="400"', html)

# Make Tailwind duration class variants faster
html = re.sub(r'duration-1000', 'duration-500', html)
html = re.sub(r'duration-700', 'duration-300', html)
html = re.sub(r'duration-500', 'duration-300', html)

# Speed up custom floating keyframes/delays
html = re.sub(r'animation-delay-2000', 'animation-delay-1000', html)
html = re.sub(r'animation-delay-4000', 'animation-delay-2000', html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated animation durations successfully!")
