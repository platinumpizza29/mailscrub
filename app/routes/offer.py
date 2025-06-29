from fastapi import APIRouter, HTTPException, Form
from typing import Optional
from app.db import offers_collection
from app.utils import parse_email_body

router = APIRouter()

@router.post("/mailgun/offer")
async def receive_offer(
    sender: str = Form(..., alias="sender"),
    subject: str = Form(""),
    body_html: str = Form("", alias="body-html"),
    body_plain: str = Form("", alias="body-plain"),
    brand: Optional[str] = Form(None),
    source: Optional[str] = Form(None),
    tags: Optional[str] = Form(None),
):
    body = body_html if body_html.strip() else body_plain
    tags_list = [tag.strip() for tag in tags.split(",")] if tags else []

    text, images, ctas = parse_email_body(body)

    offer_data = {
        "sender_email": sender,
        "subject": subject,
        "tags": tags_list,
        "text": text,
        "images": images,
        "ctas": ctas,
    }

    try:
        result = offers_collection.insert_one(offer_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to store offer: {str(e)}")

    return {"message": "Offer stored successfully", "offer_id": str(result.inserted_id)}
