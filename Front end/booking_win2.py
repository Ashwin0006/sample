from tkinter import *
from tkinter import messagebox
from linklist import *
from functools import partial
import os


path = os.path.join(".", "Front end\\data", "seats.txt")
with open(path, "r") as f:
    for line in f:
        seats = int(line)


def check():
    global seats
    if seats <= 0:
        win.destroy()
        messagebox.showinfo("Seats full", "All Seats are Occupied")


def book(req_seats, available):
    global seats
    customer_seats = int(req_seats.get())
    if customer_seats > seats:
        messagebox.showerror(
            "Seats not available!",
            "Seats are currently occupied Please try again later!",
        )
    seats -= customer_seats
    available.destroy()
    available = Label(win, text=f"Available seats :{seats}", font=(25))
    available.grid(row=1, column=0, padx=5, pady=10)
    check()
    path1 = os.path.join(".", "Front end\\data", "customer_notifications.txt")
    path2 = os.path.join(".", "Front end\\data", "data.txt")
    path3 = os.path.join(".", "Front end\\data", "hotel_notifications.txt")

    with open(path2, "r") as f:
        data = f.readlines()
        last_user = eval(data[-1])
        username = last_user[0]

    with open(path1, "a") as f:
        notification = username + " has booked " + str(customer_seats) + " seats!\n"
        f.write(notification)

    with open(path3, "a") as f:
        notification = str(last_user) + " has booked " + str(customer_seats) + " seats!\n" 
        f.write(notification)


def close():
    win.destroy()


win = Tk()
win.title("Table Reservation System")
win.geometry("400x500")


Label(win, text="Table Reservation System", font=(25)).grid(
    row=0, column=0, padx=5, pady=10
)
available = Label(win, text=f"Available seats :{seats}", font=(25))
available.grid(row=1, column=0)

requiredseats_label = Label(win, text="Please Enter the number of seats :").grid(
    row=2, column=0, padx=5, pady=10
)
required_seats = IntVar()
requiredseats_entry = Entry(win, textvariable=required_seats).grid(
    row=2, column=1, padx=5, pady=10
)

submit = partial(book, required_seats, available)
submit_button = Button(win, text="BOOK", command=submit).grid(
    row=4, column=0, padx=5, pady=10
)

close = Button(win, text="Close", command=close).grid(row=4, column=1, padx=5, pady=10)
win.mainloop()

with open(path, "w") as f:
    f.write(str(seats))




