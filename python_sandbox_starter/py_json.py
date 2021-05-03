# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# sample json
userJSON = '{"fname":"Rish","lname":"Raj","age":40}'

# parse to dict
user = json.loads(userJSON)

print(user)
print(user['fname'])

car = {'make':'ford','model':'mustang','year':1730}

carJSON = json.dumps(car)

print (carJSON) 