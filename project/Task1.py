# A program showing some python class functionality for an example class Pet.
#
# @author McMillian, Caleb
# @assignment CSCI 333 Project
# @date 8/9/2022
#

class Pet(object):
    def __init__(self, pet_name="", pet_animal_type="", pet_age=0):
        self.__name = pet_name
        self.__animal_type = pet_animal_type
        self.__age = pet_age

    def set_name(self, pet_name):
        self.__name = pet_name

    def set_animal_type(self, pet_animal_type):
        self.__animal_type = pet_animal_type

    def set_age(self, pet_age):
        self.__age = pet_age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


if __name__ == '__main__':
    pet = Pet()
    name = input("Enter a name for the pet: ")
    pet.set_name(name)
    animal_type = input("Enter a type for the pet: ")
    pet.set_animal_type(animal_type)
    age = input("Enter an age for the pet: ")
    try:
        age = int(age)
        pet.set_age(age)
    except ValueError:
        print("Please give an integer for age. Defaulted to 0.")

    print("Pet name:", pet.get_name())
    print("Pet type:", pet.get_animal_type())
    print("Pet age:", pet.get_age())
