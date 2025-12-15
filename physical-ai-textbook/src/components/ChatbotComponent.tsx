import React, { useState, useRef, useEffect, JSX } from 'react';
import clsx from 'clsx';

type Message = {
    id: string;
    text: string;
    sender: 'user' | 'bot';
};

export default function ChatbotComponent(): JSX.Element {
    const [isOpen, setIsOpen] = useState(false);
    const [messages, setMessages] = useState<Message[]>([
        { id: '1', text: 'Hello! I am your Physical AI assistant. Ask me anything about the course!', sender: 'bot' },
    ]);
    const [inputValue, setInputValue] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const messagesEndRef = useRef<HTMLDivElement>(null);

    const toggleChat = () => setIsOpen(!isOpen);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages, isOpen]);

    // Global Selection Listener
    useEffect(() => {
        const handleSelection = async () => {
            const selection = window.getSelection();
            if (selection && selection.toString().trim().length > 0) {
                const selectedText = selection.toString().trim();

                // Show chat if hidden
                if (!isOpen) setIsOpen(true);

                // Add selection query to chat
                const newMessage: Message = {
                    id: Date.now().toString(),
                    text: `Explain selection: "${selectedText.substring(0, 50)}..."`,
                    sender: 'user'
                };
                setMessages(prev => [...prev, newMessage]);
                setIsLoading(true);

                try {
                    const response = await fetch('https://sobansaud028382-huggingnewback.hf.space/api/ask-selection', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            question: "Explain this text in context of the course.",
                            selection: selectedText
                        })
                    });

                    if (!response.ok) throw new Error('Backend error');

                    const data = await response.json();

                    setMessages(prev => [...prev, {
                        id: (Date.now() + 1).toString(),
                        text: data.answer,
                        sender: 'bot'
                    }]);
                } catch (error) {
                    setMessages(prev => [...prev, {
                        id: (Date.now() + 1).toString(),
                        text: "Sorry, I couldn't process that selection. Ensure the backend is running.",
                        sender: 'bot'
                    }]);
                } finally {
                    setIsLoading(false);
                }
            }
        };

        const onMouseUp = () => {
            // slight delay to ensure selection is populated
            setTimeout(handleSelection, 100);
        };

        document.addEventListener('mouseup', onMouseUp);
        return () => document.removeEventListener('mouseup', onMouseUp);
    }, [isOpen]); // Depend on isOpen to open it? No, checking state inside.

    const handleSendMessage = async () => {
        if (!inputValue.trim()) return;

        const newUserMessage: Message = {
            id: Date.now().toString(),
            text: inputValue,
            sender: 'user',
        };

        setMessages((prev) => [...prev, newUserMessage]);
        setInputValue('');
        setIsLoading(true);

        try {
            const response = await fetch('https://sobansaud028382-huggingnewback.hf.space/api/ask', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question: newUserMessage.text })
            });

            if (!response.ok) throw new Error('Backend error');

            const data = await response.json();

            setMessages((prev) => [...prev, {
                id: (Date.now() + 1).toString(),
                text: data.answer,
                sender: 'bot',
            }]);
        } catch (error) {
            setMessages((prev) => [...prev, {
                id: (Date.now() + 1).toString(),
                text: "Error connecting to backend. Please try again later.",
                sender: 'bot',
            }]);
        } finally {
            setIsLoading(false);
        }
    };

    const handleKeyPress = (e: React.KeyboardEvent) => {
        if (e.key === 'Enter') {
            handleSendMessage();
        }
    };

    return (
        <div className="chatbot-container">
            <div className={clsx('chatbot-window', { open: isOpen })}>
                <div className="chatbot-header">
                    <span style={{ fontWeight: 'bold' }}>Physical AI assistant</span>
                    <button
                        onClick={toggleChat}
                        style={{ background: 'none', border: 'none', color: 'white', cursor: 'pointer', fontSize: '1.2rem' }}
                    >
                        ×
                    </button>
                </div>
                <div className="chatbot-messages">
                    {messages.map((msg) => (
                        <div key={msg.id} className={clsx('message', msg.sender)}>
                            {msg.text}
                        </div>
                    ))}
                    {isLoading && <div className="message bot">Thinking...</div>}
                    <div ref={messagesEndRef} />
                </div>
                <div className="chatbot-input-area">
                    <input
                        type="text"
                        className="chatbot-input"
                        placeholder="Type a message..."
                        value={inputValue}
                        onChange={(e) => setInputValue(e.target.value)}
                        onKeyPress={handleKeyPress}
                        disabled={isLoading}
                    />
                    <button className="chatbot-send" onClick={handleSendMessage} disabled={isLoading}>
                        ➤
                    </button>
                </div>
            </div>

            <button className="chatbot-toggle" onClick={toggleChat} aria-label="Toggle Chatbot">
                {/* Robot Icon or Chat Icon */}
                <span style={{ fontSize: '24px' }}>🤖</span>
            </button>
        </div>
    );
}