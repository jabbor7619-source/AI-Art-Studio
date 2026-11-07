
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageOps, ImageTk

class ArtStudio:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Art Studio - Drawing Tools")
        self.root.geometry("900x650")
        self.image = None
        self.preview = None

        toolbar = tk.Frame(root)
        toolbar.pack(pady=12)

        tk.Button(toolbar, text="Open Image",
                  command=self.open_image).pack(side="left", padx=5)
        tk.Button(toolbar, text="Grayscale",
                  command=self.grayscale).pack(side="left", padx=5)
        tk.Button(toolbar, text="Save Image",
                  command=self.save_image).pack(side="left", padx=5)

        self.canvas = tk.Label(root, text="Open an image to begin")
        self.canvas.pack(expand=True, fill="both", padx=20, pady=20)

    def open_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp")]
        )
        if path:
            try:
                with Image.open(path) as img:
                    self.image = img.convert("RGB")
                self.show_image()
            except Exception as error:
                messagebox.showerror("Error", str(error))

    def show_image(self):
        if self.image is None:
            return
        preview = self.image.copy()
        preview.thumbnail((800, 500))
        self.preview = ImageTk.PhotoImage(preview)
        self.canvas.config(image=self.preview, text="")

    def grayscale(self):
        if self.image is not None:
            self.image = ImageOps.grayscale(self.image)
            self.show_image()

    def save_image(self):
        if self.image is None:
            messagebox.showwarning("Warning", "Open an image first")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG", "*.png")]
        )
        if path:
            try:
                self.image.save(path)
                messagebox.showinfo("Success", "Image saved")
            except Exception as error:
                messagebox.showerror("Error", str(error))

if __name__ == "__main__":
    root = tk.Tk()
    ArtStudio(root)
    root.mainloop()

