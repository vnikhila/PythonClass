n = int(input('Enter the number: '))
fact = 1
for i in range(1,n+1):
	fact *= i
print(fact)

#------using recursive function-------
def fact(f,n):
	f = f * n
	return f

n = int(input('Enter the number: '))
f = 1
for i in range(1,n+1):
	f = fact(f,i)
print(f)