class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # This is similar to the String method overriding
    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object is deleted")

    def __add__(self, other):
        return self.pages + other


book = Book('P', 'Jose', 200)
print(book)
print(len(book))

print(book.pages + 200)

del book
# print(book.pages)

# !/usr/bin/python

class Vector:
    c = 1234

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.test = Vector.c

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def class_variable(self):
        return self.test

    def foo(self):
        pass


v1 = Vector(2, 7)
v2 = Vector(1, 8)
print(v1 + v2)

print(f"The value of Class variable 'c' is {Vector.c} and it's stored at address {id(Vector.c)}")
print(f"Vector.foo is kept at address {id(Vector.foo)}")

v3 = Vector(1, 8)

print(f"The value of Instance variable 'c' is {v3.c} and it's stored at address {id(v3.c)}")
