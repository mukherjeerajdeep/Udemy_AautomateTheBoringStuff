def spam():
    eggs = 99 # after here the local scope vanishes, so eggs is gone

spam()
print(eggs) # will throw error
