# #------Lists-------
# l = [1,2.56,'Nikhi',5+6j]
# print('Operations on a list\n')

# print('List: ',l)
# print('Adress of List: ',id(l))
# print('Type of list l: ',type(l))
# print('Accessing an element in the list: ',l[2])
# print('Type of element in list: ',type(l[2]))

# #------Slicing------
# print('\nSlicing: ',l[1:3])
# print('Reversing using backward indexing: ',l[::-1])

# # #------Deleting------
# # del l
# # print(l)
# del l[1]
# print('After deleting element: ',l)

# #-------Concat-------
# l1 = [1,2,3,4,5,-3,-4]
# l2 = ['Nikhi','Sindhu','Mek']
# print('\nList l: ',l)
# print('List l1: ',l1)
# print('List l2: ',l2)
# l += l1 +l2
# print('Concating lists: ',l)
# print('Length of l: ',len(l))

# #--------Repetion(Duplicating)-----
# dup = 2*l2
# print('\nDuplicatig list: ',dup)
# #---Membership---
# print('Membership of Sindhu in l: ','Sindhu' in l)
# print('Membership of Naren in l: ','Naren' in l)
# #---Iterations of lists---
# print('Printing list using loop:')
# for i in l:
# 	print(i)

# #============================================
# #------Inbuilt functions-------
# # a = ['Mek','Sudhir']
# # b = ['Sindhu','Sandeep']
# # c = ['abc',34]
# # print(cmp(a,b))
# #-----Min Max------
# print('\nMax val of list l1:',max(l1))
# print('Min val of list l2(Returns char with least ascii value for str lists): ',min(l2))

# #================Methods for lists========================
# #----Append------
# l.append('Chinki')
# print('\nAppending using append:\n',l) #Append appends elements at the end of the list
# #----Extend------
# l.extend(['Tom','Jerry']) #l.extend([list_name])
# print('\nAdding multiple elements using extend fnctn:\n',l)
# #-----Pop--------
# l.pop(12)
# print('\nRemove element at an index: pop(val):\n',l)
# print('\nPop removes element from the last: ',l.pop())
# print(l)
# #-------Index,Insert---------
# print('\nIndex of Nikhi in l: ',l.index('Nikhi'))
# l.insert(4,'Naren')
# print('\nInsert Naren at index 4:\n',l)
# l.remove('Naren')
# print('\nRemoved Naren from l using remove():\n',l)
# #-----Count-----
# print('\nCount: Counts the num of instances the element is in the list: ',l.count('Nikhi'))
# l.reverse()
# print('\nReverse the list using reverse():\n',l)
# #----Sort----
# l2.sort()
# print('\nSort: Sorts only lists with similar elements: ',l2)
# print('\nSorting using sorted(list_name) function: ',sorted(l1))

# #========================================================
# #------List Inside a List------
# a = [1,2,['niki','abhi'],3.34,1+2j]
# print('\nNested lists:',a)
# print('Index of element within child list: ',a[2].index('niki'))
# print('Access element within child list using .index(): ',a[2][1])

#--------List Comprehension--------
p = [i for i in range(0,11)]
print('Basic list comp example: ',p)

#----Taking values for list from user----
x = int(input('\nEnter num of values to enter: '))
q = []
print('Enter the numbers:\n')
for i in range(x):
	q.append(int(input()))
print(q)
