from pypdf import PdfReader, PdfWriter

class CompressPDF():
    def compressPDF(self,path:str,Quality:int,name:str):
        reader = PdfReader(path)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        name=name[:-4]
        for page in writer.pages:
            for img in page.images:
                img.replace(img.image,quality=Quality)
            page.compress_content_streams() 
        with open(name+" compressed.pdf", "wb") as f:
            writer.write(f)
        return
    


