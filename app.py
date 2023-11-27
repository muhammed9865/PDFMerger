import tkinter as tk
from tkinter.messagebox import showinfo
from merger import PDFMerger
from file_dialog import FileDialog

class App:
    def __init__(self) -> None:
        self.window = tk.Tk(
            screenName="MergGradPdfProject"
        )
        self.window.wm_title("MergGradPdfProject")
        self.window.geometry("500x500")
        self.window.configure(bg="white")
        self.filedialog = FileDialog()

        self.pdfMerger = PDFMerger()
        self.init()

        # Close merger on window close
        self.window.protocol("WM_DELETE_WINDOW", lambda: self.pdfMerger.close() or self.window.destroy())

        self.window.mainloop()


    def select_file(self) -> str:
        """Opens a file dialog and returns a list of file paths"""
        file = self.filedialog.select_file(
            title="Select PDF Files",
            extension="pdf"
        )

        return file
    
    def select_result_file(self) -> str:
        """Opens a file dialog and returns a file path"""
        file = self.filedialog.save_as(
            title="Select Result File",
        )

        return file
    
    def on_select_files_clicked(self):
        file = self.select_file()
        self.pdfMerger.add_file(file)
        self.filesNamesLabel["text"] = ", ".join(self.pdfMerger.get_files_names())
        self.mergeButton["state"] = "normal"

    
    def on_merge_clicked(self):
        isSuccess, message = self.pdfMerger.merge()
        
        color = "green" if isSuccess else "red"
        self.mergeStatus["text"] = message
        self.mergeStatus["fg"] = color
        self.mergeButton["state"] = "disabled" if isSuccess else "normal"
        

    def on_save_clicked(self):
        file = self.filedialog.save_as(
            title="Save Result file as",
            extension="pdf"
        )
        showinfo("Saved", "Saved successfully!")
        self.pdfMerger.save_as(file)
        self.pdfMerger.clear()
        self.filesNamesLabel["text"] = ""
        self.mergeStatus["text"] = ""
        self.mergeButton["state"] = "normal"


    def init(self):
        # Create widgets
        # Label
        headline = tk.Label(text="Hello, welcome to MergGradPdfProject!", font= ("Arial", 20),
                            fg="black", bg="white")
        headline.pack()

        # Add margin
        tk.Label(text="", height=2, width=0, bg="white").pack()

        # Select Files button
        self.selectFilesButton = tk.Button(
            text="Add a file",
            fg="black",
            bg="yellow",
            font= ("Arial", 20),
            width=20,
            borderwidth=5,
            command= self.on_select_files_clicked
        ).pack()

        # Add files names Label
        self.filesNamesLabel = tk.Label(text="", font= ("Arial", 14), fg="black", bg="white")
        self.filesNamesLabel.pack()

        # Add margin
        tk.Label(text="", height=2, width=0, bg="white").pack()

        # Merge button
        self.mergeButton = tk.Button(
            text="Merge",
            fg="black",
            bg="green",
            font= ("Arial", 20),
            width=20,
            borderwidth=5,
            command=self.on_merge_clicked
        )
        self.mergeButton.pack()

        self.mergeStatus = tk.Label(text="", font= ("Arial", 14), fg="black", bg="white")
        self.mergeStatus.pack()

         # Add margin
        tk.Label(text="", height=2, width=0, bg="white").pack()

        self.saveAsButton = tk.Button(
            text="Save Merged File As",
            fg="white",
            bg="blue",
            font= ("Arial", 16),
            command= self.on_save_clicked
        ).pack()


if __name__ == "__main__":
    app = App()