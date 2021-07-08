import os
import qrcode

initial = (input("Enter A URL: "))

img = qrcode.make(initial)
img.show()