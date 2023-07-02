def send_notification():
    with open(r"Front end\data\customer_notifications.txt", "r") as file:
        notifications = file.readlines()
        print("Cutomer Notification :", notifications[-1])
    with open(r"Front end\data\hotel_notifications.txt", "r") as file:
        notifications = file.readlines()
        print("Manager Notificaation :", notifications[-1])