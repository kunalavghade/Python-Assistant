from tkinter import*
from DatabaseHandleS import *

class MassageBoxss(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
    
        # create new window
        self.geometry("400x160+470+250")
        self.title("Path Directory")
        self.resizable(False,False)

        # Frame 
        self.frame=Frame(self,bg="black",height=200,width=400)
        self.frame.pack()

        # Label
        self.pathOp=Label(self.frame,bg="black",fg="white",font="arial 20 bold",text="Path Operation")
        self.pathOp.place(x=100,y=30)

        # cancel button 
        self.cancelButton = Button(self.frame,text="Cancel",font="arial 15 bold",padx=20,pady=0,fg="#d2d2d2",background="#212121",borderwidth=0,activebackground="#252525",activeforeground="#b9b9b9",command=self.destroy)
        self.cancelButton.place(x=20,y=100)

        # Add button 
        self.addButton = Button(self.frame,text="Add",font="arial 15 bold",padx=32,pady=0,fg="#d2d2d2",background="#212121",borderwidth=0,activebackground="#252525",activeforeground="#b9b9b9",command=self.addFunc)
        self.addButton.place(x=147,y=100)

        # remove button 
        self.removeButton = Button(self.frame,text="Remove",font="arial 15 bold",padx=10,pady=0,fg="#d2d2d2",background="#212121",borderwidth=0,activebackground="#252525",activeforeground="#b9b9b9",command=self.removeFunc)
        self.removeButton.place(x=270,y=100)


    def addFunc(self):

        # remove previous Frame 
        self.destroy()
        # create new box
        self.c=Toplevel(background="black")
        self.c.geometry("400x160+470+250")
        self.c.title("Add Path")
        self.c.resizable(False,False)

        # create heading
        self.addLabel=Label(self.c,bg="black",fg="white",font="arial 20 bold",text="Please Enter Path !")
        self.addLabel.place(x=80,y=20)

        # get input 
        self.pathEntryName=Entry(self.c,width=10,font="arial 15",bg="#252525",bd=0,fg="#bbbbbb")
        self.pathEntryName.insert(0,"Enter Name")
        self.pathEntryName.place(x=30,y=70)


        self.pathEntryPath=Entry(self.c,width=20,font="arial 15",bg="#252525",bd=0,fg="#bbbbbb")
        self.pathEntryPath.insert(0,"Enter Path")
        self.pathEntryPath.place(x=150,y=70)

        # cancel
        self.cancelButton2 = Button(self.c,text="Cancel",font="arial 15 bold",padx=50,pady=0,fg="#d2d2d2",background="#212121",borderwidth=0,activebackground="#252525",activeforeground="#b9b9b9",command=self.c.destroy)
        self.cancelButton2.place(x=20,y=110)

        # add 
        self.addButton2 = Button(self.c,text="Add",font="arial 15 bold",padx=60,pady=0,fg="#d2d2d2",background="#212121",borderwidth=0,activebackground="#252525",activeforeground="#b9b9b9",command=self.addDb)
        self.addButton2.place(x=210,y=110)

    def removeFunc(self):

        # remove previous Frame 
        self.destroy()
        
        # create new box
        self.d=Toplevel(background="black")
        self.d.geometry("400x160+470+250")
        self.d.title("Remove Path")
        self.d.resizable(False,False)

        # create heading
        self.addLabel1=Label(self.d,bg="black",fg="white",font="arial 20 bold",text="Remove Enter Path !")
        self.addLabel1.place(x=60,y=20)


        # get input 
        self.pathEntryPathR=Entry(self.d,width=30,font="arial 15",bg="#252525",bd=0,fg="#bbbbbb")
        self.pathEntryPathR.insert(0,"Enter Name")
        self.pathEntryPathR.place(x=35,y=70)

        # cancel
        self.cancelButton1 = Button(self.d,text="Cancel",font="arial 15 bold",padx=50,pady=0,fg="#d2d2d2",background="#212121",borderwidth=0,activebackground="#252525",activeforeground="#b9b9b9",command=self.d.destroy)
        self.cancelButton1.place(x=20,y=110)

        # add 
        self.removeButton1 = Button(self.d,text="remove",font="arial 15 bold",padx=43,pady=0,fg="#d2d2d2",background="#212121",borderwidth=0,activebackground="#252525",activeforeground="#b9b9b9",command=self.removeDb)
        self.removeButton1.place(x=210,y=110)

    def removeDb(self):
        self.qury=self.pathEntryPathR.get()
        Remove=dbRemove(self.qury)
        self.d.destroy()
    

    def addDb(self):
        self.name=self.pathEntryName.get()
        self.path=self.pathEntryPath.get()
        add=dbAdd(self.name,self.path)
        self.c.destroy()

