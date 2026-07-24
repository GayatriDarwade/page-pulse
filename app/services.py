import time
import httpx
from app.parser import parse_html
from fastapi import HTTPException

def audit_url(url):

    try:
        start = time.perf_counter()
        response = httpx.get(
            str(url),
            timeout=10,
            follow_redirects=True,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        end = time.perf_counter()
        response_time = round((end - start) * 1000, 2)

    except httpx.TimeoutException:
        raise HTTPException(
            status_code=408,
            detail="The website took too long to respond."
        )
    
    except httpx.ConnectError:
        raise HTTPException(
            status_code=503,
            detail="Could not connect to the website."
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=500,
            detail="An unexpected network error occurred."
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"The website returned HTTP {response.status_code}."
        )

    content_type = response.headers.get("content-type", "")

    if "text/html" not in content_type:
        raise HTTPException(
            status_code=400,
            detail="The URL does not point to an HTML page."
        )


    report = parse_html(response.text)

    return {
        "status_code": response.status_code,
        "response_time": response_time,
        **report
    }