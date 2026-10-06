import os
import json
import anthropic
from dotenv import load_dotenv
from datetime import datetime, timezone

from config import DEFAULT_MODEL

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise SystemExit("ANTHROPIC_API_KEY is missing. Add it to the .env file in the repo root.")

client = anthropic.Anthropic(api_key=api_key)

def load_prompt(filepath: str) -> str:
    """Load a prompt template from file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read().strip()

def run_prompt(system_prompt: str, user_message: str, model: str = DEFAULT_MODEL, max_tokens: int = 1024) -> dict:
    """Send a prompt to Claude and return structured output."""
    try:
        response = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )
    except anthropic.AuthenticationError:
        print("ERROR 401: API key rejected. Check ANTHROPIC_API_KEY in .env.")
        return None
    except anthropic.NotFoundError:
        print(f"ERROR 404: Model '{model}' not found or retired. Update DEFAULT_MODEL in config.py.")
        return None
    except anthropic.RateLimitError:
        print("ERROR 429: Rate limit hit. Wait a moment and try again.")
        return None
    except anthropic.APIConnectionError:
        print("ERROR: Could not reach the API. Check your internet connection.")
        return None
    except anthropic.APIStatusError as e:
        print(f"ERROR {e.status_code}: {e.message}")
        return None

    # Collect the text from EVERY text block, not just the first one
    text = "".join(block.text for block in response.content if block.type == "text")

    # Read the delivery note: was the answer cut off?
    if response.stop_reason == "max_tokens":
        print(f"WARNING: response hit the {max_tokens}-token limit and is incomplete.")

    return {
        "model": model,
        "system_prompt_preview": system_prompt[:80] + "...",
        "user_message": user_message,
        "response": text,
        "stop_reason": response.stop_reason,
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

def save_result(result: dict, output_dir: str = "results") -> str:
    """Save result to a timestamped file."""
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{output_dir}/result_{result['timestamp'].replace(':', '-')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for key, value in result.items():
            f.write(f"{key}: {value}\n")
    return filename

def save_result_json(result: dict, output_dir: str = "results") -> str:
    """Save result as JSON."""
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{output_dir}/result_{result['timestamp'].replace(':', '-')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    return filename

# --- Run ---
if __name__ == "__main__":
    system = load_prompt("prompts/system/general_assistant.txt")
    user = "What are the three most important habits for staying productive?"

    print("Running pipeline...\n")
    result = run_prompt(system, user)
    if result is None:
        raise SystemExit(1)

    print(f"Response:\n{result['response']}")
    print(f"\nTokens used: {result['input_tokens']} in / {result['output_tokens']} out")

    saved = save_result(result)
    print(f"\nResult saved to: {saved}")
