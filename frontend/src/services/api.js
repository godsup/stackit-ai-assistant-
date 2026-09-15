const CHAT_ENDPOINT = 'http://127.0.0.1:8000/chat'

export async function sendChatMessage(question) {
  const response = await fetch(CHAT_ENDPOINT, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ question }),
  })

  if (!response.ok) {
    let detail = 'The assistant could not answer right now.'

    try {
      const error = await response.json()
      detail = error.detail || detail
    } catch {
      // Keep the generic message when the API does not return JSON.
    }

    throw new Error(detail)
  }

  return response.json()
}