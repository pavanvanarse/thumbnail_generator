import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .stability_client import generate_image
from .text_overlay import overlay_title  # optional

app = FastAPI(title="AI Thumbnail Generator")

class Prompt(BaseModel):
    title: str
    overlay: bool = False  # if true, embed the title text on top and return base64

@app.post("/generate-thumbnail/")
async def generate_thumbnail(data: Prompt):
    prompt = (f"Create a vibrant, cinematic YouTube thumbnail, 16:9 aspect ratio, "
              f"eye‑catching text layout, inspired by: '{data.title}'")

    try:
        url = await generate_image(prompt)
        if data.overlay:
            img_b64 = overlay_title(url, data.title)
            return {"title": data.title, "prompt": prompt, "image_base64": img_b64}
        return {"title": data.title, "prompt": prompt, "image_url": url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"status": "Thumbnail generator is running!"}
