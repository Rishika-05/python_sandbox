# A module is basically a file containing a set of functions to include in your application. 
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# core modules
import datetime
from datetime import date
import time
from time import time
# today = date.today()
timestamp = time()
print(timestamp)

# pip module
from camelcase import CamelCase

c = CamelCase()
# print(c.hump('hello there world'))


# example of a custom module 

import validator 
from validator import validate_email

email = "test@test.from"
if validate_email(email):
    print('email is valid')
else:
    print('invalid')
    
    
import emoji
result = emoji.emojize('Python is :red_heart:')
print(result)
# 'Python is 👍'

# You can also reverse this:
result = emoji.demojize('Python is 👍')
print(result)
# 'Python is :thumbs_up:'