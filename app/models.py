from pydantic import BaseModel, EmailStr
from typing import List, Optional

class OfferRequest(BaseModel):
    sender_email: str  # Changed from EmailStr to match Go struct
    subject: str = ""  # Changed from Optional to required with default
    body: str
    brand: str = ""    # Changed from Optional to required with default
    source: str = ""   # Changed from Optional to required with default
    tags: List[str] = []  # Changed from Optional to required with default

class MailgunOfferRequest(BaseModel):
    """Exact match for Go MailgunOfferRequest struct"""
    sender_email: str
    subject: str = ""
    body: str
    brand: str = ""
    source: str = ""
    tags: List[str] = []
