from flask import Flask, render_template, request, jsonify
from chatbot import get_answer

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    user_question = data.get("question", "").strip()

    if not user_question:
        return jsonify({
            "answer": "Please enter a question."
        })

    answer = get_answer(user_question)

    return jsonify({
        "answer": answer
    })


if __name__ == "__main__":
    app.run(debug=True)