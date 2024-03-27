from abc import ABC, abstractmethod

# Interface define a regra de construção das outras classes.
class NotificationSender(ABC):

    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass


class EmailNotificationSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f'Email message - {message}')

# obj = EmailNotificationSender()
# obj.send_notification('Ola mundo')

class SMSNotificationSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f'SMS message - {message}')

class Notificator():
    def __init__(self, notification_sender: NotificationSender) -> None:
        self.__notification_sender = notification_sender

    def send(self, message: str) -> None:
        self.__notification_sender.send_notification(message)

objeto = Notificator(SMSNotificationSender())
objeto.send('Ola Mundo')
