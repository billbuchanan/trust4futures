from diffusers import StableDiffusionPipeline
import torch

model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.to("mps")  # "mps" enables Apple Metal support for fast generation

prompt = "Portrait photo of cyber security professional"
image = pipe(prompt).images[0]
image.show()
