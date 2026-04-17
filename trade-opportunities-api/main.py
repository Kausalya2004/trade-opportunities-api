from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Simple API key
API_KEY = "AQ.Ab8RN6K3_h0qWWpHibMZGGr57emSs33CM5HAjUbQgXtcHWpsWA"

@app.get("/")
def home():
    return {"message": "API is working"}

@app.get("/analyze/{sector}")
def analyze(sector: str, x_api_key: str = Header(None)):

    # Auth check
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # Simple report (no errors, guaranteed working)
    report = f"""
# {sector.upper()} SECTOR ANALYSIS (INDIA)

## Overview
The {sector} sector is growing in India.

## Opportunities
- Increasing demand
- Government support
- Export potential

## Risks
- Market fluctuation
- Competition

## Conclusion
Good sector for trading and investment.
"""

    return PlainTextResponse(report)