Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tuple = ('apple','guava','melon')
>>> print(tuple)
('apple', 'guava', 'melon')
>>> print(tuple[1])
guava
>>> tuple[1] = 'mango'
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tuple[1] = 'mango'
TypeError: 'tuple' object does not support item assignment
>>> tuple[1] = 'guava'
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tuple[1] = 'guava'
TypeError: 'tuple' object does not support item assignment
>>> for x in tuple:
	print(x)

	
apple
guava
melon
>>> if 'apple' in tuple:
	print('yes, 'apple is in the fruit tuple tracy')
	      
SyntaxError: invalid syntax
>>> if 'apple' in tuple:
	print('yes, 'apple' is in the fruit tuple tracy')
	      
SyntaxError: invalid syntax
>>> if 'apple' in tuple:
	print("yes, 'apple' is in the fruit tuple tracy")

	      
yes, 'apple' is in the fruit tuple tracy
>>> if 'banana' in tuple:
	print("yes, 'apple' is in the fruit tuple tracy")

	      
>>> 
	      
>>> 
	      
>>> print(len(tuple))
	      
3
>>> del tuple
	      
>>> print
	      
<built-in function print>

(
>>> print(tuple)
<class 'tuple'>
>>> print(tuple)
<class 'tuple'>
>>> 
>>> tuple = ("dog","cat","frog","snake")
>>> tuple
('dog', 'cat', 'frog', 'snake')
>>> tuple = tuple(("dog","cat","frog","snake"))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tuple = tuple(("dog","cat","frog","snake"))
TypeError: 'tuple' object is not callable
>>> thistuple = tuple(("dog","cat","frog","snake"))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    thistuple = tuple(("dog","cat","frog","snake"))
TypeError: 'tuple' object is not callable
>>> tuple = thistuple(("dog","cat","frog","snake"))
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    tuple = thistuple(("dog","cat","frog","snake"))
NameError: name 'thistuple' is not defined
>>> tuple.count()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    tuple.count()
TypeError: count() takes exactly one argument (0 given)
>>> count(tuple)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    count(tuple)
NameError: name 'count' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> set = {"egg","fish","milk"}
>>> set
{'fish', 'egg', 'milk'}
>>> for x in set:
print(x)
SyntaxError: expected an indented block
>>> 
=============================== RESTART: Shell ===============================
>>> set = {"egg","fish","milk"}
>>> set
{'egg', 'milk', 'fish'}
>>> for x in set:
print(x)
SyntaxError: expected an indented block
>>> 
