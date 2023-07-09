from tkinter import *
from tkinter import messagebox
from functools import partial

flag = False


def run_pay(seats):
    def pay():
        global flag
        flag = True
        win.destroy()

    def decline():
        global flag
        flag = False
        win.destroy()

    # Price for 1 seat reservation = 10Rs
    price = 10
    booked_price = price * seats

    win = Tk()
    win.geometry("450x400")
    win.title("Payment Portal")

    Label(win, text="Welcome to Payment Portal!", font=(
        "Copperplate Gothic Bold", 18), fg="Brown").grid(row=0, column=0, padx=10, pady=10)
    Label(win, text=f"Total seats booked are {seats}", font=(
        "Segoe UI bold", 14)).grid(row=1, column=0, padx=10, pady=10)
    Label(win, text=f"Total cost for the reservation is Rs.{booked_price} ", font=(
        "Segoe UI bold", 14), fg="Blue").grid(row=2, column=0, padx=10, pady=10)

    par_pay = partial(pay)
    pay = Button(win, text="Pay", command=par_pay, font=(
        "Segoe UI bold", 14), fg="white", bg="green").grid(row=4, column=0, padx=3, pady=5)
    decline_par = partial(decline)
    decline = Button(win, text="Decline", command=decline_par, font=(
        "Segoe UI bold", 14), fg="white", bg="Red").grid(row=5, column=0, padx=3, pady=5)

    win.mainloop()
