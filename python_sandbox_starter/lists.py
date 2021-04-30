# A List is a collection which is ordered and changeable. Allows duplicate members.

# create list
numbers = [1,2,3,4,5]
fruits = ['apple','oranges','grapes','pears']
# constructor
# numbers2=list((1,2,3,4,5))

print(fruits[1])

# get length
print(len(fruits))

# appemd to list
fruits.append('mangoes')

# remove from list
fruits.remove('grapes')

# insert into position 
fruits.insert(2,'strawberries')

# change value
fruits[0]='blueberries'

# remove from position
fruits.pop(2)

# sort list
fruits.sort()

# reverse sort
fruits.sort(reverse=True)

print(fruits)