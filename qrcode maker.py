import pyqrcode
import png
from pyqrcode import QRCode

print("welcome to qrcode_generator_by_Vigilante120\n")
link = input("Enter Link.. ")

url = pyqrcode.create(link)

url.svg(input("Enter Filename With .svg extension -> "), scale=10)

url.png(input("Enter Filename With .Png extension -> "), scale=10)

print("Thanks for Using :)")