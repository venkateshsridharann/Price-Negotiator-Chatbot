document.addEventListener('DOMContentLoaded', function() {
    const userInput = document.getElementById('user-input');
    const userText = userInput.value; // Get the value entered by the user
    const sendButton = document.getElementById('send-button');
    const chatOutput = document.getElementById('chat-output');
    const chat_id = document.getElementById('chat-session-id');

    sendButton.addEventListener('click', function() {
        sendMessage();
    });

    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const userInput = document.getElementById('user-input');
        const userText = userInput.value.trim(); // Get the trimmed value entered by the user
        const chat_id = document.getElementById('chat-session-id').value;
    
        if (userText) {
            userInput.disabled = true;
            sendButton.disabled = true;
            addMessage(userText, 'user');
    
            fetch('send_message/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': getCookie('csrftoken') // Add CSRF token for security
                },
                body: new URLSearchParams({
                    'user_input': userText,
                    'chat_id': chat_id,
                    'sender': 'user',
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    const botResponse = data.message; // Adjust based on your server's response structure
                    addMessage(botResponse, 'bot');
                } else {
                    console.log('Failed to send message:', data.message);
                }
            })
            .catch(error => console.error('Error:', error))
            .finally(() => {
                // Re-enable input and button after response
                userInput.disabled = false;
                sendButton.disabled = false;
            });

            userInput.value = '';
        }
    }
    
    // Function to add message to chat output
    function addMessage(text, sender) {
        const message = document.createElement('div');
        message.classList.add('message', `${sender}-message`);
        message.textContent = text;
        const chatOutput = document.getElementById('chat-output');
        chatOutput.appendChild(message);
        chatOutput.scrollTop = chatOutput.scrollHeight;
    }
    
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
});


