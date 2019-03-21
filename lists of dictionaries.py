Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> student1={"name":"Natasha","age":20}
>>> student2={"name":"Joy","age":20}
>>> student3={"name":"peshy","age":19}
>>> student4={"name":"Tracy","age":19}
>>> student5={"name":"Lucy","age":19}
>>> students=[student1,student2,student3,student4,student5]
>>> students
[{'name': 'Natasha', 'age': 20}, {'name': 'Joy', 'age': 20}, {'name': 'peshy', 'age': 19}, {'name': 'Tracy', 'age': 19}, {'name': 'Lucy', 'age': 19}]
>>> for student in students:
	print(student["name"])

	
Natasha
Joy
peshy
Tracy
Lucy
>>> for student in students:
	print(student["2019-["age"]]
		      
SyntaxError: invalid syntax
>>> for student in students:
	print(student["2019-"age"]
		      
SyntaxError: invalid syntax
>>> for student in students:
	print(student["2019-"age"])
		      
SyntaxError: invalid syntax
>>> for student in students:
	print(student["2019-"age"])
		      
SyntaxError: invalid syntax
>>> print(2019-student["age"])
		      
2000
>>> for student in students:
	print(2019-student["age"])

		      
1999
1999
2000
2000
2000
>>> customer1={"name":"Chesang","balance":1000}
		      
>>> custome2={"name":"Charity","balance":2000}
		      
>>> custome3={"name":"Lucian","balance":4800}
		      
>>> custome4={"name":"Asher","balance":3600}
		      
>>> customers=[customer1,customer2,customer3,customer4,customer5,]
		      
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    customers=[customer1,customer2,customer3,customer4,customer5,]
NameError: name 'customer2' is not defined
>>> customer1={"name":"Chesang","balance":1000}
		      
>>> customer2={"name":"Charity","balance":1000}
		      
>>> customer3={"name":"Luciana","balance":1000}
		      
>>> customer4={"name":"Asher","balance":1000}
		      
>>> customer5={"name":"Asher","balance":5000}
		      
>>> customers=[customer1,customer2,customer3,customer4,customer5,]
		      
>>> customers
		      
[{'name': 'Chesang', 'balance': 1000}, {'name': 'Charity', 'balance': 1000}, {'name': 'Luciana', 'balance': 1000}, {'name': 'Asher', 'balance': 1000}, {'name': 'Asher', 'balance': 5000}]
>>> for customer in customers:
		      print("Hello {} your current balance is {}")

		      
Hello {} your current balance is {}
Hello {} your current balance is {}
Hello {} your current balance is {}
Hello {} your current balance is {}
Hello {} your current balance is {}
>>> for customer in customers:
		      print("Hello {"name"} your current balance is {"balance}")
		      
SyntaxError: invalid syntax
>>> for customer in customers:
		      print("Hello {} your current balance is {}.format")

		      
Hello {} your current balance is {}.format
Hello {} your current balance is {}.format
Hello {} your current balance is {}.format
Hello {} your current balance is {}.format
Hello {} your current balance is {}.format
>>> for customer in customers:
		      print("Hello {} your current balance is {}.format(name,balance)
			    
SyntaxError: EOL while scanning string literal
>>> for customer in customers:
			    messege=("Hello {} your current balance is {}".format('name','balance')
				     print(messege)
				     
SyntaxError: invalid syntax
>>> for customer in customers:
		message=("Hello {} your current balance is {}".format('name','balance')
			 print(message)
			 
SyntaxError: invalid syntax
>>> for customer in customers:
		message="Hello {} your current balance is {}".format(customer["name",customer["balance"])
								     
SyntaxError: invalid syntax
>>> for customer in customers:
		message="Hello {}, your current balance is {}".format(customer["name",customer["balance"])
								      
SyntaxError: invalid syntax
>>> print(messafor customer in customers:
		message="Hello {}, your current balance is {}".format(customer["name"],customer["balance"])
	  
SyntaxError: invalid syntax
>>> for customer in customers:
		message="Hello {}, your current balance is {}".format(customer["name"],customer["balance"])
	  print(message)
	  
SyntaxError: unindent does not match any outer indentation level
>>> for customer in customers:
		message="Hello {}, your current balance is {}".format(customer["name"],customer["balance"])
		print(message)

	  
Hello Chesang, your current balance is 1000
Hello Charity, your current balance is 1000
Hello Luciana, your current balance is 1000
Hello Asher, your current balance is 1000
Hello Asher, your current balance is 5000
>>> for customer in customers:
	  print(customer["balance"]/2.6)

	  
384.6153846153846
384.6153846153846
384.6153846153846
384.6153846153846
1923.076923076923
>>> for customer in customers:
		message="Hello {}, your current balance is {} and you qualify for a loan of customer["balance"]/2.6.format(customer["name"],customer["balance"])
	  
SyntaxError: invalid syntax
>>> for customer in customers:
		message="Hello {}, your current balance is {} and you qualify for a loan of customer["balance"]/2.6.format(customer["name"],customer["balance"])
	  
SyntaxError: invalid syntax
>>> for customer in customers:
		message="Hello {}, your current balance is {}.\n and you qualify for a loan of {}.format(customer["name"],customer["balance"],customer["balance"]/2.6)
	  
SyntaxError: invalid syntax
>>> for customer in customers:
		message="Hello {}, your current balance is {}.\n and you qualify for a loan of {}".format(customer["name"],customer["balance"],customer["balance"]/2.6)
		print(message)

	  
Hello Chesang, your current balance is 1000.
 and you qualify for a loan of 384.6153846153846
Hello Charity, your current balance is 1000.
 and you qualify for a loan of 384.6153846153846
Hello Luciana, your current balance is 1000.
 and you qualify for a loan of 384.6153846153846
Hello Asher, your current balance is 1000.
 and you qualify for a loan of 384.6153846153846
Hello Asher, your current balance is 5000.
 and you qualify for a loan of 1923.076923076923
>>> 
