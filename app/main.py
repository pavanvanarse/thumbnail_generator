import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .stability_client import generate_image
from .text_overlay import overlay_title # Ensure this is not commented out

app = FastAPI(title="AI Thumbnail Generator")

class Prompt(BaseModel):
    title: str
    overlay: bool = False

@app.post("/generate-thumbnail/")
async def generate_thumbnail(data: Prompt):
    # It's good practice to ensure the API key is available early.
    if not os.getenv("STABILITY_API_KEY"):
        raise HTTPException(status_code=500, detail="STABILITY_API_KEY not set.")

    # The prompt for Stability AI can be simpler, let the model handle the creative details.
    # The API expects just the core concept.
    # The v2beta core model is good at interpreting "16:9 aspect ratio" directly in the prompt if needed,
    # but aspect_ratio is also a parameter in stability_client.py
    prompt_for_stability = data.title # Simplified prompt

    try:
        # generate_image function in stability_client.py already sets aspect_ratio="16:9"
        image_url = await generate_image(prompt_for_stability)

        if data.overlay:
            # Call overlay_title with the image_url and data.title
            img_base64 = await overlay_title(image_url, data.title) # Made async
            return {"title": data.title, "prompt_sent_to_stability": prompt_for_stability, "image_base64": img_base64}

        return {"title": data.title, "prompt_sent_to_stability": prompt_for_stability, "image_url": image_url}
    except HTTPException as e: # Re-raise HTTPExceptions directly
        raise e
    except Exception as e:
        # Catch-all for other exceptions, including those from generate_image or overlay_title
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.get("/")
def root():
    return {"status": "running"} # Changed this line
