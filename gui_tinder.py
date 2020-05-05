from tkinter import *

from tinderbackend import *
from tkinter import messagebox


class TinderGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("tinderclone")
        self.root.maxsize(600, 600)
        self.root['bg']='Pink'
        self.tinderbackend=Tinder()
        lblWelcome = Label(self.root,text="Welcome to tinder", width=30, height=3,
                           font=("Courier", 15),bg='Red').grid(row=0,column=0)



        btnLogin = Button(self.root,bg='SkyBlue',text="Login", width=10, height=2,
                         command=lambda: self.loginWindow()).grid(row=1,column=0)


        btnRegister = Button(self.root,bg='SkyBlue', text="Register",width=10, height=2,
                            command=lambda: self.registerwindow()).grid(row=2,column=0)


        btnExit = Button(self.root,bg='SkyBlue',text="Exit", width=10, height=2,
                         command=lambda: self.root.destroy()).grid(row=3,column=0)
        self.root.mainloop()
    def loginWindow(self):
        if self.tinderbackend.currentUserId !=0:
            self.showUserMenu()
        else:


            child=Toplevel(self.root)
            child.title("Login screen")
            child.maxsize(400,400)
            child['bg']='Blue'
            lblLogin=Label(child,text="Email:",width=10,height=2,
                           font=('Arial',15)).grid(row=0,column=0)
            entEmail=Entry(child,width=35,font=('Arial,14'))
            entEmail.grid(row=0,column=1)
            lblPass=Label(child,text="Password:",width=10,height=2,
                          font=('Arial',15)).grid(row=1,column=0)
            entPass=Entry(child,width=35,font=('Arial',14))
            entPass.grid(row=1,column=1)
            btnLogin= Button(child,text="Login",width=10,height=2,bg='Yellow',
                            font=('Arial',15),command=lambda: self.validate(child,entEmail.get(),entPass.get()))
            btnLogin.grid(row=2,column=1)
            btnRegister= Button(child,text="Register",width=10,height=2,bg='Pink',
                                font=('Arial',15),command=lambda: self.valid(entName.get(),entGender.get(),entCity.get(),entEmail.get(),entPassword.get()))
            btnRegister.grid(row=3,column=1)

    def validate(self,child,email,password):
        result=self.tinderbackend.userLogin(email,password)

        if result:
            messagebox.showinfo('Sucess','Successfully Logged in')
            self.showUserMenu()
            child.destroy()
        else:
            messagebox.showinfo('Error', 'Invalid Login')

    def registerwindow(self):
        child = Toplevel(self.root)
        child.title("Register screen")
        child.maxsize(400, 400)
        child['bg'] = 'Blue'
        lblName = Label(child, text="Name",width=10,height=2,
                      font=('Arial',15)).grid(row=0,column=0)
        entName = Entry(child, width=35, font=('Arial,14'))
        entName.grid(row=0, column=1)
        lblGender = Label(child, text="Gender", width=10, height=2,
                        font=('Arial', 15)).grid(row=1, column=0)
        entGender = Entry(child, width=35, font=('Arial,14'))
        entGender.grid(row=1, column=1)
        lblCity = Label(child, text="City", width=10, height=2,
                        font=('Arial', 15)).grid(row=2, column=0)
        entCity = Entry(child, width=35, font=('Arial,14'))
        entCity.grid(row=2, column=1)
        lblEmail = Label(child, text="Email", width=10, height=2,
                        font=('Arial', 15)).grid(row=3, column=0)
        entEmail = Entry(child, width=35, font=('Arial,14'))
        entEmail.grid(row=3, column=1)
        lblPassword = Label(child, text="Password", width=10, height=2,
                        font=('Arial', 15)).grid(row=4, column=0)
        entPassword = Entry(child, width=35,show='*', font=('Arial,14'))
        entPassword.grid(row=4, column=1)
        btnRegister = Button(child, text="Register", width=10, height=2, bg='Pink',
                             font=('Arial', 15),
                             command=lambda: self.valid(entName.get(), entGender.get(), entCity.get(), entEmail.get(),
                                                        entPassword.get(),child))
        btnRegister.grid(row=5, column=1)


    def valid(self,name,gender,city,email,password,child):

        k=self.tinderbackend.userRegister(name,gender,city,email,password)

        if k:
            messagebox.showinfo('Success','successfully Registered')
            child.destroy()
        else:
            messagebox.showinfo('Unsuccessful','Already Exist')

    def showUserMenu(self):
        child = Toplevel(self.root)
        child.title("Proposal screen")
        child.maxsize(400, 400)
        child['bg'] = 'Blue'
        uname=self.tinderbackend.fetchUserName()
        lblWelcome = Label(child, text="Welcome %s"%(uname[0][0]), width=30, height=3,
                        font=('Arial', 16,'bold')).grid(row=0, column=0,pady=20)
        btnAll = Button(child, text="View All Users", width=20, height=2, bg='Pink',
                        command=lambda :self.showUsers()).grid(row=1, column=0,pady=10)
        btnsent = Button(child, bg='SkyBlue', text="View All Sent Proposals", width=20, height=2,
                         command=lambda :self.viewSent()).grid(row=2, column=0,pady=10)
        btnRev = Button(child, bg='SkyBlue', text="View All Received Proposals", width=20, height=2,
                        command=lambda :self.viewRcvd()).grid(row=3, column=0,pady=10)
        btnMatch = Button(child, bg='SkyBlue', text="View Matches", width=20, height=2,
                          command=lambda :self.viewMatches()).grid(row=4, column=0,pady=10)
        btnLogout = Button(child, bg='SkyBlue', text="LOGOUT", width=20, height=2,
                           command=lambda :self.logout(child)).grid(row=5,  column=0,pady=10)
    def showUsers(self):
        child=Toplevel(self.root)
        child.title("User List")
        child.maxsize(900,600)
        child['bg'] = 'Black'
        userList=self.tinderbackend.viewAllUsers()
        i=1
        lWelcome=Label(child, text="User List", width=55,height=3,bg='Red',
                       font=('Courier',16,'bold')).grid(row=0,column=0,columnspan=4)
        k=0
        for user in userList:
            if user[0]!=self.tinderbackend.currentUserId:

                lName = Label(child, text=user[1], width=20, height=1, bg='Red', font=('Arial', 15)
                             ).grid(row=i, column=0, pady=10)
                lGender = Label(child, text=user[2], width=10, height=1, bg='Red', font=('Arial', 15)
                             ).grid(row=i, column=1, pady=10)
                lCity = Label(child, text=user[3], width=10, height=1, bg='Red', font=('Arial', 15)
                             ).grid(row=i, column=2,pady=10)
                if self.tinderbackend.check(user[0]):


                    btnPropose=Button(child,text="Propose",width=10,height=2,
                                  font=('Arial',10),bg='Red',
                                      command=lambda k=i: self.sendProposal(userList[k-1][0])).grid(row=i, column=3)

                else:
                    btnMatches=Button(child,text="Matches",width=10,height=2,
                                  font=('Arial',10),bg='Yellow').grid(row=i, column=3)
                i=i+1

    def sendProposal(self,userid):
        self.tinderbackend.propose(userid)
        messagebox.showinfo('Sent','Proposal Sent.Now PRAY!')





    def viewSent(self):
        child=Toplevel(self.root)
        child.title("User List")
        child.maxsize(900, 600)
        child['bg'] = 'Pink'
        userList = self.tinderbackend.viewSentProposals()
        i = 1
        lWelcome = Label(child, text="Crush List", width=55, height=3, bg='Red',
                         font=('Courier', 16, 'bold')).grid(row=0, column=0, columnspan=4)
        for user in userList:
            lID = Label(child, text=user[3], width=3, height=1, bg='Red', font=('Arial', 15)
                        ).grid(row=i, column=0, pady=10)
            lName = Label(child, text=user[4], width=20, height=1, bg='Red', font=('Arial', 15)
                          ).grid(row=i, column=1, pady=10)
            lGender = Label(child, text=user[5], width=10, height=1, bg='Red', font=('Arial', 15)
                            ).grid(row=i, column=2, pady=10)
            lCity = Label(child, text=user[6], width=10, height=1, bg='Red', font=('Arial', 15)
                          ).grid(row=i, column=3, pady=10)
            i = i + 1


    def viewRcvd(self):
        child=Toplevel(self.root)
        child.title("Fan List")
        child.maxsize(900, 600)
        child['bg'] = 'Pink'
        userList = self.tinderbackend.viewReceivedProposals()
        i = 1
        lWelcome = Label(child, text="Fan List", width=55, height=3, bg='Red',
                         font=('Courier', 16, 'bold')).grid(row=0, column=0, columnspan=4)
        for user in userList:
            lID = Label(child, text=user[3], width=3, height=1, bg='Red', font=('Arial', 15)
                        ).grid(row=i, column=0, pady=10)
            lName = Label(child, text=user[4], width=20, height=1, bg='Red', font=('Arial', 15)
                          ).grid(row=i, column=1, pady=10)
            lGender = Label(child, text=user[5], width=10, height=1, bg='Red', font=('Arial', 15)
                            ).grid(row=i, column=2, pady=10)
            lCity = Label(child, text=user[6], width=10, height=1, bg='Red', font=('Arial', 15)
                          ).grid(row=i, column=3, pady=10)
            i = i + 1
        lPropose = Label(child, text="Enter the ID to propose User:",
                         width=25, height=2).grid(row=i, column=0)
        entPropose = Entry(child, width=4)
        entPropose.grid(row=i, column=2)
        btnPropose = Button(child, text="Propose", width=10, height=2,
                            font=('Arial', 12), bg='Yellow',
                            command=lambda: self.sendProposal(entPropose.get())).grid(row=i, column=3)

    def viewMatches(self):
        child = Toplevel(self.root)
        child.title("User List")
        child.maxsize(900, 600)
        child['bg'] = 'Pink'
        userList = self.tinderbackend.viewMatches()
        i = 1
        lWelcome = Label(child, text="Matches List", width=55, height=3, bg='Red',
                         font=('Courier', 16, 'bold')).grid(row=0, column=0, columnspan=4)
        for user in userList:
            lID = Label(child, text=user[3], width=3, height=1, bg='Red', font=('Arial', 15)
                        ).grid(row=i, column=0, pady=10)
            lName = Label(child, text=user[4], width=20, height=1, bg='Red', font=('Arial', 15)
                          ).grid(row=i, column=1, pady=10)
            lGender = Label(child, text=user[5], width=10, height=1, bg='Red', font=('Arial', 15)
                            ).grid(row=i, column=2, pady=10)
            lCity = Label(child, text=user[6], width=10, height=1, bg='Red', font=('Arial', 15)
                          ).grid(row=i, column=3, pady=10)
            i = i + 1
            lPropose = Label(child, text="Enter the ID to propose User:",
                             width=25, height=2).grid(row=i, column=0)
            entPropose = Entry(child, width=4)
            entPropose.grid(row=i, column=2)
            btnPropose = Button(child, text="Propose", width=10, height=2,
                                font=('Arial', 12), bg='Yellow',
                                command=lambda: self.sendProposal(entPropose.get())).grid(row=i, column=3)
    def logout(self,child):
        messagebox.showinfo('Thanks','Thanks for playing around')
        self.tinderbackend.logout()
        child.destroy()


obj=TinderGUI()