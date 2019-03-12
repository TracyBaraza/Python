Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> names= ['tracy','ann','maggie']
>>> print(names)
['tracy', 'ann', 'maggie']
>>> print(names[1])
ann
>>> names[1] = 'nick'
>>> print(names)
['tracy', 'nick', 'maggie']
>>> for x in names:
	print(x)

	
tracy
nick
maggie
>>> if 'tracy' in names:
	print('yes, 'tracy' is in the names list')
	
SyntaxError: invalid syntax
>>> if 'tracy' in names:
	print("yes, 'tracy' is in the names list")

	
yes, 'tracy' is in the names list
>>> print(len(names))
3
>>> names.append('levis')
>>> print(names)
['tracy', 'nick', 'maggie', 'levis']
>>> names.insert(1, 'otieno')
>>> print(names)
['tracy', 'otieno', 'nick', 'maggie', 'levis']
>>> names.remove('nick')
>>> print(names)
['tracy', 'otieno', 'maggie', 'levis']
>>> names.pop()
'levis'
>>> print(names)
['tracy', 'otieno', 'maggie']
>>> names.pop(1)
'otieno'
>>> print(names)
['tracy', 'maggie']
>>> del names[0]
>>> print(names)
['maggie']
>>> del names
>>> print(names)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(names)
NameError: name 'names' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> animals=animals(('dog','cat','cow','donkey'))
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    animals=animals(('dog','cat','cow','donkey'))
NameError: name 'animals' is not defined
>>> animals=list(('dog','cat','cow','donkey'))
>>> print(animals)
['dog', 'cat', 'cow', 'donkey']
>>> ['dog', 'cat', 'cow', 'donkey']
['dog', 'cat', 'cow', 'donkey']
>>> copy(animals)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    copy(animals)
NameError: name 'copy' is not defined
>>> names.copy()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    names.copy()
NameError: name 'names' is not defined
>>> animals.copy()
['dog', 'cat', 'cow', 'donkey']
>>> animals.extend('sheep')
>>> print(animals)
['dog', 'cat', 'cow', 'donkey', 's', 'h', 'e', 'e', 'p']
>>> animals.extend("sheep")
>>> print(animals)
['dog', 'cat', 'cow', 'donkey', 's', 'h', 'e', 'e', 'p', 's', 'h', 'e', 'e', 'p']
>>> animals.extend("monkey")
>>> print(animals)
['dog', 'cat', 'cow', 'donkey', 's', 'h', 'e', 'e', 'p', 's', 'h', 'e', 'e', 'p', 'm', 'o', 'n', 'k', 'e', 'y']
>>> animals.extend("monkey"))
SyntaxError: invalid syntax
>>> animals.extend(("monkey"))
>>> print(animals)
['dog', 'cat', 'cow', 'donkey', 's', 'h', 'e', 'e', 'p', 's', 'h', 'e', 'e', 'p', 'm', 'o', 'n', 'k', 'e', 'y', 'm', 'o', 'n', 'k', 'e', 'y']
>>> animals.index[0]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    animals.index[0]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> animals.index("cat")
1
>>> animals.insert(2, "duck")
>>> print(animals)
['dog', 'cat', 'duck', 'cow', 'donkey', 's', 'h', 'e', 'e', 'p', 's', 'h', 'e', 'e', 'p', 'm', 'o', 'n', 'k', 'e', 'y', 'm', 'o', 'n', 'k', 'e', 'y']
>>> animals.pop(0)
'dog'
>>> print(animals)
['cat', 'duck', 'cow', 'donkey', 's', 'h', 'e', 'e', 'p', 's', 'h', 'e', 'e', 'p', 'm', 'o', 'n', 'k', 'e', 'y', 'm', 'o', 'n', 'k', 'e', 'y']
>>> animals.remove(0)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    animals.remove(0)
ValueError: list.remove(x): x not in list
>>> animals.remove("monkey")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    animals.remove("monkey")
ValueError: list.remove(x): x not in list
>>> animals.remove("cow")
>>> print(animals)
['cat', 'duck', 'donkey', 's', 'h', 'e', 'e', 'p', 's', 'h', 'e', 'e', 'p', 'm', 'o', 'n', 'k', 'e', 'y', 'm', 'o', 'n', 'k', 'e', 'y']
>>> animals.reverse()
>>> print(animals)
['y', 'e', 'k', 'n', 'o', 'm', 'y', 'e', 'k', 'n', 'o', 'm', 'p', 'e', 'e', 'h', 's', 'p', 'e', 'e', 'h', 's', 'donkey', 'duck', 'cat']
>>> animals.sort()
>>> print
<built-in function print>
>>> 

>>> 



9
>>> print(animals)
['cat', 'donkey', 'duck', 'e', 'e', 'e', 'e', 'e', 'e', 'h', 'h', 'k', 'k', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 's', 's', 'y', 'y']
>>> more_animals=['snake','pig','hen']
>>> animals.update(more_animals)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    animals.update(more_animals)
AttributeError: 'list' object has no attribute 'update'
>>> animals.update(more_animals)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    animals.update(more_animals)
AttributeError: 'list' object has no attribute 'update'
>>> 
