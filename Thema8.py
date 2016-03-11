import Array
DoYouEvenArrayBro = Array.DisIstEineArray
print ('This is the first table\n')
for x in range(8):
		print ('\n')
		for y in range(8):
			if DoYouEvenArrayBro[y][x] == 0:
				print ('X  '),
			else:
				print ('O  '),
print('\n')
print ('This are the rest rotations\n')
for k in range(3):
	for x in range(4):
		for y in range(4):
			a = DoYouEvenArrayBro[7-y][x]
			DoYouEvenArrayBro[7-y][x] = DoYouEvenArrayBro[x][y]
			b = DoYouEvenArrayBro[7-x][7-y]
			DoYouEvenArrayBro[7-x][7-y] = a
			c = DoYouEvenArrayBro[y][7-x]
			DoYouEvenArrayBro[y][7-x] = b
			DoYouEvenArrayBro[x][y] = c
	for x in range(8):
		print ('\n')
		for y in range(8):
			if DoYouEvenArrayBro[y][x] == 0:
				print ('X  '),
			else:
				print ('O  '),
	print('\n')
