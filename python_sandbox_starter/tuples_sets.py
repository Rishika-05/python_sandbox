# A Tuple is a collection which is ordered and 'unchangeable'. Allows duplicate members.
''' 
# create tuple 
fruits = ('apples','oranges','grapes')

#constructor 
# fruits2 = tuple(('apples','oranges','grapes'))

# single value needs trailing comma 
fruits2 = ('apples',)

# get value
print(fruits[1])

# can't change value
# fruits[0] = 'pears'

# delete tuple 
del fruits2

# get length 
print(len(fruits))


'''
# A Set is a collection which is unordered and unindexed. No duplicate members.

# create set
fru_set = {'apples','oranges','mangoe'}
fru_set2 = set({'apples','oranges','mangoe'})


# check if in set 
print('apples' in fru_set)

# add to set 
fru_set.add('grapes')

# remove from set
fru_set.remove('grapes')

# clear set
fru_set.clear()

# delete 
del fru_set

print(fru_set)

