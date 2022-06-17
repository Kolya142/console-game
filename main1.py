import keyboard
import random
import time
import os

nam = -1
lp = ""
ui = ""
y = 0
cols = 80
lines = 20
max = cols * lines
jump = 0
timesleep = 0.015
player = 'p'
fps = 0
collision = True
namy = 0
bot = "b"
jumpbost = 5

os.system("mode con:cols=80 lines=23")

levelf = open("level.g2")
level1 = []
level1 += levelf.read()
nam = 0
while True:
	nam += 1
	if level1[nam] == "p":
		level1[nam] = "."
		break
n1 = nam
for i in range(cols * (lines - 1) + 1, max + 1, 1): level1[i] = "*"

def print_hi(place,object1):

	global y
	global lp
	while place > y:
		y += 1
		if y > max: 
			break
		lp += level1[y]
	lp += object1
	y += 1


def main(nam):

	global lp
	global ui
	global y
	y = 0
	lp = ""
	time.sleep(timesleep)
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
	qi = ('y:' + str(int((nam / 80) + 1)) + ', x:' + str(ox + 1) + ", fps: " + str(round(fps)) + "\ndebug:1.5")
	os.system("cls")
	print(lp)
	print(qi)
	# ............................................................
os.system("cls")
print("press any button")
os.system("pause >nul")
main(nam)
while 2>1:
	time1 = time.time()
	max = 80 * 20
	if not nam > cols * (lines - 1) and jump == 0:
		if not level1[nam + cols + 1] == "*": nam += cols
	if not nam > max:
		if keyboard.is_pressed('a') and not level1[nam] == "*" and not jump == 2:
			n1 = nam
			nam -= 1
			player = 'q'

		if keyboard.is_pressed('d') and not nam + 1 == max and not jump == 2:
			if not level1[nam + 2] == "*":
				n1 = nam
				nam += 1
				player = 'p'
		if keyboard.is_pressed('space'):
			if jump == 0:
				n2 = nam
				jump = 1
	if jump == 1:
		if not nam < (n2 - (cols * jumpbost)) and not level1[nam - cols + 1] == "*":
			nam -= cols
		else:
			jump = 2
	if jump == 2:
		if nam + cols > max - cols:
			n2 -= cols
			jump = 1
		if not nam == n2 and not nam + cols > max and not level1[nam + 81] == "*":
			nam += cols
		else:
			jump = 0



	main(nam)
	fps = 1.0 / (time.time() - time1)
