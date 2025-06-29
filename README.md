# LoyalTea Email Offer Microservice

This is a lightweight Python microservice built with FastAPI that processes incoming offer emails forwarded via Mailgun. It parses the email content to extract clean text, images, and call-to-action (CTA) links, then stores the structured offer data in MongoDB.

---

## Overview

- Receives POST requests from Mailgun with raw email data.
- Cleans and extracts relevant information (text, images, CTAs) using BeautifulSoup.
- Stores parsed offer data in a MongoDB collection.
- Designed to work alongside the main LoyalTea Go server, handling email parsing and offer ingestion.

---

## Tech Stack

- **Python 3.11+**
- **FastAPI** – web framework for building the API.
- **BeautifulSoup4** – for robust HTML parsing and cleaning.
- **PyMongo** – MongoDB client.
- **Uvicorn** – ASGI server for running FastAPI.

---

## Setup & Run

1. Clone the repo.

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
