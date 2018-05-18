# #-----Tuples Examples ----------
# a = (1,2,3,4)
# b = 1.2,2.2,3.3,4.4
# c = 'niki','abhi'

# # '+' concats the two tuples
# f = a + b + c
# print('Final tuple: ',f)


# for i in range(len(f)):
# 	print(f[i])

# # If we have two instances of a tuple var it overweites the previous value
# a = 2*b
# print(a)

# #Slicing
# print(f[0:3])

# #Membership
# print('niki' in a)
# print('niki' in f)

# #----pattern in a string------
# c = ('nik','nikhi','nikki','nikhil','d43df')
# for i in c:
# 	if i.find('nik') == 0:
# 		print(i)

# #Iterate through tuple
# a = (a for a in range(0,11))
# print(a)

# for i in a:
# 	print(i)

# #----list within tuples-----
# x = (1,2,3,[5,6,7],45,'hello')
# print(x)
# x[3][1] = 'some'
# print(x[3])
# # x[3] = 'hello'
# print(x)
# x.pop()
# x.remove(3)

#------Tuple comprehension-------
# tup = (a for a in range(0,11))
# print(tup)

# print(next(tup))
# print(next(tup))

# for i in tup:
# 	print(i)

#-----_Enumerator-------
lst = [i for i in range(11)]

enum = enumerate(lst)
print(enum)

print(next(enum))
print(next(enum))
print(next(enum))
# for a in enum:
# 	print(a)