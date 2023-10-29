from tkinter import *
import pyshorteners
import webbrowser

root = Tk()
root.title('SYNC | Task-3: URL Shortner')
root.geometry('500x350')
root.config(background = "#a0522d")  


#Main function
def callback():
    webbrowser.open_new(out.get())

def shorten():
    if out.get():
        out.set("")
    if inp.get():
        #Convert Url to Short
        url = pyshorteners.Shortener().tinyurl.short(inp.get())
        #Output to window
        out.set(url)
        return url
    
    
inp=StringVar()  
out=StringVar()  

Label(root, text="URL Shortener",bg="#a0522d",fg="#A5D65D", font=("Helvetica",18)).place(x=200,y=20)
Label(root, text="Enter the link: ",bg="#a0522d",fg="#fff", font=("Helvetica",14)).place(x=20,y=80)
Entry(root, font=("Helvetica",18),textvariable=inp, width=24).place(x=160,y=80)
Button(root, command=shorten , text="Shorten Link",bg="#69922C",fg="#fff",font=("Helvetica",16)).place(x=210,y=130)
Label(root, text="Shortened link:" ,fg="#fff" ,bg="#a0522d", font=("Helvetica",14)).place(x=20,y=220)
Entry(root, font=("Helvetica",18) ,fg="#000",textvariable=out, width=24).place(x=160,y=220)

Button(root,command=callback,text="Open the shortened link",bg="#69922C",fg="#fff",font=("Helvetica",16)).place(x=160,y=270)

root.mainloop()
