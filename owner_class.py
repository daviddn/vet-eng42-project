from human_class import *

class Owner(Human):

    def __init__(self, name, phone, email, payment_details):
        super().__init__(name, phone, email)
        self.payment_details = payment_details

    def identify_details(self):
        return '|Owner: ' + self.name + ' ' + '|Phone: ' + ' ' + self.phone + ' ' + '|Email: ' + ' ' + self.email + ' ' + '|Payment Details: ' + ' ' + self.payment_details