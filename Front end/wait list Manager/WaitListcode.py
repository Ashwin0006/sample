from hashtable1 import HashTable
from tkinter import *
from tkinter import messagebox
from Queue import Queue
from functools import partial

path = r"Front end\data\data.txt"
with open(path, "r") as file:
    lst = file.readlines()
    lst = lst[1:]

class WaitlistManager:
    def __init__(self):
        self.waitlist = Queue()

    def add_to_waitlist(self, name):
        self.waitlist.enqueue(name)

    def remove_from_waitlist(self):
        if not self.is_empty():
            return self.waitlist.dequeue()
        else:
            return None

    def is_empty(self):
        return len(self.waitlist) == 0

    def print_waitlist(self):
        if self.is_empty():
            print("The waitlist is empty")
        else:
            print("Waitlist:")
            for hashtable in self.waitlist.getqueue():
                print(hashtable["name"], hashtable["phone_number"])
    
    def __str__(self):
        string = ""
        if self.is_empty():
           return string
        else:
            string += "Waitlist:\n"
            for hashtable in self.waitlist.getqueue():
                string += str(hashtable["name"]) + ", " + str(hashtable["phone_number"])
        return string
    
    def string(self):
        string = ""
        if self.is_empty():
           return string
        else:
            string += "Waitlist:\n"
            for hashtable in self.waitlist.getqueue():
                string += str(hashtable["name"]) + " - " + str(hashtable["phone_number"]) + "\n"
        return string
    
    def release_from_waitlist(self):
        if not self.is_empty():
            released_person = self.waitlist.dequeue()
            return released_person
        else:
            return None

def release(waitlist_manager):
    global WaitlistLabel
    released_person = waitlist_manager.remove_from_waitlist()
    WaitlistLabel.destroy()
    txt = waitlist_manager.string()
    if(txt is None or txt == ""):
        txt = "Wait List is Empty!"
    label = Label(win, text=txt, font=("Segoe UI bold", 16), fg="Black")
    label.grid(row=0, column=0, padx=20, pady=20, columnspan=2)
    WaitlistLabel = label
    

#TESTCASES
waitlist_manager = WaitlistManager()

#HashTable implementations
for details in lst:
    detail = eval(details)
    hash_table = HashTable()
    hash_table.add("name", detail[0])
    hash_table.add("phone_number", detail[1])
    #Adding Customers!
    waitlist_manager.add_to_waitlist(hash_table)

win = Tk()
win.title("Wait List Management")
win.geometry("400x400")


lst = waitlist_manager.string()
WaitlistLabel = Label(win, text=lst, font=("Segoe UI bold", 16), fg="Black")
WaitlistLabel.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

# Releasing and sending notification
remove = partial(release, waitlist_manager)
rem_but = Button(win, text="Release User", command=remove).grid(row=2, column=0, padx=20, pady=12, columnspan=2)


win.mainloop()
