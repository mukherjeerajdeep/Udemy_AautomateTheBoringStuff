Class structure and namings 

```python
mylist = [1,2,3]
       
mylist.count()
       
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    mylist.count()
TypeError: list.count() takes exactly one argument (0 given)

class SampleWord():
    pass

type(SampleWord)
<class 'type'>

mysample = SampleWord()

type(mysample)
<class '__main__.SampleWord'>

class Dog():
    def __init__(self, breed):
        self.breed = breed

        
my_dog = Dog()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    my_dog = Dog()
TypeError: Dog.__init__() missing 1 required positional argument: 'breed'

my_dog = Dog(breed='Lab')

type(my_dog)
<class '__main__.Dog'>

my_dog.breed
'Lab'

class Dog():
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        # expects a boolean
        self.spots = spots

        
my_dog = Dog(breed='lab', name = 'Sammy', spots = False)

my_dog.spots
False

```
Class level attribute, this is similar to the static attribute

```python
class Dog():
    # Class level attribute, this is similar to the static attribute
    species = 'mammal'
        
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        # expects a boolean
        self.spots = spots

        

my_dog = Dog(breed='lab', name = 'Sammy', spots = False)

my_dog.species
'mammal'
```

Method Call

```python
class Dog():
    # Class level attribute
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    #methods
    def bark(self):
        print("Woof!")

        
my_dog = Dog(breed='lab', name = 'Sammy')

my_dog.bark
<bound method Dog.bark of <__main__.Dog object at 0x00000263B7A87B80>>


my_dog.bark()
Woof!

class Dog():
    # Class level attribute
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    #methods
    def bark(self):
        print(self.name + "Woof!")

        

my_dog = Dog(breed='lab', name = 'Sammy')

my_dog.bark()
SammyWoof!




class Dog():
    # Class level attribute
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    #methods
    def bark(self):
        print("{} is barking Woof!".format(self.name))

        

my_dog = Dog(breed='lab', name = 'Sammy')

my_dog.bark()
Sammy is barking Woof!

# Passing the number in the method

class Dog():
    # Class level attribute
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    #methods
    def bark(self, number):
        print("{} is barking Woof! {} of times".format(self.name, number))

        
my_dog = Dog(breed='lab', name = 'Sammy')

my_dog.bark()
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    my_dog.bark()
TypeError: Dog.bark() missing 1 required positional argument: 'number'


my_dog.bark(3)
Sammy is barking Woof! 3 of times

```
Special or Dunder methods

```python
class Book():

    def __init__(self, title, author, pages):
        self.name = title
        self.author = author
        self.pages = pages


book = Book('P', 'Jose', 200)
print(book)

# If we want to print it then it will be printed as this.

C:/Rajdeep_Mukherjee/Udemy_AautomateTheBoringStuff/AI-Stewart-Python-Udemy-Course/16-OOP/special-dundar-methods.py
<__main__.Book object at 0x0000013B609B5C00>
```
