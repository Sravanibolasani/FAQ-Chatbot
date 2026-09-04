import json
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load FAQs
with open("faqs.json", "r", encoding="utf-8") as file:
    faqs = json.load(file)


# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.strip()


# Prepare FAQ questions
questions = [clean_text(faq["question"]) for faq in faqs]


# TF-IDF with stop words and two-word phrases
vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2)
)

faq_vectors = vectorizer.fit_transform(questions)


def get_answer(user_question):
    cleaned_question = clean_text(user_question)

    if not cleaned_question:
        return "Please enter a question."

    # Handle common abbreviations
    if cleaned_question in ["ai", "what is ai", "what does ai mean", "what is artificial intelligence"]:
        for faq in faqs:
            if "artificial intelligence" in faq["question"].lower():
                return faq["answer"]


    # Convert user question into TF-IDF vector
    user_vector = vectorizer.transform([cleaned_question])


    # Calculate similarity
    similarities = cosine_similarity(user_vector, faq_vectors)

    best_match_index = similarities.argmax()
    best_score = similarities[0][best_match_index]


    # Confidence threshold
    if best_score < 0.35:
        return (
            "I'm sorry, I couldn't find a relevant answer. "
            "Please try asking your question in a different way."
        )


    return faqs[best_match_index]["answer"]


# Run terminal chatbot only when this file is executed directly
if __name__ == "__main__":

    print("\n===================================")
    print("      CodeAlpha FAQ Chatbot")
    print("===================================")
    print("Type 'exit' to close the chatbot.\n")

    while True:

        user_question = input("You: ")

        if user_question.lower().strip() == "exit":
            print("Bot: Thank you for using the FAQ Chatbot!")
            break

        answer = get_answer(user_question)

        print("Bot:", answer)