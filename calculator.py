from tkinter import *
class Calculator:
    def __init__(self):
        self.root=Tk()
        self.root.title("My Calc")
        self.root.maxsize(600,600)
        self.firstnum=0
        self.secondnum=0
        self.opt=""

        self.lblDisplay=Label(self.root,width=20,height=2,bg='White')
        self.lblDisplay.grid(row=0,column=0,columnspan=4)

        btn9=Button(self.root,width=5,height=2,bg='SkyBlue',text="9",
                    command=lambda :self.getNum("9")).grid(row=1,column=0)

        btn8=Button(self.root,width=5,height=2,bg='SkyBlue',text="8",
                    command=lambda :self.getNum("8")).grid(row=1,column=1)
        btn7=Button(self.root,width=5,height=2,bg='SkyBlue',text="7",
                    command=lambda :self.getNum("7")).grid(row=1,column=2)
        btnAdd = Button(self.root, width=5, height=2, bg='SkyBlue', text="+",
                        command=lambda: self.getOpt("+")).grid(row=1, column=3)

        btn6 = Button(self.root, width=5, height=2, bg='SkyBlue', text="6",
                      command=lambda: self.getNum("6")).grid(row=2, column=0)

        btn5 = Button(self.root, width=5, height=2, bg='SkyBlue', text="5",
                      command=lambda: self.getNum("5")).grid(row=2, column=1)

        btn4 = Button(self.root, width=5, height=2, bg='SkyBlue', text="4",
                      command=lambda: self.getNum("4")).grid(row=2, column=2)
        btnSub=Button(self.root,width=5, height=2, bg='SkyBlue', text="-",
                        command=lambda: self.getOpt("-")).grid(row=2, column=3)


        btn3 = Button(self.root, width=5, height=2, bg='SkyBlue', text="3",
                      command=lambda: self.getNum("3")).grid(row=3, column=0)

        btn2 = Button(self.root, width=5, height=2, bg='SkyBlue', text="2",
                      command=lambda: self.getNum("2")).grid(row=3, column=1)

        btn1 = Button(self.root, width=5, height=2, bg='SkyBlue', text="1",
                      command=lambda: self.getNum("1")).grid(row=3, column=2)
        btnMul=Button(self.root,width=5,height = 2, bg = 'SkyBlue', text = "*",
                      command = lambda: self.getOpt("*")).grid(row=3, column=3)
        btnClr=Button(self.root,width=5, height=2, bg='SkyBlue', text="Clr",
                        command=lambda: self.clr()).grid(row=4, column=0)

        btn0 = Button(self.root, width=5, height=2, bg='SkyBlue', text="0",
                      command=lambda: self.getNum("0")).grid(row=4, column=1)
        btnEquals=Button(self.root,width=5, height=2, bg='SkyBlue', text="=",
                        command=lambda: self.cal()).grid(row=4, column=2)
        btnDiv=Button(self.root,width=5, height=2, bg='SkyBlue', text="/",
                        command=lambda: self.getOpt("/")).grid(row=4, column=3)


        self.root.mainloop()
    def getNum(self,s):
        n=self.lblDisplay['text']
        n=n+s
        self.lblDisplay.configure(text=n)


        if self.opt!="":
            self.firstnum=n

        else:
            self.secondnum=n
    def getOpt(self,s):
        self.lblDisplay.configure(text="")
        self.opt=s
    def cal(self):
        n1=int(self.firstnum)
        n2=int(self.secondnum)
        if self.opt=="+":
            r=n1+n2
        if self.opt=="-":
            r=n1-n2
        if self.opt=="*":
            r=n1*n2
        if self.opt=="/":
            r=n1/n2
        self.lblDisplay.configure(text=r)
    def clr(self):
        self.firstnum=0
        self.secondnum=0
        self.lblDisplay.configure(text="")
        self.opt=""


ob=Calculator()




