from abc import abstractmethod, ABCMeta

class Animal(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        print("say nothing")

animal = Animal('Bob')
animal.speak()

# The old way
class Super:
    def delegate(self):
        self.action()

    def action(self):
        assert False, 'action must be defined!'  # If this version is called


super_instance = Super()
super_instance.action()
