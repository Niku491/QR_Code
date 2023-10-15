import qrcode 

# create a qrcode instance
qr = qrcode.QRCode(
    version=1,

error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# add data to the QR code
data = "Hello, World!"
qr.add_data(data)
qr.make(fit=True)

# create an image from the qrcode
img = qr.make_image(fill_color="black",
back_color="white")

# save the image to a file or display it
img.save("my_qr_code.png")
img.show()