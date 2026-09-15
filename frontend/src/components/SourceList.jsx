function SourceList({ sources = [] }) {
  if (!sources.length) {
    return null
  }

  return (
    <section className="source-list" aria-label="Sources">
      <div className="source-list__label">Sources</div>
      <ul>
        {sources.map((source, index) => (
          <li key={`${source}-${index}`}>
            <span className="source-list__marker">{String(index + 1).padStart(2, '0')}</span>
            <span>{source}</span>
          </li>
        ))}
      </ul>
    </section>
  )
}

export default SourceList