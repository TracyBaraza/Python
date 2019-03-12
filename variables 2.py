Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('i love me')
i love me
>>> A=Tracy
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    A=Tracy
NameError: name 'Tracy' is not defined
>>> A='tracy'
>>> print(A)
tracy
>>> firstname=input('what is your first name')
what is your first name tracy
>>> lastName=input('what is your last name?)
		   
SyntaxError: EOL while scanning string literal
>>> lastName=input('what is your last name?')
		   
what is your last name? Tracy
>>> Baraza
		   
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    Baraza
NameError: name 'Baraza' is not defined
>>> print('hello'+ firstname + lastName)
		   
hello tracy Tracy
>>> print("hey "+firstname + " " + lastName)
		   
hey  tracy  Tracy
>>> animal=input("what is your favorite animal?")
		   
what is your favorite animal? cat
>>> building=input("Name a famous building: ")
		   
Name a famous building: 
>>> color=input("what is your favorite color? ")
		   
what is your favorite color? 
>>> print("Hickory Dickory Dock!")
		   
Hickory Dickory Dock!
>>> print("the "+color+" "animal+" ran up the "+building)
		   
SyntaxError: invalid syntax
>>> pet=input("what is your best pet?")
		   
what is your best pet? cat
>>> tower=input("name a tall building: ")
		   
name a tall building: times tower
>>> color=input("what is your best color? ")
		   
what is your best color? white
>>> print("The "+color+" "+pet+" ran up the "+tower)
		   
The white  cat ran up the times tower
>>> 
