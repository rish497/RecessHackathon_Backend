from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# --- Gemini AI Setup ---
GENAI_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GENAI_API_KEY:
    raise ValueError("Missing GOOGLE_API_KEY environment variable!")
client = genai.Client(api_key=GENAI_API_KEY)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_message,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0)
            )
        )
        bot_reply = response.text or "Sorry, no reply."
    except Exception as e:
        bot_reply = "Sorry, something went wrong."
    return jsonify({"response": bot_reply})

# --- YouTube Search API ---
YOUTUBE_API_KEY = os.getenv("API_KEY_YOUTUBE")

@app.route("/youtube", methods=["GET"])
def youtube_search():
    query = request.args.get("q")
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=8&q={query}&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    return jsonify(response.json())

# --- Homepage ---
@app.route("/")
def home():
    return render_template("index.html")

# --- Run Flask ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
