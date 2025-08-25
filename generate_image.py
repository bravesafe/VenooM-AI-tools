import os

prompt = os.environ.get("prompt", "a futuristic city with flying cars")
steps = os.environ.get("steps", "30")

os.chdir("stable-diffusion")
os.system(f"python scripts/txt2img.py --prompt \"{prompt}\" --steps {steps} --outdir ../VenooM-AI/outputs/image")