// Toggle chat box visibility
function toggleChat() {
    const chatBoxContainer = document.getElementById('chatBoxContainer');
    const chatBox = document.getElementById('chatBox');
    const inputContainer = document.querySelector('.input-container');
    const isOpen = chatBox.style.display === 'block';

    // Slide the chatbox up/down
    if (isOpen) {
        chatBox.style.display = 'none';
        inputContainer.style.display = 'none';
        chatBoxContainer.style.height = '0px';
    } else {
        chatBox.style.display = 'block';
        inputContainer.style.display = 'flex';
        chatBoxContainer.style.height = '300px';
    }
}

// Example bot responses
const botResponses = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! What would you like to know?",
    "bye": "Goodbye! Have a nice day!",
    "how are you": "I'm just a bot, but I'm here to help!",
    "easter egg": "I'm Batman"
};

// Send message and save to localStorage
function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    if (userInput.trim() !== "") {
        displayMessage(userInput, 'user');
        saveMessage(userInput, 'user');  // Save user message
        getBotResponse(userInput);
        document.getElementById('userInput').value = '';
    }
}

// Display message in the chatbox
function displayMessage(message, sender) {
    const chatBox = document.getElementById('chatBox');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender === 'user' ? 'user-message' : 'bot-message');
    messageElement.innerHTML = `<div class="message-content">${message}</div>`;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Get bot response and save it to localStorage
function getBotResponse(userMessage) {
    const message = userMessage.toLowerCase();
    const botReply = botResponses[message] || "I'm not sure how to respond to that.";
    setTimeout(() => {
        displayMessage(botReply, 'bot');
        saveMessage(botReply, 'bot');  // Save bot message
    }, 500); // Simulate bot thinking delay
}

// Save message to localStorage
function saveMessage(message, sender) {
    const chatHistory = JSON.parse(localStorage.getItem('chatHistory')) || [];
    chatHistory.push({ message, sender });
    localStorage.setItem('chatHistory', JSON.stringify(chatHistory));
}

// Load chat history from localStorage
function loadChatHistory() {
    const chatHistory = JSON.parse(localStorage.getItem('chatHistory')) || [];
    chatHistory.forEach(chat => {
        displayMessage(chat.message, chat.sender);
    });
}

// Dynamically load the chatbox into the page and load chat history
document.addEventListener('DOMContentLoaded', () => {
    const chatBoxHTML = `
        <div class="chat-container">
            <div class="chat-header" onclick="toggleChat()">Chatbot</div>
            <div id="chatBoxContainer">
                <div class="chat-box" id="chatBox">
                    <!-- Messages will be displayed here -->
                </div>
                <div class="input-container">
                    <input type="text" id="userInput" placeholder="Type a message..." onkeydown="if (event.key === 'Enter') sendMessage()">
                    <button onclick="sendMessage()">Send</button>
                </div>
            </div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', chatBoxHTML);

    // Load the chat history from localStorage when the page is loaded
    window.onload = loadChatHistory();
});
