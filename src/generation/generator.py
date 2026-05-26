import os
import requests
import time

from dotenv import load_dotenv


class Generator:

    def __init__(self):

        # =====================================
        # Load Environment Variables
        # =====================================

        load_dotenv()

        self.api_key = os.getenv(
            "GROQ_API_KEY"
        )

        # =====================================
        # API Configuration
        # =====================================

        self.url = (
            "https://api.groq.com/openai/v1/chat/completions"
        )

        self.model = (
            "llama-3.1-8b-instant"
        )

        print(
            "✅ Generator initialized"
        )

    # =====================================
    # Generate Response
    # =====================================

    def generate(

        self,

        prompt
    ):

        # =====================================
        # Empty Prompt Protection
        # =====================================

        if prompt is None:

            return (
                "No prompt provided."
            )

        # =====================================
        # Headers
        # =====================================

        headers = {

            "Authorization":
            f"Bearer {self.api_key}",

            "Content-Type":
            "application/json"
        }

        # =====================================
        # Request Payload
        # =====================================

        payload = {

            "model": self.model,

            "messages": [

                {

                    "role": "system",

                    "content": (
                        "You are a grounded "
                        "enterprise AI assistant."
                    )
                },

                {

                    "role": "user",

                    "content": prompt
                }
            ],

            "temperature": 0.1,

            "top_p": 0.9,

            "max_tokens": 700
        }

        # =====================================
        # API Request
        # =====================================

        try:

            response = requests.post(

                self.url,

                headers=headers,

                json=payload,

                timeout=60
            )

            response.raise_for_status()

            result = response.json()

            generated_answer = (

                result["choices"][0]
                ["message"]["content"]
            )

            print(
                "✅ Response generated"
            )

            return generated_answer

        # =====================================
        # Error Handling
        # =====================================

        except Exception as error:

            return (
                f"Generation Error: {error}"
            )