from tkinter import *
from tkinter import messagebox
from hashtable import HashTable
from functools import partial

# Paths change according to system
path  = r"Front end\data\data.txt"
def get_data(phno, ht):
    key = int(phno.get())
    if(ht[key] != False):
        data = ht[key]
        print(data)
        messagebox.showinfo("User Found", f"Name :{data[0]}\nPh.No :{data[1]}\nEmail :{data[2]}\nUser_id :{data[4]}")
    else:
        messagebox.showerror("User Not found", "User does not exist")
        


if(__name__ == "__main__"):
    ht = HashTable(10)
    with open(path, "r") as file:
        for line in file:
            if(line != "\n"):
                data = eval(line)
                key = phno = data[1]
                val = data
                ht.add(int(phno), data)

    win = Tk()
    win.geometry("400x500")
    win.title("UserData Book")

    phnolabel = Label(win, text="Enter Phone Number :").grid(row=0, column=0, padx=5, pady=10)
    phno = StringVar()
    phnoentry = Entry(win, textvariable=phno).grid(row=0, column=1, padx=5, pady=10)
    retrieve = partial(get_data, phno, ht)
    submit_button = Button(win, text="Check", command=retrieve).grid(row=1, column=1, padx=5, pady=10)

    win.mainloop()
