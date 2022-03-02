print('My name is')

for i in range(0, 10, 2): # step is applied directly with the range() method
    print("My name is : " + str(i))


print("Same program with while loop")

i = 0
while i < 5: #Step can't be applied directly 
    print("My name is : " + str(i))
    i +=1
