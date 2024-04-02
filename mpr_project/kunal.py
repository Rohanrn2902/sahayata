import tkinter as tk
from PIL import ImageTk, Image
import customtkinter as ctk

root = tk.Tk()
root.title("Image Scroll")
root.geometry("700x500")

framescr= ctk.CTkScrollableFrame(root)
framescr.place(x=0,y=0)
 
def show_images(frame, image_paths):
    for i, path in enumerate(image_paths):
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)

        label = ctk.CTkLabel(frame, image=photo)
        label.image = photo
        label.pack(padx=5, pady=5)

image_paths = [
    r"C:\tensorflow\mpr_project\kunal\py_logo.png",
    r"C:\tensorflow\mpr_project\kunal\hamburger.png",
    r"C:\tensorflow\mpr_project\kunal\hamburger.png",
    r"C:\tensorflow\mpr_project\kunal\hamburger.png",
    r"C:\tensorflow\mpr_project\kunal\py_logo.png",
    r"C:\tensorflow\mpr_project\kunal\hamburger.png",
    r"C:\tensorflow\mpr_project\kunal\py_logo.png",
    r"C:\tensorflow\mpr_project\kunal\hamburger.png",
    r"C:\tensorflow\mpr_project\kunal\py_logo.png",
    r"C:\tensorflow\mpr_project\kunal\hamburger.png",
    r"C:\tensorflow\mpr_project\kunal\py_logo.png",
    r"C:\tensorflow\mpr_project\kunal\hamburger.png",
    r"C:\tensorflow\mpr_project\kunal\py_logo.png",
    r"C:\tensorflow\mpr_project\kunal\hamburger.png",
    r"C:\tensorflow\mpr_project\kunal\py_logo.png",
    r"C:\tensorflow\mpr_project\kunal\hamburger.png",
]

show_images(framescr, image_paths)

root.mainloop()
