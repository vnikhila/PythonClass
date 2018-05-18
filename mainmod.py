'''Main Module document'''

print('Module sucessfully imported')

def findindex(l,val):
	ind = 0
	a=1
	for i in range(len(l)):
		if val == l[i]:
			ind = i
			print('Occurance ',a,': ',i)
			a+=1

	if ind == 0:
		return 'Value not available'