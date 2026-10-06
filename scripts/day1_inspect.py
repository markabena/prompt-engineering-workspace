import os
from dotenv import load_dotenv
import anthropic
from config import DEFAULT_MODEL

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

question = "What are the three most important habits for staying productive?"

# Ask the same question twice: once with plenty of room, once with almost none
for limit in [1024, 20]:
    response = client.messages.create(
        model=DEFAULT_MODEL,
        max_tokens=limit,
        messages=[{"role": "user", "content": question}],
    )
    print(f"\n===== max_tokens = {limit} =====")
    print("stop_reason :", response.stop_reason)
    print("tokens      :", response.usage.input_tokens, "in /", response.usage.output_tokens, "out")
    print("text        :", response.content[0].text)