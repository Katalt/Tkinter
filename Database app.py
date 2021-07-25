from tkinter import *
import tkinter as tk
import psycopg2

root = Tk()

def get_data(Name,age,address):
    conn = psycopg2.connect(dbname="postgres",port=5432,user="postgres",host="localhost",password="isgsql")
    cur = conn.cursor() 
    query = '''Insert into student(NAME,AGE,ADDRESS) values (%s,%s,%s) ;'''
    cur.execute(query,(Name,age,address))
    print("Data entered")
    conn.commit()
    conn.close()
    display_all()

def search(id):
    conn = psycopg2.connect(dbname="postgres",port=5432,user="postgres",host="localhost",password="isgsql")
    cur = conn.cursor()   
    query = '''Select * from student where ID=%s;'''
    cur.execute(query,id)
    row = cur.fetchone()
    display_search(row)
    conn.commit()
    conn.close()

def display_search(row):
    listbox = Listbox(frame,width=20,height=1)
    listbox.grid(row=7,column=1)
    listbox.insert(END,row)

def display_all():
    conn = psycopg2.connect(dbname="postgres",port=5432,user="postgres",host="localhost",password="isgsql")
    cur = conn.cursor()
    query = '''Select * from student'''
    cur.execute(query)
    row = cur.fetchall()
    
    listbox = Listbox(frame,width=20,height=5)
    listbox.grid(row=8,column=1)
    for x in row:
        listbox.insert(END,x)

canvas = Canvas(root, height=480, width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3,rely=0.1,relheight=0.8,relwidth=0.8)

label = Label(frame,text="Add data")
label.grid(row=0,column=1)

label = Label(frame,text="Name")
label.grid(row=1,column=0)

entry_name = Entry(frame)
entry_name.grid(row=1,column=1)

label = Label(frame,text="Age")
label.grid(row=2,column=0)

entry_age = Entry(frame)
entry_age.grid(row=2,column=1)

label = Label(frame,text="Address")
label.grid(row=3,column=0)

entry_address = Entry(frame)
entry_address.grid(row=3,column=1)

button=Button(frame,text="Add",command=lambda:get_data(entry_name.get(),entry_age.get(),entry_address.get()))
button.grid(row=4,column=1)

label = Label(frame,text="Search Data")
label.grid(row=5,column=1)

label = Label(frame,text="Search_name")
label.grid(row=6,column=0)

entry_ID = Entry(frame)
entry_ID.grid(row=6,column=1)

button=Button(frame,text='Search',command=lambda:search(entry_ID.get()))
button.grid(row=6,column=2)

display_all()

root.mainloop()