tt = [[0 for i in range(3)] for j in range(3)]
a = 0
print('Available Positions:')
for i in range(3):
	for j in range(3):
		# tt[i][j] = str(i) + str(j)
		tt[i][j] = a + 1
		a += 1
		print(tt[i][j],end = ' ')
	print('\n')

gameover = 0

while(gameover == 0):
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

	#-----Gameover condition------
	if gameover == 1:
		break

	# -----------------Player1 turn-------------
	p1 = int(input('Enter Player1 position: '))
	for i in range(3):
		for j in range(3):
			if tt[i][j] == p1:
				tt[i][j] = '*'
			print(tt[i][j],end = ' ')
		print('\n')


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

	#-----Gameover condition------
	if gameover == 1:
		break
#------------Player2 turn--------------
	p2 = int(input('Enter Player2 position: '))
	for i in range(3):
		for j in range(3):
			if tt[i][j] == p2:
				tt[i][j] = '@'
			print(tt[i][j],end = ' ')
		print('\n')
