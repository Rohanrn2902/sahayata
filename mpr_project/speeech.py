import tkinter as tk
from PIL import Image, ImageTk
from customtkinter import *
import os

top = tk.Tk()
top.geometry("1100x700")
top.config(bg="White")



tabview = CTkFrame(master=top,fg_color="#1F2354",width=1100, height=700)
tabview.pack()


background_image = Image.open(r"C:\tensorflow\mpr_project\hello.png")
background_image = background_image.resize((1100, 700))
background_photo = ImageTk.PhotoImage(background_image)


background_label = tk.Label(tabview, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

background_image1 = Image.open(r"C:\tensorflow\mpr_project\hello1.png")
background_image1 = background_image1.resize((850, 500))
background_photo1 = ImageTk.PhotoImage(background_image1)

panel = CTkFrame(master=tabview, bg_color="transparent",fg_color="#6A1C56", corner_radius=50, width=850, height=490)
panel.place(x=100,y=200)
panel.lift()




background_label1 = tk.Label(panel, image=background_photo1)
background_label1.place(x=0, y=0, relwidth=1, relheight=1)
background_label1.lower()

matching_files = []
gif_frames = []
frame_delay = 0
frame_count = 0
current_gif_index = 0  
gif_lb = None
current_index =0

def box():
    global frame_count, current_gif_index,matching_files,current_index
    text = str(e1.get()).lower()
    words = text.split()
    directory = r"C:\tensorflow\mpr_project\aplhabets\filtered_data"
    directory2 = r"C:\tensorflow\mpr_project\aplhabets\alphabet"
    matching_files = []
    frame_count = 0
    current_gif_index = 0
    current_index =0

    for word in words:
        filename = word + ".gif"
        if os.path.isfile(os.path.join(directory, filename)):
            matching_files.append(os.path.join(directory, filename))
        else:
            char_files = []
            for char in word:
                char_filename = char + ".gif"
                if os.path.isfile(os.path.join(directory2, char_filename)):
                    char_files.append(os.path.join(directory2, char_filename))
            if char_files:
                matching_files.extend(char_files)
            else:
                print(f"No GIF found for word or character: {word}")

    print(matching_files)

    if matching_files:
        ready_gif(matching_files)
    else:
        print("No matching files found.")




def ready_gif(file_paths):
    global frame_delay, gif_frames, frame_count,current_gif_index
    gif_frames.clear()
    frame_count = 0
    current_gif_index = 0  
    

    for file_path in file_paths:
        print("Started for", file_path)
        try:
            gif_file = Image.open(file_path)
            gif_frames.append([]) 
            i=0 
            for r in range(0, gif_file.n_frames):
                gif_file.seek(r)
                gif_frames[-1].append(gif_file.copy())
                i=0
            frame_delay = gif_file.info['duration']
            print('Complete')
        except Exception as e:
            print(f"Error loading file {file_path}: {e}")
    if gif_frames:
        play_gif()
        file_path = matching_files[current_index]
        file_name = os.path.basename(file_path)[:-4].upper()
        letter = CTkLabel(master=panel, text=file_name)
        letter.place(x=100, y=0)
    else:
        print("No frames loaded.")

def play_gif():
    global frame_count, gif_lb
    if gif_lb is None:
        gif_lb = tk.Label(panel,bg="#6A1C56")
        gif_lb.pack()
        gif_lb.place(x=50, y=50, width=410,height=275)
        

    frame_count = (frame_count + 1) % len(gif_frames[current_gif_index])
    try:
        current_frame = ImageTk.PhotoImage(gif_frames[current_gif_index][frame_count])
        gif_lb.config(image=current_frame)
        gif_lb.image = current_frame
        top.after(frame_delay, play_gif)
    except Exception as e:
        print(f"Error displaying frame: {e}")

def next_gif(event=None):
    global frame_count, current_gif_index, matching_files, current_index
    if matching_files:  
        current_index = (current_index + 1) % len(matching_files)
        
        file_path = matching_files[current_index]
        file_name = os.path.basename(file_path)[:-4].upper()
        letter = CTkLabel(master=panel, text=file_name+"                 ")
        letter.place(x=100, y=0)
        current_gif_index = (current_gif_index + 1) % len(gif_frames)
        frame_count = 0
        top.focus_set()
           
txt = CTkLabel(
    master=tabview,
    text="Enter Text here:",
    bg_color="transparent",
    text_color="white",
    font=("Arial", 36)  
)
txt.place(x=140, y=140)
e1 = CTkEntry(
    master=tabview,
    width=300,
    height=40,
    border_width=2,
    corner_radius=10,
    fg_color="white",
    text_color="black",
    font=("Arial Rounded MT", 26),  
    border_color="#DDDDDD"  
)
e1.place(x=400, y=140) 
convert = CTkButton(
    master=tabview,
    text="Convert",
    command=box,  
    width=150,  
    height=40, 
    fg_color="#cd4a71",   
    bg_color="transparent",
    border_width=0,
    border_color="white",
    corner_radius=100  
)
convert.place(x=725, y=140)

def on_enter(event):
    convert.configure(fg_color=("white"),text_color="black")  

def on_leave(event):
    convert.configure(fg_color="#6A1C56",text_color="white")  

convert.bind("<Enter>", on_enter)
convert.bind("<Leave>", on_leave)

top.bind("<space>", next_gif)

top.mainloop()
