# Trade Opportunities API

## Overview
This project is a FastAPI-based service that analyzes different market sectors in India and provides trade opportunity insights in a structured markdown format.

## Features
- Sector-based market analysis
- Markdown report generation
- API key authentication
- Simple and clean FastAPI implementation

## Tech Stack
- FastAPI
- Python
- Uvicorn

## How to Run

1. Install dependencies:
pip install fastapi uvicorn

2. Run the server:
python -m uvicorn main:app --reload

3. Open in browser:
http://127.0.0.1:8000/docs

## API Endpoint

GET /analyze/{sector}

Example:
/analyze/technology

## Headers

x-api-key: "AQ.Ab8RN6K3_h0qWWpHibMZGGr57emSs33CM5HAjUbQgXtcHWpsWA"

## Sample Output

# TECHNOLOGY SECTOR ANALYSIS (INDIA)

## Overview
The technology sector is growing in India.

## Opportunities
- Increasing demand
- Government support
- Export potential

## Risks
- Market fluctuation
- Competition

## Conclusion
Good sector for trading and investment.

## Author
Kausalya
