import random
TreasureMap = [[0 for x in range(10)] for x in range(10)]
TreasureMap [4][3] = 1
TreasureMap [2][7] = 2
random.shuffle (TreasureMap)
TrX = 0
TrY = 0
PlX = 0
PlY = 0
print ('Your player is the circle that can be found in the map \n''and you need to find the treasure which is hidden inside one of the many Xs\n')
for y in range(10):
	for x in range(10):
		if TreasureMap[y][x] == 2:
			TrX = x
			TrY = y
		elif TreasureMap[y][x] == 1:
			PlX = x
			PlY = y

while True:
	for y in range(10):
		for x in range(10):
			if TreasureMap[y][x] == 0 or TreasureMap[y][x] == 2:
				print ('X  '),
			else:
				print ('O  '),
			if x==9:
				print '\n'
	DistanceX = abs(TrX-PlX)
	DistanceY = abs(TrY-PlY)
	Distance = DistanceX + DistanceY
	if Distance == 0:
		break
	MoveBarrierX = 0
	MoveBarrierY = 0
	print ('You need %d moves to get to the treasure from your current position'%(Distance))
	if PlX == 9:
		MoveBarrierX = 1
		print ('You cannot move to the right\n')
	elif PlX == 0:
		MoveBarrierX = 2
		print ('You cannot move to the left\n')
	if PlY == 9:
		MoveBarrierY = 1
		print ('You cannot move down\n')
	elif PlY ==0:
		MoveBarrierY = 2
		print ('You cannot move up\n')
	print ('Where do you want to move?\n')
	if MoveBarrierX == 0:
		if MoveBarrierY == 0:
			print ('Insert U/u(up) or D/d(down) or R/r(right) or L/l(left)\n')
			while True:
				move = raw_input()
				if move == 'U' or move == 'u' or move == 'D' or move == 'd' or move == 'R' or move == 'r' or move == 'L' or move == 'l':
					break
				else:
					print ('Wrong input, try again\n')
					print ('Insert U/u(up) or D/d(down) or R/r(right) or L/l(left)\n')
		elif MoveBarrierY == 1:
			print ('Insert U/u(up) or R/r(right) or L/l(left)\n')
			while True:
				move = raw_input()
				if move == 'U' or move == 'u' or move == 'R' or move == 'r' or move == 'L' or move == 'l':
					break
				else:
					print ('Wrong input, try again\n')
					print ('Insert U/u(up) or R/r(right) or L/l(left)\n')
		else:
			print ('Insert D/d(down) or R/r(right) or L/l(left)\n')
			while True:
				move = raw_input()
				if move == 'D' or move == 'd' or move == 'R' or move == 'r' or move == 'L' or move == 'l':
					break
				else:
					print ('Wrong input, try again\n')
					print ('Insert D/d(down) or R/r(right) or L/l(left)\n')
	if MoveBarrierX == 1:
		if MoveBarrierY == 0:
			print ('Insert U/u(up) or D/d(down) or L/l(left)\n')
			while True:
				move = raw_input()
				if move == 'U' or move == 'u' or move == 'D' or move == 'd' or move == 'L' or move == 'l':
					break
				else:
					print ('Wrong input, try again\n')
					print ('Insert U/u(up) or D/d(down) or L/l(left)\n')
		elif MoveBarrierY == 1:
			print ('Insert U/u(up) or L/l(left)\n')
			while True:
				move = raw_input()
				if move == 'U' or move == 'u' or move == 'L' or move == 'l':
					break
				else:
					print ('Wrong input, try again\n')
					print ('Insert U/u(up) or L/l(left)\n')
		else:
			print ('Insert D/d(down) or L/l(left)\n')
			while True:
				move = raw_input()
				if move == 'D' or move == 'd' or move == 'L' or move == 'l':
					break
				else:
					print ('Wrong input, try again\n')
					print ('Insert D/d(down) or L/l(left)\n')
	if MoveBarrierX == 2:
		if MoveBarrierY == 0:
			print ('Insert U/u(up) or D/d(down) or R/r(right)\n')
			while True:
				move = raw_input()
				if move == 'U' or move == 'u' or move == 'D' or move == 'd' or move == 'R' or move == 'r':
					break
				else:
					print ('Wrong input, try again\n')
					print ('Insert U/u(up) or D/d(down) or R/r(right)\n')
		elif MoveBarrierY == 1:
			print ('Insert U/u(up) or R/r(right)\n')
			while True:
				move = raw_input()
				if move == 'U' or move == 'u' or move == 'R' or move == 'r':
					break
				else:
					print ('Wrong input, try again\n')
					print ('Insert U/u(up) or R/r(right)\n')
		else:
			print ('Insert D/d(down) or R/r(right)\n')
			while True:
				move = raw_input()
				if move == 'D' or move == 'd' or move == 'R' or move == 'r':
					break
				else:
					print ('Wrong input, try again\n')
					print ('Insert D/d(down) or R/r(right)\n')
	if move == 'u' or move == 'U':
		helper = PlY - 1
		TreasureMap[helper][PlX] = TreasureMap[PlY][PlX]
		TreasureMap[PlY][PlX] = 0
		PlY = helper
	elif move == 'd' or move == 'D':
		helper = PlY + 1
		TreasureMap[helper][PlX] = TreasureMap[PlY][PlX]
		TreasureMap[PlY][PlX] = 0
		PlY = helper
	elif move == 'l' or move == 'L':
		helper = PlX - 1
		TreasureMap[PlY][helper] = TreasureMap[PlY][PlX]
		TreasureMap[PlY][PlX] = 0
		PlX = helper
	elif move == 'r' or move == 'R':
		helper = PlX + 1
		TreasureMap[PlY][helper] = TreasureMap[PlY][PlX]
		TreasureMap[PlY][PlX] = 0
		PlX = helper 
