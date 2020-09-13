from pdb import set_trace as breakpoint
"""
Create a Person class with the following attributes and methods

Instance Attributes

name
age - age should be between 0 and 120, if the age is outside of this range at the time of instantiation, set it to 21
add 2 more instance attributes
Methods

greets - a method that takes in a name and returns 'Hello, [INPUT NAME]! My name is [INSTANCE NAME], nice to meet you!'
had_birthday - a method that increments age by 1
Write a method that uses one of the instance attributes you added

"""

class Person():
    def __init__(self, name, age, birth_year, home_state):
        self.name=name
  
        # Create if statement for the age
        if 0 <= age <= 120:
           self.age = age
        else:
           self.age = 999
    
        self.birth_year=birth_year
        self.home_state=home_state
    
    # Define for model
    def greets(self):
        print(f'Hello Harun! My name is {self.name}, nice to meet you!')

    def had_birth(self):
        self.age += 1

    def where_you_from(self):
        print(f'I am from {self.home_state}!')


if __name__=="__main__":

    person1=Person("Elif",38, 1981 ,"Wisconsin")
    person2=Person("Musa",41, 1979,"Wisconsin")
    breakpoint()





