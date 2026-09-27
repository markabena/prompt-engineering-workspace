from dotenv import load_dotenv
import os
import anthropic

from config import DEFAULT_MODEL


def main():
    load_dotenv()

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set in .env")

    client = anthropic.Anthropic(api_key=api_key)

    system_prompt = "You are a helpful assistant."

    messages = [
        {
            "role": "user",
            "content": "Write a short, friendly greeting and summarize what this prompt engineering workspace is for.",
        },
    ]

    response = client.messages.create(
        model=DEFAULT_MODEL,
        system=system_prompt,
        messages=messages,
        max_tokens=200,
        temperature=0.7,
    )

    print("--- Anthropic response ---")
    try:
        if hasattr(response, "content"):
            print(response.content[0].text)
        elif isinstance(response, dict) and "completion" in response:
            print(response["completion"])
        else:
            print(response)
    except Exception:
        print(response)


if __name__ == "__main__":
    main()
