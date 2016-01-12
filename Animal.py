import random
import sys
import os


#Classes

class Animal:
    _name = ""
    _height = 0
    _weigth = 0
    _sound = 0

    def __init__(self, name, height, weight, sound): #constructor
        self._name = name
        self._height = height
        self._weigth = weight
        self._sound = sound

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_height(self):
        return self._height

    def get_weight(self):
        return self._weigth

    def get_sound(self):
        return self._sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self._name,
                                                                     self._height,
                                                                     self._weigth,
                                                                     self._sound)
cat = Animal("whiskers", 33, 10, 'Meow')  #instantiation
print(cat.toString)

#Inheritance
class Dog(Animal): #extending the class

    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound) # calling super class constructor

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self, owner):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        print( "{} is {} cm tall and {} kilograms and say {} and {}".format(self._name,
                                                                            self._height,
                                                                            self._weigth,
                                                                            self._sound,
                                                                            self.__owner))

    def multiple_sounds(self, how_many=None):
        if how_many is None:
             print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

spot = Dog("Spot", 53, 27, "Ruff", "Sandeep")
print(spot.toString())
print(spot.multiple_sounds(4))
print(spot.multiple_sounds(None))

##Polymorphism
class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()
test_animals.get_type(cat)
test_animals.get_type(spot)
