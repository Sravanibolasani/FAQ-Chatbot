# 🤖 CodeAlpha FAQ Chatbot

An NLP-based FAQ chatbot developed as part of the CodeAlpha internship.

## 📌 Project Overview

This chatbot answers frequently asked questions using Natural Language Processing and text similarity techniques.

The system preprocesses user questions, converts FAQ questions into TF-IDF vectors, calculates cosine similarity, and returns the most relevant answer.

## ✨ Features

- NLP-based question processing
- TF-IDF text vectorization
- Cosine similarity matching
- Confidence threshold for irrelevant questions
- AI abbreviation handling
- Suggested FAQ questions
- Clear Chat button
- Typing indicator
- Enter-key support
- Responsive web interface
- Flask backend

## 🛠️ Technologies Used

- Python
- NLTK
- Scikit-learn
- Flask
- HTML
- CSS
- JavaScript
- TF-IDF
- Cosine Similarity

## 📂 Project Structure

CodeAlpha_FAQChatbot/
│
├── app.py
├── chatbot.py
├── faqs.json
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── venv/

## ▶️ How to Run

### 1. Create virtual environment

python -m venv venv

### 2. Activate environment

Windows:

venv\Scripts\activate.bat

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run Flask

python app.py

### 5. Open browser

http://127.0.0.1:5000

## 🧠 How It Works

1. User enters a question.
2. The question is cleaned and normalized.
3. FAQ questions are converted into TF-IDF vectors.
4. Cosine similarity compares the user's question with the FAQs.
5. The highest-confidence matching FAQ is selected.
6. The chatbot displays the corresponding answer.

## 👩‍💻 Internship

Developed for the CodeAlpha Internship Program.

## 📜 License

This project is created for educational and internship purposes.