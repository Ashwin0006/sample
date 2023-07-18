from linkedlist import LinkedList
from tkinter import *
from tkinter import messagebox
from functools import partial


path = r"Front end\data\hotel_notifications.txt"
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
def check_no(phno):
    number = phno.get()
    ele = data.search_phno(number)
    if(ele is None):
        messagebox.showinfo("User Not Found!", "User Hasn't Reserved any Tables!")
        return
    else:
        messagebox.showinfo("User Details", 
                            f"Name :{ele[0]}\nPh.No :{ele[1]}\nEmail :{ele[2]}\nSeats :{ele[5]}\nTime :{ele[6]}\nDate :{ele[7]}")


win = Tk()
win.geometry("500x500")
win.title("Guest Profile History")

Label(win, text="Enter Phone Number to Check Reservation", font=("Segoe UI bold", 16), fg="dark green").grid(
    row=0, column=0, padx=20, pady=20, columnspan=2)


phno = StringVar()
number_entry = Entry(win, textvariable=phno, font=("Segoe UI bold", 16), fg="dark green").grid(
    row=1, column=0, padx=20, pady=20, columnspan=2)

checker = partial(check_no, phno)
check_button = Button(win, text="Check", command=checker).grid(
    row=3, column=0, padx=20, pady=20, columnspan=2)
win.mainloop()




