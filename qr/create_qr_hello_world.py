import qrcode

# Generate QR code
qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data("Hello, World!")
qr.make(fit=True)

# Create and show the QR code
img = qr.make_image(fill="black", back_color="white")
img.show()  # Display the QR code
img.save("hello_world_qr.png")  # Save as an image
