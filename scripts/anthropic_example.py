from dotenv import load_dotenv
import os
import anthropic


def main():
    load_dotenv()

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set in .env")

    client = anthropic.Anthropic(api_key=api_key)

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a short, friendly greeting and summarize what this prompt engineering workspace is for.",
        },
    ]

    response = client.messages.create(
        model="claude-3.5-mini",
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
