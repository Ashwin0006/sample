from tkinter import *
from tkinter import messagebox
from functools import partial
from linkedlist import LinkedList

path = r"Front end\data\hotel_notifications.txt"
path1 = r"Front end\data\booked_tables.txt"
path2 = r"Front end\data\bookings.txt"




def del_seats(imp_seats):
    global path, path1, path2
    with open(path, "r") as f:
        new_data = []
        for line in f.readlines():
            if (str(imp_seats) not in line):
                new_data.append(line)
    with open(path, "w") as file:
        for i in new_data:
            file.write(str(i))
    
    with open(path1, "r") as f1:
        new_data = []
        for line in f1.readlines():
            if (str(imp_seats) not in line):
                new_data.append(line)
    with open(path1, "w") as file1:
        for i in new_data:
            file1.write(str(i))

    with open(path2, "r") as f2:
        new_data = []
        for line in f2.readlines():
            if (str(imp_seats) not in line):
                new_data.append(line)
    with open(path2, "w") as file2:
        for i in new_data:
            file2.write(str(i))
def data_func():
    global path
    
    with open(path, "r") as file:
        data = LinkedList()
        lst = file.readlines()
        for i in lst:
            if(i != "\n"):
                for j in i:
                    if(j == "]"):
                        index = i.index(j)+1
                        data_cust = i[:index]
                        temp = eval(data_cust)
                        remaining = i[index:]
                        for k in range(len(remaining)):
                            if(remaining[k] == "("):
                                index1 = k
                            elif(remaining[k] == ")"):
                                index2 = k
                                break
                        tup = remaining[index1 : index2 + 1]
                        temp.append(tup)
                        remaining = remaining[index2+1 : ].strip()
                        remaining = remaining.split(" ")
                        temp.append(remaining[2])
                        date = remaining[-1]
                        date = date[:len(date)-1]
                        temp.append(date)
                        break
                data.append(temp)
    return data
def check_no(phno, data):
    ele = data.search_phno(phno)
    if(ele is None):
        messagebox.showinfo("User Not Found!", "User Hasn't Reserved any Tables!")
        exit(0)
    else:
        acquired_data = eval(ele[5])
        return acquired_data

def refund_func(refund, win, seats):
    win.destroy()
    messagebox.showinfo("Seatings Cancelled", f"Booked Seats-{seats} are cancelled and Amount of {refund} is refunded!")
    del_seats(seats)
    

def run_cancel(customer, win1):
    win1.destroy()
    win = Tk()
    win.geometry("500x500")
    win.title("Cancellation of Seats Portal")

    phno = customer._phno
    name = customer._name
    data = data_func()
    seats = check_no(phno, data) # Important 
    if(seats is not None):
        no_seats = len(seats)
        Original_Charge = 10 #Cost of Booking is Rs.10
        charge = 5 #Cost of Deeletion is Rs.5
        Total = Original_Charge * no_seats
        fine = charge * no_seats
        refund = Total - fine
        Label(win, text = f"Total Seats Booked by {name} is {no_seats}").grid(row=0, column=0)
        Label(win, text = f"Amount To be Refunded is {refund}").grid(row=1, column=0)

        canc = partial(refund_func, refund, win, seats)
        refund_Button = Button(win, text="Cancel and Refund", command = canc).grid(row=2, column=0)

    win.mainloop()


