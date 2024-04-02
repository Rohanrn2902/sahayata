import tkinter as tk
from PIL import Image, ImageTk
import os

top = tk.Tk()
top.geometry("1000x800")

panel = tk.Frame(top, bg="lightblue", relief="raised", borderwidth=2)
panel.pack(padx=200, pady=200, fill="both", expand=True)

gif_frames = []
frame_delay = 0
frame_count = 0
current_gif_index = 0  
gif_lb = None
i=0


def box():
    global frame_count, current_gif_index
    text = str(e1.get()).lower()
    words = text.split()
    directory = r"C:\tensorflow\mpr_project\aplhabets\filtered_data"
    directory2 = r"C:\tensorflow\mpr_project\aplhabets\alphabet"
    matching_files = []
    frame_count = 0
    current_gif_index = 0

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

    if matching_files:
        ready_gif(matching_files)
        current_string(matching_files)
    else:
        print("No matching files found.")




def ready_gif(file_paths):
    global frame_delay, gif_frames, frame_count,current_gif_index,i
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
    else:
        print("No frames loaded.")

def play_gif():
    global frame_count, gif_lb
    if gif_lb is None:
        gif_lb = tk.Label(panel)
        gif_lb.pack()
        gif_lb.place(x=20, y=30, width=300,height=200)

    frame_count = (frame_count + 1) % len(gif_frames[current_gif_index])

    try:
        current_frame = ImageTk.PhotoImage(gif_frames[current_gif_index][frame_count])
        gif_lb.config(image=current_frame)
        gif_lb.image = current_frame

        top.after(frame_delay, play_gif)
    except Exception as e:
        print(f"Error displaying frame: {e}")

def next_gif(event=None):
    global frame_count, current_gif_index
    if gif_frames and len(gif_frames) > 1: 
        current_gif_index = (current_gif_index + 1) % len(gif_frames)
        frame_count = 0

        top.focus_set()

def current_string(matching_files):
    for file_path in matching_files:
        file_name = os.path.basename(file_path)
        file_r_name = file_name[:-4]
        tk.Label(top, text=file_r_name.upper()).place(x=0, y=200)  
    
    

txt = tk.Label(top, text="Enter Text here")
txt.place(x=30, y=60)
e1 = tk.Entry(top)
e1.place(x=160, y=60)
convert = tk.Button(top, text="Convert", command=box)
convert.place(x=50, y=90)

top.bind("<space>", next_gif)

top.mainloop()
