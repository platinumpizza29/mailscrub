from bs4 import BeautifulSoup, Tag

def parse_email_body(html: str):
    soup = BeautifulSoup(html, "html.parser")

    # Cleaned text
    text = soup.get_text(separator=" ", strip=True)

    # Extract image URLs
    images = []
    for img in soup.find_all("img"):
        if isinstance(img, Tag):
            src = img.get("src")
            if src:
                images.append(src)

    # CTA Links - filter anchors with common CTA keywords
    cta_keywords = ["download", "shop", "view", "buy", "order", "get"]
    ctas = []
    for a in soup.find_all("a", href=True):
        if isinstance(a, Tag):
            anchor_text = a.get_text(strip=True).lower()
            if any(keyword in anchor_text for keyword in cta_keywords):
                ctas.append(a.get("href"))

    return text, images, ctas
