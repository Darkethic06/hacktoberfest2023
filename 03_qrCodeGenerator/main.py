import qrcode 
from PIL import Image

qr = qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_H, box_size=10, border=4)

url = input("Enter Your URL: ")

qr.add_data(url)

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("qr.png")

