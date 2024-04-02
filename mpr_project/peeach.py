import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import customtkinter as ctk
import os
import pyttsx3
#from autocorrect import Speller
from googletrans import Translator, LANGUAGES
from ttkthemes import ThemedStyle

top = ctk.CTk()
#top.overrideredirect(True)
top.geometry("1100x700+200+100")
top.title("सहायता")
top.config(bg="White")

style = ThemedStyle(top)
style.set_theme("breeze")

def show_home():
    tab1.lift()
    tab2.lower()
    home.configure(text_color="yellow") 
    sign_reco.configure(text_color="white")  
    sign_text.configure(text_color="white")
    translate.configure(text_color="white")
    catalogue.configure(text_color="white")
    home_label.configure(text_color="yellow",fg_color="yellow")
    sign_label.configure(text_color="#3059F3",fg_color="#3059F3")
    text_label.configure(text_color="#3059F3",fg_color="#3059F3")
    trans_label.configure(text_color="#3059F3",fg_color="#3059F3")
    cat_label.configure(text_color="#3059F3",fg_color="#3059F3")

def show_sign():
    tab2.lift()
    tab1.lower()
    tab3.lower()
    tab4.lower()
    tab5.lower()
    sign_reco.configure(text_color="yellow") 
    home.configure(text_color="white")  
    sign_text.configure(text_color="white")
    translate.configure(text_color="white")
    catalogue.configure(text_color="white")
    home_label.configure(text_color="#3059F3",fg_color="#3059F3")
    sign_label.configure(text_color="yellow",fg_color="yellow")
    text_label.configure(text_color="#3059F3",fg_color="#3059F3")
    trans_label.configure(text_color="#3059F3",fg_color="#3059F3")
    cat_label.configure(text_color="#3059F3",fg_color="#3059F3")

def show_text():
    tab3.lift()
    sign_text.configure(text_color="yellow") 
    home.configure(text_color="white")  
    translate.configure(text_color="white")
    sign_reco.configure(text_color="white")
    catalogue.configure(text_color="white")
    home_label.configure(text_color="#3059F3",fg_color="#3059F3")
    sign_label.configure(text_color="#3059F3",fg_color="#3059F3")
    text_label.configure(text_color="yellow",fg_color="yellow")
    trans_label.configure(text_color="#3059F3",fg_color="#3059F3") 
    cat_label.configure(text_color="#3059F3",fg_color="#3059F3")

def show_trans():
    tab4.lift()
    translate.configure(text_color="yellow")
    sign_text.configure(text_color="white") 
    home.configure(text_color="white")  
    sign_reco.configure(text_color="white")
    catalogue.configure(text_color="white")
    home_label.configure(text_color="#3059F3",fg_color="#3059F3")
    sign_label.configure(text_color="#3059F3",fg_color="#3059F3")
    trans_label.configure(text_color="yellow",fg_color="yellow")
    text_label.configure(text_color="#3059F3",fg_color="#3059F3")
    cat_label.configure(text_color="#3059F3",fg_color="#3059F3")

def show_cat():
    tab5.lift()
    translate.configure(text_color="white")
    sign_text.configure(text_color="white") 
    home.configure(text_color="white")  
    sign_reco.configure(text_color="white")
    catalogue.configure(text_color="yellow")
    home_label.configure(text_color="#3059F3",fg_color="#3059F3")
    sign_label.configure(text_color="#3059F3",fg_color="#3059F3")
    trans_label.configure(text_color="#3059F3",fg_color="#3059F3")
    text_label.configure(text_color="#3059F3",fg_color="#3059F3")
    cat_label.configure(text_color="yellow",fg_color="yellow")


tabview = ctk.CTkFrame(master=top,fg_color="#3059F3",width=1100, height=100,corner_radius=0)
tabview.place(x=0,y=0)

tabside1 = ctk.CTkFrame(master=top,fg_color="#3059F3",width=200, height=10,corner_radius=0)
tabside1.place(x=0,y=99.5)
tabside2 = ctk.CTkFrame(master=top,fg_color="#3059F3",width=200, height=10,corner_radius=0)
tabside2.place(x=900,y=99.5)

