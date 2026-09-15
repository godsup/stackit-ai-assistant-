import { useEffect, useRef, useState } from 'react'
import ChatInput from './components/ChatInput'
import ChatMessage from './components/ChatMessage'
import { sendChatMessage } from './services/api'
import './App.css'

const welcomeMessage = {
  id: 'welcome',
  role: 'assistant',
  content:
    'Welcome. I can help you find clear answers across the STACKIT AI Model Serving documentation.',
  sources: [],
}

function App() {
  const [messages, setMessages] = useState([welcomeMessage])
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState('')
  const messagesEndRef = useRef(null)

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, isLoading])

  async function handleQuestion(question) {
    const userMessage = {
      id: `user-${Date.now()}`,
      role: 'user',
      content: question,
      sources: [],
    }

    setMessages((currentMessages) => [...currentMessages, userMessage])
    setError('')
    setIsLoading(true)

    try {
      const result = await sendChatMessage(question)
      setMessages((currentMessages) => [
        ...currentMessages,
        {
          id: `assistant-${Date.now()}`,
          role: 'assistant',
          content: result.answer,
          sources: result.sources || [],
        },
      ])
    } catch (requestError) {
      setError(requestError.message)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <main className="app-shell">
      <header className="app-header">
        <div className="brand-lockup">
          <span className="brand-mark" aria-hidden="true">S</span>
          <div>
            <div className="brand-name">STACKIT</div>
            <div className="brand-product">Documentation Assistant</div>
          </div>
        </div>
        <div className="status-indicator">
          <span aria-hidden="true" /> API connected
        </div>
      </header>

      <section className="chat-layout" aria-label="Documentation assistant">
        <div className="chat-heading">
          <div>
            <p className="eyebrow">AI Model Serving</p>
            <h1>How can we help?</h1>
            <p className="chat-intro">Ask a question and get answers grounded in STACKIT documentation.</p>
          </div>
          <div className="chat-meta">{messages.length - 1} {messages.length - 1 === 1 ? 'question' : 'questions'}</div>
        </div>

        <div className="message-list" aria-live="polite">
          {messages.map((message) => (
            <ChatMessage key={message.id} message={message} />
          ))}
          {isLoading && (
            <div className="message message--assistant message--loading">
              <div className="message__identity">
                <span className="avatar avatar--assistant" aria-hidden="true">S</span>
                <span>STACKIT Assistant</span>
              </div>
              <div className="loading-dots" aria-label="Assistant is thinking"><span /><span /><span /></div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {error && (
          <div className="error-banner" role="alert">
            <strong>Unable to reach the assistant.</strong> {error}
          </div>
        )}

        <div className="composer-area">
          <ChatInput onSubmit={handleQuestion} disabled={isLoading} />
          <p className="composer-hint">Enter to send. Shift + Enter for a new line.</p>
        </div>
      </section>
    </main>
  )
}

export default App
