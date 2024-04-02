import tkinter as tk
list_of_texts = ["Text 1", "Text 2", "Text 3"]
# Assuming len is the length of the list containing text for labels
len_of_list = len(list_of_texts)

# Create a tkinter window
root = tk.Tk()

# Assuming list_of_texts contains the texts for labels


# Create labels using a for loop
for i in range(len_of_list):
    desc_label = tk.Label(root, text=list_of_texts[i], fg="black", font=("Arial", 12))
    desc_label.pack()

# Run the tkinter event loop
root.mainloop()
