import os
import sys
import subprocess

try:
    import pygltflib
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygltflib", "--quiet"])
    import pygltflib

model_path = r"d:\hazemelerefy website\my website\assets\models\Meshy_AI_biped\Meshy_AI_Animation_Idle_withSkin.glb"
print(f"Loading {model_path}")
gltf = pygltflib.GLTF2().load(model_path)

print("Materials found:")
for i, mat in enumerate(gltf.materials):
    pbr = mat.pbrMetallicRoughness
    color = pbr.baseColorFactor if pbr else "No base color"
    print(f"Index: {i} | Name: {mat.name} | BaseColor: {color}")
