from tkinter import *
from tkinter import messagebox
from functools import partial
from hashtable_string import HashTable

#Paths
path = r"Front end\data\NewStorage\bookings.txt"
path1 = r"Front end\data\booked_tables.txt"
seats_booked = 0
data_seats = "("

def booker(win):
    global data_seats
    global path1
    data_seats = data_seats[: len(data_seats)-1]
    data_seats += ")"
    with open(path1, "a") as f:
        f.write("\n")
        f.write(data_seats)
    win.destroy()

def run_book_table():
    def book_seat(seat_id):
        global seats_booked
        global path
        global data_seats

        button = seats[seat_id]
        if button.cget("bg") == "red":
            messagebox.showinfo("Seat Booking", "This seat is already booked.")
        elif(button.cget("bg") == "green"):
            confirm = messagebox.askyesno("Seat Booking", f"Book Seat {seat_id}?")         
            if confirm:
                seats_booked += 1
                button.config(bg="red")
                button.config(state="disabled")
                messagebox.showinfo("Seat Booking", f"Seat {seat_id} is booked successfully!")
                temp = seat_id.split("-")
                data_seats += str([int(temp[0]),int(temp[1])]) + ","
            else:
                messagebox.showinfo("Seat Booking", "Seat booking cancelled.")

    win = Tk()
    win.title("Seat Booking Window")
    win.geometry("500x500")
    seats = HashTable(100)
    seat_image = PhotoImage(file=r"Front end\images\—Pngtree—blue seat_4881221.png")
    seat_image = seat_image.subsample(45,45)

    # Checking for booked tables!
    with open(path1, "r") as file:
        data_set = file.readlines()
        tup = ([None, None],)
        for data in data_set:
            if(data != "\n"):
                tup += eval(data)
        
    for row in range(1, 11):
        if(row == 3 or row == 7):
            Label(win, text=" ").grid(row=row, column=col, padx=5, pady=5)
            continue
        for col in range(1, 11):
            if(col == 4 or col == 8 or (row == 10 and (col == 9 or col ==10)) or (col == 5 and (row == 8 or row == 9 or row ==10))):
                Label(win, text=" ").grid(row=row, column=col, padx=5, pady=5)
                continue
            #Checking for Previous Booked data!
            for lst in tup:
                if(row == lst[0] and col == lst[1]):
                    seat_id = f"{row}-{col}"
                    button = Button(win, image=seat_image, bg="red", state="disabled")
                    seats[seat_id] = button
                    button.grid(row=row, column=col, padx=5, pady=5)
                    break
                else:
                    seat_id = f"{row}-{col}"
                    button = Button(win, text=seat_id, image=seat_image, bg="green", command=lambda seat=seat_id: book_seat(seat))
                    seats[seat_id] = button
                    button.grid(row=row, column=col, padx=5, pady=5)
            
    close = partial(booker, win)
    Button(win, text="Book", command=close).grid(row = row + 2, column = col)
    win.mainloop()
    