import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
SOCIAL_WEBHOOK_URL = os.getenv("SOCIAL_WEBHOOK_URL")


def validate_config():
    required = {
        "AZURE_OPENAI_API_KEY": AZURE_OPENAI_API_KEY,
        "AZURE_OPENAI_ENDPOINT": AZURE_OPENAI_ENDPOINT,
        "AZURE_OPENAI_API_VERSION": AZURE_OPENAI_API_VERSION,
        "AZURE_OPENAI_DEPLOYMENT": AZURE_OPENAI_DEPLOYMENT,
    }

    missing = [
        key
        for key, value in required.items()
        if not value
    ]

    if missing:
        raise RuntimeError(
            f"Missing required environment variables: {', '.join(missing)}"
        )


def print_config_status():
    print("\nConfiguration")
    print("-" * 40)
    print("AZURE_OPENAI_API_KEY:", bool(AZURE_OPENAI_API_KEY))
    print("AZURE_OPENAI_ENDPOINT:", bool(AZURE_OPENAI_ENDPOINT))
    print("AZURE_OPENAI_API_VERSION:", bool(AZURE_OPENAI_API_VERSION))
    print("AZURE_OPENAI_DEPLOYMENT:", bool(AZURE_OPENAI_DEPLOYMENT))
    print("SERPER_API_KEY:", bool(SERPER_API_KEY))
    print("SOCIAL_WEBHOOK_URL:", bool(SOCIAL_WEBHOOK_URL))
    print("-" * 40)