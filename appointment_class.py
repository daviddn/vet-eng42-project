class Appointment():

    def __init__(self, date, illness, pet, veterinary, price):
        self.date = date
        self.illness = illness
        self.pet = pet
        self.veterinary = veterinary
        self.price = price

    def add_pet_appointment(self, new_pet):
        self.pet = new_pet

    def appointment_details(self):
        appointment_details_dict = {
            'date': self.date,
            'illness': self.illness,
            'pet': self.pet,
            'veterinary': self.veterinary,
            'price': self.price
        }
        return appointment_details_dict

    def get_pet(self):
        return self.pet

    def get_vet(self):
        return self.veterinary