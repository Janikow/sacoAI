from dotenv import load_dotenv
import os
from openai import OpenAI

# =========================
# ENV / SETUP
# =========================
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# =========================
# AI POWER SCALING FUNCTION
# =========================
def scale_characters(name_a: str, name_b: str) -> str:
    prompt = f"""
You are comparing two fictional characters for a VS-style power scale.
Keep your answer concise and structured.

Character A: {name_a}
Character B: {name_b}

Provide ONLY:
- Strength
- Speed
- Durability
- Abilities
- Battle Intelligence
- Winner

Format exactly like this:

Character A:
Strength:
Speed:
Durability:
Abilities:
Battle Intelligence:

Character B:
Strength:
Speed:
Durability:
Abilities:
Battle Intelligence:

Winner:
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content

# =========================
# EXAMPLE USAGE
# =========================
if __name__ == "__main__":
    result = scale_characters("Luffy", "Goku")
    print(result)
