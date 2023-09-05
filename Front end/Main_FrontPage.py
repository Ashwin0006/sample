from tkinter import *
from functools import partial
from usersignup import run1
from cutomerclass import *
from new_Bookingwin import run_new
from PIL import ImageTk, Image


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
        run_new(customer)
    else:
        messagebox.showerror("Invalid credentials",
                            "Please Enter proper details!")


if __name__ == "__main__":
    win = Tk()
    win.title("TABLE RESERVATION SYSTEM")
    win.geometry("600x470")

    canvas = Canvas(win)
    canvas.pack(fill=BOTH, expand=True)

    bg_image = ImageTk.PhotoImage(Image.open(r"Front end\images\hotel.png"))
    canvas.create_image(0, 0, anchor=NW, image=bg_image)

    canvas.create_text(300, 50, text="Welcome to Table Reservations", font=("Copperplate Gothic Bold", 18))

    canvas.create_text(300, 100, text="Login if you already have an account!", font=("Georgia Italic", 14), fill="black")

    canvas.create_text(150, 160, text="Username :", font=("Segoe UI bold", 14), fill="Black")

    name = StringVar()
    name_entry = Entry(win, textvariable=name, font=("Verdana", 13), bg="grey")
    canvas.create_window(350, 160, window=name_entry)

    canvas.create_text(150, 210, text="Phone Number :", font=("Segoe UI bold", 14))
    phno = StringVar()
    phno_entry = Entry(win, textvariable=phno, font=("Verdana", 13), bg="grey")
    canvas.create_window(350, 210, window=phno_entry)

    canvas.create_text(150, 260, text="Password :", font=("Segoe UI bold", 14))
    pwd = StringVar()
    pwd_entry = Entry(win, textvariable=pwd, font=("Verdana", 13), bg="grey")
    canvas.create_window(350, 260, window=pwd_entry)

    login_button = Button(win, text="Login", command=gologin, font=("Segoe UI bold", 14), fg="white", bg="green")
    canvas.create_window(280, 310, window=login_button)

    canvas.create_text(300, 360, text="Signup if you are a new user", font=("Georgia Italic", 20), fill="white")

    signup_button = Button(win, text="Signup", command=nextpage, font=("Segoe UI bold", 14), fg="white", bg="blue")
    canvas.create_window(280, 410, window=signup_button)

    win.mainloop()
