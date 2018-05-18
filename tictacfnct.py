def CheckCondition(tt,gameover):
	#------Checking if game is won---------
	for i in range(3):
		#--------Condition for rows---------
		if str(tt[i][0]) == str(tt[i][1]) and str(tt[i][0]) == str(tt[i][2]):
			if tt[i][0] == '*':
				print('Player1 won the game')
				gameover = 1
				break
			else:
				print('Player2 won the game')
				gameover = 1
				break
		
		#-----------Condition for columns-------
		elif str(tt[0][i]) == str(tt[1][i]) and str(tt[0][i]) == str(tt[2][i]):
			if tt[0][i] == '*':
				print('Player1 won the game')
				gameover = 1
				break
			else:
				print('Player2 won the game')
				gameover = 1
				break

		#---------Condition for diagonal possibilities--------
		elif (str(tt[0][0]) == str(tt[1][1]) and str(tt[0][0]) == str(tt[2][2])) or (str(tt[2][0]) == str(tt[0][2]) and str(tt[2][0]) == str(tt[1][1])):
			if tt[1][1] == '*':
				print('Player1 won the game')
				gameover = 1
				break
			else:
				print('Player2 won the game')
				gameover = 1
				break
	return gameover

def fillpositions(tt,po,symb):
	for i in range(3):
		for j in range(3):
			if tt[i][j] == po:
				tt[i][j] = symb
			print(tt[i][j],end = ' ')
		print('\n')


tt = [[0 for i in range(3)] for j in range(3)]
l = [i for i in range(1,10)]
a = 0
print('Available Positions:')
for i in range(3):
	for j in range(3):
		tt[i][j] = a + 1
		a += 1
		print(tt[i][j],end = ' ')
	print('\n')

gameover = 0
while(gameover == 0):
	#-----Check for Condition--------
	gameover = CheckCondition(tt,gameover)
	if gameover == 1:
		break

	#-------Player1 turn---------
	po = int(input('Enter Player1 position: '))
	while(po not in l):
		po = int(input('Player1: Enter valid position: '))
	l.remove(po)
	fillpositions(tt,po,'*')

	#-----Check for Condition--------
	gameover = CheckCondition(tt,gameover)
	if gameover == 1:
		break

	#-------Player2 turn---------
	po = int(input('Enter Player2 position: '))
	while(po not in l):
		po = int(input('Player1: Enter valid position: '))
	l.remove(po)
	fillpositions(tt,po,'@')
