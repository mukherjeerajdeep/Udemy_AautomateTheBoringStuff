class Animal:

    def __init__(self, breed='lab', color='black'):
        self.breed = breed
        self.color = color

    def number_of_legs(self):
        print(f"{self.breed} has four legs and color is {self.color}")


class Dog(Animal):

    def __init__(self, breed, color, name):
        super().__init__(breed, color)
        self.name = name

    def number_of_legs(self):
        print("Dog has name %s" % self.name)  # Oldest
        print("Dog has name {}".format(self.name))  # Old/new
        print(f"Dog has name {self.name}")  # Newest, called f-string


an_animal = Animal('German-Shepherd', 'brown')
an_animal.number_of_legs()

my_dog = Dog('Doberman', 'spotted with black', 'blacky')
print(my_dog.name + " " + my_dog.color + " " + my_dog.breed)
my_dog.number_of_legs()
