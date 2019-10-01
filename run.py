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
app_1 = Appointment('01/10/19', 'Broken Ankle', pet_1, vet_1, '100£')
app_2 = Appointment('02/10/19', 'Leg Cut', pet_2, vet_2, '50£')
app_3 = Appointment('03/10/19', 'Rabies', pet_3, vet_3, '150£')

# List of appointments
appointment_list = []
appointment_list.append(app_1)
appointment_list.append(app_2)
appointment_list.append(app_3)

# Add pet to appointment
app_1.add_pet_app(pet_4)
print(app_1.app_details())

# iterate over list of appointments and print
for appointment in appointment_list:
    print('Date: ' + appointment.get_date(), 'Illness: ' + appointment.get_illness(), 'Pet: ' + appointment.get_pet().identify_name(), 'Veterinary: ' + appointment.get_vet().identify_vet(), 'Price: ' + appointment.get_price())