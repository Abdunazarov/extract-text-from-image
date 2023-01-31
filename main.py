# import PyPDF2


# def extract_text_from_pdf(pdf_file: str) -> str:
#     with open(pdf_file, 'rb') as pdf:
#         reader = PyPDF2.PdfReader(pdf, strict=False)
#         pdf_text = []

#         for page in reader.pages:
#             content = page.extract_text()
#             pdf_text.append(content)

#         return pdf_text    


# extracted_text = extract_text_from_pdf('polis.pdf')

# for text in extracted_text:
#     print(text)





from PIL import Image
import pytesseract

file = Image.open('polis.jpg')
str = pytesseract.image_to_string(file, lang='rus')

print(str)

# crop/resize the image 
# ask to generate the image in a bigger size