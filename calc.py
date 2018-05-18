def mainmenu():
	print('Which operation do you want to perform:\n1.Arithmetic\n2.Logical\n3.Relational\n4.Boolean\n5.Bitwise\n6.Assignment\n7.Special\n')

def arith():
	x = int(input('\nEnter\n1.Sum\n2.Difference\n3.Product\n4.Division\n5.Remainder\n6.Floor DIvision\n7.Exponent\n'))
	a = int(input('Enter value for a: '))
	b = int(input('Enter value for b: '))
	if x == 1:
		print('Sum: ',a+b)
	elif x == 2:
		print('Difference: ',a-b)
	elif x == 3:
		print('Product: ',a*b)
	elif x == 4:
		print('Division: ',a/b)
	elif x == 5:
		print('Remainder: ',a%b)
	elif x == 6:
		print('Floor Division: ',a//b)
	elif x == 7:
		print('Exponent: ',a**b)

def logical():
	x = int(input('\nEnter which to perform:\n1.AND\n2.OR\n3.NOT\n'))
	a = int(input('Enter value for a: '))
	b = int(input('Enter value for b: '))
	if x == 1:
		print('a AND b: ',a and b)
	elif x == 2:
		print('a OR b: ',a or b)
	elif x == 3:
		print('NOT b: ',not a)

def relational(a,b):
	x = int(input('Enter which action to perform:\n1."=="\n2."!="\n3.">"\n4."<"\n5.">="\n6."<="'))
	if x == 1:
		print('a == b: ',a==b)
	if x == 2:
		print('a != b: ',a!=b)
	if x == 3:
		print('a > b: ',a>b)
	if x == 4:
		print('a < b: ',a<b)
	if x == 5:
		print('a >= b: ',a>=b)
	if x == 6:
		print('a <= b: ',a<=b)

def assign():
	x = int(input('Enter which action to perform:\n1."+="\n2."-="\n3."*="\n4."/="\n'))
	a = int(input('Enter value for a: '))
	b = int(input('Enter value for b: '))
	if x == 1:
		a += b
		print('a += b: ',a)
	if x == 2:
		a -= b
		print('a -= b: ',a)
	if x == 3:
		a *= b
		print('a *= b: ',a)
	if x == 4:
		a /= b
		print('a /= b: ',a)

def bitwise(a,b):
	x = int(input('Enter which action to perform:\n1."&"\n2."|"\n3.">>"\n4."<<"\n'))
	print('a is ',a)
	print('b is ',b)
	if x == 1:
		print('Binary addition of ',a,' and ',b,': ',a&b)
	if x == 2:
		print('Binary sub of ',a,' and ',b,': ',a|b)
	if x == 3:
		print('Right shift ',a,' by 2: ',a>>2)
	if x == 4:
		print('Left shift ',b,' by 2: ',b<<2)	

mainmenu()
n = int(input('Enter an option: '))
if n == 1:
	print('Arithmetic Operators:')
	arith()
elif n == 2:
	print('Logical Operators:')
	logical()
elif n == 3:
	print('Relational Operators:')
	a = int(input('Enter value for a: '))
	b = int(input('Enter value for b: '))
	relational(a,b)
elif n == 5:
	print('Bitwise Operators:')
	bitwise(5,3)
elif n == 6:
	print('Assignment Operators:')
	assign()


# if n == 1:
# 	arith(2,3)
# x = 10
# if x in range(1,11):
# 	print('yes')