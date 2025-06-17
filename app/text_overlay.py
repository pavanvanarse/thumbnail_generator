import httpx
from PIL import Image, ImageDraw, ImageFont
import io
import base64

async def overlay_title(image_url: str, title: str) -> str:
    """
    Downloads an image, overlays text, and returns a base64 encoded PNG.
    """
    try:
        # Download the image
        async with httpx.AsyncClient() as client:
            response = await client.get(image_url)
        response.raise_for_status()
        image_bytes = response.content
        img = Image.open(io.BytesIO(image_bytes)).convert("RGBA")

        # Prepare to draw
        draw = ImageDraw.Draw(img)

        # Attempt to load a font, fall back to default if not found
        try:
            font = ImageFont.truetype("arial.ttf", 60)
        except IOError:
            try:
                # Try a common alternative path for fonts on Linux
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
            except IOError:
                # Fallback to PIL default font if specific fonts are not available
                font = ImageFont.load_default()

        text_position = (30, 30)  # Top-left with some padding
        text_color_fill = (255, 255, 255, 255)  # White
        shadow_color = (0, 0, 0, 255)  # Black

        # Shadow effect (draw text multiple times with slight offsets)
        shadow_offset = 2
        for x_offset in [-shadow_offset, 0, shadow_offset]:
            for y_offset in [-shadow_offset, 0, shadow_offset]:
                if x_offset != 0 or y_offset != 0: # don't draw center for shadow
                     draw.text((text_position[0] + x_offset, text_position[1] + y_offset), title, font=font, fill=shadow_color)

        # Main text
        draw.text(text_position, title, font=font, fill=text_color_fill)

        # Save image to a bytes buffer as PNG
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")

        # Encode to base64
        img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return img_base64

    except httpx.HTTPStatusError as e:
        # Re-raise HTTP errors to be caught by the main app
        raise Exception(f"Error downloading image: {e.response.status_code} - {e.response.text}")
    except Exception as e:
        # Catch any other errors during image processing
        raise Exception(f"Error processing image or overlaying text: {str(e)}")

if __name__ == '__main__':
    # Example Usage (for testing this module directly)
    # This part will not run when imported by FastAPI, but can be useful for standalone testing.
    # You would need a live image URL to test this.
    # For example:
    # test_image_url = "https://via.placeholder.com/1280x720.png?text=Sample+Image"
    # test_title = "My Awesome Title!"
    # try:
    #     base64_image = overlay_title(test_image_url, test_title)
    #     print("Base64 Image String (first 100 chars):", base64_image[:100])
    #     # To save the image locally for verification:
    #     # with open("test_overlay_output.png", "wb") as f:
    #     #     f.write(base64.b64decode(base64_image))
    #     # print("Test image saved to test_overlay_output.png")
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    pass
