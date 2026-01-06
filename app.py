from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from openai import OpenAI

# =========================
# SETUP
# =========================
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

# =========================
# AI FUNCTION
# =========================
def talk_to_ai(user_message: str) -> str:
    prompt = f"""
Answer the following message in the tone of a highly stereotypical Indian.

Message:
{user_message}
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content

# =========================
# ROUTES
# =========================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        ai_reply = talk_to_ai(user_message)
        return jsonify({"reply": ai_reply}), 200

    except Exception as e:
        return jsonify({
            "error": "Something went wrong",
            "details": str(e)
        }), 500

# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True)
