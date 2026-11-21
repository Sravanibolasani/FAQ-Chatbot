
from flask import Flask, render_template, request, jsonify
from chatbot import get_answer

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json(silent=True) or {}
        user_question = data.get("question", "").strip()

        if not user_question:
            return jsonify({
                "answer": "Please enter a question."
            }), 400

        answer = get_answer(user_question)

        return jsonify({
            "answer": answer
        })

    except Exception as error:
        app.logger.exception("Chatbot error: %s", error)

        return jsonify({
            "answer": "Sorry, something went wrong. Please try again."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
