from dotenv import load_dotenv
import os
import sys


def main():
    load_dotenv()

    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        print("ANTHROPIC_API_KEY not found in environment (.env).")
        print("Create a .env file with ANTHROPIC_API_KEY or set the env var before running.")
        sys.exit(2)

    try:
        import anthropic  # noqa: F401
    except Exception as e:
        print("The 'anthropic' package is not installed or failed to import:", e)
        print("Run: python -m pip install anthropic")
        sys.exit(3)

    print("ANTHROPIC_API_KEY is present and 'anthropic' is importable.")
    print("To perform a real API request, run: python scripts/anthropic_example.py")
    # Explicit success confirmation
    print("SUCCESS: API key and package check passed.", flush=True)


if __name__ == "__main__":
    main()
