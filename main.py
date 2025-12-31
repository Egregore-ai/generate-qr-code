import json
import qrcode
import qrcode_terminal
from io import BytesIO
from typing import Tuple, Dict, Any

def create_auth_qr_data(url: str, secret_key: str) -> str:
    """
    Creates a JSON payload containing URL and SECRET_KEY, suitable for QR encoding.
    Pure function: no side effects, deterministic.
    """
    payload: Dict[str, str] = {
        "url": url,
        "secret_key": secret_key
    }
    return json.dumps(payload, separators=(',', ':'))  # compact JSON, no whitespace


def generate_qr_code(data: str) -> bytes:
    """
    Generates a QR code (as PNG bytes) from input string data.
    Pure function in spirit — but IO-bound operation (image generation).
    Accepts only data, returns only bytes — no mutation or external state.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Use in-memory bytes buffer (no disk I/O unless caller chooses to save)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return buffer.getvalue()


def qr_pipeline(url: str, secret_key: str) -> Tuple[str, bytes]:
    """
    End-to-end functional pipeline:
      1. Build JSON payload
      2. Encode as QR code (PNG bytes)
    Returns both the raw JSON string and the QR image bytes.
    """
    json_data = create_auth_qr_data(url, secret_key)
    qr_bytes = generate_qr_code(json_data)
    return json_data, qr_bytes


# Example usage (not part of pure logic — only for demo):
if __name__ == "__main__":
    import secrets

    # Your provided helper
    def generate_secret_key(length: int = 64) -> str:
        return secrets.token_urlsafe(length)

    url = "http://localhost:8080/"
    secret_key = generate_secret_key(64)

    json_payload, qr_png_bytes = qr_pipeline(url, secret_key)
    
    # Display QR code in terminal
    print("\n📋 QR Code in Terminal:")
    qrcode_terminal.draw(json_payload)

    print("✅ JSON Payload (scannable content):")
    print(json_payload)
    print("\n✅ QR PNG size:", len(qr_png_bytes), "bytes")

    # Optional: save to file for testing
    with open("auth_qr.png", "wb") as f:
        f.write(qr_png_bytes)
    print("\n💾 QR code saved as 'auth_qr.png'")