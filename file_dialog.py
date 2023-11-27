from tkinter import filedialog

class FileDialog:

    def select_files(self, title, extension) -> list[str]:
        """Opens a file dialog and returns a list of file paths"""
        files = filedialog.askopenfilenames(
            title=title,
            filetypes=[(f"{extension.upper()} Files", f"*.{extension}")]
        )

        return files
    
    def select_file(self, title, extension) -> str:
        file = filedialog.askopenfile(
            title=title,
            filetypes=[(f"{extension.upper()} Files", f"*.{extension}")]
        ).name

        return file
    
    def save_as(self, title, extension) -> str:
        """Opens a file dialog and returns a file path"""
        file = filedialog.asksaveasfilename(
            title=title,
            filetypes=[(f"{extension.upper()} Files", f"*.{extension}")]
        )

        return file