logo_label= ctk.CTkLabel(master=tabview,text="SAHAYATA",fg_color="#3059F3", text_color = "#ffffff" ,font=("Arial",24,"bold"))
logo_label.place(x=44,y=39)



image= tk.PhotoImage(file= r"./exit.png")
button = tk.Button(tabview, image=image)
#button.place(x=1000,y=20)

tab5 = ctk.CTkFrame(master=top,fg_color="#3059F3",width=1100, height=600,corner_radius=0)
tab5.place(x=0,y=100.5)
tab4 = ctk.CTkFrame(master=top,fg_color="#3059F3",width=1100, height=600,corner_radius=0)
tab4.place(x=0,y=100.5)
tab2 = ctk.CTkFrame(master=top,fg_color="#3059F3",width=1100, height=600,corner_radius=0)
tab2.place(x=0,y=100.5)
tab3 = ctk.CTkFrame(master=top,fg_color="#3059F3",width=1100, height=600,corner_radius=0)
tab3.place(x=0,y=100.5)
tab1 = ctk.CTkFrame(master=top,fg_color="#3059F3",width=1100, height=600,corner_radius=0)
tab1.place(x=0,y=100.5)


background_image = Image.open(r"./back.png")
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(tab1, image=background_photo, borderwidth=0)
background_label.place(x=235, y=100)

desc_label=ctk.CTkLabel(master=tab1,text="Everyone Deserves to Be Heard",fg_color="#3059F3", text_color = "#ffffff",font=("Arial",24,"bold"))
desc_label.place(x=350,y=350)

desc_label1 = ctk.CTkLabel(master=tab1, text="Let's build a society where all voices are valued and communication is accessible.Bridge the gap and create a world where everyone can connect.", fg_color="#3059F3", text_color = "#ffffff", font=("Arial", 18), wraplength=650, justify="center")
desc_label1.place(x=250,y=410)



home_label= ctk.CTkLabel(
    master=tabview,
    text="________",
    fg_color="yellow",   
    bg_color="#3059F3",
    font=("Arial",16,"bold"),
    text_color="#3059F3"
    )
home_label.place(x=220, y=96)
sign_label= ctk.CTkLabel(
    master=tabview,
    text="___________________",
    fg_color="#3059F3",   
    bg_color="#3059F3",
    font=("Arial",16,"bold"),
    text_color="#3059F3"
    )
sign_label.place(x=315, y=96)
text_label= ctk.CTkLabel(
    master=tabview,
    text="_____________",
    fg_color="#3059F3",   
    bg_color="#3059F3",
    font=("Arial",16,"bold"),
    text_color="yellow"
    )
text_label.place(x=495, y=96)
trans_label= ctk.CTkLabel(
    master=tabview,
    text="___________",
    fg_color="#3059F3",   
    bg_color="#3059F3",
    font=("Arial",16,"bold"),
    text_color="yellow"
    )
trans_label.place(x=645, y=96)
cat_label= ctk.CTkLabel(
    master=tabview,
    text="__________",
    fg_color="#3059F3",   
    bg_color="#3059F3",
    font=("Arial",16,"bold"),
    text_color="yellow"
    )
cat_label.place(x=775, y=96)



home = ctk.CTkButton(
    master=tabview,
    text="Home",
    command=show_home,  
    width=150,  
    height=40, 
    fg_color="#3059F3",   
    bg_color="transparent",
    hover_color="#3059F3", 
    font=("Arial",16,"bold"),
    border_width=0,
    border_color="white",
    text_color="yellow",
    corner_radius=100  
)
home.place(x=180, y=55)
sign_reco = ctk.CTkButton(
    master=tabview,
    text="Sign Recognition",
    command=show_sign,  
    width=150,  
    height=40, 
    fg_color="#3059F3",   
    bg_color="transparent",
    hover_color="#3059F3",
    font=("Arial",16,"bold"), 
    border_width=0  
)
sign_reco.place(x=325, y=55)
sign_text = ctk.CTkButton(
    master=tabview,
    text="Text To Sign",
    command=show_text,  
    width=150,  
    height=40, 
    fg_color="#3059F3",
    hover_color="#3059F3",  
    bg_color="transparent",
    font=("Arial",16,"bold"),
    border_width=0 
)
sign_text.place(x=475, y=55)
translate = ctk.CTkButton(
    master=tabview,
    text="Translate",
    command=show_trans,  
    width=150,  
    height=40, 
    fg_color="#3059F3",   
    bg_color="transparent",
    hover_color="#3059F3",
    font=("Arial",16,"bold"), 
    border_width=0
)
translate.place(x=615,y=55)
catalogue = ctk.CTkButton(
    master=tabview,
    text="Catalogue",
    command=show_cat,  
    width=150,  
    height=40, 
    fg_color="#3059F3",   
    bg_color="transparent",
    hover_color="#3059F3",
    font=("Arial",16,"bold"), 
    border_width=0
)
catalogue.place(x=745,y=55)


