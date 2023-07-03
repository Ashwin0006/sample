from tkinter import *
from tkinter import messagebox
from linklist import *
from functools import partial
from notification import send_notification
from payment import run_pay
import datetime
import os


path = os.path.join(".", "Front end\\data", "seats.txt")
with open(path, "r") as f:
    for line in f:
        seats = int(line)

def check_time(time, day, month, year):
    try:
        date = datetime.datetime(year, month, day)
    except ValueError:
        messagebox.showerror(
            "Invalid date", "Please enter valid date or check the format!"
        )
        return False
    today = datetime.date.today()
    today = str(today)
    today = today.split("-")
    # Date handling!
    if (int(today[2]) + 2 < day) or (int(today[2]) > day):
        messagebox.showerror(
            "Invalid day", "Reservation can be done only within 2 days!"
        )
        return False
    if int(today[1]) != month:
        messagebox.showerror(
            "Invalid month", "Reservation acn only be done thsi month!"
        )
        return False
    if int(today[0]) != year:
        messagebox.showerror("Invalid date", "Reservation can occur only this year!")
        return False
    time = time.split(":")
    if int(time[0]) > 22 or int(time[0]) < 8:
        messagebox.showerror("Invalid time", "Hotel working time is from 8:00 to 22:00")
        return False
    if int(time[1]) > 60 or int(time[1]) < 0:
        messagebox.showerror("Invalid time", "Please enter valid time!")
        return False
    return True


def run2(customer):
    def check():
        global seats
        if seats <= 0:
            win.destroy()
            messagebox.showinfo("Seats full", "All Seats are Occupied!")

    def book(req_seats, available, date, time):
        global seats
        dt = date.get()
        tt = time.get()
        if tt.isdigit():
            messagebox.showerror("Invalid time", "Please enter proper time format!")
        else:
            dt = dt.split(".")
            day = int(dt[0])
            month = int(dt[1])
            year = int(dt[2])
            customer_seats = int(req_seats.get())
            available.destroy()
            available = Label(win, text=f"Available seats :{seats}", font=(25))
            available.grid(row=1, column=0, padx=5, pady=10)
            check()
            if check_time(tt, day, month, year):
                if customer_seats > seats:
                    messagebox.showerror(
                        "Seats not available!",
                        "Seats are currently occupied Please try again later!",
                    )
                win.destroy()
                run_pay(customer_seats)
                from payment import flag
                if(flag):
                    seats -= customer_seats
                    path1 = os.path.join(
                        ".", "Front end\\data", "customer_notifications.txt"
                    )
                    path2 = os.path.join(".", "Front end\\data", "booked_tables.txt")
                    path3 = os.path.join(".", "Front end\\data", "hotel_notifications.txt")

                    last_user = eval(customer.attributes())
                    username = last_user[0]
                    with open(path1, "a") as f:
                        notification = (
                            username
                            + " has booked "
                            + str(customer_seats)
                            + f" seats at {tt} on {day}.{month}.{year}!\n"
                        )
                        f.write(notification)

                    with open(path2, "a") as f:
                        reserve = "Name :" + username + " Seats :" + str(customer_seats) + " time :" + str(tt) + " date :" + str(dt) + "\n"
                        f.write(reserve)
                    with open(path3, "a") as f:
                        notification = str(last_user) + " has booked " + str(customer_seats) + f" seats at {tt} on {day}.{month}.{year}!\n"
                        f.write(notification)
                    messagebox.showinfo(
                        "Seats Booked", f"{customer_seats} seats has been booked!"
                    )
                    send_notification()

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

    datelabel = Label(win, text="Enter date(example: 2.7.2023) :").grid(
        row=3, column=0, padx=5, pady=10
    )
    date = StringVar()
    date_entry = Entry(win, textvariable=date).grid(row=3, column=1, padx=5, pady=10)

    timelabel = Label(win, text="Enter time(example: 14:30) :").grid(
        row=4, column=0, padx=5, pady=10
    )
    time = StringVar()
    time_entry = Entry(win, textvariable=time).grid(row=4, column=1, padx=5, pady=10)

    submit = partial(book, required_seats, available, date, time)
    submit_button = Button(win, text="BOOK", command=submit).grid(
        row=5, column=0, padx=5, pady=10
    )
    win.mainloop()

    with open(path, "w") as f:
        f.write(str(seats))
