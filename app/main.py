from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.models import  AuditRequest, AuditResponse
from app.services import audit_url


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://webaudit-gu0liwabd-gayatri10.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Hello, Page Pulse!"}

@app.post('/audit', response_model=AuditResponse)
def audit(request: AuditRequest):
    url = request.url
    return audit_url(url)