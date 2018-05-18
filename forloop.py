#loops
# #FOR LOOP Examples
# increments the value of a, starting from 0 to 11 and prints the 
# value of a each time

print('Example of for loop')
for a in range(0,11): #range(11) works the same
	print(a)

print('\nFor loop Example- single line')
for a in range(0,11):
 	print(a,end = '')

print('\nPrinting even numbers')
for a in range (1,100):
    if a%2==0:
    	print(a)

print('\nWhen range is given is range(val1,val2,val3) format: the var is incremented by val3')
for a in range(0,100,10):
 	print(a)

print('\nPrinting each letter in a string:')
for letter in 'NIKHI':
	print(letter)

print('\nPrinting elements in string array:')
friends = ['Nikhi','Mek','Sindhu','Chinki','Teja']
for frnd in friends:
	print(frnd)

print('\nPrinting elements in string using index value of array:')
for index in range(len(friends)):
	if index%2==0:
		print('Even index :',friends[index])
	else:
		print('Odd index :',friends[index])

#----------------------------------------------------------------
#Printing a table
num = int(input('Enter an integer\n'))
for a in range(1,11):
	print(num,'  * ',a,' = ',num*a)

#------------------------------------
#printing characters in a pattern
num = int(input('Enter a number\n'))
for a in range(1,num+1):
	for b in range(1,a+1):
		print('*',end = ' ')
	print('\n')

#------------------------------------
#printing row number
#num = int(input('Enter a number\n'))
for a in range(1,num+1):
	for b in range(1,a+1):
		print(a,end = ' ')
	print('\n')


#---------Printing charater in inverted order---------
#num = int(input('Enter the number\n'))
print('Stars in reverse order\n')
for i in range(num,0,-1):
	for j in range(1,i+1):
		print('*',end=' ')
	print('\n')
