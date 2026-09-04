const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");


function addMessage(message, sender) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message");

    if (sender === "user") {
        messageDiv.classList.add("user-message");
    } else {
        messageDiv.classList.add("bot-message");
    }

    const messageSpan = document.createElement("span");
    messageSpan.textContent = message;

    messageDiv.appendChild(messageSpan);
    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}


// Typing indicator
function showTyping() {
    const typingDiv = document.createElement("div");

    typingDiv.id = "typing-indicator";
    typingDiv.classList.add("message", "bot-message");

    typingDiv.innerHTML = `
        <span>🤖 Bot is typing...</span>
    `;

    chatBox.appendChild(typingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}


function removeTyping() {
    const typingIndicator = document.getElementById("typing-indicator");

    if (typingIndicator) {
        typingIndicator.remove();
    }
}


async function sendMessage() {

    const question = userInput.value.trim();

    if (question === "") {
        return;
    }

    // Show user's message
    addMessage(question, "user");

    // Clear input
    userInput.value = "";

    // Show typing indicator
    showTyping();

    try {

        const response = await fetch("/ask", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })
        });

        const data = await response.json();

        // Remove typing indicator
        removeTyping();

        // Show bot response
        addMessage(data.answer, "bot");

    } catch (error) {

        console.error("Error:", error);

        removeTyping();

        addMessage(
            "Sorry, something went wrong. Please try again.",
            "bot"
        );
    }
}


// Suggested question buttons
function askSuggestion(question) {
    userInput.value = question;
    sendMessage();
}


// Clear chat
function clearChat() {

    chatBox.innerHTML = `
        <div class="message bot-message">
            <span>
                Hello! 👋 I'm your CodeAlpha FAQ Assistant.
                How can I help you?
            </span>
        </div>
    `;
}


// Press Enter to send
userInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});