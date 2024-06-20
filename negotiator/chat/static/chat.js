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

    function sendMessage()
    {
        const userInput = document.getElementById('user-input');
        const userText = userInput.value; // Get the value entered by the user
        let botResponse_ = '';

        if (userText) {
            addMessage(userText, 'user');
            setTimeout(() => {
                const botResponse = `${userText} + Response`; // Generate bot response
                botResponse_= botResponse.replace("Bot: ", "");
                addMessage(botResponse, 'bot');
                
                // saving bot message
                fetch('send_message/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-CSRFToken': getCookie('csrftoken') // Add CSRF token for security
                    },
                    body: new URLSearchParams({
                        'user_input': botResponse_,
                        'chat_id': chat_id_,
                        'sender': 'bot',
                        
                    })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        console.log('Data saved successfully!')
                    } else {
                        console.log('Failed to save data.')
                    }
                })
                .catch(error => console.error('Error:', error));
            }, 1000);
            userInput.value = '';
        }// const sendButton = document.getElementById('send-button');
        // const chatOutput = document.getElementById('chat-output');
        const chat_id = document.getElementById('chat-session-id');
        console.log(chat_id);
        const chat_id_ = chat_id.value;
        
        // saving user message
        fetch('send_message/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken') // Add CSRF token for security
            },
            body: new URLSearchParams({
                'user_input': userText,
                'chat_id': chat_id_,
                'sender': 'user',
                
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                console.log('Data saved successfully!')
            } else {
                console.log('Failed to save data.')
            }
        })
        .catch(error => console.error('Error:', error));

    
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
    function addMessage(text, sender) {
        const message = document.createElement('div');
        message.classList.add('message', `${sender}-message`);
        message.textContent = text;
        chatOutput.appendChild(message);
        chatOutput.scrollTop = chatOutput.scrollHeight;
    }
});


