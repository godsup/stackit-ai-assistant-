import SourceList from './SourceList'

function ChatMessage({ message }) {
  const isAssistant = message.role === 'assistant'

  return (
    <article className={`message message--${message.role}`}>
      <div className="message__identity">
        <span className={`avatar avatar--${message.role}`} aria-hidden="true">
          {isAssistant ? 'S' : 'Y'}
        </span>
        <span>{isAssistant ? 'STACKIT Assistant' : 'You'}</span>
      </div>
      <div className="message__body">
        <p>{message.content}</p>
        {isAssistant && <SourceList sources={message.sources} />}
      </div>
    </article>
  )
}

export default ChatMessage