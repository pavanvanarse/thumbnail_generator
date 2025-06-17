# AI Thumbnail Generator (FastAPI + Stability AI)

Generate catchy YouTube thumbnails from plain-text titles using Stability AI. This FastAPI application provides an endpoint to generate images and optionally overlay text on them.

## Features

- Generate images from text prompts using Stability AI (v2beta, core model).
- Aspect ratio fixed at 16:9.
- Option to overlay the input title text onto the generated image.
- Returns image URL or base64-encoded PNG if text overlay is applied.
- Swagger UI for easy API testing.

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py             # FastAPI app, endpoints
│   ├── stability_client.py # Client for Stability AI API
│   └── text_overlay.py     # Image manipulation for text overlay
├── .env.example            # Example environment variables
├── requirements.txt        # Python dependencies
└── README.md
```

## Setup and Running

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create and activate a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    *   Copy `.env.example` to a new file named `.env`:
        ```bash
        cp .env.example .env
        ```
    *   Open the `.env` file and add your Stability AI API key:
        ```
        STABILITY_API_KEY=your_actual_stability_api_key
        ```

5.  **Run the application using Uvicorn:**
    ```bash
    uvicorn app.main:app --reload
    ```
    The application will typically be available at `http://127.0.0.1:8000`.

## API Endpoints

### Root

-   **GET /**
    -   **Description:** Returns the status of the application.
    -   **Response (200 OK):**
        ```json
        {
          "status": "running"
        }
        ```

### Generate Thumbnail

-   **POST /generate-thumbnail/**
    -   **Description:** Generates an image based on the provided title. Can optionally overlay the title on the image.
    -   **Request Body (JSON):**
        ```json
        {
          "title": "string",
          "overlay": "boolean (optional, default: false)"
        }
        ```
        -   `title` (str, required): The text prompt for the thumbnail.
        -   `overlay` (bool, optional): If `true`, the title text will be overlaid on the generated image, and the image will be returned as a base64-encoded PNG. If `false` (default), the URL of the generated image is returned.
    -   **Response (200 OK):**
        -   If `overlay` is `false`:
            ```json
            {
              "title": "Your Input Title",
              "prompt_sent_to_stability": "Your Input Title",
              "image_url": "url_to_generated_image.png"
            }
            ```
        -   If `overlay` is `true`:
            ```json
            {
              "title": "Your Input Title",
              "prompt_sent_to_stability": "Your Input Title",
              "image_base64": "base64_encoded_png_string"
            }
            ```
    -   **Response (500 Internal Server Error):**
        If an error occurs during image generation or processing.
        ```json
        {
          "detail": "Error message"
        }
        ```

## Swagger UI

API documentation and testing interface is available at `/docs` when the application is running. (e.g., `http://127.0.0.1:8000/docs`)

---

Happy creating! ✨