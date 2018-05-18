a = {}
print(a)
print(type(a))

b = {1:'nikhi',2.4:'abhi','hi':34,(11,22):'tuple key'}
print(b)
print(b.items())

#ASccessing value
print(b[2.4])
print(b)
b[2] = 'added new value'
print(b)

b.popitem()
b.popitem()
print(b)

# .clear() #empties the dictionary
# .get(keyvalue)
# .items() #returns key-value pairs in form of tuples
# .keys() #returns only keys in form of lists
# .values() #returns all values in form of lists

key = {1,2,3,4,4,3,2,1}
values = 'singlevalue'
dic = dict.fromkeys(key,values)
print(dic)

d = {a:a**3 for a in range(1,11)}
print(d)

# len()
# all()
# any()

#---values for diff keys diff values using fromkeys----