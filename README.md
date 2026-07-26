# webaudit

Page Pulse is a web application that audits any website URL and returns key SEO and accessibility metrics. It consists of a FastAPI backend that analyzes web pages and a React frontend that provides a simple user interface for running audits.

## Features

- Audit any valid website URL
- Measure HTTP status code
- Measure response time
- Extract page title
- Extract meta description
- Count H1 tags
- Count images missing `alt` attributes
- Estimate visible word count
- Handle invalid URLs, timeouts, and non-HTML responses gracefully

---

## Tech Stack

### Backend
- FastAPI
- httpx
- BeautifulSoup4
- Pydantic

### Frontend
- React
- Vite
- CSS

### Testing
- pytest

---

## Project Structure

```
DigiH/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── parser.py
│   └── services.py
│
├── tests/
│   └── test_parser.py
│
├── page-pulse-frontend/
│
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd DigiH
```

### Backend Setup

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the backend:

```bash
uvicorn app.main:app --reload
```

The backend runs on:

```
http://localhost:8000
```

---

### Frontend Setup

```bash
cd page-pulse-frontend
npm install
npm run dev
```

The frontend runs on:

```
http://localhost:5173
```

---

## API Contract

### Endpoint

```
POST /audit
```

### Request

```json
{
  "url": "https://python.org"
}
```

### Example Response

```json
{
  "status_code": 200,
  "response_time": 245.81,
  "title": "Welcome to Python.org",
  "meta_description": "The official home of the Python Programming Language.",
  "h1_count": 1,
  "img_no_alt": 2,
  "word_count": 542
}
```

---

## Error Handling

The API returns meaningful errors for:

- Invalid URLs
- Connection failures
- Timeouts
- Non-HTML responses
- HTTP errors returned by websites

---

## Tests

Parser tests were written using **pytest** and include:

- Happy path
- Missing title
- Missing meta description
- No H1 tags

Run tests:

```bash
python -m pytest tests
```

---

## Design Decisions

### 1. Separation of Concerns

The project separates responsibilities into different modules:

- `main.py` handles API routes.
- `services.py` performs network requests.
- `parser.py` extracts information from HTML.
- `models.py` defines request and response schemas.

This makes the project easier to maintain and extend.

---

### 2. Graceful Error Handling

Instead of crashing when a website cannot be reached or returns invalid content, the API returns meaningful HTTP errors. This improves reliability and provides a better user experience.

---

### 3. Visible Word Count

Word count is calculated from the HTML `<body>` rather than the entire document. This avoids counting metadata such as the page title and provides a better estimate of visible page content. If a `<body>` tag is missing, the parser falls back to the entire document.

---

## Future Improvements

- SEO score calculation
- Support for Open Graph metadata
- Lighthouse-style performance metrics
- Dark mode
- Export audit reports as PDF

---

## Built For

Built for **Digital Heroes Training Task**.
