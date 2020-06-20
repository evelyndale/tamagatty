import random
import datetime

pet_name = input("What is the name of your pet?")
pet_color = input("What color is your pet?")

def random_event():
    dice_state = random.randrange(10)
    if(dice_state < 5):
        print("Your dog was eaten by a slightly smaller dog")
    elif(dice_state >= 5 <= 10):
        print("Your dog ate an eagle. Good job!")
    else:
        print("Your dice are seriously busted, friend")
    return(dice_state)

class MyPet:
    def __init__(self, name, color, species):
        self.name = name
        self.color = color
        self.species = species

pet_1 = MyPet(pet_name, pet_color, "cat")

print(f"The name of your pet is {pet_1.name}")
print(f"{pet_1.name} is a lovely {pet_1.color} {pet_1.species}!")
print(f"{pet_1.name} was born on {datetime.datetime.now()}")
random_event()

