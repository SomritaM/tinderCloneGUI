from tkinter import *

root=Tk()
root.title("Hello GUI")
root.maxsize(600,600)

lbl=Label(root,width=10,height=3,text="HELLO")
lbl.grid(row=0,column=0)

ent=Entry(root,width=5)
ent.grid(row=1,column=0)

lbll=Label(root,width=10,height=3,text="Look Here")
lbll.grid(row=2,column=0)

btn=Button(root,width=7,height=5,text="Click Me",
           command=lambda: btnclicked())

btn.grid(row=3,column=0)
def btnclicked():
    s=ent.get()
    lbll.configure(text=s)

root.mainloop()
