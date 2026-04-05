import sys
import subprocess

try:
    import imageio_ffmpeg
except ImportError:
    print("Installing imageio-ffmpeg...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "imageio-ffmpeg", "--quiet"])
    import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
print(f"Found ffmpeg at: {ffmpeg_exe}")

cmd = [
    ffmpeg_exe, "-y", "-i", "banner.mp4",
    "-vf", "fps=15,scale=1000:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse",
    "-loop", "0", "banner.gif"
]

print("Running FFmpeg conversion...")
subprocess.check_call(cmd)
print("Conversion successful!")
