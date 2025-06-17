# AI Thumbnail Generator (FastAPI + Stability AI)

Generate catchy YouTube thumbnails from plain‑text titles.

## Quick Start on Replit

1. **Fork / import** this repo into your Replit workspace.
2. Add a secret named `STABILITY_API_KEY` under **Secrets** ➜ **Environment Variables**.
3. Run!  Replit will install the packages and launch `uvicorn`.
4. Open `/docs` to test in Swagger UI.

## Endpoints

| Method | Path                     | Body             | Response                         |
|--------|--------------------------|------------------|----------------------------------|
| POST   | `/generate-thumbnail/`   | `{ "title": "Your text", "overlay": false }` | Image URL or base64‑encoded PNG |

Use the `overlay` flag to burn your title text onto the image (requires `pillow`).

---

Built with **FastAPI + Stability AI**.  Happy creating! ✨
