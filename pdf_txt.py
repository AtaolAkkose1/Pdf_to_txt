from pdf2image import convert_from_path
import pytesseract, os
from PIL import Image

def PDF_to_txt(PDF_file_path=None):

    pages = convert_from_path(PDF_file_path, poppler_path= r'C:\Program Files\poppler-21.11.0\Library\bin') # Firstly you have to download poppler and pdf2image modules
                                                                                                            # Go to " https://poppler.freedesktop.org/ " and download last version.
                                                                                                            # And then move " poppler-.... " folder to C:\Program Files\
                                                                                                            # Download via terminal that  " pip install python-poppler "
                                                                                                            # And  " pip install pdf2image "
    image_counter = 1

    for page in pages:
        filename = "page_" + str(image_counter) + ".jpg"
        page.save(filename, 'JPEG')
        image_counter = image_counter + 1

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"                 # like pdf2image, firstly you have to download pytesseract modules
                                                                                                            # Go to " https://github.com/UB-Mannheim/tesseract/wiki " and download last version.
                                                                                                            # And then install folders to C:\Program Files\
                                                                                                            # Download via terminal that  " pip install pytesseract "
    for i in range(1, image_counter):
        img = Image.open(f'page_{i}.jpg')
        data = pytesseract.image_to_string(img, lang='eng', config='--psm 6')
        print(data,file=open('extract-text.txt',"a"))

    for i in range(1, image_counter):
        os.remove(f'page_{i}.jpg')

    os.open(path='extract-text.txt', flags=1)


PDF_to_txt(PDF_file_path="".pdf')
