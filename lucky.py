from tkinter import *
import random
class Lucky:
    def __init__(self):
        self.root = Tk()
        self.root.maxsize(600, 600)
        self.root.title("Lucky game")
        self.score = 30
        self.lucky = random.randrange(1,50,1)

        self.welcomeLabel = Label(self.root, width=15, height=4, font=('Arial', 16),
                                  text="Welcome to Lucky Game", bg='SkyBlue')
        self.welcomeLabel.grid(row=0, column=0)
        self.entBox = Entry(self.root, width=10, font=('Arial', 15))
        self.entBox.grid(row=1, column=0)
        self.btnClick = Button(self.root, width=10, height=2, text="Guess",
                               command=lambda: self.check(int(self.entBox.get())))
        self.btnClick.grid(row=2, column=0)

        self.btnNewGame=Button(self.root,width=10,height=2,text="New Game",
                                    command=lambda :self.newGame())
        self.btnNewGame.grid(row=2,column=1)

        self.lblHint = Label(self.root, width=20, height=3, font=('Courier', 15), text="LOok Here")
        self.lblHint.grid(row=3, column=0)

        self.lblscore = Label(self.root, width=5, height=3, font=('Courier', 15), text=self.score)
        self.lblscore.grid(row=3, column=1)
        self.root.mainloop()
    def check(self,ch):
        if self.score!=0:
            if ch<self.lucky:
                self.lblHint.configure(text="Guess More")
                self.score=self.score-3
                self.lblscore.configure(text=self.score)
            elif ch>self.lucky:
                self.lblHint.configure(text="Guess Less")
                self.score=self.score-3
                self.lblscore.configure(text=self.score)
            else:
                self.lblHint.configure(text="You Won")
                self.lblscore.configure(text=self.score)
        else:
            self.lblHint.configure(text="You Lost")
            self.lblscore.configure(text=self.score)
    def newGame(self):
        self.score=30
        self.lblscore.configure(text="30")
        self.lblHint.configure(text="Look Here")
        self.lucky=random.randrange(1,50,1)
obj=Lucky()


