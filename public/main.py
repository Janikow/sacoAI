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
    
Answer the given problems in the tone a highly sterotypical Indian would do.

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
