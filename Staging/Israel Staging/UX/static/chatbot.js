function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const messageBox = document.getElementById('messages');

    if (userInput) {
        // Add user message to chat
        const userMessage = document.createElement('div');
        userMessage.className = 'user-message';
        userMessage.textContent = userInput;
        messageBox.appendChild(userMessage);

        // Clear input box
        document.getElementById('user-input').value = '';

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
            const botMessage = document.createElement('div');
            botMessage.className = 'bot-message';
            botMessage.textContent = data.reply;
            messageBox.appendChild(botMessage);
        });
    }
}
function checkKey(event) {
    if (event.keyCode === 13) {
        sendMessage();
    }
}