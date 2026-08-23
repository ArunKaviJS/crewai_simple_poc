import os
from pathlib import Path
from typing import Optional

import requests


def publish_to_webhook(
    text: str,
    image_path: Optional[str] = None
) -> str:

    webhook_url = os.getenv("SOCIAL_WEBHOOK_URL")

    if not webhook_url:
        raise ValueError(
            "SOCIAL_WEBHOOK_URL is not configured."
        )

    if image_path:
        image_file = Path(image_path)

        if not image_file.exists():
            raise FileNotFoundError(
                f"Image not found: {image_file}"
            )

        with image_file.open("rb") as handle:

            response = requests.post(
                webhook_url,
                data={"text": text},
                files={"image": handle},
                timeout=60,
            )

    else:

        response = requests.post(
            webhook_url,
            data={"text": text},
            timeout=60,
        )

    response.raise_for_status()

    return (
        f"Webhook accepted with "
        f"status code {response.status_code}."
    )