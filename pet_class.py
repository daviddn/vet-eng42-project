class Pet():

    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def pet_details(self):
        pet_details = {
            'name': self.name,
            'breed': self.breed,
            'owner': self.owner
        }
        return pet_details

    def get_owner(self):
        return self.owner

    def print_pet_details(self):
         print('Name: ' + self.name, '|Breed: ' + self.breed, self.get_owner().identify_details())