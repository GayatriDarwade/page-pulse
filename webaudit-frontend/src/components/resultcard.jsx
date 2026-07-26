function ResultCard({ result }) {
  return (
    <div className="result-card">
      <h2>Audit Results</h2>

      <div className="metrics-grid">
        <div className="metric">
          <h3>Status Code</h3>
          <p>{result.status_code}</p>
        </div>

        <div className="metric">
          <h3>Response Time</h3>
          <p>{result.response_time} ms</p>
        </div>

        <div className="metric">
          <h3>H1 Tags</h3>
          <p>{result.h1_count}</p>
        </div>

        <div className="metric">
          <h3>Missing Alt</h3>
          <p>{result.img_no_alt}</p>
        </div>

        <div className="metric">
          <h3>Word Count</h3>
          <p>{result.word_count}</p>
        </div>
      </div>

      <div className="details">
        <p><strong>Title:</strong> {result.title}</p>

        <p>
          <strong>Meta Description:</strong>{" "}
          {result.meta_description || "Not Found"}
        </p>
      </div>
    </div>
  );
}

export default ResultCard;