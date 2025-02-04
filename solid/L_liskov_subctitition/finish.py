class Notification:
    def notify(self, message):
        raise NotImplementedError
    
class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Email(Notification):
    def __init__(self, email):
        self.email = email
    
    def notify(self, message):
        print(f'send {message} to email: {self.email}')

class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f"Send {message} sms to phone: {self.phone}")

class NotificationService:
    def __init__(self, notification:Notification):
        self.notificaion = notification
    
    def send(self, message):
        self.notificaion.notify(message)

if __name__ == '__main__':
    
    person = Contact("Dima", "dima@gmail.com", "+380663332211")
    notification_SMS = SMS(person.phone)
    notification_Email = Email(person.email)
    notification_service = NotificationService(notification_Email)

    notification_service.send('Hello bro')
    notification_service = NotificationService(notification_SMS)
    notification_service.send('Hello bro')

    
