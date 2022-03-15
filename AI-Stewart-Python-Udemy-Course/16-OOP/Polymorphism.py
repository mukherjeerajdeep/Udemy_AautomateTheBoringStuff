class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("say nothing")


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("say Woof!")


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("say Meow!")

def pet_speak(pet):
    print(pet.speak())
    print('Nothing To Do')

my_dog = Dog("Blacky")
my_cat = Cat("Katy")

# my_dog.speak()
# my_cat.speak()

pet_speak(my_cat)
# pet_speak(my_dog)

