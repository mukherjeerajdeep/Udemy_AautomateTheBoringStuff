Decorators and their use cases 

[Jose Portilla Decorator Presentation](https://docs.google.com/presentation/d/1K1GcA_VI72-Y7bBTWRD27dqkQRgMQOq-l0PwmISd2cE/edit#slide=id.g342ea89f58_0_35)

```python
def func_needs_decorator(): # Simple sunction that runs 
    print('Hi i am desperately need a decorator')
    
>>func_needs_decorator
>><function func_needs_decorator at 0x000002102D0F64D0>

>>func_needs_decorator() # Here the actual fucntion call happens
>>Hi i am desperately need a decorator
```

pass this function as a parameter to the decorator function

```python
def new_decorator(func_needs_decorator):
    def wrapper():
        print('Some extra bit of code before the actual function runs')
        func_needs_decorator()
        print('Some extra bit of code after the actual function runs')
    return wrapper
```

calling the new_decorator will return the reference of the function
```python
>>new_decorator
>><function new_decorator at 0x000002102D166440>
```

passing the function will give back the reference of the wrapper/decorated function
```python
>>new_decorator(func_needs_decorator)
>><function new_decorator.<locals>.wrapper at 0x000002102D1663B0>
```

check the return, it says there is a local "wrapper" inside "new_decorator", so actually it poits to the wrapper reference
In this case i can assign the reference to some variable,

```python
new_ref = new_decorator(func_needs_decorator)
```

Now executing new_ref will give us the actual output

```python
>>new_ref()
>>Some extra bit of code before the actual function runs
>>Hi i am desperately need a decorator
>>Some extra bit of code after the actual function runs
```

making the whole story short we can use @sympbol in front of the function which needs decoration

```python
@new_decorator
def func_needs_decorator(): # Simple sunction that runs 
    print('Hi i am desperately need a decorator')
```

Now see what happens here, calling with @symbol will call the decorated one

```python
>>func_needs_decorator() 
>>Some extra bit of code before the actual function runs
>>Hi i am desperately need a decorator
>>Some extra bit of code after the actual function runs
```
