# a = 'Digital'
# b = 'Lync'
# c = 'Hello'

# print(type(a))

# print(a+b)
# print(a*2)
# print(a,b)

# #Indexing
# print(a[2])


# #Slicing
# d=a+b
# print(d[0:11:1])
# print(d[0:11:2])
# print(d[-1::-1])

# #Stripping
# e = 20 * '-' + 'DigitalLync' + '-' *20
# print(e)
# print(e.strip('-'))
# print(e.lstrip('-'))
# print(e.rstrip('-'))

# print(min(e)) #prints the character in the string which has least ASCII value
# print(max(e)) #prints the character with largest ASCII value

# print('*' in e) #returns true if the character is present in the string, else false

#Formatting Strings

#---------Old Format---------
a = 'Iron Man'
b = 'Hulk'
print('%s and %s are a part of Avengers'%('Black Panther','Captain America'))

#---------New Format----------
a = 'Iron Man'
b = 'Hulk'
print('{} and {} are a part of Avengers'.format(a,b))

print('She scored {:.2f} in finals'.format(99.34567))