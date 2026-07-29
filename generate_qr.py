#!/usr/bin/env python3
"""Generate a QR code PNG that links to the landing page."""

import qrcode
import os

# ---------- Configuration ----------
# Replace this URL with your actual hosted URL
# For local testing, use: http://127.0.0.1:8000
TARGET_URL = "https://your-domain.com"

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qr_code.png")

# ---------- Generate QR Code ----------
qr = qrcode.QRCode(
    version=None,         # auto-detect size
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30% error correction
    box_size=10,
    border=4,
)

qr.add_data(TARGET_URL)
qr.make(fit=True)

img = qr.make_image(fill_color="#1e293b", back_color="white")
img.save(OUTPUT_PATH)

print(f"QR code saved to: {OUTPUT_PATH}")
print(f"QR code points to: {TARGET_URL}")
print(f"Image size: {img.size[0]}x{img.size[1]} px")
