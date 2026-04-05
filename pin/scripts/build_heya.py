import os
import sys
import subprocess
from io import BytesIO

try:
    import pygltflib
    from PIL import Image
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygltflib", "pillow", "numpy", "--quiet"])
    import pygltflib
    from PIL import Image
    import numpy as np

def shift_cyan_to_pink(img_bytes):
    img = Image.open(BytesIO(img_bytes)).convert("RGBA")
    # Convert image to HSV
    import colorsys
    
    # We will use numpy to vectorize the hue shift for speed
    data = np.array(img)
    r, g, b, a = data.T
    
    # Convert RGB to HSV
    # Cyan is around Hue=0.5 (180deg). Pink is around Hue=0.83 (300deg)
    # We find pixels that have higher G and B than R, and shift their hue
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            px = data[y, x]
            # Simple heuristic for cyan: G and B are prominent, R is lower
            # Or just shift EVERYTHING that has color
            h, s, v = colorsys.rgb_to_hsv(px[0]/255.0, px[1]/255.0, px[2]/255.0)
            
            # Cyan hue is between 0.45 and 0.55 (160 to 200 degrees)
            # Or broadly blue/cyan: 0.4 to 0.65
            if 0.4 < h < 0.65 and s > 0.1:
                # Shift to Pink (approx 0.85 to 0.9)
                new_h = (h + 0.35) % 1.0 # 180 + 126 = 306 deg
                # convert back
                new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, s, v)
                data[y, x, 0] = int(new_r * 255)
                data[y, x, 1] = int(new_g * 255)
                data[y, x, 2] = int(new_b * 255)
                
    new_img = Image.fromarray(data, "RGBA")
    out_img = BytesIO()
    # check format
    new_img.save(out_img, format="PNG")
    return out_img.getvalue()

def create_heya(input_glb, output_glb):
    print(f"Loading {input_glb}...")
    gltf = pygltflib.GLTF2().load(input_glb)
    
    # GTLF resources are stored in binary blobs in gltf.binary_blob()
    blob = gltf.binary_blob()
    new_blob = bytearray(blob)
    
    for image in gltf.images:
        if image.bufferView is not None:
            bv = gltf.bufferViews[image.bufferView]
            start = bv.byteOffset
            end = start + bv.byteLength
            img_bytes = blob[start:end]
            
            print(f"Found embedded texture. Shifting colors...")
            new_img_bytes = shift_cyan_to_pink(img_bytes)
            
            # Since the new png might be a different size, we cannot just inject it into the same blob easily.
            # Instead, we set the image uri to a relative path and clear bufferView, OR we reconstruct the blob.
            # Easiest way in pygltflib: set uri to a base64 data URI!
            import base64
            b64_data = base64.b64encode(new_img_bytes).decode('ascii')
            image.uri = f"data:image/png;base64,{b64_data}"
            image.bufferView = None
            
    print(f"Saving {output_glb}...")
    gltf.save(output_glb)
    print("Done!")

os.makedirs('hey_bot_gallery', exist_ok=True)
os.makedirs('hey_bot_gallery/models', exist_ok=True)

# Copy original "Hey" models to the gallery
import shutil
shutil.copy2(r'assets\models\Meshy_AI_biped\Meshy_AI_Animation_Idle_withSkin.glb', r'hey_bot_gallery\models\hey_idle.glb')
shutil.copy2(r'assets\models\sitting\Meshy_AI_Animation_Sit_and_Doze_Off_withSkin.glb', r'hey_bot_gallery\models\hey_sitting.glb')

# Convert
create_heya(r'hey_bot_gallery\models\hey_idle.glb', r'hey_bot_gallery\models\heya_idle.glb')
create_heya(r'hey_bot_gallery\models\hey_sitting.glb', r'hey_bot_gallery\models\heya_sitting.glb')
