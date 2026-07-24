from typing import Optional
from pydantic import BaseModel, HttpUrl

class AuditRequest(BaseModel):
    url: HttpUrl


class AuditResponse(BaseModel):
    status_code: int
    response_time: float
    title: Optional[str] = None
    meta_description: Optional[str] = None
    h1_count: int
    img_no_alt: int
    word_count: int