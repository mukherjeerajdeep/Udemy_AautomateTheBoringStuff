name = 'Bob'
age = 500

if name == 'Aline':
    print("Ohh God !! You are found")
elif age < 100:
    print("You are not Alice")
elif age > 1000:
    print("Are you immortal")
# Check out that this statement was never executed as the first
# one already being satisfied so that this one will be skipped  
elif age > 100:
    print("Alice is not that old")  
else:
    print("Ooops Nothing Matched")
        
