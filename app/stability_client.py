import os, httpx

STABILITY_URL = "https://api.stability.ai/v2beta/stable-image/generate/core"
API_KEY = os.getenv("STABILITY_API_KEY")

async def generate_image(prompt: str, aspect_ratio: str = "16:9") -> str:
    """
    Calls Stability AI and returns a hosted image URL.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {"prompt": prompt, "aspect_ratio": aspect_ratio, "output_format": "url"}

    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(STABILITY_URL, headers=headers, json=payload)
        r.raise_for_status()
        return r.json()["image"]
