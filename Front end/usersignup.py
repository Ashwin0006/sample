from tkinter import *
from tkinter import messagebox
from linklist import *
from functools import partial
from cutomerclass import *
import os
from new_Bookingwin import run_new
from PIL import ImageTk, Image


# Paths change according to system
path = os.path.join(".", "Front end\\data", "id_data.txt")
path1 = os.path.join(".", "Front end\\data", "data.txt")
path2 = os.path.join(".", "Front end\\data", "id_data.txt")

with open(path, "r") as file:
    for id in file:
        if id != "\n":
            identity = int(id)


def run1():
    global path1, path2
    # Data Storage!
    data = LinkedList()

    def signup(name, phno, mail, pwd):
        global identity
        ph_no_data = phno.get()
        mail_data = mail.get()
        name_data = name.get()
        password = pwd.get()
        if (check_qty(ph_no_data, mail_data, name_data, password)):
            customer = Customer(name_data, ph_no_data,
                                mail_data, password, identity)
            check_user(customer)
            identity += 1

            details = add_data(customer)

            with open(path1, "a") as file:
                file.write(details)

            with open(path2, "a") as file:
                file.write("\n")
                file.write(str(identity))

            win1.destroy()
            run_new(customer)

    def add_data(customer):
        data.append(customer)
        string = ""
        cust = data._head
        while cust is not None:
            string += cust._item.attributes() + "\n"
            cust = cust._next
        return string

    # Main Code!
    win1 = Tk()
    win1.title("User Signup Portal")
    win1.geometry("550x300")

    canvas1 = Canvas(win1)
    canvas1.pack(fill=BOTH, expand=True)

    #Adding the images!
    bg_image = ImageTk.PhotoImage(Image.open(r"Front end\images\hotel2.jpg"))
    canvas1.create_image(0, 0, anchor=NW, image=bg_image)

    #Adding the text and labels using the create_text and create_window methods
    canvas1.create_text(150, 40, text="Username :", font=("Segoe UI bold", 14), fill="#FF00F7")
    name = StringVar()
    name_entry = Entry(win1, textvariable=name, font=("Verdana", 13), bg="lightblue")
    canvas1.create_window(400, 40, window=name_entry)

    canvas1.create_text(150, 90, text="Phone Number :", font=("Segoe UI bold", 14), fill="#FF00F7")
    phno = StringVar()
    phno_entry = Entry(win1, textvariable=phno, font=("Verdana", 13), bg="lightblue")
    canvas1.create_window(400, 90, window=phno_entry)

    canvas1.create_text(150, 140, text="Email :", font=("Segoe UI bold", 14), fill="#FF00F7")
    mail_id = StringVar()
    mail_entry = Entry(win1, textvariable=mail_id, font=("Verdana", 13), bg="lightblue")
    canvas1.create_window(400, 140, window=mail_entry)

    canvas1.create_text(150, 190, text="Password :", font=("Segoe UI bold", 14), fill="#FF00F7")
    pwd = StringVar()
    pwd_entry = Entry(win1, textvariable=pwd, font=("Verdana", 13), bg="lightblue")
    canvas1.create_window(400, 190, window=pwd_entry)

    signup_func = partial(signup, name, phno, mail_id, pwd)
    signup_button = Button(win1, text="Signup", command=signup_func, font=("Segoe UI bold", 14), fg="white", bg="green")
    canvas1.create_window(300, 260, window=signup_button)

    win1.mainloop()

