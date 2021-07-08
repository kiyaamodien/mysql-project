from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector

def insert():
    name = e_name.get()
    username = e_username.get()
    surname = e_surname.get()
    id = e_id.get()
    mobile = e_mobile.get()
    next_of_kin = e_next_of_kin.get()
    next_of_kin_mobile = e_next_of_kin_mobile.get()

    if(name=="" or username=="" or surname=="" or id=="" or mobile=="" or next_of_kin=="" or next_of_kin_mobile==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        my_db  = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                                        database="mydatabase", auth_plugin="mysql_native_password")
        my_cursor = my_db.cursor()
        xy = my_cursor.execute("select * from login")

        for i in my_cursor:
            print(i)


root = Tk()
root.geometry("600x300")
root.title("sign in")

name = Label(root, text="Enter name", font=('bold', 10))
name.place(x=20, y=30)

username = Label(root, text="Enter username", font=('bold', 10))
username.place(x=20, y=60)

surname = Label(root, text="Enter surname", font=('bold', 10))
surname.place(x=20, y=90)

id = Label(root, text="Enter id", font=('bold', 10))
id.place(x=20, y=120)

mobile = Label(root, text="Enter mobile", font=('bold', 10))
mobile.place(x=20, y=150)

next_of_kin = Label(root, text="Enter next of kin", font=('bold', 10))
next_of_kin.place(x=20, y=180)

next_of_kin_mobile = Label(root, text="Enter next of kin mobile", font=('bold', 10))
next_of_kin_mobile.place(x=20, y=210)

e_name = Entry()
e_name.place(x=150, y=30)

e_username = Entry()
e_username.place(x=150, y=60)

e_surname = Entry()
e_surname.place(x=150, y=90)

e_id = Entry()
e_id.place(x=150, y=120)

e_mobile = Entry()
e_mobile.place(x=150, y=150)

e_next_of_kin = Entry()
e_next_of_kin.place(x=150, y=180)

e_next_of_kin_mobile = Entry()
e_next_of_kin_mobile.place(x=180, y=210)

insert = Button(root, text="insert", font="italic 10", bg="white", command=insert)
insert.place(x=20, y=250)

# delete = Button(root, text="delete", font="italic 10", bg="white", command=delete)
# delete.place(x=20, y=140)
#
# update = Button(root, text="update", font="italic 10, bg="white", command=update)
# update.place(x=20, y=140)
#
# get = Button(root, text="insert", font="italic 10, bg="white", command=get)
# get.place(x=20, y=140)
#
# my_db = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1", database="mydatabase", auth_plugin="mysql_native_password")
# my_cursor = my_db.cursor()
# xy = my_cursor.execute("select * from login")
#
# for i in my_cursor:
#     print(i)

root.mainloop()
