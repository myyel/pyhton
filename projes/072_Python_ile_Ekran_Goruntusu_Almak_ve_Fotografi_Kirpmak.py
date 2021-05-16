from PIL import Image, ImageGrab
import pytesseract

ImageGrab.grab().save("C:/Users/Casper/Desktop/img.png")

img=Image.open("C:/Users/Casper/Desktop/img.png")

kirp=img.crop((210,150,1200,650))

text= pytesseract.image_to_string(kirp)

print(text)

Image._show(kirp)


