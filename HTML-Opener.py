from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from tkinter import messagebox

root = Tk()
root.title("HTML READER")
root.minsize(600, 600)
root.maxsize(600, 600)

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
run_img = ImageTk.PhotoImage(Image.open("play.png"))

label_file_name = Label(root, text = "File Name :", bg = "white")
label_file_name.place(relx = 0.40, rely = 0.05, anchor = CENTER)

input_file_name = Entry(root)
input_file_name.place(relx = 0.57, rely = 0.05, anchor = CENTER)

my_text = Text(root, height = 33, width = 74, bg = "gray", fg = "white")
my_text.place(relx = 0.5, rely = 0.55, anchor = CENTER)

name="";

def openFile():
    global name
    my_text.delete(1.0,END)
    input_file_name.delete(0,END)
    html_file=filedialog.askopenfilename(title=" Open Text File",filetypes=(("Html Files","*.html"),))
    print(html_file)
    name=os.path.basename(html_file)
    formatted_name=name.split('.')[0]
    input_file_name.insert(END,formatted_name)
    root.title(formatted_name)
    html_file=open(name,'r')
    paragraph=html_file.read()
    my_text.insert(END,paragraph)
    html_file.close()

open_button = Button(root, image = open_img, text = "Open File", command=openFile)
open_button.place(relx = 0.05, rely = 0.05, anchor = CENTER)

def saveFile():
    input_name=input_file_name.get()
    file=open(input_name+".txt","w")
    data=my_text.get("1.0",END)
    print(data)
    file.write(data)
    input_file_name.delete(0,END)
    my_text.delete("1.0",END)
    messagebox.showinfo("Update","Success")

save_button = Button(root, image = save_img, text = "Save File", command=saveFile)
save_button.place(relx = 0.15, rely = 0.05, anchor = CENTER)

run_button = Button(root, image = run_img, text = "Run File")
run_button.place(relx = 0.25, rely = 0.05, anchor = CENTER)

root.mainloop()