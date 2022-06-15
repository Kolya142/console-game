import keyboard
import random
import level
import time
import os
max = 80 * 20
level.ran(max,2)
nam = 40
lp = ""
y = 0
n1 = nam
cols = 80
lines = 20
jump = 0
timesleep = 0.005
player = 'p'
fps = 0
namy = 0
bot = "b"
#leve = "p"
#for i in range(80 * 20): 
#	leve += "."
#level = open("level.g", 'w')
#level.write(leve)
#level.close()
os.system("mode con:cols=80 lines=23")

level = open("level.g")
level1 = []
level1 += level.read()
if not level1[0] == "p":
	print("not init player, error")
	os.system("pause >nul")
	exit()


def print_hi(place,entiti):

	global y
	global lp
	while place > y:
		y += 1
		lp += level1[y]
	lp += entiti
	y += 1


def main(nam):

	global lp
	global y
	y = 0
	lp = ""
	#time.sleep(timesleep)
	print_hi(nam,player)	
	print_hi(max,"")
	# print x, y
	if nam < 79:
		ox = nam
	else:
		we = int(nam / 80)
		qw = 1
		ox = nam - 80
		while qw < we:
			qw += 1
			ox -= 80
		if ox == -1:
			ox = 79
	qip = ('y:' + str(int((nam / 80) + 1)) + ', x:' + str(ox + 1) + ", fps: " + str(round(fps)) + "\nrelease:1.0")
	lp += qip
	os.system("cls")
	print(lp)
	# ............................................................
os.system("cls")
print("press any button")
os.system("pause >nul")
main(nam)
while 2>1:
	max = 80 * 20
	if keyboard.is_pressed('a') and not nam - 1 == -1 and not level1[nam] == "*":
		n1 = nam
		nam -= 1
		player = 'q'

	if keyboard.is_pressed('d') and not nam + 1 == max :
		if not level1[nam + 2] == "*":
			n1 = nam
			nam += 1
			player = 'p'
		
	if keyboard.is_pressed('w') and not nam - 80 < 0 and not level1[nam - 79] == "*":
		n1 = nam
		nam = nam - 80
	if keyboard.is_pressed('s') and not nam + 80 > max - 1 and not level1[nam + 81] == "*":
		n1 = nam
		nam = nam + 80

	x = range(79, 1841, 80)
	for x in x:
		if nam == x:
			if player == 'q':
				nam = n1

		if nam == x + 1:
			if player == 'p':
				nam = n1
	if keyboard.is_pressed('space'):
		if jump == 0:
			jump = 1
	if jump == 1:
		if not nam < cols * (lines - 6):
			nam -= cols
		else:
			jump = 2
	if jump == 2:
		if not nam > cols * (lines - 1):
			nam += cols
		else:
			jump = 0
	time1 = time.time()
	main(nam)
	fps = 1.0 / (time.time() - time1)