import os
from dotenv import load_dotenv
import anthropic


def main():
    load_dotenv()

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set in .env")

    client = anthropic.Anthropic(api_key=api_key)

    # Test call using the messages API
    resp = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=256,
        messages=[
            {"role": "user", "content": "Say 'API connection successful' and nothing else."}
        ],
    )

    # Print the assistant reply
    try:
        # Depending on SDK response shape, try common fields
        if hasattr(resp, "content"):
            print(resp.content[0].text)
        elif isinstance(resp, dict) and "completion" in resp:
            print(resp["completion"]["content"][0]["text"])  # fallback
        else:
            print(resp)
    except Exception:
        print(resp)


if __name__ == "__main__":
    main()
