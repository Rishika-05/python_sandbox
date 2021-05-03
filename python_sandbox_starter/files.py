# Python has functions for creating, reading, updating, and deleting files.

# open file
myFile = open('myFile.txt','w')

# get some info 
print('name : ',myFile.name)
print('isClosed : ',myFile.closed)
print('opening mode : ',myFile.mode)

# write to file 
myFile.write('I love Python ')
myFile.write('and javaScript.')
myFile.close()

# append to file
myFile = open('myFile.txt','a')
myFile.write('I also like PHP')
myFile.close()

# read from a file 
myFile = open('myFile.txt','r+')
text = myFile.read(100)
print(text)