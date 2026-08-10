import os

from openai import OpenAI


class LLM:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.environ["OPENROUTER_API_KEY"],
            base_url="https://openrouter.ai/api/v1",
        )

    def generate(self, prompt: str) -> dict:
        response = self.client.chat.completions.create(
            model="openrouter/free",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return {
            "answer": response.choices[0].message.content,
            "model": response.model,
        }
