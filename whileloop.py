# #While Loop examples
# a=0
# while a<=10:
# 	print(a)
# 	a+=1

# #----------Searches character in a string----------
# name = input('Enter a name\n')
# char = input('Enter character to search\n')
# for i in name:
# 	print(i)
# 	if i == char:
# 		print('Found the character\n')
# 		print('Index of the character:',name.index(char)) #index of a char in string
# 		break #stops the loop iteretion when char is found

# #----------Fibonacci Series---------------
# a = 0
# b = 1
# limit = int(input('Enter the limit\n'))
# print('Fibonacci Series:\n')
# while a <= limit:
# 	print(a,end = '  ')
# 	c = a + b
# 	a = b
# 	b = c
# print('\n')

#--------Printing alternatives at every 3 and 5 multiple---------
string = input('Enter the string\n')
a = int(input('Enter the index number where to slice the string\n'))
for i in range(1,101):
	if i % 3 == 0 and i % 5 == 0:
		print(string)
	elif i % 3 == 0:
		print(string[0:a])
	elif i % 5 == 0:
		print(string[a:])
	else:
		print(i)
