import os
import qrcode

os.system('cls')
initial = (input("Enter A URL or qr code data: "))

img = qrcode.make(qr)
img.show()