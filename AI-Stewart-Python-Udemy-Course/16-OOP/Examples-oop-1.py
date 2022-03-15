class Dog():
    # Class level attribute
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # methods
    def bark(self, number):
        print("{} is barking Woof! {} times".format(self.name, number))


my_dog = Dog(breed='lab', name='Sammy')

my_dog.bark(3)
