from newspaper import Article
from PIL import Image
import fitz
from docx2pdf import convert
from pytesseract import pytesseract
import os
import pythoncom
import win32com.client

# Component used for data extraction from text.
def extract(type, link):
    tmp_type = ""
    if type == 1:  # Article link
        # url = "https://www.gadgetsnow.com/tech-news/india-becomes-the-first-country-in-asia-pacific-to-use-satellite-navigation-to-land-aircrafts/articleshow/91172431.cms"
        url = link
        article = Article(url)
        article.download()
        article.parse()
        result = article.text
        tmp_type = "Article"
    elif type == 2:  # Image taken
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        # image_path = r"assets\footercredits.png"
        image_path = link
        img = Image.open(image_path)
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(img)
        result = text[:-1]
        tmp_type = "Image"
    elif type == 3:  # PDF file
        # pdfFileObj = open("example.pdf", "rb")
        fileObj = fitz.open(link)
        result = ""
        for page in fileObj:
            result += page.get_text() + chr(12)
        tmp_type = "PDF"
        result = result.encode("ascii", "ignore")
        result = result.decode()
        result = result.replace("\x92", "")
        result = result.replace("\x0c", "")
        tmp_type = "PDF"
    elif type == 4:  # Document file
        xl = win32com.client.Dispatch("Word.Application", pythoncom.CoInitialize())
        convert(link, output_path="temp/output.pdf")
        tmp_type = "Document"
        link = "temp/output.pdf"
        fileObj = fitz.open(link)
        result = ""
        for page in fileObj:
            result += page.get_text() + chr(12)
        tmp_type = "PDF"
        result = result.encode("ascii", "ignore")
        result = result.decode()
        result = result.replace("\x92", "")
        result = result.replace("\x0c", "")
        fileObj.close()
        os.remove("temp/output.pdf")
    else:
        return {"error": "Invalid type"}
    result = " ".join(result.splitlines())
    return {"type": tmp_type, "link": link, "content": result}
