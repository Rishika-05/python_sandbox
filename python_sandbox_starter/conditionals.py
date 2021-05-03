# If/ Else conditions are used to decide to do something based on something being true or false

# if x>y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{y} is greater than {x}')
x=5
y=9
if x>y:
    print(y)
elif x<y:
    print(x)
else:
    print('equal')
# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values



# Logical operators (and, or, not) - Used to combine conditional statements




# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
num =[1,2,3,4,5]
n=2
if x in num:
    print(x in num)



# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
a=2
b=2
if a is b:
    print(a is b)