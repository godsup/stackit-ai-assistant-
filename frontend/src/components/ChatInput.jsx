import { useState } from 'react'

function ChatInput({ onSubmit, disabled }) {
  const [question, setQuestion] = useState('')

  function handleSubmit(event) {
    event.preventDefault()
    const trimmedQuestion = question.trim()

    if (!trimmedQuestion || disabled) {
      return
    }

    onSubmit(trimmedQuestion)
    setQuestion('')
  }

  function handleKeyDown(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault()
      event.currentTarget.form.requestSubmit()
    }
  }

  return (
    <form className="chat-input" onSubmit={handleSubmit}>
      <label className="sr-only" htmlFor="question">Ask a documentation question</label>
      <textarea
        id="question"
        rows="1"
        value={question}
        onChange={(event) => setQuestion(event.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="Ask about STACKIT AI Model Serving..."
        disabled={disabled}
      />
      <button type="submit" disabled={disabled || !question.trim()} aria-label="Send question">
        <span aria-hidden="true">-&gt;</span>
      </button>
    </form>
  )
}

export default ChatInput