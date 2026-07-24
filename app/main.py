from fastapi import FastAPI

from app.models import  AuditRequest, AuditResponse
from app.services import audit_url


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, Page Pulse!"}

@app.post('/audit', response_model=AuditResponse)
def audit(request: AuditRequest):
    url = request.url
    return audit_url(url)