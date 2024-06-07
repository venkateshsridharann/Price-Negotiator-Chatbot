document.addEventListener('DOMContentLoaded', function() {
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const chatOutput = document.getElementById('chat-output');

    sendButton.addEventListener('click', function() {
        sendMessage();
    });

    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const userText = userInput.value.trim();
        if (userText) {
            addMessage('You: ' + userText, 'user');
            setTimeout(() => {
                const botResponse = `Bot: ${userText} + Response`; // Generate bot response
                addMessage(botResponse, 'bot');
            }, 1000);
            userInput.value = '';
        }
    }

    function addMessage(text, sender) {
        const message = document.createElement('div');
        message.classList.add('message', `${sender}-message`);
        message.textContent = text;
        chatOutput.appendChild(message);
        chatOutput.scrollTop = chatOutput.scrollHeight;
    }
});
