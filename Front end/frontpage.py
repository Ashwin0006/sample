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
        messagebox.showerror("Invalid credentials",
                             "Please Enter proper details!")


if __name__ == "__main__":
    win = Tk()
    win.title("TABLE RESERVATION SYSTEM")
    win.geometry("500x600")

    Label(win, text="Welcome to Table Reservations",
          font=("Copperplate Gothic Bold", 18), fg="Brown").grid(row=0, column=0, padx=20, pady=20, columnspan=2)
    Label(win, text="Login if you already have an account!",
          font=("Georgia Italic", 14)).grid(row=2, column=0, columnspan=2, padx=30, pady=20)

    namelabel = Label(win, text="Username :", font=(
        "Segoe UI bold", 14)).grid(row=5, column=0, padx=5, pady=10)
    name = StringVar()
    nameentry = Entry(win, textvariable=name, font=("Verdana", 13)).grid(
        row=5, column=1, padx=5, pady=10)

    phnolabel = Label(win, text="Phone Number :", font=(
        "Segoe UI bold", 14)).grid(row=6, column=0, padx=5, pady=10)
    phno = StringVar()
    phnoentry = Entry(win, textvariable=phno, font=("Verdana", 13)).grid(
        row=6, column=1, padx=5, pady=10)

    password = Label(win, text="Password :", font=(
        "Segoe UI bold", 14)).grid(row=7, column=0, padx=5, pady=10)
    pwd = StringVar()
    pwdentry = Entry(win, textvariable=pwd, font=("Verdana", 13)).grid(
        row=7, column=1, padx=5, pady=10)

    Login = partial(gologin)
    loginbutton = Button(win, text="Login", command=Login, font=(
        "Segoe UI bold", 14), fg="white", bg="green").grid(row=8, column=0, columnspan=2, pady=20)

    Label(win, text="Signup if you are a new user", font=(
        "Georgia Italic", 14)).grid(row=9, column=0, columnspan=2, pady=30)

    take_signup = partial(nextpage)
    signup = Button(win, text="Signup", command=take_signup,
                    font=("Segoe UI bold", 14), fg="white", bg="blue").grid(row=10, column=0, columnspan=2)

    win.mainloop()
