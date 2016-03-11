print ('Please insert the date you want in this format DD/MM/YYYY')
while True:
	date = raw_input()
	day , month , year = date.split('/')
	day = int(day)
	month = int(month)
	year = int(year)
	if day > 0 and month > 0 and month < 13:
		if month % 2 == 1 and day < 32:
			break
		elif month == 2:
			if year % 4 == 0:
				if day < 30:
					break
			else:
				if day < 29:
					break
		else:
			if day < 31:
				break
	else:
		print ('Something went wrong, please give the date again')
a = (year % 100) / 12
b = abs((year % 100) - a * 12)
c = b / 4
if (year - (year % 100)) % 400 == 0:
	anchday = 2
elif (year - (year % 100)) % 400 == 100:
	anchday = 0
elif (year - (year % 100)) % 400 == 200:
	anchday = 5
else:
	anchday = 3
special = a + b + c + anchday
doomsday = special - (special / 7) * 7
r = doomsday
if month == 1:
	if year / 4 == 0:
		if day > 4:
			dif = day - 4
			for x in range(dif%7):
				r = r + 1
				if r == 7:
					r = 0
		elif day < 4:
			dif = 4 - day
			for x in range(dif%7):
				r = r - 1
				if r == -1:
					r = 6
	else:
		if day > 3:
			dif = day - 3
			for x in range(dif%7):
				r = r + 1
				if r == 7:
					r = 0
		elif day < 3:
			dif = 3 - day
			for x in range(dif%7):
				r = r - 1
				if r == -1:
					r = 6 
elif month == 2:
	if year / 4 == 0:
		if day < 29:
			dif = 29 - day
			for x in range(dif%7):
				r = r - 1
				if r == -1:
					r = 6
	else:
		if day < 28:
			dif = 28 - day
			for x in range(dif%7):
				r = r - 1
				if r == -1:
					r = 6
elif month == 3:
		if day > 7:
			dif = day - 7
			for x in range(dif%7):
				r = r + 1
				if r == 7:
					r = 0
		elif day < 7:
			dif = 7 - day
			for x in range(dif%7):
				r = r - 1
				if r == -1:
					r = 6
elif month == 4:
		if day > 4:
			dif = day - 4
			for x in range(dif%7):
				r = r + 1
				if r == 7:
					r = 0
		elif day < 4:
			dif = 4 - day
			for x in range(dif%7):
				r = r - 1
				if r == -1:
					r = 6
elif month == 5:
		if day > 9:
			dif = day - 9
			for x in range(dif%7):
				r = r + 1
				if r == 7:
					r = 0
		elif day < 9:
			dif = 9 - day
			for x in range(dif%7):
				r = r - 1
				if r == -1:
					r = 6
elif month == 6:
		if day > 6:
			dif = day - 6
			for x in range(dif%7):
				r = r + 1
				if r == 7:
					r = 0
		elif day < 6:
			dif = 6 - day
			for x in range(dif%7):
				r = r - 1
				if r == -1:
					r = 6
elif month == 7:
		if day > 11:
			dif = day - 11
			for x in range(dif%7):
				r = r + 1
				if r == 7:
					r = 0
		elif day < 11:
			dif = 11 - day
			for x in range(dif%7):
				r = r - 1
				if r == -1:
					r = 6
elif month == 8:
		if day > 8:
			dif = day - 8
			for x in range(dif%7):
				r = r + 1
				if r == 7:
					r = 0
		elif day < 8:
			dif = 8 - day
			for x in range(dif%7):
				r = r - 1
				if r == -1:
					r = 6
elif month == 9:
		if day > 5:
			dif = day - 5
			for x in range(dif%7):
				r = r + 1
				if r == 7:
					r = 0
		elif day < 5:
			dif = 5 - day
			for x in range(dif%7):
				r = r - 1
				if r == -1:
					r = 6
elif month == 10:
		if day > 10:
			dif = day - 10
			for x in range(dif%7):
				r = r + 1
				if r == 7:
					r = 0
		elif day < 10:
			dif = 10 - day
			for x in range(dif%7):
				r = r - 1
				if r == -1:
					r = 6
elif month == 11:
		if day > 7:
			dif = day - 7
			for x in range(dif%7):
				r = r + 1
				if r == 7:
					r = 0
		elif day < 7:
			dif = 7 - day
			for x in range(dif%7):
				r = r - 1
				if r == -1:
					r = 6
elif month == 12:
		if day > 12:
			dif = day - 12
			for x in range(dif%7):
				r = r + 1
				if r == 7:
					r = 0
		elif day < 12:
			dif = 12 - day
			for x in range(dif%7):
				r = r - 1
				if r == -1:
					r = 6
if r == 0:
	print ('Sunday')
elif r == 1:
	print ('Monday')
elif r == 2:
	print ('Tuesday')
elif r == 3:
	print ('Wednesday')
elif r == 4:
	print ('Thursday')
elif r == 5:
	print ('Friday')
else:
	print ('Saturday')
