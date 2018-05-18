# --------Basic Addition of two matrices-------
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
c= [[0,0],[0,0]]
for i in range(len(a)):
	for j in range(len(a[0])):
		c[i][j] = a[i][j]+b[i][j]
print(c)

# -------Taking values of nested lists from user--------
n = int(input('Enter no of row and column: '))
a = [[0 for i in range(n)] for j in range(n)] #to create a nested list of desired size
b = [[0 for i in range(n)] for j in range(n)]
c = [[0 for i in range(n)] for j in range(n)]
print('Enter the elements: ')
for i in range(n):
	for j in range(n):
		a[i][j] = int(input('Enter val for list a: '))
		b[i][j] = int(input('Enter val for list b: '))

for i in range(n):
	for j in range(n):
		c[i][j] = a[i][j] + b[i][j]
print('List a: ',a)
print('List b: ',b)
print('a + b:',c)


# -------Values from user method2 (Using While loop)--------
n = int(input('Enter no of rows and col: '))
a,b,rowa,rowb = [],[],[],[]
c = [[0 for i in range(n)] for j in range(n)]
j = 0
print('Enter values for a')
while(j < n):
	for i in range(n):
		rowa.append(int(input('Enter value for a: ')))
		rowb.append(int(input('Enter value for b: ')))
	a.append(rowa)
	b.append(rowb)
	rowa,rowb = [],[]
	j += 1
for i in range(n):
	for j in range(n):
		c[i][j] = a[i][j] + b[i][j]
print('a: ',a)
print('b: ',b)
print('a + b: ',c)

# -------Matrix Multiplication----------
n = int(input('Enter no of rows and col: '))
a,b,rowa,rowb = [],[],[],[]
c = [[0 for i in range(n)] for j in range(n)]
j = 0
print('Enter values for a')
while(j < n):
	for i in range(n):
		rowa.append(int(input('Enter value for a: ')))
		rowb.append(int(input('Enter value for b: ')))
	a.append(rowa)
	b.append(rowb)
	rowa,rowb = [],[]
	j += 1
for i in range(n):
	for j in range(n):
		c[i][j] = a[i][j] * b[j][i]
print('a: ',a)
print('b: ',b)
print('a * b: ',c)