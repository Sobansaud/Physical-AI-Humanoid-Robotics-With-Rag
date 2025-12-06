import React from 'react';

export default function ChatbotPlaceholder(): JSX.Element {
  return (
    <aside className="chatbot-placeholder" aria-hidden="true">
      <div style={{display: 'flex', flexDirection: 'column', gap: 8}}>
        <div style={{fontWeight: 700, fontFamily: 'Inter, sans-serif'}}>Assistant</div>
        <div style={{fontSize: 13, color: 'rgba(255,255,255,0.8)'}}>Select text to send to the assistant (placeholder)</div>
        <div style={{height: 8}} />
        <button className="button--primary">Open Chat</button>
      </div>
    </aside>
  );
}
