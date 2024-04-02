import pyttsx3
import tkinter as tk
import customtkinter as ctk
from autocorrect import Speller

spell = Speller()

top = tk.Tk()
top.geometry("1000x800")
top.config(bg="White")

text_speech = pyttsx3.init()

text_speech.setProperty('rate', 150)
gender_var = tk.IntVar(value=0)
male_radio = ctk.CTkRadioButton(
    master=top, text="Male", variable=gender_var, value=0
)
male_radio.pack(padx=20, pady=10)  

female_radio = ctk.CTkRadioButton(
    master=top, text="Female", variable=gender_var, value=1
)
female_radio.pack(padx=20, pady=10)
voices = text_speech.getProperty('voices')
text_speech.setProperty('voice', voices[gender_var.get()].id)  
text_speech.setProperty('volume', 10.0)  
def speak_text(event=None):
    text1 = txt.get()

    if '@' in text1:
        text1 = text1.split('@')[0]
        txt.delete(0, tk.END)
        text = spell(text1)
        selected_voice = voices[gender_var.get()].id  
        text_speech.setProperty('voice', selected_voice)
        text_speech.say(text1)
        text_speech.runAndWait()

txt = tk.Entry(top)
txt.place(x=50, y=50)
txt.bind('<KeyRelease>', speak_text)

top.mainloop()