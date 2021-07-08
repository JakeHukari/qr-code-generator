import os
import qrcode

inital = (input("Enter A URL: "))

img = qrcode.make(initial)
img.show()