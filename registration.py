from tkinter import *
import mysql.connector
from tkinter import messagebox as mb


reg = Tk()
reg.title("Create User")
reg.resizable(False, False)

db = mysql.connector.connect(
    user="lifechoices",
    password="@Lifechoices1234",
    host="localhost",
    database="mydb",
    auth_plugin="mysql_native_password"
)

cursor = db.cursor()

db.commit()


def show():
    psswrd.config(show="")


#  intro
nameRegLb = Label(reg, text="Full Name:", fg="white", bg="black")
nameReg = Entry(reg)
usrNamelb = Label(reg, text="Username:", fg="white", bg="black")
psswrdlb = Label(reg, text="Password:", fg="white", bg="black")

snameLb = Label(reg, text="surname:", fg="white", bg="black")
sname = Entry(reg)

idLb = Label(reg, text="id:", fg="white", bg="black")
id = Entry(reg)

mobileLb = Label(reg, text="mobile:", fg="white", bg="black")
mobile = Entry(reg)

next_of_kin_mobileLb = Label(reg, text="next of kin mobile:", fg="white", bg="black")
next_of_kin_mobile = Entry(reg)



usrName = Entry(reg)
psswrd = Entry(reg, show='*')


def addUser():
    try:
        user_info = (nameReg.get(), str(usrName.get()), str(psswrd.get()))
        comm = "INSERT INTO users(name, username, password, surname, id, mobile, next_of_kin, next_of_kin_mobile) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        cursor.execute(comm, user_info)

        db.commit()
        mb.showinfo("Confirmation", "User Created Successfully")
        reg.destroy()
        import main1

    except:
        mb.showerror("error", "Username already exist")
        reg.destroy()
        import main1


def back():
    reg.destroy()
    import main



cBtn = Button(reg, text="Create student", command=addUser)
bBtn = Button(reg, text="Back", command=back)
shwPss = Checkbutton(reg, text="Show Password", command=show, fg="white", bg="black")

nameRegLb.place(x=10, y=100)
nameReg.place(x=90, y=100)
usrNamelb.place(x=10, y=140)
usrName.place(x=90, y=140)
psswrdlb.place(x=10, y=180)
psswrd.place(x=90, y=180)
cBtn.place(x=10, y=400)
bBtn.place(x=350, y=220)
shwPss.place(x=280, y=180)
snameLb.place(x=10, y=220)
sname.place(x=90, y=220)
idLb.place(x=10, y=260)
id.place(x=90, y=260)
mobileLb.place(x=10, y=300)
mobile.place(x=90, y=300)
next_of_kin_mobileLb.place(x=10, y=340)
next_of_kin_mobile.place(x=160, y=340)



# Center Gui to screen
window_height = 270
window_width = 400

screen_width = reg.winfo_screenwidth()
screen_height = reg.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))

reg.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

reg.config(bg="black")
reg.geometry("700x450")
reg.mainloop()
