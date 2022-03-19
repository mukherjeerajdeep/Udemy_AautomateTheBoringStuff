Decorators and their use cases 

```python
def func_needs_decorator(): # Simple sunction that runs 
    print('Hi i am desperately need a decorator')

    
>>func_needs_decorator
>><function func_needs_decorator at 0x000002102D0F64D0>

>>func_needs_decorator() # Here the actual fucntion call happens
>>Hi i am desperately need a decorator


# pass this function as a parameter to the decorator function
def new_decorator(func_needs_decorator):

    def wrapper():
        print('Some extra bit of code before the actual function runs')
        func_needs_decorator()
        print('Some extra bit of code after the actual function runs')
    return wrapper


# calling the new_decorator will return the reference of the function
>>new_decorator
>><function new_decorator at 0x000002102D166440>

# passing the function will give back the reference of the wrapper/decorated function
>>new_decorator(func_needs_decorator)
>><function new_decorator.<locals>.wrapper at 0x000002102D1663B0>

# check the return, it says there is a local "wrapper" inside "new_decorator", so actually it poits to the wrapper reference

# In this case i can assign the reference to some variable,

new_ref = new_decorator(func_needs_decorator)

# Now executing new_ref will give us the actual output
>>new_ref()
>>Some extra bit of code before the actual function runs
>>Hi i am desperately need a decorator
>>Some extra bit of code after the actual function runs

# making the whole story short we can use @sympbol in front of the function which needs decoration
@new_decorator
def func_needs_decorator(): # Simple sunction that runs 
    print('Hi i am desperately need a decorator')

# Now see what happens here, calling with @symbol will call the decorated one    
>>func_needs_decorator() 
>>Some extra bit of code before the actual function runs
>>Hi i am desperately need a decorator
>>Some extra bit of code after the actual function runs


```