from PyPDF3 import PdfFileMerger

class MergePDF():
    def merge_pdfs(self,paths:list):
        merger = PdfFileMerger()


        for file_name in paths:
            merger.append(file_name)

        merger.write("merged.pdf")
        merger.close()
        return