def update_text(event):
    entry_text.delete(0, 'end')
    entry_text.insert('end', txt.get())

#aryan parts 
    

def update_and_speak_text(event):
    update_text(event)
    speak_text(event)

# spell = Speller()
text_speech = pyttsx3.init()

text_speech.setProperty('rate', 150)
gender_var = tk.IntVar(value=0)

def speak_text(event=None):
    text1 = txt.get()

    if '@' in text1:
        text1 = text1.split('@')[0]
        txt.delete(0, tk.END)
        # text = spell(text1)
        text_speech.say(text1)
        text_speech.runAndWait()

txt = tk.Entry(tab2)
txt.place(x=50, y=50)
txt.bind('<KeyRelease>', update_and_speak_text)



#rohan part(caution)
panel = ctk.CTkFrame(master=tab3, bg_color="transparent",fg_color="#042f66", corner_radius=50, width=850, height=490)
panel.place(x=150,y=100)
panel.lift()

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
    directory = r"./aplhabets/filtered_data"
    directory2 = r"./aplhabets/alphabet"
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
        letter = ctk.CTkLabel(master=panel, text=file_name+"                 ",font=("Arial",24,"bold"))
        letter.place(x=150, y=50)
    else:
        print("No frames loaded.")

def play_gif():
    global frame_count, gif_lb
    if gif_lb is None:
        gif_lb = tk.Label(panel,bg="#042f66")
        gif_lb.pack()
        gif_lb.place(x=250, y=150, width=410,height=275)
        

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
        letter = ctk.CTkLabel(master=panel, text=file_name+"                 ",font=("Arial",24,"bold"))
        letter.place(x=150, y=50)
        current_gif_index = (current_gif_index + 1) % len(gif_frames)
        frame_count = 0
        top.focus_set()
           
txte = ctk.CTkLabel(
    master=tab3,
    text="Enter Text here:",
    bg_color="transparent",
    text_color="white",
    font=("Arial", 36)  
)
txte.place(x=190, y=40)
e1 = ctk.CTkEntry(
    master=tab3,
    width=300,
    height=40,
    border_width=2,
    corner_radius=10,
    fg_color="white",
    text_color="black",
    font=("Arial Rounded MT", 26),  
    border_color="#DDDDDD"  
)
e1.place(x=455, y=40) 
convert = ctk.CTkButton(
    master=tab3,
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
convert.place(x=780, y=40)

def on_enter(event):
    convert.configure(fg_color=("white"),text_color="black")  

def on_leave(event):
    convert.configure(fg_color="#cd4a71",text_color="white")  

convert.bind("<Enter>", on_enter)
convert.bind("<Leave>", on_leave)

top.bind("<space>", next_gif)


#kunal parts

def translate_text():
    translator = Translator()
    translated = translator.translate(text=entry_text.get(), dest=dest_lang.get())
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, translated.text)
    status_var.set("Translation Successful")


def clear_text():
    entry_text.delete(0, tk.END)
    output_text.delete(1.0, tk.END)
    status_var.set("Text cleared")


def copy_text():
    tab4.clipboard_clear()
    tab4.clipboard_append(output_text.get(1.0, tk.END))
    status_var.set("Text copied to clipboard")

# "radiance", "arc", .
panel_trans = ctk.CTkFrame(master=tab4, bg_color="transparent",fg_color="#042f66", corner_radius=50, width=1000, height=500)
panel_trans.place(x=50,y=50)
panel_trans.lift()

input_frame = ctk.CTkFrame(master=panel_trans, width=500, height=450, fg_color="#042f66")
input_frame.place(x=100,y=50)

