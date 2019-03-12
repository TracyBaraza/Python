Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numbers=[1,2,3,4,5,6]
>>> letters=["a","b","c","d"]
>>> 2 in numbers
True
>>> 8 in numbers
False
>>> "c" in letters
True
>>> "e" in letters
False
>>> numbers*3
[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
>>> numbers+letters
[1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd']
>>> fruits=["apple","melon","grapes","mango","banana"]
>>> fruits.append("orange")
>>> fruits
['apple', 'melon', 'grapes', 'mango', 'banana', 'orange']
>>> fruits.extend(["guava","avocado"])
>>> fruits
['apple', 'melon', 'grapes', 'mango', 'banana', 'orange', 'guava', 'avocado']
>>> fruits.pop()
'avocado'
>>> fruits
['apple', 'melon', 'grapes', 'mango', 'banana', 'orange', 'guava']
>>> fruits.remove("melon")
>>> fruits
['apple', 'grapes', 'mango', 'banana', 'orange', 'guava']
>>> fruits
['apple', 'grapes', 'mango', 'banana', 'orange', 'guava']
>>> fruits.reverse()
>>> fruits
['guava', 'orange', 'banana', 'mango', 'grapes', 'apple']
>>> fruits.sort()
>>> fruits
['apple', 'banana', 'grapes', 'guava', 'mango', 'orange']
>>> fruits.reverse()
>>> fruits
['orange', 'mango', 'guava', 'grapes', 'banana', 'apple']
>>> fruits.append("grapes")
>>> fruits.append("mango")
>>> fruits.append("grapes")
>>> fruits
['orange', 'mango', 'guava', 'grapes', 'banana', 'apple', 'grapes', 'mango', 'grapes']

>>> fruits.count("grapes")
3
>>> fruits.count("mango")
2
>>> numbers
[1, 2, 3, 4, 5, 6]
>>> sum(numbers)
21
>>> max(numbers)
6
>>> min(numbers)
1
>>> max(fruits)
'orange'
>>> min(fruits)
'apple'
>>> fruits[0]
'orange'
>>> fruits[2]
'guava'
>>> fruits[4]
'banana'
>>> numbers[1]
2
>>> numbers[3]
4
>>> numbers[5]
6
>>> fruits[-3]
'grapes'
>>> numbers[-1:-4]
[]
>>> numbers[-4:-1]
[3, 4, 5]
>>> fruits[3:]
['grapes', 'banana', 'apple', 'grapes', 'mango', 'grapes']
>>> numbers[:-2]
[1, 2, 3, 4]
>>> fruits[-5:-2]
['banana', 'apple', 'grapes']
>>> for item in list:
	do something with (item)
	
SyntaxError: invalid syntax
>>> for print in fruits:
	print(fruit)

	
Traceback (most recent call last):
  File "<pyshell#52>", line 2, in <module>
    print(fruit)
NameError: name 'fruit' is not defined
>>> for fruit in fruits:
	print(fruit)

	
Traceback (most recent call last):
  File "<pyshell#54>", line 2, in <module>
    print(fruit)
TypeError: 'str' object is not callable
>>> for fruit in fruits:
	print(fruit)

	
Traceback (most recent call last):
  File "<pyshell#56>", line 2, in <module>
    print(fruit)
TypeError: 'str' object is not callable
>>> for fruit in fruits
SyntaxError: invalid syntax
>>> for fruit in fruits:
	print(fruit)

	
Traceback (most recent call last):
  File "<pyshell#60>", line 2, in <module>
    print(fruit)
TypeError: 'str' object is not callable
>>> fruits
['orange', 'mango', 'guava', 'grapes', 'banana', 'apple', 'grapes', 'mango', 'grapes']
>>> print
'orange'
>>> for number in numbers:
	print(numbers)

	
Traceback (most recent call last):
  File "<pyshell#65>", line 2, in <module>
    print(numbers)
TypeError: 'str' object is not callable
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> 

>>> numbers=[1,2,3,4,5,6,]
>>> print(numbers)
[1, 2, 3, 4, 5, 6]
>>> for numbers in number:
	print(number)

	
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    for numbers in number:
NameError: name 'number' is not defined
>>> for number in numbers:
	print(number*10)

	
10
20
30
40
50
60
>>> for number in numbers:
	print(number**2)

	
1
4
9
16
25
36
>>> x=range(5,15)
>>> x
range(5, 15)
>>> for n in x:
	print(n)

	
5
6
7
8
9
10
11
12
13
14
>>> y=range(9,19)
>>> y
range(9, 19)
>>> for n in y:
	print(n)

	
9
10
11
12
13
14
15
16
17
18
>>> print(n*5)
90
>>> for n in y:
	print(n*5)

	
45
50
55
60
65
70
75
80
85
90
>>> squares=[numbers*number for number in numbers]
>>> print(squares)
[[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]]
>>> squares
[[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]]
>>> squares=[number*number for number in numbers]
>>> squares
[1, 4, 9, 16, 25, 36]
>>> doubles=[number*2 for number in numbers]
>>> doubles
[2, 4, 6, 8, 10, 12]
>>> e=[]
>>> e
[]
>>> for number in numbers:
	x=number*2
	e.append(x)
	e

	
[2]
[2, 4]
[2, 4, 6]
[2, 4, 6, 8]
[2, 4, 6, 8, 10]
[2, 4, 6, 8, 10, 12]
>>> e
[2, 4, 6, 8, 10, 12]
>>> 
>>> e==doubles
True
>>> m=[100,200,300,400,500]
>>> m
[100, 200, 300, 400, 500]
>>> p=[]
>>> p
[]
>>> m%7
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    m%7
TypeError: unsupported operand type(s) for %: 'list' and 'int'
>>> p=[m%7]
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    p=[m%7]
TypeError: unsupported operand type(s) for %: 'list' and 'int'
>>> p=[numbers% for in m]
SyntaxError: invalid syntax
>>> p=[numbers%7 for in m]
SyntaxError: invalid syntax
>>> p=[numbers%7 for numbers in m]
>>> p
[2, 4, 6, 1, 3]
>>> m
[100, 200, 300, 400, 500]
>>> 
>>> 
>>> 
>>> k=[]
>>> 
>>> for n in m:
	a=n%7
	k.append(a)

	
>>> k
[2, 4, 6, 1, 3]
>>> w=range(78,88)
>>> 
>>> w
range(78, 88)
>>> [x*2 for x in w]
[156, 158, 160, 162, 164, 166, 168, 170, 172, 174]
>>> for x in w:
	print(x*2)

	
156
158
160
162
164
166
168
170
172
174
>>> [x+2 for y in w]
[89, 89, 89, 89, 89, 89, 89, 89, 89, 89]
>>> x=[o,1,2,3,4,5,6,7,8,9]
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    x=[o,1,2,3,4,5,6,7,8,9]
NameError: name 'o' is not defined
>>> j=[0,1,2,3,4,5,6,7,8,9]
>>> j
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for h in j:
	h.append(1)

	
Traceback (most recent call last):
  File "<pyshell#145>", line 2, in <module>
    h.append(1)
AttributeError: 'int' object has no attribute 'append'
>>> for h in j:
	h.append(h)

	
Traceback (most recent call last):
  File "<pyshell#147>", line 2, in <module>
    h.append(h)
AttributeError: 'int' object has no attribute 'append'
>>> 
