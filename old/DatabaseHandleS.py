from tkinter import messagebox
import sqlite3

con=sqlite3.connect("database.db")
cur=con.cursor()

class dbAdd:
    def __init__(self,name,path):

        self.name = name.lower()
        self.path = path
        if self.name and self.path != "":
            try:
            # add to Database 
                data="insert into 'progPath' (name,path) values(?,?)"

                cur.execute(data,(self.name,self.path))
                con.commit()
                self.SuccessAdd()
            except:
                messagebox.showerror("Error","EE")
        else:
            messagebox.showerror("Error","                  Please Enter Correct Path                   ")


    def SuccessAdd(self):
            messagebox.showinfo("Success","                      Added successfully                       ")

    

class dbRemove:
    def __init__(self,path):
        self.path=path
        if self.path != "":
            try:
            # add to Database 
                data=f"delete from progPath where name = '{self.path}'"

                con.execute(data)
                con.commit()

                self.SuccessRemove()

            except EXCEPTION as e:
                messagebox.showerror("Error",str(e))
        else:
            messagebox.showerror("Error","                  Please Enter Correct Name                  ")

    def SuccessRemove(self):
        messagebox.showinfo("Romoved","                    Removed Successfully                   ")


class createDb:
    def __init__(self):
        con=sqlite3.connect("database.db")
        cur=con.cursor()
        data='''CREATE TABLE "progPath" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT,
	"path"	TEXT
);'''
        try:
            con.execute(data)
            con.commit()
            self.SuccessCreate()
        except:
            self.warning()

    def SuccessCreate(self):
            messagebox.showinfo("Success","                      Created successfully                       ")

    def warning(self):
        messagebox.showwarning("Warning...","                     Database Already Exist                     ")
