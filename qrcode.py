import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10, border = 4)

QRurl = input("Provide link for qr generation: ")
qr.add_data(QRurl)
qr.make(fit=True)
fillColor = input("Provide color inside QR code: ")
backColor = input("Provide color background of QR code: ")
img = qr.make_image(fill_color = fillColor, back_color = backColor)
name  = input("Provide name of your QR code  image (include .png): ")
img.save(name)