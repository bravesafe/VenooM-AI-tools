import os

prompt = os.environ.get("prompt", "a futuristic city with flying cars")
duration = os.environ.get("duration", "4")

os.chdir("Text2Video-Zero")
os.system(f"python inference.py --prompt \"{prompt}\" --duration {duration} --output ../VenooM-AI/outputs/text2video")