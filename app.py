import tkinter as tk
from tkinter import filedialog
from merger import PDFMerger
class App:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title = "PDF Merger"
        self.window.geometry("500x500")
        self.window.configure(bg="white")

        self.pdfMerger = PDFMerger()
        self.init()

        self.window.mainloop()


    def selectFiles(self) -> list[str]:
        """Opens a file dialog and returns a list of file paths"""
        files = filedialog.askopenfilenames(
            title="Select PDF Files",
            filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*"))
        )

        return files


    def init(self):
        # Create widgets
        # Label
        headline = tk.Label(text="Hello, welcome to PDF Merger!", font= ("Arial", 24),
                            fg="black", bg="white")
        headline.pack()

        # Add margin
        tk.Label(text="", height=2, width=0, bg="white").pack()

        # Select Files button
        self.selectFilesButton = tk.Button(
            text="Select PDF Files",
            fg="black",
            bg="yellow",
            font= ("Arial", 20),
            width=20,
            borderwidth=5,
            command= lambda: self.pdfMerger.add_files(self.selectFiles())
        ).pack()

        # Add margin
        tk.Label(text="", height=2, width=0, bg="white").pack()


        self.mergeButton = tk.Button(
            text="Merge",
            fg="black",
            bg="green",
            font= ("Arial", 20),
            width=20,
            borderwidth=5,
            command= lambda: self.pdfMerger.merge()
        )


