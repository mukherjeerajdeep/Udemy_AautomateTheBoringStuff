def eggs(cheese):
    cheese.append('Hello')

spam = [1,2,3]
# method called here and passes the reference, the method parameter copies it
# and uses it and then goes out of scope, however the changes are done in both
# cheese list and spam list. 
eggs(spam) 
print(spam)
