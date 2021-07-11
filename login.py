import mysql.connector
from tkinter import messagebox as mb
from tkinter import *
from datetime import *
import os

ad_login = Tk()
ad_login.resizable(False, False)
ad_login.title("Admin login")


# intro
db = mysql.connector.connect(
    user="lifechoices",
    password="@Lifechoices1234",
    host="127.0.0.1",
    database="mydatabase",
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS admin(id int(11) Not null primary key AUTO_INCREMENT, full_name varchar(60) Default null, "
    "username varchar(50) Default null ,password varchar(20) Default null)")
db.commit()

cursor.execute("INSERT INTO admin(full_name, username, password) \
   SELECT * FROM (SELECT 'Admin', 'lifechoices', '@Lifechoices1234') as temp \
   WHERE NOT EXISTS \
   (SELECT 'lifechoices' FROM admin WHERE username = 'lifechoices') LIMIT 1")

db.commit()


def login(my_db=None):
    usr = usrEnt.get()
    p = adUps.get()
    sql = "select * from admin where username=%s and password=%s"
    cursor.execute(sql, [(usr), (p)])
    datab = cursor.fetchall()

    if datab:
        my_db.showinfo("Login", "login successful")
        ad_login.destroy()
        import admin_r
    else:
        my_db.showerror("Unsuccessful", "Login failed")

def back():
    ad_login.destroy()
    import main1
    if __name__ == '__main__':
        ip = main1.Login



logBtn = Button(ad_login, text="Back", command=back)
privBtn = Button(ad_login, text="Login", command=login)

usrAdLb = Label(ad_login, text="User/Admin Name:", fg="white", bg="black")
usrEnt = Entry(ad_login)
usrAdp = Label(ad_login, text="Password", fg="white", bg="black")
adUps = Entry(ad_login)
usrAdLb.place(x=20, y=100)
usrEnt.place(x=150, y=100)
usrAdp.place(x=20, y=140)
adUps.place(x=150, y=140)
privBtn.place(x=20, y=180)
logBtn.place(x=320, y=180)



#Center gui on screen
window_height = 240
window_width = 400

screen_width = ad_login.winfo_screenwidth()
screen_height = ad_login.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

ad_login.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
ad_login.geometry("400x240")
ad_login.configure(bg="black")
ad_login.mainloop()

