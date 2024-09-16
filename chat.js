document.addEventListener('DOMContentLoaded', () => {
    const chatBody = document.querySelector('.chat-body');
    const inputText = document.querySelector('.input-text');
    const sendButton = document.querySelector('.send-button');
    
    // Connect to the WebSocket server
    const socket = io();
  
    // Handle incoming messages
    socket.on('receive_message', (message) => {
      addMessageToChat(message);
    });
  
    // Add a message to the chat
    function addMessageToChat(message) {
      const messageDiv = document.createElement('div');
      messageDiv.classList.add('message', message.position);
      messageDiv.innerHTML = `
        <div class="message-bubble${message.type === 'audio' ? ' audio' : ''}${message.color ? ' ' + message.color : ''}">
          ${message.type === 'text' ? `<p>${message.content}</p>` : `<img src="${message.content}" alt="Audio Wave" class="audio-wave-image">`}
        </div>
        <span class="message-time">${message.time}</span>
      `;
      chatBody.appendChild(messageDiv);
      chatBody.scrollTop = chatBody.scrollHeight; // Scroll to the latest message
    }
  
    // Send a message
    function sendMessage() {
      const message = {
        content: inputText.value,
        position: 'right',
        time: new Date().toLocaleTimeString(),
        type: 'text',
        color: 'purple'
      };
      
      socket.emit('send_message', message);
      inputText.value = ''; // Clear input
    }
  
    sendButton.addEventListener('click', sendMessage);
  
    // Optional: Send message on Enter key press
    inputText.addEventListener('keypress', (event) => {
      if (event.key === 'Enter') {
        sendMessage();
      }
    });
  });
  