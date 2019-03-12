Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=20
>>> c='dog'
>>> d='cat'
>>> e=a/3
>>> e
3.3333333333333335
>>> f=str(a)
>>> f
'10'
>>> type(e)
<class 'float'>
>>> g='123'
>>> g
'123'
>>> h=int(g)
>>> h
123
>>> type(f)
<class 'str'>
>>> type(g)
<class 'str'>
>>> type(h)
<class 'int'>
>>> i=int(c)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    i=int(c)
ValueError: invalid literal for int() with base 10: 'dog'
>>> print('Hello Akirachix')
Hello Akirachix
>>> print('hello akirachix.\n class of 2019.')
hello akirachix.
 class of 2019.
>>> print('hello akirachix.\t class of 2019.')
hello akirachix.	 class of 2019.
>>> print('hello akirachix.\b class of 2019.')
hello akirachix. class of 2019.
>>> first='Tracy'
>>> last='Baraza'
>>> print(greeting)='hello,{}{}'.format(first,last)
SyntaxError: can't assign to function call
>>> (greeting)="hello,{}{}".format(first,last)
>>> print(greeting)
hello,TracyBaraza
>>> (greeting)="hello,{} {}".format(first,last)
>>> print(greeting)
hello,Tracy Baraza
>>> code='ABC123'
>>> amount=1000
>>> recepient='0712202431'
>>> print(code) 'confirmed' '!' print(greeting)"'"\n 'you have sent Ksh'ksh print(amount)\n 'to'print(recepient)
SyntaxError: invalid syntax
>>> print(code) 'confirmed' '!' print(greeting)"'"\n 'you have sent Ksh'ksh print(amount)\n 'to' print(recepient)
SyntaxError: invalid syntax
>>> print(code) 'confirmed' '!' print(greeting)"'".\n 'you have sent Ksh'ksh print(amount)\n 'to' print(recepient)
SyntaxError: invalid syntax
>>> print(code) 'confirmed' '!' 'print(greeting)'"'".\n 'you have sent Ksh'ksh print(amount)\n 'to' print(recepient)
SyntaxError: invalid syntax
>>> print(code) 'confirmed' '!' print(greeting)"'". 'you have sent Ksh'ksh print(amount) 'to' print(recepient)
SyntaxError: invalid syntax
>>> print(code) 'confirmed' '!' print(greeting)"'".\n 'you have sent Ksh' print(amount) .\n 'to' print(recepient)
SyntaxError: invalid syntax
>>> print(code) 'confirmed' '!' print(greeting)"'".\n 'you have sent Ksh' print(amount) .\n 'to' print(recepient)
SyntaxError: invalid syntax
>>> message=code 'confirmed' '!' print(greeting)
SyntaxError: invalid syntax
>>> message=print code
SyntaxError: invalid syntax
>>> message=print(code)'confirmed' "!" "Hello,{} {}".format(first,last).\n
SyntaxError: invalid syntax
>>> message=print(code)'confirmed' "!" "Hello,{} {}".format(first,last)
SyntaxError: invalid syntax
>>> print(greeting)
hello,Tracy Baraza
>>> sms="{} confirmed! Hi {},\n you have sent Ksh{}\n to {}.".format(code,first,amount)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    sms="{} confirmed! Hi {},\n you have sent Ksh{}\n to {}.".format(code,first,amount)
IndexError: tuple index out of range
>>> print(sms)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(sms)
NameError: name 'sms' is not defined
>>> "{} confirmed! Hi {},\n you have sent Ksh{}\n to {}.".format(code,first,amount)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    "{} confirmed! Hi {},\n you have sent Ksh{}\n to {}.".format(code,first,amount)
IndexError: tuple index out of range
>>> sms="{} confirmed! Hi ,{}\n you have sent Ksh,{},\n to {}.".format(code,first,amount)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    sms="{} confirmed! Hi ,{}\n you have sent Ksh,{},\n to {}.".format(code,first,amount)
IndexError: tuple index out of range
>>> sms="{} confirmed! Hi ,{}\n you have sent Ksh,{},\n to {}".format(code,first,amount)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    sms="{} confirmed! Hi ,{}\n you have sent Ksh,{},\n to {}".format(code,first,amount)
IndexError: tuple index out of range
>>> sms="{} confirmed! Hi ,{}\n you have sent Ksh,{}\n to {}".format(code,first,amount)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    sms="{} confirmed! Hi ,{}\n you have sent Ksh,{}\n to {}".format(code,first,amount)
IndexError: tuple index out of range
>>> sms="{} confirmed! Hi ,{} \n you have sent Ksh,{} \n to {}".format(code,first,amount)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    sms="{} confirmed! Hi ,{} \n you have sent Ksh,{} \n to {}".format(code,first,amount)
IndexError: tuple index out of range
>>> sms="{} confirmed! Hi ,{} \n you have sent Ksh,{} \n to {}".format(code,first,amount)
