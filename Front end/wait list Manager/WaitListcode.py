from twilio.rest import Client

# Twilio account credentials
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'

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
            self.send_notification(released_person)
            return released_person
        else:
            return None

    def send_notification(self, person):
        # Initialize the Twilio client
        client = Client(account_sid, auth_token)

        # Assuming the person's phone number is stored along with their name
        phone_number = person.get('phone_number')

        # Customize the SMS message content
        message = client.messages.create(
            body=f"Hello {person['name']}, you have been released from the waitlist.",
            from_=twilio_phone_number,
            to=phone_number
        )

        print(f"Notification sent to {person['name']} at {phone_number}.")


#TESTCASES
waitlist_manager = WaitlistManager()

# Adding customers
waitlist_manager.add_to_waitlist({"name": "Dhoni", "phone_number": "+1234567890"})
waitlist_manager.add_to_waitlist({"name": "Kohli", "phone_number": "+9876543210"})
waitlist_manager.add_to_waitlist({"name": "Sachin", "phone_number": "+1122334455"})

# Printing 
waitlist_manager.print_waitlist()


# Releasing and sending notification
released_person = waitlist_manager.release_from_waitlist()
if released_person:
    print("Released person:", released_person['name'])


# Printing the updated waitlist
waitlist_manager.print_waitlist()
