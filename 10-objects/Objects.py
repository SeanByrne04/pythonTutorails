import random
import sys
import os

class Animal:
    __name = ''      #'' means no value also can use none
    __height = 0
    __weight = 0
    __sound = 0

    def __init(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

        def set_name(self, name):
            self.__name = name

        def set_height(self, height):
            self.__height = height

        def set_weight(self,weight):
            self.__weight = weight

        def set_sound(self,sound):
            self.__sound =weight
        #set

        def get_name(self):
            return self.__name

        def get_height(self):
            return str(self.__height)

        def get_weight(self):
            return str(self.__weight)

        def get_sound(self):
            return self.__sound
        #get

        def get_type(self):
            print('animal')
        #prints class

        def toString(self):
            return '{} is {} cm tall and {} kilograms and says {}'.format(self.__name,
                                                                         self.__height,
                                                                         self.__weight,
                                                                         self.__sound)
#print all info


cat = Animal('Whiskers', 33, 10, 'Meow')
print(cat.toString())

class Dog(Animal):    #gives dog class data from animal class
    def__owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print('Dog')

    def toString(self):
        return '{} is {} cm tall and {} kilograms and says {} His owner is {}'.format(self.__name,
                                                                         self.__height,
                                                                         self.__weight,
                                                                         self.__sound,
                                                                         self.__owner)

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)


spot = Dog('Spot', 53, 27, 'Ruff', 'Sean')
print(spot.toString)

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)


spot.multiple_sounds(4)
spot.multiple_sounds()


        

        
        
        

    
    
