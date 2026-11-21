
console.log("FAQ Chatbot JavaScript loaded!");

const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");
const sendButton = document.getElementById("send-btn");

console.log("Input:", userInput);
console.log("Chat box:", chatBox);
console.log("Send button:", sendButton);

function addMessage(message, sender) {
    const div = document.createElement("div");
    div.className = "message " + (sender === "user" ? "user-message" : "bot-message");

    const span = document.createElement("span");
    span.textContent = message;

    div.appendChild(span);
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    console.log("Send button clicked!");

    const question = userInput.value.trim();

    if (!question) return;

    addMessage(question, "user");
    userInput.value = "";

    const typing = document.createElement("div");
    typing.id = "typing-indicator";
    typing.className = "message bot-message";
    typing.innerHTML = "<span>🤖 Bot is typing...</span>";
    chatBox.appendChild(typing);

    sendButton.disabled = true;

    try {
        console.log("Sending request to Flask...");

        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        console.log("Server response:", response.status);

        const data = await response.json();

        document.getElementById("typing-indicator")?.remove();

        addMessage(data.answer || "No answer received.", "bot");

    } catch (error) {
        console.error("Chatbot error:", error);

        document.getElementById("typing-indicator")?.remove();

        addMessage("Unable to connect to the chatbot server.", "bot");

    } finally {
        sendButton.disabled = false;
    }
}

function askSuggestion(question) {
    userInput.value = question;
    sendMessage();
}

function clearChat() {
    chatBox.innerHTML = "";
    addMessage("Hello! 👋 Welcome to FAQ Chatbot. How can I help you?", "bot");
}

window.sendMessage = sendMessage;
window.askSuggestion = askSuggestion;
window.clearChat = clearChat;

sendButton.addEventListener("click", sendMessage);

userInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});
