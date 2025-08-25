import os

# Stable Diffusion
os.system("git clone https://github.com/CompVis/stable-diffusion.git")
os.system("pip install -r stable-diffusion/requirements.txt")

# AnimateDiff
os.system("git clone https://github.com/guoyww/AnimateDiff.git")
os.system("pip install -r AnimateDiff/requirements.txt")

# FramePack
os.system("git clone https://github.com/VolgaNaut/FramePack.git")
os.system("pip install -r FramePack/requirements.txt")

# Text2Video-Zero
os.system("git clone https://github.com/Picsart-AI-Research/Text2Video-Zero.git")
os.system("pip install -r Text2Video-Zero/requirements.txt")