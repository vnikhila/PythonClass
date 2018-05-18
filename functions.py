def f1():
	'''Sample Function'''
	print('Fucntion Example')

f1()
print(f1.__doc__)

print(f1)
print(f1())
print(type(f1))
print(id(f1))

#---------Arguments in functions--------
#------Positional arguments------
def add(a,b):
	print(a+b)
	return a-b

print(add(2,3))
c = add(4,3)
print('Returns diff: ',c)

#------Default argumrnts------
def add(a=1,b=2):
	print(a+b)
	return a-b

print(add(7,5))
c = add()
print('returns diff with Default values: ',c)

#--------Variable Length argument------
#======Type1========
def greetings(*names):
	print('Welcome ',names,' to python class')

greetings('nikhi','abhi','chinki',2,3,4)
print()
def greetings1(*names):
	for name in names:
		print('Welcome ',name,' to python class')

greetings1('nikhi','abhi','chinki',2,3,4)

#--------Variable Length argument------
#======Type1========
def type2_var_arg(**details):
	# print(details)
	for key,val in details.items():
		print(key,' - ',val)
	print()
	for key in details:
		print(key,' - ',details[key])

type2_var_arg(ironman = 'india',blackpanther = 'wakanda',thor='china',antman='usa')

#------LAMBDA function-------
sqrt = lambda a:a**2
print(sqrt(4))

l = [a for a in range(1,21)]
print(l)

odd = list(map(lambda a:a%2 != 0,l))
print(odd)

even = list(filter(lambda a:a%2 == 0,l))
print(even)


#----List example for function------
def list_val_index(lst,val):
	for i in lst:
		if val in lst:
			return lst.index(val)
		# if i == val:
		# 	return lst.index(val)

l1 = [1,2,3,4,5,'hi']
print(list_val_index(l1,4))
