from tkinter import *
from tkinter import messagebox
from linklist import *
from functools import partial
from notification import send_notification
from payment import run_pay
import datetime
import os
from TableBooking import *
from Cancellation import run_cancel


# Paths change according to system
path1 = os.path.join(".", r"Front end\data", "customer_notifications.txt")
path2 = os.path.join(".", r"Front end\data", "bookings.txt")
path3 = os.path.join(".", r"Front end\data", "hotel_notifications.txt")



def run_new(customer):
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
            if int(today[2]) <= 31 and int(today[2] >= 28):
                return True
            if (int(today[1]) == 2):
                if int(today[2]) <= 29 and int(today[2] >= 27):
                    return True
            messagebox.showerror(
                "Invalid month", "Reservation can only be done this month!"
            )
            return False
        if int(today[0]) != year:
            if (int(today[1]) == 12):
                if int(today[2]) <= 31 and int(today[2] >= 29):
                    return True
            messagebox.showerror(
                "Invalid date", "Reservation can occur only this year!")
            return False
        # Time Handling !
        time_list = time.split(":")
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")
        if int(time_list[0]) > 22 or int(time_list[0]) < 8:
            messagebox.showerror(
                "Invalid time", "Hotel working time is from 8:00 to 22:00")
            return False
        if int(time_list[1]) >= 60 or int(time_list[1]) < 0:
            messagebox.showerror("Invalid time", "Please enter valid time!")
            return False
        if (day == int(today[2])):
            if (current_time >= time):
                messagebox.showerror("Invalid time", "Please enter future time!")
                return False
        return True



    def book(date, time):
        global seats, path1, path2, path3
        dt = date.get()
        tt = time.get()
        if tt.isdigit():
            messagebox.showerror(
                "Invalid time", "Please enter proper time format!")
        else:
            dt = dt.split(".")
            day = int(dt[0])
            month = int(dt[1])
            year = int(dt[2])
            if check_time(tt, day, month, year):
                win.destroy()
                run_book_table()
                from TableBooking import seats_booked, data_seats
                run_pay(seats_booked)
                from payment import flag
                if (flag):
                    last_user = eval(customer.attributes())
                    username = last_user[0]
                    with open(path1, "a") as f:
                        notification = (
                            username
                            + " has booked "
                            + str(seats_booked)
                            + f" seats at {tt} on {day}.{month}.{year}!\n"
                        )
                        f.write(notification)

                    with open(path2, "a") as f:
                        reserve = "Name :" + username + " Seats :" + \
                            str(data_seats) + " time :" + \
                            str(tt) + " date :" + str(dt) + "\n"
                        f.write(reserve)
                    with open(path3, "a") as f:
                        notification = str(last_user) + " has booked " + str(
                            data_seats) + f" seats at {tt} on {day}.{month}.{year}!\n"
                        f.write(notification)
                    messagebox.showinfo(
                        "Seats Booked", f"{data_seats} seats has been booked!"
                    )
                    send_notification()

    win = Tk()
    win.title("Table Reservation System")
    #win.geometry("650x500")

    Label(win, text="Welcome to Table Reservations",
            font=("Copperplate Gothic Bold", 18), fg="Brown").grid(
        row=0, column=0, padx=15, pady=20, columnspan=2
    )
    Label(win, text="Reservation Available only within 2 days!\nWorking Time : 8:00 to 22:00",
            font=("Copperplate Gothic Bold", 18), fg="Brown").grid(
        row=1, column=0, padx=15, pady=20, columnspan=2
    )

    datelabel = Label(win, text="Enter date(example: 12.7.2023) :", font=("Segoe UI bold", 14)).grid(
        row=4, column=0, padx=5, pady=10
    )
    date = StringVar()
    date_entry = Entry(win, textvariable=date, font=("Verdana", 13)).grid(
        row=4, column=1, pady=10)

    timelabel = Label(win, text="Enter time(example: 14:30) :", font=("Segoe UI bold", 14)).grid(
        row=5, column=0, padx=5, pady=10
    )
    time = StringVar()
    time_entry = Entry(win, textvariable=time, font=("Verdana", 13)).grid(
        row=5, column=1, pady=10)

    submit = partial(book, date, time)
    submit_button = Button(win, text="BOOK", command=submit, font=("Segoe UI bold", 14), fg="white", bg="green").grid(
        row=6, column=0, pady=20, columnspan=2
    )

    delete = partial(run_cancel, customer, win)
    Label(win, text="Please Click On This Button \nIf You Want To Cancel Booked Seats!", font=("Copperplate Gothic Bold", 14), fg="Brown").grid(
        row=7, column=0, padx=15, pady=20, columnspan=2)
    delete_button = Button(win, text="Cancel Booked Seats", command=delete, font=("Segoe UI bold", 14), fg="white", bg="green").grid(
        row=8, column=0, padx = 5, pady=20, columnspan=2)
    win.mainloop()
