from flask import Flask, request, jsonify, render_template
from google import genai
import os

app = Flask(__name__)

# API key (Render environment থেকে আসবে)
client = genai.Client(api_key=os.getenv("KEY"))

personal_info = "আমি একজন AI assistant। আমাকে বানিয়েছে মাসুম Billh।"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    prompt_text = f"""
    তুমি এখন আমার personal AI assistant।
    Personal info: {personal_info}
    User বলেছে: "{user_input}"

    User যদি জিজ্ঞেস করে "তোমাকে কে বানিয়েছে?" বা "কে বানিয়েছে তোমাকে?",
    তুমি সবসময় উত্তর দাও: "আমাকে মাসুম Billh বানিয়েছে।"
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_text
    )

    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)