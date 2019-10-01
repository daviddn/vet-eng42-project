from veterinarian_class import *
from owner_class import *
from pet_class import *
from appointment_class import *

# create 3 owners
owner_1 = Owner('David', '05555123456', 'davidowner@gmail.com', '12345')
owner_2 = Owner('Cesare', '05555654321', 'cesareowner@gmail.com', '23456')
owner_3 = Owner('Thomas', '05555567890', 'thomasowner@gmail.com', '34567')

# List of owners
owner_list = [owner_1, owner_2, owner_3]

# create 3 vets
vet_1 = Veterinarian('Bob', '0555098765', 'bobvet@gmail.com', 'Fractures')
vet_2 = Veterinarian('Frank', '0555121212', 'frankvet@gmail.com', 'Wounds')
vet_3 = Veterinarian('Joe', '0555909090', 'joevet@gmail.com', 'Diseases')

# create 4 pets
pet_1 = Pet('Charlie', 'Cavalier King', owner_1)
pet_2 = Pet('Otto', 'Mutt', owner_2)
pet_3 = Pet('Cookie', 'Golden Retriever', owner_3)
pet_4 = Pet('Pickles', 'Jack Russell', owner_1)

# List of Pets
pet_list = [pet_1, pet_2, pet_3, pet_4]

# create 3 appointments
appointment_1 = Appointment('01/10/19', 'Broken Ankle', pet_1, vet_1, '100£')
appointment_2 = Appointment('02/10/19', 'Leg Cut', pet_2, vet_2, '50£')
appointment_3 = Appointment('03/10/19', 'Rabies', pet_3, vet_3, '150£')

# List of appointments
appointment_list = [appointment_1, appointment_2, appointment_3]

# Add pet to appointment
appointment_1.add_pet_appointment(pet_4)

# Iterate over list of appointments and print
print('                                 APPOINTMENTS                                 ')
for appointment in appointment_list:
    print('Date: ' + appointment.date, '|Illness: ' + appointment.illness, '|Pet: ' + appointment.get_pet().name, '|Veterinary: ' + appointment.get_vet().name, '|Price: ' + appointment.price)

# Iterate over list of pets and print
print('                                                        PETS                                 ')
for pet in pet_list:
    print('Name: ' + pet.name, '|Breed: ' + pet.breed, pet.get_owner().identify_details())

# List one pet and owner details
print('                                                        PET 1                                 ')
pet_1.print_pet_details()

q_add_pet = ''

while q_add_pet != 'no':
    q_add_pet = input(print('Would you like to add a pet? ')).lower()
    if q_add_pet == 'no':
        print('Ok!')
    elif q_add_pet == 'yes':
        q_name_pet = input(print('What is the name of the pet? ')).capitalize()
        q_breed_pet = input(print('What is the breed of the pet? ')).capitalize()
        q_owner_name = input(print('Who is the owner of the pet? ')).capitalize()
        q_owner_phone = input(print('What is the phone of the owner? '))
        q_owner_email = input(print('What is the email of the owner? ')).lower()
        q_owner_payment_details = input(print('What are the payment details of the owner? '))
        new_owner = Owner(q_owner_name, q_owner_phone, q_owner_email, q_owner_payment_details)
        new_pet = Pet(q_name_pet, q_breed_pet, new_owner)
        pet_list.append(new_pet)
        owner_list.append(new_owner)
        for pet in pet_list:
            print('Name: ' + pet.name, '|Breed: ' + pet.breed, pet.get_owner().identify_details())
    else:
        print('Not a valid input')

q_show_pet_details = ''

while q_show_pet_details != 'no':
    q_show_pet_details = input(print('Would you like to see details for a pet? ')).lower()
    if q_show_pet_details == 'no':
        print('Bye!')
    elif q_show_pet_details == 'yes':
        q_what_pet = int(input(print('Which pet would you like to see? Please input a number: ')))
        if q_what_pet <= len(pet_list):
            q_what_pet_detail = input(print('Which pet detail would you like to see? ')).lower()
            if q_what_pet_detail == 'name':
                print(pet_list[q_what_pet-1].name)
            if q_what_pet_detail == 'breed':
                print(pet_list[q_what_pet-1].breed)
            if q_what_pet_detail == 'owner':
                q_what_owner_detail = input(print('Which owner detail would you like to see? ')).lower()
                if q_what_owner_detail == 'name':
                    print(pet_list[q_what_pet-1].get_owner().name)
                if q_what_owner_detail == 'phone':
                    print(pet_list[q_what_pet-1].get_owner().phone)
                if q_what_owner_detail == 'email':
                    print(pet_list[q_what_pet-1].get_owner().email)
                if q_what_owner_detail == 'payment details':
                    print(pet_list[q_what_pet-1].get_owner().payment_details)
        else:
            print('Not a valid input')