output_frame = ctk.CTkFrame(master=panel_trans, width=500, height=450,fg_color="#042f66")
output_frame.place(x=650,y=50)


tk.Label(input_frame, text="Language Translator", font="Arial 25 bold",bg="#3059F3",fg="white").place(x=0,y=0)


tk.Label(master=input_frame, text="Enter Text", font='Arial 15 bold',bg="#042f66",fg="white").place(x=0,y=73)
entry_text = ctk.CTkEntry(input_frame, width=120,fg_color="white")
entry_text.place(x=90,y=62)
entry_text.focus_set()


languages = list(LANGUAGES.values())
dest_lang = ttk.Combobox(input_frame, values=languages, width=25)
dest_lang.set('Choose language')
dest_lang.place(x=100,y=130)


translate_btn = ctk.CTkButton(master=input_frame, text='Translate', command=translate_text)
translate_btn.place(x=00,y=160)

clear_btn = ctk.CTkButton(master=input_frame, text=' Clear ', command=clear_text)
clear_btn.place(x=200,y=160)

tk.Label(output_frame, text=" Output ", font='Arial 15 bold',bg="#042f66",fg="white").place(x=0,y=0)

output_text = tk.Text(output_frame, font='Arial 10', wrap=tk.WORD,  width=50, height=14)
output_text.place(x=0,y=25)

copy_btn = ctk.CTkButton(output_frame, text=' Copy', command=copy_text)
copy_btn.place(x=25,y=250)

status_var = tk.StringVar()
status_bar = tk.Label(tab4, textvariable=status_var, font='Arial 10 italic', anchor=tk.W,bg="#042f66")
status_bar.place(x=200,y=450)


#kunals & rohan catalogue
but_image1 = Image.open(r"./kunal/abcd.png")
but_image2 = Image.open(r"./kunal/abcd1.png")
but_image3 = Image.open(r"./kunal/abcd2.png")

image_width, image_height = but_image1.size
aspect_ratio = image_width / image_height

button_width = 300
button_height = int(button_width / aspect_ratio)  

but_image1 = but_image1.resize((button_width, button_height))
but_image2 = but_image2.resize((button_width, button_height))
but_image3 = but_image3.resize((button_width, button_height))


button_image1 = ImageTk.PhotoImage(but_image1)
button_image2 = ImageTk.PhotoImage(but_image2)
button_image3 = ImageTk.PhotoImage(but_image3)


one_panel= ctk.CTkFrame(master=tab5, bg_color="transparent",fg_color="#3059F3", width=1100, height=600)
one_panel.place(x=0,y=0)
one_panel.lower()


sub_2_panel=ctk.CTkFrame(master=one_panel, bg_color="transparent",fg_color="#042f66", corner_radius=50, width=850, height=490)
sub_2_panel.place(x=150,y=100)

sub_1_panel=ctk.CTkFrame(master=one_panel, bg_color="transparent",fg_color="white", corner_radius=50, width=850, height=490)
sub_1_panel.place(x=150,y=100)

sub_3_panel=ctk.CTkFrame(master=one_panel, bg_color="transparent",fg_color="red", corner_radius=50, width=850, height=490)
sub_3_panel.place(x=150,y=100)

def show_1():
    one_panel.lift()
    sub_1_panel.lift()
    show_images(framescr, image_paths)

def show_2():
    one_panel.lift()
    sub_2_panel.lift()
    show_images(framescr1, image_paths2)

def show_3():
    one_panel.lift()
    sub_3_panel.lift()
    show_images(framescr2, image_paths3)

def show_back():
    tab5.lift()
    one_panel.lower()

button1 = ctk.CTkButton(
    master=tab5,
    image=button_image1,
    text="",
    width=button_width,
    height=button_height,
    border_width=0,
    command=show_1,
    compound="bottom"
)
button1.place(x=100, y=50)

button2 = ctk.CTkButton(
    master=tab5,
    image=button_image2,
    text="",
    width=button_width,
    height=button_height,
    command=show_2,
    border_width=0,
    compound="bottom",
    fg_color="#85eec6"
)
button2.place(x=400, y=50)

