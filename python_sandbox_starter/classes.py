# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# create class 
class user:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.age = age
        self.email = email
        
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age+=1
        
# extend class
class customer(user):
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.age = age
        self.email = email
        self.balance = 0
        
    def set_balance(self,balance):
        self.balance = balance
             
    def greeting(self):
         return f'My name is {self.name} and I am {self.age} and balance is {self.balance}'  


# init user object
brad = user('Rish','abc@gmail.com',18)

# init customer object
janel= customer('janed','asdfg@yyv.com',22)
janel.set_balance(500)
print(janel.greeting())

brad.has_birthday()
print(brad.greeting())

