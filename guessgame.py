from tkinter import *
root=Tk()
root.title("Hello GUI")
root.maxsize(600,600)

lbl=Label(root,width=10,height=3,text="WELCOME")
lbl.grid(row=0,column=0)
lbll=Label(root,width=10,height=3,text="ENTER")
lbll.grid(row=1,column=0)
lbll2=Label(root,width=10,height=3)
lbll2.grid(row=1,column=0)
ent=Entry(root,width=5)
ent.grid(row=1,column=2)
btn=Button(root,width=7,height=5,text="Click Me",
           command=lambda: btnclicked())

btn.grid(row=2,column=2)
def btnclicked():
   lucky=24
   guess=0
   bank=15
   while bank!=0:
       guess = int(ent.get())
       if guess==lucky:

           lbll2.configure(text="you won")
           break
       elif guess>lucky:
           lbll2.configure(text="Choose a lower no")
           bank=bank-3
       else:
           lbll2.configure(text="Choose a higher no")
           bank=bank-3
root.mainloop()


