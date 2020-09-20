from tkinter import*
from massageboxs import MassageBoxss
import win32com.client
import datetime
import wikipedia
import webbrowser
import random
import os
import sqlite3
from DatabaseHandleS import createDb



class mainWindow:

    speach = win32com.client.Dispatch("SAPI.SpVoice")

    helpString='''
    
    1.Open Youtube.com
    2.Open Google.com
    3.Open instagram
    4.Open Edge Browser
    5.Open Blender
    6.Open.
    7.Open Sublime
    8.Play Music
    9.Wikipedia
    10.what is time

    shortcut key: Enter-Ctrl+l
    '''


    def __init__(self,master):
        # define loacal variable 
        self.master=master
        self.master.bind("<Control-l>",self.getInput)

        # top Frame
        self.topFrame=Frame(self.master,height=100,bg="black")
        self.topFrame.pack(fill=X,side=TOP)

        # heading label 
        self.label=Label(self.topFrame,text="Assistant", font="arial 40 bold",bg="black",fg="white")
        self.label.place(x=285,y=15)

        # help button 
        self.enterHelp=Button(self.topFrame,text="HELP",font="arial 15 bold",padx=30,pady=0,fg="#d2d2d2",background="#212121",borderwidth=0,activebackground="#252525",activeforeground="#b9b9b9",command=self.getHelp)
        self.enterHelp.place(x=650,y=30)

        # path button 
        self.getPath=Button(self.topFrame,text="Path",font="arial 15 bold",padx=30,pady=0,fg="#d2d2d2",background="#212121",borderwidth=0,activebackground="#252525",activeforeground="#b9b9b9",command=self.getPaths)
        self.getPath.place(x=30,y=30)

        # middle Frame        
        self.MiddleFrame=Frame(self.master,height=400)
        self.MiddleFrame.pack(fill=X)

        # Scrollbar
        self.scroll=Scrollbar(self.MiddleFrame,width=15)
        self.scroll.pack(side=RIGHT,fill=Y)

        # text Area Output window
        self.textarea=Text(self.MiddleFrame,yscrollcommand=self.scroll.set,width=99,borderwidth=0,foregroun="white",height=23,bg="#191919",font="15",wrap=WORD)
        self.scroll.config(command=self.textarea.yview)
        self.textarea.pack(side=LEFT)

        # bottom Frame
        self.bottomFrame=Frame(root,height=100,bg="black")
        self.bottomFrame.pack(fill=X,side=BOTTOM)
       
        #Label command 
        self.cmd=Label(self.bottomFrame,text="Command: ",font="arial 20 bold",bg="black",fg="white")
        self.cmd.place(x=10,y=20)

        # input commnad 
        self.entry=Entry(self.bottomFrame,width=31,font="arial 20",bg="#252525",bd=0,fg="#bbbbbb")
        self.entry.place(x=170,y=20)

        # enter button
        self.enter=Button(self.bottomFrame,text="Enter",font="arial 15 bold",padx=30,pady=0,fg="#d2d2d2",background="#212121",borderwidth=0,activebackground="#313131",activeforeground="#b9b9b9",command=self.getInput)
        self.enter.place(x=650,y=18)


    # insert new values 
    def getHelp(self):
        self.textarea.delete(1.0,END)
        self.output("\n Here is some command to interact...")
        self.textarea.insert(INSERT,mainWindow.helpString)

    # get input 
    def getInput(self,event=""):
        self.textarea.delete(1.0,END)
        qury=self.entry.get()
        self.proceess(qury)

    def grabData(self,dataDb):
        self.dataDb=dataDb
        self.con=sqlite3.connect("database.db")
        command = f"select path from progPath where name ='{self.dataDb}'"
        dataDD=self.con.execute(command).fetchone()
        try:
            dataDD=dataDD[0]
        except:
            dataDD=False
        return dataDD

    # intsert input 
    def output(self,arg):
        self.textarea.insert(INSERT,arg)
        mainWindow.speach.speak(arg)

    def getPaths(self):
        msg =MassageBoxss()

    # proccess of assistant
    def proceess(self,ipQury):
        ipQury=ipQury.lower()
        if "wikipedia" in ipQury:
            output("Serching Wikipedi.....")
            ipQury=ipQury.replace("wikipedia","")
            result=wikipedia.summary(ipQury,sentences=2)
            self.output("\nAccording to wikipedia...")
            self.output("\n",result)
            
        elif "open youtube" in ipQury:
            self.output("Openning Youtube.com")
            webbrowser.open_new_tab("youtube.com") 

        elif "open google" in ipQury:
            self.output("Openning Google.com")
            webbrowser.open_new_tab("google.com") 

        elif "open instagram" in ipQury:
            self.output("Openning Instagram.com")
            webbrowser.open_new_tab("instagram.com") 

        elif "what is time" in ipQury:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            self.output(f"the time is {time}")

        elif"what is your name" in ipQury:
            self.output("According to My creator...")
            self.output("\nMy name is Baburav.\nJaay Maharashtra")

        elif "what is my name" in ipQury:
            self.output("I don't have any intrest ask you to your name.")
        
        elif "what can you do" in ipQury:
            self.output("Don't ask me sily questions.")
        
        elif "your language" in ipQury:
            self.output("\npython!")

        elif "open" in ipQury:
            ipQury=ipQury.replace("open ","")
            r=self.grabData(ipQury)
            print(r)
            if r != False:
                try:
                    self.output(f"opening {ipQury} !! .....")
                    os.startfile(r)
                except:
                    self.output("Sorry! you dont have desired path")
            else:
                self.output("Sorry! you dont have desired path")

        elif "play music" in ipQury:
            r=self.grabData("music")
            if r != False:
                try:
                    songs=os.listdir(r)
                    self.output("playing Music...\n")
                    self.textarea.insert(INSERT,songs)
                    os.startfile(os.path.join(r,random.choice(songs)))
                except:
                    self.output("Sorry! you dont have desired path")
            else:
                self.output("Sorry! you dont have desired path")

        elif "help" in ipQury:
            self.getHelp()

        elif "clear screen" in ipQury:
            self.textarea.delete(1.0,END)

        elif "create database" in ipQury:
            database=createDb()
            print("ssss")

        else:
            self.output('''Sorry !
            i cant recognize...
            check whether you entered correct command.
            you can click on help button from more informattion.
            ''')



root = Tk()
root.geometry('800x600+280+60')
root.resizable(FALSE,FALSE)
root.title("Assistant")

window=mainWindow(root)

root.mainloop()

