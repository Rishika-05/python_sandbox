# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# create function
def sayHello(name='sam'):
    print(f'Hello {name}')

sayHello()

# return value
def getSum(x,y):
  total = x+y
  return total

num=getSum(3,4)
print(num)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum1 = lambda x,y : x+y 

print(getSum1(10,3))