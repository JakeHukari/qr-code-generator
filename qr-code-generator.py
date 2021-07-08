import os
import qrcode

os.system('cls')
initial = (input("Enter A URL: "))

img = qrcode.make(initial)
img.show()