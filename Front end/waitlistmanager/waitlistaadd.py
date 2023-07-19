from tkinter import *
from functools import partial
from tkinter import messagebox
from hashtable import HashTable

def run5():
    path1 = r"Front end\data\waitlist.txt"
    path2 = r"Front end\data\data.txt"
    ht = HashTable(10)
    with open(path2, "r") as file:
        for line in file:
            if(line != "\n"):
                data = eval(line)
                key = phno = data[1]
                val = data
                ht.add(int(phno), data)


    def get_data(phno, ht, seat, time):
        key = int(phno.get())
        if(ht[key] != False):
            data = ht[key]
            with open(path1, "a") as file:
                file.write("\n" + str(data) + " has booked " + str(seat) + " at " + str(time))
        else:
            messagebox.showerror("User Not found", "User does not exist")

    def add_wait(ph_no, seat, time):
        get_data(ph_no, ht, seat.get(), time.get())





    win = Tk()
    win.geometry("500x600")
    win.title("Add Waitlist")

    Label(win, text="Enter the Customer Details to add to WaitList").grid(row=0, column=0, padx=5, pady=10)

    Label(win, text="Enter the Phone Number of the person :").grid(row=1, column=0, padx=5, pady=10)
    ph_no = StringVar()
    phnoEntry = Entry(win, textvariable=ph_no).grid(row=1, column=1, padx=5, pady=10)

    Label(win, text="Enter Number of Seats :").grid(row=2, column=0, padx=5, pady=10)
    seat = StringVar()
    seat_Entry = Entry(win, textvariable=seat).grid(row=2, column=1, padx=5, pady=10)

    Label(win, text="Enter The time for reservation :").grid(row=3, column=0, padx=5, pady=10)
    time = StringVar()
    time_Entry = Entry(win, textvariable=time).grid(row=3, column=1, padx=5, pady=10)

    add_entry = partial(add_wait, ph_no, seat, time)
    add_button = Button(win, text="Add To WaitList", command=add_entry).grid(row=4, column=0, padx=5, pady=10)


    win.mainloop()

run5()