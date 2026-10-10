import os
import logging
from pathlib import Path
from dotenv import load_dotenv

from PIL import Image
from google import genai
from google.genai import types

from app.models import BlueprintInspection
from app.prompts import PROMPT

# Load .env from backend folder or current directory
env_path = Path(__file__).resolve().parent.parent / ".env"
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
load_dotenv()

logger = logging.getLogger(__name__)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def analyze_blueprint(image_path: str) -> BlueprintInspection:
    image = Image.open(image_path)

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=[PROMPT, image],
        config=types.GenerateContentConfig(
            temperature=0.2,
            response_mime_type="application/json",
            response_schema=BlueprintInspection
        )
    )

    if response.parsed is None:
        logger.error("Gemini returned unparseable response: %s", response.text)
        raise ValueError(f"Gemini did not return a valid response. Raw text: {response.text[:500]}")

    return response.parsed