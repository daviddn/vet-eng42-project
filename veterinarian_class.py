from human_class import *


class Veterinarian(Human):

    def __init__(self, name, phone, email, specialization):
        super().__init__(name, phone, email)
        self.specialization = specialization

    def identify_vet(self):
        return self.name