button3 = ctk.CTkButton(
    master=tab5,
    image=button_image3,
    text="",
    command=show_3,
    width=button_width,
    height=button_height,
    fg_color="#a080f2",
    border_width=0,
    compound="bottom"
)
button3.place(x=700, y=50)


hello1=ctk.CTkLabel(master=button1,text="Alphabets",bg_color="#76bce8",fg_color="#76bce8",text_color="black")
hello1.place(x=30,y=37)

hell2=ctk.CTkLabel(master=button2,text="0 to 9",bg_color="#80e9c1",fg_color="#80e9c1",text_color="black")
hell2.place(x=30,y=37)

hello3=ctk.CTkLabel(master=button3,text="Most Common words",bg_color="#a080f2",fg_color="#a080f2",text_color="black")
hello3.place(x=30,y=37)


back_one_panel = ctk.CTkButton(
    master=one_panel,
    text="back",
    command=show_back,
    fg_color="#8d68ee",
    border_width=0,
)
back_one_panel.place(x=50, y=50)

framescr= ctk.CTkScrollableFrame(sub_1_panel,width=850, height=490)
framescr.place(x=0,y=0)

framescr1= ctk.CTkScrollableFrame(sub_2_panel,width=850, height=490)
framescr1.place(x=0,y=0)

framescr2= ctk.CTkScrollableFrame(sub_3_panel,width=850, height=490)
framescr2.place(x=0,y=0)
 
def show_images(frame, image_paths):
    for i, path in enumerate(image_paths):
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)

        label = ctk.CTkLabel(frame, image=photo)
        label.image = photo
        label.pack(padx=5, pady=5)

image_paths = [
    r"./aplhabets/alphabet/a.gif",
    r"./aplhabets/alphabet/b.gif",
    r"./aplhabets/alphabet/c.gif",
    r"./aplhabets/alphabet/d.gif",
    r"./aplhabets/alphabet/e.gif",
    r"./aplhabets/alphabet/f.gif",
    r"./aplhabets/alphabet/g.gif",
    r"./aplhabets/alphabet/h.gif",
    r"./aplhabets/alphabet/i.gif",
    r"./aplhabets/alphabet/j.gif",
    r"./aplhabets/alphabet/k.gif",
    r"./aplhabets/alphabet/l.gif",
    r"./aplhabets/alphabet/m.gif",
    r"./aplhabets/alphabet/n.gif",
    r"./aplhabets/alphabet/o.gif",
    r"./aplhabets/alphabet/p.gif",
    r"./aplhabets/alphabet/q.gif",
    r"./aplhabets/alphabet/r.gif",
    r"./aplhabets/alphabet/s.gif",
    r"./aplhabets/alphabet/t.gif",
    r"./aplhabets/alphabet/u.gif",
    r"./aplhabets/alphabet/v.gif",
    r"./aplhabets/alphabet/w.gif",
    r"./aplhabets/alphabet/x.gif",
    r"./aplhabets/alphabet/y.gif",
    r"./aplhabets/alphabet/z.gif"
    
]



image_paths2 = [
    r"./aplhabets/alphabet/0.gif",
    r"./aplhabets/alphabet/1.gif",
    r"./aplhabets/alphabet/2.gif",
    r"./aplhabets/alphabet/3.gif",
    r"./aplhabets/alphabet/4.gif",
    r"./aplhabets/alphabet/5.gif",
    r"./aplhabets/alphabet/6.gif",
    r"./aplhabets/alphabet/7.gif",
    r"./aplhabets/alphabet/8.gif",
    r"./aplhabets/alphabet/9.gif"
]

image_paths3 = [
    r"./kunal/py_logo.PNG",
    r"./kunal/hamburger.png",
    r"./kunal/hamburger.png",
    r"./kunal/hamburger.png",
    r"./kunal/py_logo.PNG",
    r"./kunal/hamburger.png",
    r"./kunal/py_logo.PNG",
    r"./kunal/hamburger.png",
    r"./kunal/py_logo.PNG",
    r"./kunal/hamburger.png",
    r"./kunal/py_logo.PNG",
    r"./kunal/hamburger.png",
    r"./kunal/py_logo.PNG",
    r"./kunal/hamburger.png",
    r"./kunal/py_logo.PNG",
    r"./kunal/hamburger.png"
]

top.mainloop()