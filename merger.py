from pypdf import PdfMerger

class PDFMerger:
    def __init__(self) -> None:
        self.merger = PdfMerger()
        self.files = []

    
    def add_file_path(self, file: str):
        self.files.append(file)

    
    def add_files(self, files: list[str]):
        self.files.extend(files)
    

    def merge(self) -> bool:
        for file in self.files:
            self.merger.append(file)
        
    
    def save_as(self, path: str):
        if path.endswith(".pdf") != True:
            raise ValueError()
        
        self.merger.write(path)
        self.merger.close()


