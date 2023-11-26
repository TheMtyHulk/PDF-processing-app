    
from pdf2docx import Converter

class PDF2DOCX():
    def convert_pdf_to_docx(self,pdf_file:str,name:str):
        name=name[:-4]
        cv = Converter(pdf_file)
        docx_file=name+".docx"
        cv.convert(docx_file, start=0, end=None)
        cv.close()
        return

 