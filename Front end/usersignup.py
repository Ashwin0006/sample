from tkinter import *
from tkinter import messagebox
from linklist import *
from functools import partial
import os


# Data Storage!
data = LinkedList()
details = ""
path = os.path.join(".", "Front end\\data", "id_data.txt")
with open(path, "r") as file:
    for id in file:
        if id != "\n":
            identity = int(id)


class Customer:
    def __init__(self, name, phno, mail_id, identity):
        self._name = name.upper()
        self._phno = phno
        self._mail = mail_id
        self._id = identity

    def attributes(self):
        return str([self._name, self._phno, self._mail, self._id])


def check_qty(ph_no_data, mail_data):
    if (len(ph_no_data)) != 10 or ph_no_data.isdigit() != True:
        messagebox.showerror(
            "Invalid Phone number!", "Please Enter valid Phone Number!"
        )
        exit(0)
    if not (
        (mail_data.endswith(".com") or mail_data.endswith(".in")) and ("@" in mail_data)
    ):
        messagebox.showerror("Invalid Email id", "Please Enter valid Email Id!")
        exit(0)


def signup(name, phno, mail):
    global details
    global identity

    ph_no_data = phno.get()
    mail_data = mail.get()
    name_data = name.get()
    check_qty(ph_no_data, mail_data)
    customer = Customer(name_data, ph_no_data, mail_data, identity)
    identity += 1
    details = add_data(customer)
    win1.destroy()


def add_data(customer):
    global data
    data.append(customer)
    string = ""
    cust = data._head
    while cust._next is not None:
        cust = cust._next
        string += cust._item.attributes() + "\n"
    return string


# Main Code!
win1 = Tk()
win1.title("User Signup Portal")
win1.geometry("400x500")

namelabel = Label(win1, text="Username :").grid(row=0, column=0, padx=5, pady=10)
name = StringVar()
nameentry = Entry(win1, textvariable=name).grid(row=0, column=1, padx=5, pady=10)

phnolabel = Label(win1, text="Phone Number :").grid(row=1, column=0, padx=5, pady=10)
phno = StringVar()
phnoentry = Entry(win1, textvariable=phno).grid(row=1, column=1, padx=5, pady=10)

maillabel = Label(win1, text="Email :").grid(row=2, column=0, padx=5, pady=10)
mail_id = StringVar()
mailentry = Entry(win1, textvariable=mail_id).grid(row=2, column=1, padx=5, pady=10)

signup = partial(signup, name, phno, mail_id)

logbutton = Button(win1, text="Signup", command=signup)
logbutton.grid(row=4, column=1, padx=5, pady=10)

win1.mainloop()

path1 = os.path.join(".", "Front end\\data", "data.txt")
with open(path1, "a") as file:
    file.write(details)

path2 = os.path.join(".", "Front end\\data", "id_data.txt")
with open(path2, "a") as file:
    file.write("\n")
    file.write(str(identity))

# Running of second window!
import booking_win2
