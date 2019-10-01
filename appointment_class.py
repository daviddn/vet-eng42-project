class Appointment():

    def __init__(self, date, illness, pet, veterinary, price):
        self.date = date
        self.illness = illness
        self.pet = pet
        self.veterinary = veterinary
        self.price = price
        self.appointment_list = []

    def add_pet_app(self, new_pet):
        self.pet = new_pet

    def app_details(self):
        app_details_dict = {
            'date': self.date,
            'illness': self.illness,
            'pet': self.pet,
            'veterinary': self.veterinary,
            'price': self.price
        }
        return app_details_dict

    def get_date(self):
        return self.date

    def get_illness(self):
        return self.illness

    def get_pet(self):
        return self.pet

    def get_vet(self):
        return self.veterinary

    def get_price(self):
        return self.price