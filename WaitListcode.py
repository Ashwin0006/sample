

class WaitlistManager:
    def __init__(self):
        self.waitlist = []

    def add_to_waitlist(self, name):
        self.waitlist.append(name)

    def remove_from_waitlist(self):
        if not self.is_empty():
            return self.waitlist.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.waitlist) == 0

    def print_waitlist(self):
        if self.is_empty():
            print("The waitlist is empty")
        else:
            print("Waitlist:")
            for name in self.waitlist:
                print(name)

    def release_from_waitlist(self):
        if not self.is_empty():
            released_person = self.waitlist.pop(0)
            return released_person
        else:
            return None

  
        

       


#TESTCASES
waitlist_manager = WaitlistManager()

# Adding customers
waitlist_manager.add_to_waitlist({"name": "Dhoni", "phone_number": "+1234567890"})
waitlist_manager.add_to_waitlist({"name": "Kohli", "phone_number": "+9876543210"})
waitlist_manager.add_to_waitlist({"name": "Sachin", "phone_number": "+1122334455"})

# Printing 
waitlist_manager.print_waitlist()


# Releasing and sending notification
released_person = waitlist_manager.remove_from_waitlist()
if released_person:
    print("Released person:", released_person['name'])


# Printing the updated waitlist
waitlist_manager.print_waitlist()
