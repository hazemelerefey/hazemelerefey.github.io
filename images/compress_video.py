import sys
import subprocess
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

cmd = [
    ffmpeg_exe, "-y", "-i", "banner.mp4",
    # Scale down to standard 720p web-friendly height
    "-vf", "scale=-2:720",
    # Compress effectively
    "-c:v", "libx264", "-crf", "28", "-preset", "veryfast",
    # No audio needed for background banner
    "-an",
    # CRITICAL: Shifts metadata to the front so the video plays instantly before fully downloading
    "-movflags", "+faststart",
    "banner_opt.mp4"
]

print("Compressing video for web playback...")
subprocess.check_call(cmd)
print("Compression complete!")
