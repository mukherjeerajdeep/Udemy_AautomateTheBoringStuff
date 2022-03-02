myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

for k in list(myCat.keys()):
    print(k)

print()
print(':::: Dict way :::')

for k,v in list(myCat.items()):
    print(k, v)

print()
print(':::: Tuple way :::')

# Or in Tuple way
for i in list(myCat.items()):
    print(i)
