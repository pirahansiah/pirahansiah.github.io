import qrcode


# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file in the writable directory
file_path = 'chat_openai_inspirer_qr.png'
img.save(file_path)

# Provide the path to the saved image
file_path
