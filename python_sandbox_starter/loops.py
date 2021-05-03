# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# range
for x in range(1,6):
    print(x," ")

people = ['a','b','c','d']

# for person in people:
#     print(f'current person: {person}')
    
# break
for person in people:
    if(person=='c'):
 #    break
        continue
    print(f'current person: {person}')

# While loops execute a set of statements as long as a condition is true.
count = 0
while count<=10 :
  print(count)
  count = count +1