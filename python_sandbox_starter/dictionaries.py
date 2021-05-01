# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# create dict
person = {
    'first_name': 'Rish',
    'last_name': 'Raj',
    'age':18
}

# constructor 
# person2 = dict(first_name='Rish',last_name='Raj')


# get value
print(person['first_name'])
print(person.get('last_name'))

# add key/value
person['phone']='555-555-5555'

# get dict keys
print(person.keys())

# get dict items
print(person.items())

# copy dict
person2 = person.copy()
person2['city']='delhi'

# remove item
del(person['age'])
person.pop('phone')

# clear
person.clear()

# get length
print(len(person2))

# list of dict
people = [
    {'name':'martha','age':30},
    {'name':'kevin','age':25}
]

print(people[1]['name'])

