Generator functions allow us to write a function that can send back a value and then later resume to 
pick up where it left off

[Generator Presentation-Jose](https://docs.google.com/presentation/d/1zx2OryDGyK0pajO2G5nplxJ4XT_UTV5KdCf6vYtyBnc/edit#slide=id.g342e6de5aa_0_53)

Basically, `yield` works like a return in a function body, except it returns a generator. As a generator, 
it'll not store all values in the memory, like a non-generator `iterable`, it'll generate the values on the fly.
So, to exemplify, `range()`  is a generator (yielding a value), and if we use:

```python

for i in range(1,6):
    print(i)
```
First, it'll `yield`  the value 1 , forget about this value, then, `yield` 2 , forget about this value, then, 
`yield` 3 , and so on, one by one.
That's pretty much the basics of yield.

This type of function is a generator in Python, allowing us to generate a sequence of values over time. 
The main difference in syntax will be the use of a `yield` statement.

[Python Generator](https://www.programiz.com/python-programming/generator "optional-title")

```python
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)

Output
>>This is printed first
>>1
>>This is printed second
>>2
>>This is printed at last
>>3
```

When a generator function is compiled they become an object that supports an iteration protocol. 
That means when they are called in your code they don't actually return a value and then exit.

The advantage is that instead of having to compute an entire series of values up front, the generator computes 
one value waits until the next value is called for.

For example, the range() function doesn’t produce a list in memory for all the values from start to stop.
Instead, it just keeps track of the last number and the step size, to provide a flow of numbers.

If a user did need the list, they have to transform the generator to a list with list(range(0,10))
Let’s explore how to create our own generators!

Here is an example of a program **_without_** generators.

```python
class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result
```
The above program was lengthy and confusing. Now, let's do the same using a generator function.
Generator functions will automatically suspend and resume their execution and state around the last point of 
value generation. 

```python
def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
```

**Pipelining Generators**

Multiple generators can be used to pipeline a series of operations. This is best illustrated using an example.

Suppose we have a generator that produces the numbers in the Fibonacci series. And we have another generator 
for squaring numbers.

If we want to find out the sum of squares of numbers in the Fibonacci series, we can do it in the following 
way by pipelining the output of generator functions together.

```python
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))
```




