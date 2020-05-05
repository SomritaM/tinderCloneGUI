from tkinter import *
import random
class Factorial:
    def __init__(self):
        self.root = Tk()
        self.root.maxsize(600, 600)
        self.root.title("Factorial number")

        self.welcomeLabel = Label(self.root, width=15, height=4, font=('Arial', 16),
                                  text="Factorial of a number", bg='SkyBlue')
        self.welcomeLabel.grid(row=0, column=0)
        self.entBox = Entry(self.root, width=10, font=('Arial', 15))
        self.entBox.grid(row=1, column=0)


        self.btnClick = Button(self.root, width=10, height=2, text="Factorial",
                               command=lambda: self.fact(int(self.entBox.get())))
        self.btnClick.grid(row=2, column=0)

        self.root.mainloop()

    def fact(self,n):
        f=1


        i=n+1
        for i in range(1,i):
            f=f*i
            self.welcomeLabel.configure(text=f)

obj=Factorial()
