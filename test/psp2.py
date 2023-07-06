class TableReservation:
    def __init__(self):
        self.reservations = {}
        self.support_tickets = {}
        self.offers = []

    def make_reservation(self, name, table_number, date, time):
        if table_number not in self.reservations:
            self.reservations[table_number] = []
        reservation = {'name': name, 'date': date, 'time': time}
        self.reservations[table_number].append(reservation)
        print(f"Reservation for {name} at table {table_number} on {date} at {time} has been made.")

    def get_reservations(self):
        return self.reservations

    def request_review(self, table_number, name, review):
        if table_number in self.reservations:
            for reservation in self.reservations[table_number]:
                if reservation['name'] == name:
                    reservation['review'] = review
                    print(f"Thank you, {name}, for your review!")

    def get_reviews(self, table_number):
        reviews = []
        if table_number in self.reservations:
            for reservation in self.reservations[table_number]:
                if 'review' in reservation:
                    reviews.append(reservation['review'])
        return reviews

    def create_support_ticket(self, name, issue):
        ticket_id = len(self.support_tickets) + 1
        ticket = {'name': name, 'issue': issue, 'status': 'Open'}
        self.support_tickets[ticket_id] = ticket
        print(f"Support ticket #{ticket_id} has been created for {name}.")
        return ticket_id

    def close_support_ticket(self, ticket_id):
        if ticket_id in self.support_tickets:
            self.support_tickets[ticket_id]['status'] = 'Closed'
            print(f"Support ticket #{ticket_id} has been closed.")
        else:
            print(f"Support ticket #{ticket_id} does not exist.")

    def get_support_tickets(self):
        return self.support_tickets

    def add_offer(self, offer):
        self.offers.append(offer)
        print(f"New offer added: {offer}")

    def notify_customers(self, message):
        for table_number in self.reservations:
            for reservation in self.reservations[table_number]:
                print(f"Notifying customer {reservation['name']}: {message}")

# Example usage
reservation_system = TableReservation()

# Make reservations
reservation_system.make_reservation('John', 1, '2023-07-05', '18:00')
reservation_system.make_reservation('Sarah', 2, '2023-07-05', '19:30')

# Request review
reservation_system.request_review(1, 'John', 'Great experience!')

# Create support ticket
ticket_id = reservation_system.create_support_ticket('John', 'Issue with reservation')
print(reservation_system.get_support_tickets())

# Close support ticket
reservation_system.close_support_ticket(ticket_id)
print(reservation_system.get_support_tickets())

# Add an offer
reservation_system.add_offer('50% off on desserts!')

# Notify customers about the offer
reservation_system.notify_customers("We have a special offer for you. Check it out!")