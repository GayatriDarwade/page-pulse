function UrlForm({ url, setUrl, handleAudit, loading }) {
  return (
    <form
      className="url-form"
      onSubmit={(e) => {
        e.preventDefault();
        handleAudit();
      }}
    >
      <input
        type="text"
        placeholder="https://example.com"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />

      <button
        type="submit"
        disabled={loading || !url.trim()}
      >
        {loading ? "Auditing..." : "Audit"}
      </button>
    </form>
  );
}

export default UrlForm;