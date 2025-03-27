let ws;

function connectWebSocket() {
  ws = new WebSocket("ws://localhost:8000/ws");

  ws.onmessage = function (event) {
    displayMessage(event.data, "bot");
  };

  ws.onopen = function () {
    console.log("WebSocket connected");
  };

  ws.onclose = function () {
    console.log("WebSocket disconnected");
  };
}

function sendMessage() {
  const userInput = document.getElementById("userInput").value;
  if (userInput.trim() === "") return;

  displayMessage(userInput, "user");
  ws.send(userInput);
  document.getElementById("userInput").value = "";
}

function displayMessage(message, sender) {
  const chatBox = document.getElementById("chatBox");
  const messageElement = document.createElement("div");
  messageElement.classList.add("message", sender === "user" ? "user-message" : "bot-message");
  messageElement.innerHTML = `<div class="message-content">${message}</div>`;
  chatBox.appendChild(messageElement);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function toggleChat() {
  const chatBoxContainer = document.getElementById("chatBoxContainer");
  const chatBox = document.getElementById("chatBox");
  const inputContainer = document.querySelector(".input-container");
  const isOpen = chatBox.style.display === "block";

  if (isOpen) {
    chatBox.style.display = "none";
    inputContainer.style.display = "none";
    chatBoxContainer.style.height = "0px";
  } else {
    chatBox.style.display = "block";
    inputContainer.style.display = "flex";
    chatBoxContainer.style.height = "300px";
  }
}

function checkKey(event) {
  if (event.key === "Enter") {
    sendMessage();
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const chatBoxHTML = `
        <div class="chat-container">
            <div class="chat-header" onclick="toggleChat()">Chatbot</div>
            <div id="chatBoxContainer">
                <div class="chat-box" id="chatBox"></div>
                <div class="input-container">
                    <input type="text" id="userInput" placeholder="Type a message..." onkeydown="checkKey(event)">
                    <button onclick="sendMessage()">Send</button>
                </div>
            </div>
        </div>
    `;
  document.body.insertAdjacentHTML("beforeend", chatBoxHTML);
  connectWebSocket();
});
