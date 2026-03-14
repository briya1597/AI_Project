const chatWindow = document.getElementById('chatWindow');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');

// Automatically parse markdown
marked.setOptions({
  breaks: true,
  gfm: true
});

function appendMessage(sender, text, isMarkdown=false) {
  const wrapper = document.createElement('div');
  wrapper.className = `message-wrapper ${sender}`;
  
  const avatarStr = sender === 'user' ? '👤' : '🤖';
  
  const contentHtml = isMarkdown ? marked.parse(text) : `<p>${text}</p>`;

  wrapper.innerHTML = `
    <div class="avatar">${avatarStr}</div>
    <div class="message-bubble">${contentHtml}</div>
  `;

  chatWindow.appendChild(wrapper);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function showTyping() {
  const wrapper = document.createElement('div');
  wrapper.className = 'message-wrapper bot typing';
  wrapper.id = 'typingIndicator';
  wrapper.innerHTML = `
    <div class="avatar">🤖</div>
    <div class="message-bubble">
      <div class="typing-indicator">
        <div class="dot"></div><div class="dot"></div><div class="dot"></div>
      </div>
    </div>
  `;
  chatWindow.appendChild(wrapper);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function removeTyping() {
  const indicator = document.getElementById('typingIndicator');
  if (indicator) {
    indicator.remove();
  }
}

async function handleSend() {
  const text = userInput.value.trim();
  if (!text) return;

  appendMessage('user', text, false);
  userInput.value = '';
  
  showTyping();

  try {
    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text })
    });

    const data = await response.json();
    removeTyping();
    appendMessage('bot', data.reply || "Something went wrong.", true);

  } catch (err) {
    console.error(err);
    removeTyping();
    appendMessage('bot', "⚠ Network error. Could not connect to the server.", false);
  }
}

sendBtn.addEventListener('click', handleSend);
userInput.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') handleSend();
});

// Auto-focus input
userInput.focus();
