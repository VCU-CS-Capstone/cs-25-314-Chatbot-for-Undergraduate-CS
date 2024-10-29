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

// Send message to Flask backend
function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    const messageBox = document.getElementById('chatBox');

    if (userInput.trim() !== "") {
        // Add user message to chat
        displayMessage(userInput, 'user');

        // Clear input box
        document.getElementById('userInput').value = '';

        // Send user message to Flask backend
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userInput }),
        })
        .then(response => response.json())
        .then(data => {
            // Add bot reply to chat
            displayMessage(data.reply, 'bot');
        });
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

// Save message to localStorage (optional)
function saveMessage(message, sender) {
    const chatHistory = JSON.parse(localStorage.getItem('chatHistory')) || [];
    chatHistory.push({ message, sender });
    localStorage.setItem('chatHistory', JSON.stringify(chatHistory));
}

// Load chat history from localStorage (optional)
function loadChatHistory() {
    const chatHistory = JSON.parse(localStorage.getItem('chatHistory')) || [];
    chatHistory.forEach(chat => {
        displayMessage(chat.message, chat.sender);
    });
}

// Check for Enter key to send the message
function checkKey(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
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
                    <input type="text" id="userInput" placeholder="Type a message..." onkeydown="checkKey(event)">
                    <button onclick="sendMessage()">Send</button>
                </div>
            </div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', chatBoxHTML);

    // Load the chat history from localStorage when the page is loaded
    loadChatHistory();
});
