import cv2
from pyzbar.pyzbar import decode

def read_qr_code(image_path):
    """Reads a QR code from an image file."""
    img = cv2.imread(image_path)
    qr_codes = decode(img)

    for qr in qr_codes:
        data = qr.data.decode("utf-8")  # Decode QR data
        print("QR Code Data:", data)
        return data  # Return first QR data found

    print("No QR code found.")
    return None

# Example usage
read_qr_code("hello_world_qr.png")  # Replace with your image path
