import os
import json
import anthropic
from dotenv import load_dotenv
from datetime import datetime

from config import DEFAULT_MODEL

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def load_prompt(filepath: str) -> str:
    """Load a prompt template from file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read().strip()

def run_prompt(system_prompt: str, user_message: str, model: str = DEFAULT_MODEL, max_tokens: int = 1024) -> dict:
    """Send a prompt to Claude and return structured output."""
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    return {
        "model": model,
        "system_prompt_preview": system_prompt[:80] + "...",
        "user_message": user_message,
        "response": response.content[0].text,
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
        "timestamp": datetime.utcnow().isoformat()
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

    print(f"Response:\n{result['response']}")
    print(f"\nTokens used: {result['input_tokens']} in / {result['output_tokens']} out")

    saved = save_result(result)
    print(f"\nResult saved to: {saved}")
