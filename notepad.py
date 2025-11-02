#importing libraries
from tkinter import *
from datetime import datetime
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import messagebox

#defining functions
def save():
    global saved_text
    x=messagebox.askyesno("Save?","Do you want to leave this program?")
    if x==True:
        window.destroy()
       
def Open():
    file_path=askopenfilename(filetypes=[("Text Files","*.text"),("All Files","*.*")])
    if file_path:
        with open(file_path,"r") as file:
            text.delete("1.0",END)
            text.insert("1.0",file.read())



def Save_as():
    file_path=asksaveasfilename(filetypes=[("Text Files","*.text"),("All Files","*.*")])
    if file_path:
        with open(file_path,"w") as file:
            file.write(text.get("1.0",END))

def Font_color(num):
    if num==0:
        text.configure(fg="Black")
    if num==1:
        text.configure(fg="blue")
    if num==2:
        text.configure(fg="Brown")
    if num==3:
        text.configure(fg="Red")
    if num==4:
        text.configure(fg="purple")
    if num==5:
        text.configure(fg="Yellow")


def theme(color_num):
    if color_num==0:
        text.configure(bg="White")
    if color_num==1:
        text.configure(bg="Gainsboro")
    if color_num==2:
        text.configure(bg="Lightskyblue1")
    if color_num==3:
        text.configure(bg="Khaki")
    if color_num==4:
        text.configure(bg="PaleGreen2")
    if color_num==5:
        text.configure(bg="MistyRose")

def select_font_2(font_1):
    global text
    text.configure(font=font_1)



def select_font():
    root=Tk()
    root.geometry("700x300")
    Label(root,text="Type The Font",font=("Century",23)).pack()
    eng_font=Entry(root,font=("Century",13))
    eng_font.pack()

    Button(root,text="Enter",padx=20,pady=2,command=lambda:select_font_2(eng_font.get())).place(x=300,y=200)
    root.mainloop()


def time_date():
    current_time=datetime.now()
   
    if current_time.hour<12:
        text.insert("1.0",f" {current_time.date()} {current_time.hour}:{current_time.minute} am")
    
    elif current_time.hour>=12:
        text.insert("1.0",f" {current_time.date()} {current_time.hour}:{current_time.minute} pm")
        
def select_all():
    window.event_generate('<Control-a>')

def new_window():
    global text
    text.delete("1.0",END)

#making the actual window
window=Tk()
window.geometry("600x500")

#making the menubar
menubar=Menu(window)

text=Text(height=100,font="Consolas")

text.configure(bg="White")
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)
file.add_command(label="New Window",command=lambda:new_window())
file.add_command(label="Open...",command=lambda:Open())
file.add_command(label="Save as",command=lambda:Save_as())
file.add_separator()
file.add_command(label="Exit",command=lambda:window.destroy())

edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Select All",command=lambda:select_all())
edit.add_command(label="Time/Date",command=lambda:time_date())


format=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Format",menu=format)
format.add_command(label="Font",command=lambda:select_font())
themes=Menu(format,tearoff=0)
format.add_cascade(label="Theme",menu=themes)
themes.add_command(label="White",command=lambda:theme(0))
themes.add_command(label="Gainsboro",command=lambda:theme(1))
themes.add_command(label="Lightskyblue1",command=lambda:theme(2))
themes.add_command(label="Khaki",command=lambda:theme(3))
themes.add_command(label="PaleGreen2",command=lambda:theme(4))
themes.add_command(label="MistyRose",command=lambda:theme(5))
font_color=Menu(format,tearoff=0)
format.add_cascade(label="font color",menu=font_color)
font_color.add_command(label="Black",command=lambda:Font_color(0))
font_color.add_command(label="Blue",command=lambda:Font_color(1))
font_color.add_command(label="SaddleBrown",command=lambda:Font_color(2))
font_color.add_command(label="Maroon",command=lambda:Font_color(3))
font_color.add_command(label="Purple",command=lambda:Font_color(4))
font_color.add_command(label="Yellow",command=lambda:Font_color(5))
window.config(menu = menubar)

text.pack()



window.protocol("WM_DELETE_WINDOW",lambda:save())

window.mainloop()


