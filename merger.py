from pypdf import PdfMerger

class PDFMerger:
    def __init__(self) -> None:
        self.merger = PdfMerger()
        self.files = []
        self.hasMerged = False

    
    def set_files(self, files: list[str]):
        self.files = files
        self.hasMerged = False

    def add_file(self, file: str):
        self.files.append(file)
    

    def get_files_names(self) -> list[str]:
        print(self.files)
        return map(lambda file: file.split("/")[-1], self.files)

    def merge(self) -> tuple[bool, str]:
        if self.hasMerged:
            return False, "Already merged"
        
        if self.files == []:
            return False, "No files selected"
        
        if len(self.files) == 1:
            return False, "Select more than one file"
        
        self.hasMerged = True
        for file in self.files:
            self.merger.append(file)

        return True, "Merged successfully"
        
    
    def save_as(self, path: str):
        if path.endswith(".pdf") == False:
            path += ".pdf"

        self.merger.write(path)

    def clear(self):
        self.close()
        self.merger = PdfMerger()
        self.files = []
        self.hasMerged = False
    

    def close(self):
        self.merger.close()
        self.files = []


