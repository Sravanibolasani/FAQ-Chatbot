
# 🤖 FAQ Chatbot

An NLP-based FAQ Chatbot developed using Python, Flask, and Machine Learning techniques.

## 📌 Project Overview

This project is designed to answer frequently asked questions using Natural Language Processing and text similarity techniques.

The chatbot processes user questions, converts FAQ questions into TF-IDF vectors, calculates cosine similarity, and returns the most relevant answer.

## ✨ Features

- NLP-based question processing
- TF-IDF text vectorization
- Cosine similarity matching
- Confidence threshold for irrelevant questions
- Common abbreviation handling
- Suggested FAQ questions
- Clear Chat button
- Typing indicator
- Enter-key support
- Responsive web interface
- Flask backend

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- HTML
- CSS
- JavaScript
- TF-IDF
- Cosine Similarity

## 📂 Project Structure

```text
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
└── static/
    ├── style.css
    └── script.js
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd CodeAlpha_FAQChatbot
```

### 3. Create virtual environment

```bash
python -m venv venv
```

### 4. Activate virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Windows CMD:

```cmd
venv\Scripts\activate.bat
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Flask application

```bash
python app.py
```

### 7. Open in browser

http://127.0.0.1:5000

## 🧠 How It Works

1. User enters a question in the chatbot interface.
2. The question is cleaned and normalized.
3. FAQ questions are converted into TF-IDF vectors.
4. Cosine similarity compares the user's question with stored FAQs.
5. The highest-scoring matching FAQ is selected.
6. The chatbot displays the corresponding answer if the confidence threshold is met.

## 🎯 Applications

- Frequently Asked Questions
- Internship Information Assistance
- Basic Educational Support
- Automated Question Answering

## 👩‍💻 Internship

Originally developed as part of the CodeAlpha Internship Program.

## 📜 License

This project is created for educational and internship purposes.
