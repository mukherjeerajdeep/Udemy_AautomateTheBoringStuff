
min() and max and random() and shuffle()

```python
>>> min(mylist4)
1
>>> max(mylist4)
5
>>> 
>>> from random import shuffle
>>> shuffle(mylist4)
>>> mylist4
[5, 1, 2, 4, 3]
>>> 
>>> 
>>> from random import randint
>>> mynum = randint(1,10)
>>> 
>>> mynum
5
```

Return statements 
```python
>>> def check_list_even(mylist):
	for num in mylist:
		if num%2 == 0:
			return True
	return False

>>> 
>>> check_list_even([1,2,5])
True
>>> 
>>> check_list_even([1,23,5])
False
>>> 
>>> check_list_even([1,3,6])
True
```
Return tuple 

```python
>>> #create a list of tuples
>>> work_trend = [('Abby', 100), ('Billy', 200), ('Jack', 500)]
>>> work_trend
[('Abby', 100), ('Billy', 200), ('Jack', 500)]
>>> 
>>> 
>>> def employee_of_the_month(work_trend_list):

	work_hours_max = 0
	employee_of_the_month = ''
	for employee, hours in work_trend_list:
		if work_hours_max > hours:
			work_hours_max = hours
			employee_of_the_month = employee
		else:
			pass
	return (hours, employee)

>>> employee_of_the_month(work_trend)
(500, 'Jack')
>>> 
```
**LEGB Rule:**

L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.
E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.
B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...

Validating User Input
https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/04-Milestone%20Project%20-%201/00-Warm-Up-Project-Exercises.ipynb 