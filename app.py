import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

import os
import Indexer
import Retriever

DB_FILE = "PPlqqUxaMfzL.json"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Search Engine")

        self.image_labels = []

        if not os.path.exists(DB_FILE):
            self.show_init_screen()
        else:
            self.show_search_screen()

    def show_init_screen(self):
        self.clear()

        tk.Label(self.root, text="No image database found. Initialize:").pack()
        tk.Button(self.root, text="Choose Image Folder", command=self.init_db).pack()

    def init_db(self):
        folder = filedialog.askdirectory()
        if folder:
            Indexer.createDB(folder)
            messagebox.showinfo("Done", "Image DB created!")
            self.show_search_screen()

    def show_search_screen(self):
        self.clear()

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack()

        tk.Button(self.root, text="Search", command=self.do_search).pack()
        tk.Button(self.root, text="Rebuild DB", command=self.show_init_screen).pack()

        self.frame = tk.Frame(self.root)
        self.frame.pack()

    def do_search(self):
        query = self.entry.get()

        image_paths = Retriever.search(query, DB_FILE, top=5)

        for lbl in self.image_labels:
            lbl.destroy()
        self.image_labels.clear()

        for path in image_paths:
            img = Image.open(path)
            img.thumbnail((200, 200))

            tk_img = ImageTk.PhotoImage(img)

            lbl = tk.Label(self.frame, image=tk_img)
            lbl.image = tk_img  # prevent garbage collection
            lbl.pack(side="left", padx=10)

            self.image_labels.append(lbl)

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()