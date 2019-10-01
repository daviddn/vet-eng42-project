from veterinarian_class import *
from owner_class import *
from pet_class import *
from appointment_class import *

# create 3 owners
owner_1 = Owner('David', '05555123456', 'davidowner@gmail.com', '12345')
owner_2 = Owner('Cesare', '05555654321', 'cesareowner@gmail.com', '23456')
owner_3 = Owner('Thomas', '05555567890', 'thomasowner@gmail.com', '34567')

# create 3 vets
vet_1 = Veterinarian('Bob', '0555098765', 'bobvet@gmail.com', 'Fractures')
vet_2 = Veterinarian('Frank', '0555121212', 'frankvet@gmail.com', 'Wounds')
vet_3 = Veterinarian('Joe', '0555909090', 'joevet@gmail.com', 'Diseases')

# create 4 pets
pet_1 = Pet('Charlie', 'Cavalier King', owner_1)
pet_2 = Pet('Otto', 'Mutt', owner_2)
pet_3 = Pet('Cookie', 'Golden Retriever', owner_3)
pet_4 = Pet('Pickles', 'Jack Russell', owner_1)

# create 3 appointments
appointment_1 = Appointment('01/10/19', 'Broken Ankle', pet_1, vet_1, '100£')
appointment_2 = Appointment('02/10/19', 'Leg Cut', pet_2, vet_2, '50£')
appointment_3 = Appointment('03/10/19', 'Rabies', pet_3, vet_3, '150£')

# List of appointments
appointment_list = []
appointment_list.append(appointment_1)
appointment_list.append(appointment_2)
appointment_list.append(appointment_3)

# Add pet to appointment
appointment_1.add_pet_appointment(pet_4)

# Iterate over list of appointments and print
print('                                 APPOINTMENTS                                 ')
for appointment in appointment_list:
    print('Date: ' + appointment.date, '|Illness: ' + appointment.illness, '|Pet: ' + appointment.get_pet().name, '|Veterinary: ' + appointment.get_vet().name, '|Price: ' + appointment.price)

# List of Pets
pet_list = []
pet_list.append(pet_1)
pet_list.append(pet_2)
pet_list.append(pet_3)
pet_list.append(pet_4)

# Iterate over list of pets and print
print('                                                        PETS                                 ')
for pet in pet_list:
    print('Name: ' + pet.name, '|Breed: ' + pet.breed, pet.get_owner().identify_details())

# List one pet and owner details
print('                                                        PET 1                                 ')
pet_1.print_pet_details()