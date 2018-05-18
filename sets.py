a = {1,2,3,4}
print(a)
a.add(5)
print(a)
a.pop()
print(a)
a.pop()
print(a)
a.remove(3)
print(a)
a.discard(4)
print(a)
a.add(10)
a.add(1)
a.add(5)
print(a)

# .remove()
# .discard()
# .difference()
# .union()
# .intersection()
# .issubset()
# .issuperset()
# .add()
# .pop()
# .update([])
# .update({})
# Set comprehension 

b = {2,3,4,5}
print(b)
print('Sum: ',sum(b))
print('Min:',min(b))
print('Max:',max(b))
print('Len: ',len(b))
print('Any: ',any(b))
print('All:',all(b))

print(a|b)
print(a&b)
print(a-b)
print(b-a)

c = a&b
print(c)

d = {'nikhi',1,3,4.5,(10,11)}
print(d)
d.update([34,56,'abhi',('hi','hello')])
print(d)

for i in d:
	print(i)

e = frozenset(d)
print(type(e))
print(e)
f = set(e)
print(type(f))

lst = [1,2,3,4,5,2,3,78,'hello']
print('List: ',lst)
tple = tuple(lst)
print('tuple: ',tple)
s1 = set(lst)
print('Set: ',s1)
l1 = list(s1)
print(l1)