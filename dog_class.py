import datetime
from enum import Enum
# import dog_life

class DogBreed(Enum):
    UNKNOWN = 0
    HUSKY = 1
    POODLE = 2
    BULLDOG = 3
    GOLDEN_RETRIEVER = 4

class Pet:
    def __init__(self, name, size, birth):
        self.set_name(name)
        self.size = size
        self.birth = birth
    def get_age(self):
        return datetime.timedelta(datetime.date, self.birth)
    def get_name(self):
        return self.name
    def set_name(self, name):
        if not (2 <= len(name) <= 30):
            raise ValueError('Invalid length of name')
        self.name = name.title()

class Dog(Pet):
    def __init__(self, quantity):
        super().__init__(self, quantity)
    def make_sound(self):
        print('Wooof!')
    def get_quantity(self):
        return self.quantity


class Cat(Pet):
    def __init__(self, quantity):
        super().__init__(self, quantity)
    def make_sound(self):
        print('Meeeow')
    def get_quantity(self):
        return self.quantity

def main():
    pet = Pet('tom', 'mid', datetime.date(2021, 12, 7))
    print(pet.get_name())

main()