import qrcode
from PIL import Image, ImageDraw

def create_earth_logo(size=100):
    """Creates a simple Earth logo with blue oceans and green landmasses."""
    img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Draw Earth (blue circle)
    draw.ellipse((0, 0, size, size), fill=(0, 102, 204))  # Blue ocean

    # Draw simplified continents (green blobs)
    land_color = (34, 139, 34)
    draw.ellipse((size * 0.2, size * 0.1, size * 0.4, size * 0.3), fill=land_color)
    draw.ellipse((size * 0.6, size * 0.2, size * 0.8, size * 0.4), fill=land_color)
    draw.ellipse((size * 0.4, size * 0.6, size * 0.7, size * 0.8), fill=land_color)

    return img

def create_qr_with_logo(data="Hello, World!Hello, World!Hello, World!Hello, World!", logo_size_ratio=5):
    """Generates a QR code and embeds the Earth logo in the center."""
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H  # High error correction
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white").convert("RGBA")

    # Create and resize the Earth logo
    logo = create_earth_logo()
    logo_size = min(qr_img.size) // logo_size_ratio  # Reduce logo size
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    # Calculate position and paste the logo in the center
    pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)
    qr_img.paste(logo, pos, mask=logo)

    return qr_img

# Generate QR code with the Earth logo
qr_with_logo = create_qr_with_logo()
qr_with_logo.show()  # Display the QR code
qr_with_logo.save("qr_with_earth_logo.png")  # Save the QR code
