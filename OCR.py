from PIL import Image
#from PIL import ImageFilter
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open('test.png')
#new_size = tuple(2*x for x in img.size)
#img = img.filter(ImageFilter.DETAIL)

text = pytesseract.image_to_string(img , lang = 'chi_tra')

print(text)
