from tkinter import *
from functools import partial
from usersignup import run1
from cutomerclass import *
from booking_win2 import run2


data = None
path = r"Front end\data\data.txt"

with open(path, "r") as file:
    nested_data = file.readlines()


def nextpage():
    win.destroy()
    run1()


def check_data(username, pno, password):
    global nested_data, data
    for detail in nested_data:
        if detail != "\n":
            attribute = eval(detail)
            if (
                attribute[0] == username.upper()
                and attribute[1] == pno
                and attribute[3] == password
            ):
                data = attribute
                return True
    return False


def gologin():
    global data
    username = name.get()
    pno = phno.get()
    password = pwd.get()
    if check_data(username, pno, password):
        win.destroy()
        customer = Customer(data[0], data[1], data[2], data[3], data[4])
        run2(customer)
    else:
        messagebox.showerror("Invalid credentials", "Please Enter proper details!")


if __name__ == "__main__":
    win = Tk()
    win.title("TABLE RESERVATION SYSTEM")
    win.geometry("400x500")

    Label(win, text="Welcome to Table Reservations").grid(row=0, column=0)
    Label(win, text="Login if you already have an account!").grid(row=1, column=0)

    namelabel = Label(win, text="Username :").grid(row=2, column=0, padx=5, pady=10)
    name = StringVar()
    nameentry = Entry(win, textvariable=name).grid(row=2, column=1, padx=5, pady=10)

    phnolabel = Label(win, text="Phone Number :").grid(row=3, column=0, padx=5, pady=10)
    phno = StringVar()
    phnoentry = Entry(win, textvariable=phno).grid(row=3, column=1, padx=5, pady=10)

    password = Label(win, text="Password :").grid(row=4, column=0, padx=5, pady=10)
    pwd = StringVar()
    pwdentry = Entry(win, textvariable=pwd).grid(row=4, column=1, padx=5, pady=10)

    Login = partial(gologin)
    loginbutton = Button(win, text="Login", command=Login).grid(row=5, column=1)

    Label(win, text="Signup if you are a new user").grid(row=6, column=0, pady=20)

    take_signup = partial(nextpage)
    signup = Button(win, text="Signup", command=take_signup).grid(row=7, column=0)

    win.mainloop()
