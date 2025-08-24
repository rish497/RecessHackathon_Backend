from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

client = genai.Client()  # assumes your GOOGLE_API_KEY is set in environment

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",  # choose your model
            contents=user_message,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0)
            )
        )
        bot_reply = response.text or "Sorry, no reply."
    except Exception as e:
        bot_reply = "Sorry, something went wrong."

    return jsonify({"response": bot_reply})

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
