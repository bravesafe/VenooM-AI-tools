import os

prompt = os.environ.get("prompt", "a futuristic city with flying cars")
steps = os.environ.get("steps", "30")

os.chdir("AnimateDiff")
os.system(f"python scripts/run_animatediff.py --prompt \"{prompt}\" --steps {steps} --output ../VenooM-AI/outputs/animated")