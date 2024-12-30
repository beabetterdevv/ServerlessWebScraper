import requests
from models.product import Product

def publish(webhook_url: str, product: Product) -> None:
    payload = {
        "embeds": [{
            "title": "🚨 Stock Alert!",
            "description": str(product),
            "url": product.url,
            "color": 5763719
        }]
    }

    response = requests.post(webhook_url, json=payload)
    response.raise_for_status()