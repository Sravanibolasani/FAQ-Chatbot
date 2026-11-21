
import json
import re
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load FAQ data
FAQ_FILE = Path(__file__).resolve().parent / "faqs.json"

with open(FAQ_FILE, "r", encoding="utf-8") as file:
    faqs = json.load(file)


# Abbreviation dictionary
ALIASES = {
    "ai": "artificial intelligence",
    "ml": "machine learning",
    "nlp": "natural language processing",
    "lor": "letter of recommendation"
}


# Clean and normalize text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    words = text.split()

    words = [
        ALIASES.get(word, word)
        for word in words
    ]

    return " ".join(words)


# Prepare FAQ questions using the same cleaning
questions = [
    clean_text(faq["question"])
    for faq in faqs
]


# TF-IDF vectorizer
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    stop_words="english"
)

faq_vectors = vectorizer.fit_transform(questions)


# Get chatbot answer
def get_answer(user_question):

    cleaned_question = clean_text(user_question)

    if not cleaned_question:
        return "Please enter a question."

    user_vector = vectorizer.transform([cleaned_question])

    similarities = cosine_similarity(
        user_vector,
        faq_vectors
    )

    best_match_index = similarities.argmax()
    best_score = similarities[0][best_match_index]

    print("Question:", user_question)
    print("Matched FAQ:", faqs[best_match_index]["question"])
    print("Similarity:", best_score)

    if best_score < 0.20:
        return (
            "Sorry, I couldn't find a relevant answer. "
            "Please try asking another question."
        )

    return faqs[best_match_index]["answer"]


if __name__ == "__main__":

    print("FAQ Chatbot Started!")
    print("Type exit to stop.")

    while True:

        question = input("You: ")

        if question.lower().strip() == "exit":
            break

        print("Bot:", get_answer(question))
