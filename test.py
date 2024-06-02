import os
from dotenv import load_dotenv
from openai import OpenAI
import base64

from utils import bcolors


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    assert (
        api_key is not None
    ), "Please set OPENAI_API_KEY in your environment variables"

    client = OpenAI(api_key=api_key)

    image_path = "sapien_0.png"

    base64_image = encode_image(image_path)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What's in this image?",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    print(f"{bcolors.OKCYAN}{response.choices[0].message.content}{bcolors.ENDC}")


if __name__ == "__main__":
    main()
