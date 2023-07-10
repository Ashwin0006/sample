from tkinter import messagebox

class Customer:
    def __init__(self, name, phno, mail_id, password, identity):
        self._name = name.upper()
        self._phno = phno
        self._mail = mail_id
        self._pass = password
        self._id = identity

    def attributes(self):
        return str([self._name, self._phno, self._mail, self._pass, self._id])


def check_qty(ph_no_data, mail_data, name_data, password):
    if (len(ph_no_data)) != 10 or ph_no_data.isdigit() != True:
        messagebox.showerror(
            "Invalid Phone number!", "Please Enter valid Phone Number!"
        )
        return False
    if not (
        (mail_data.endswith(".com") or mail_data.endswith(
            ".in")) and ("@" in mail_data)
    ):
        messagebox.showerror("Invalid Email id",
                             "Please Enter valid Email Id!")
        return False
    if(name_data == ""):
        messagebox.showerror("Invalid Name", "Username cannot be empty!")
        return False
    if(not name_data.isalpha()):
        messagebox.showerror("Invalid Name", "Username should contain only Alphabets!")
        return False
    if(password == ""):
        messagebox.showerror("Invalid Password",
                             "Password Field should not be Blank!")
        return False
    return True


def check_user(customer):
    details = eval(customer.attributes())
    with open("Front end\\data\\data.txt", "r") as file:
        nested_data = file.readlines()
    for detail in nested_data:
        if (detail != "\n"):
            attribute = eval(detail)
            if attribute[1] == details[1]:
                messagebox.showerror(
                    "User already exists", "User with Phone Number already exists please Login!")
                exit(0)
