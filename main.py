import keyboard
import random
import level
import time
import os
max = 80 * 20
nam = 40
lp = ""
ui = ""
y = 0
n1 = nam
cols = 80
lines = 20
jump = 0
timesleep = 0.015
player = 'p'
fps = 0
collision = True
namy = 0
bot = "b"

os.system("mode con:cols=80 lines=23")

level.ran(max,5)
levelf = open("level.g2")
level1 = []
level1 += levelf.read()



def print_hi(place,object1):

	global y
	global lp
	while place > y:
		y += 1
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
	qi = ('y:' + str(int((nam / 80) + 1)) + ', x:' + str(ox + 1) + ", fps: " + str(round(fps)) + "\nrelease:1.3")
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
	if keyboard.is_pressed('esc'):

		menu = True
		while menu:
			os.system("cls")
			print("menu:")
			print("cancel(0)")
			print("collision(1): " + str(collision))
			print("exit(2)")
			if keyboard.is_pressed("0"): menu = False
			if keyboard.is_pressed("1"):
				if collision:
					collision = False
				else:
					collision = True
				menu = False
			elif keyboard.is_pressed("2"):
				exit()
	if collision:
		if keyboard.is_pressed('a') and not level1[nam] == "*":
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
		for x in range(79, 1841, 80):
			if nam == x:
				if player == 'q':
					nam = n1

			if nam == x + 1:
				if player == 'p':
					nam = n1
	else:
		if keyboard.is_pressed('a') and not nam + 80 > max - 1:
			n1 = nam
			nam -= 1
			player = 'q'
		if keyboard.is_pressed('d') and not nam + 1 == max:
			n1 = nam
			nam += 1
			player = 'p'
		if keyboard.is_pressed('w') and not nam - 80 < 0:
			n1 = nam
			nam = nam - 80
		if keyboard.is_pressed('s') and not nam + 80 > max - 1:
			n1 = nam
			nam = nam + 80


	main(nam)
	fps = 1.0 / (time.time() - time1)