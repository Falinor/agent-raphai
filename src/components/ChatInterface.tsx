'use client';

import { useState, useRef, useEffect } from 'react';
import { useChat } from 'ai/react';
import { fr } from "@codegouvfr/react-dsfr";
import { Button } from "@codegouvfr/react-dsfr/Button";
import { Input } from "@codegouvfr/react-dsfr/Input";
import { Badge } from "@codegouvfr/react-dsfr/Badge";
import { Alert } from "@codegouvfr/react-dsfr/Alert";

export default function ChatInterface() {
  const { messages, input, handleInputChange, handleSubmit, isLoading, error } = useChat();
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const [isTyping, setIsTyping] = useState(false);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    setIsTyping(isLoading);
  }, [isLoading]);

  const handleFormSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim()) {
      handleSubmit(e);
    }
  };

  const formatTime = (date: Date) => {
    return new Intl.DateTimeFormat('fr-FR', {
      hour: '2-digit',
      minute: '2-digit'
    }).format(date);
  };

  return (
    <div className={fr.cx("fr-container")}>
      {/* Hero Section */}
      <div className="hero-section">
        <div className={fr.cx("fr-container")}>
          <h1 className={fr.cx("fr-h1", "fr-mb-2w")}>
            Assistant IA
          </h1>
          <p className={fr.cx("fr-text--lg", "fr-mb-4w")}>
            Découvrez la puissance de l'intelligence artificielle avec notre assistant conversationnel. 
            Posez vos questions, obtenez de l'aide ou engagez simplement une conversation.
          </p>
          <div className={fr.cx("fr-tags-group")}>
            <Badge severity="success">Sécurisé</Badge>
            <Badge severity="info">Accessible</Badge>
            <Badge severity="new">Innovant</Badge>
          </div>
        </div>
      </div>

      {/* Chat Container */}
      <div className={fr.cx("fr-py-6w")}>
        <div 
          className={fr.cx("fr-card", "fr-card--shadow")}
          style={{ 
            height: '70vh',
            display: 'flex',
            flexDirection: 'column',
            background: 'rgba(255, 255, 255, 0.95)',
            backdropFilter: 'blur(10px)',
            border: '1px solid rgba(255, 255, 255, 0.2)'
          }}
        >
          {/* Messages Area */}
          <div 
            className={fr.cx("fr-p-4w")}
            style={{
              flex: 1,
              overflowY: 'auto',
              display: 'flex',
              flexDirection: 'column',
              gap: '1.5rem'
            }}
          >
            {error && (
              <Alert
                severity="error"
                title="Erreur"
                description="Une erreur s'est produite lors de la communication avec l'assistant IA."
                className={fr.cx("fr-mb-2w")}
              />
            )}

            {messages.length === 0 ? (
              <div 
                style={{
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  justifyContent: 'center',
                  height: '100%',
                  textAlign: 'center'
                }}
              >
                <div 
                  className={fr.cx("fr-mb-4w")}
                  style={{
                    fontSize: '4rem',
                    opacity: 0.3
                  }}
                >
                  🤖
                </div>
                <h3 className={fr.cx("fr-h3", "fr-mb-2w")}>
                  Bienvenue dans le Chat IA !
                </h3>
                <p className={fr.cx("fr-text--lg", "fr-mb-4w")} style={{ maxWidth: '500px' }}>
                  Commencez une conversation en tapant votre message ci-dessous. 
                  Je suis là pour vous aider avec vos questions, fournir des informations ou simplement discuter !
                </p>
                <div className={fr.cx("fr-tags-group")}>
                  <Badge severity="info">Posez-moi tout</Badge>
                  <Badge severity="info">Obtenez de l'aide</Badge>
                  <Badge severity="info">Conversez</Badge>
                </div>
              </div>
            ) : (
              <>
                {messages.map((message, index) => (
                  <div
                    key={index}
                    className="chat-message"
                    style={{
                      display: 'flex',
                      gap: '1rem',
                      alignItems: 'flex-start',
                      justifyContent: message.role === 'user' ? 'flex-end' : 'flex-start',
                    }}
                  >
                    {message.role === 'assistant' && (
                      <div 
                        style={{
                          width: '40px',
                          height: '40px',
                          borderRadius: '50%',
                          background: 'var(--blue-france-sun-113-625)',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          color: 'white',
                          fontSize: '1.2rem',
                          flexShrink: 0
                        }}
                      >
                        🤖
                      </div>
                    )}
                    
                    <div
                      className={message.role === 'user' ? 'message-bubble-user' : 'message-bubble-assistant'}
                      style={{
                        padding: '1rem 1.25rem',
                        maxWidth: '70%',
                        wordBreak: 'break-word',
                        position: 'relative'
                      }}
                    >
                      <div style={{ whiteSpace: 'pre-wrap', lineHeight: '1.6' }}>
                        {message.content}
                      </div>
                      <div 
                        style={{
                          fontSize: '0.75rem',
                          opacity: 0.7,
                          marginTop: '0.5rem',
                          textAlign: 'right'
                        }}
                      >
                        {formatTime(new Date())}
                      </div>
                    </div>

                    {message.role === 'user' && (
                      <div 
                        style={{
                          width: '40px',
                          height: '40px',
                          borderRadius: '50%',
                          background: 'var(--red-marianne-main-472)',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          color: 'white',
                          fontSize: '1.2rem',
                          flexShrink: 0
                        }}
                      >
                        👤
                      </div>
                    )}
                  </div>
                ))}

                {isTyping && (
                  <div
                    className="chat-message"
                    style={{
                      display: 'flex',
                      gap: '1rem',
                      alignItems: 'flex-start',
                      justifyContent: 'flex-start',
                    }}
                  >
                    <div 
                      style={{
                        width: '40px',
                        height: '40px',
                        borderRadius: '50%',
                        background: 'var(--blue-france-sun-113-625)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        color: 'white',
                        fontSize: '1.2rem',
                        flexShrink: 0
                      }}
                    >
                      🤖
                    </div>
                    
                    <div
                      className="message-bubble-assistant"
                      style={{
                        padding: '1rem 1.25rem',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '0.75rem'
                      }}
                    >
                      <div className="typing-indicator">
                        <div className="typing-dot"></div>
                        <div className="typing-dot"></div>
                        <div className="typing-dot"></div>
                      </div>
                      <span style={{ fontSize: '0.875rem', opacity: 0.7 }}>
                        L'IA réfléchit...
                      </span>
                    </div>
                  </div>
                )}
              </>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Input Area */}
          <div 
            className="chat-input-container"
            style={{
              padding: '1.5rem',
              borderTop: '1px solid var(--border-default-grey)'
            }}
          >
            <form onSubmit={handleFormSubmit}>
              <div style={{ display: 'flex', gap: '1rem', alignItems: 'flex-end' }}>
                <div style={{ flex: 1 }}>
                  <Input
                    label=""
                    textArea
                    nativeTextAreaProps={{
                      placeholder: "Tapez votre message ici...",
                      value: input,
                      onChange: handleInputChange,
                      disabled: isLoading,
                      rows: 1,
                      style: {
                        resize: 'none',
                        minHeight: '44px',
                        maxHeight: '120px'
                      }
                    }}
                  />
                </div>
                <Button
                  type="submit"
                  disabled={isLoading || !input.trim()}
                  iconId="fr-icon-send-plane-fill"
                  priority="primary"
                  style={{
                    minWidth: '56px',
                    height: '44px'
                  }}
                >
                  Envoyer
                </Button>
              </div>
            </form>
            
            <div 
              className={fr.cx("fr-mt-2w", "fr-text--xs")}
              style={{ 
                textAlign: 'center', 
                opacity: 0.7 
              }}
            >
              Appuyez sur Entrée pour envoyer, Maj+Entrée pour une nouvelle ligne
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}