from tkinter import *
from tkinter import filedialog
def brwfiles():
    filename=filedialog.askopenfilename(initialdir='/')
    title="select file"
    filetypes=(("Textfiles",".txt"),("All files","*.*"))
    label.config(text="file opened:"+filename)
window=Tk()
window.title("File Explorer")
window.geometry("500x500")
label=Label(window,text="File Explorer using Tkinter",font=("courier,25"),fg="Orange")
buttonbrw=Button(window,text="Browser Files",command=brwfiles,fg="green",bg="skyblue",activebackground="skyblue")
exitb=Button(window,text="exit",command=exit,bg="skyblue",fg="red",activebackground="skyblue")
label.pack()
buttonbrw.pack()
exitb.pack()
window.mainloop()