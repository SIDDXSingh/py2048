import random
from os import system, name

# import sleep to show output for some time period
from time import sleep


# define our clear function
def clear():
	# for windows
	if name == 'nt':
		_ = system('cls')

	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')



def getchar():
    if name=='nt':
        import msvcrt
        ch = msvcrt.getch().decode('ASCII')
    elif name=='posix':
        import tty, termios, sys
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch





n = int(input("Enter the size of the game_board n: "))
print(n)
w = int(input("Enter the number required for winning the game: "))
gb = [[0 for i in range(n)] for j in range(n)]
clear()


def game_board(a):
    for i in a:
        for j in i:
            print(j, end="\t")
        print("\n")



def rand_generator(x):
    x1, x2 = [], []
    for i in range(len(x)):
        for j in range(len(x)):
            if (x[i][j] == 0):
                x1 = x1 + [i]
                x2 = x2 + [j]
    x3 = list(zip(x1, x2))
    n1 = random.randint(0, len(x3) - 1)
    a = x3[n1][0]
    b = x3[n1][1]
    x[a][b] = 2
    return x

def left(a):
	for i in range (len(a)):
		count = 0
		for j in range(len(a)):
			for k in range(1, len(a)):
				if (a[i][k-1] == 0 ):
					temp = a[i][k]
					a[i][k] = a[i][k-1]
					a[i][k-1] = temp
	for i in range (len(a)):
		for k in range(len(a)-1):
			if a[i][k] == a[i][k+1]:
				a[i][k] = 2*a[i][k]
				a[i][k+1] = 0
				x2 = a[i].count(0)
	for i in range(len(a)):
		count=0
		for j in range(len(a)):
			for k in range(1, len(a)):
				if (a[i][k-1] == 0 ):
					temp=a[i][k]
					a[i][k]=a[i][k-1]
					a[i][k-1]=temp
	return a

def right(a):
	for i in range (len(a)):
		count=0
		for j in reversed(range(len(a))):
			for k in reversed((range(0,len(a)-1))):
				if (a[i][k+1] == 0 ):
					temp=a[i][k]
					a[i][k]=a[i][k+1]
					a[i][k+1]=temp
	for i in range (len(a)):
		for k in reversed(range(1, len(a))):
			if a[i][k]==a[i][k-1]:
				a[i][k]=2*a[i][k]
				a[i][k-1]=0
				x2=a[i].count(0)
	for i in range (len(a)):
		count=0
		for j in reversed(range(len(a))):
			for k in reversed(range(0,len(a)-1)):
				if (a[i][k+1] == 0 ):
					temp=a[i][k]
					a[i][k]=a[i][k+1]
					a[i][k+1]=temp
	return a

def up(a):
	for k in range (len(a)):
		count = 0
		for j in range( len(a) ):
			for i in range(1,len(a)):
				if (a[i-1][k] == 0 ):
					temp = a[i][k]
					a[i][k] = a[i-1][k]
					a[i-1][k] = temp
	for k in range (len(a)):
		for i in range(len(a)-1):
			if a[i][k] == a[i+1][k]:
				a[i][k] = 2*a[i][k]
				a[i+1][k] = 0
				x2 = a[i].count(0)
	for i in range(len(a)):
		count=0
		for k in range(len(a)):
			for i in range(1, len(a)):
				if (a[i-1][k] == 0 ):
					temp=a[i][k]
					a[i][k]=a[i-1][k]
					a[i-1][k]=temp
	return a

def down(a):
	for k in range (len(a)):
		count=0
		for j in reversed(range(len(a))):
			for i in reversed((range(0,len(a)-1))):
				if (a[i+1][k] == 0 ):
					temp=a[i][k]
					a[i][k]=a[i+1][k]
					a[i+1][k]=temp
	for k in range (len(a)):
		for i in reversed(range(1, len(a))):
			if a[i][k]==a[i-1][k]:
				a[i][k]=2*a[i][k]
				a[i-1][k]=0
				x2=a[i].count(0)
	for k in range (len(a)):
		count=0
		for j in reversed(range(len(a))):
			for i in reversed(range(0,len(a)-1)):
				if (a[i+1][k] == 0 ):
					temp=a[i][k]
					a[i][k]=a[i+1][k]
					a[i+1][k]=temp
	return a

def winner(gb, win):
	return any(win in sublist for sublist in gb)

def lose(gb):
	return any(0 in sublist for sublist in gb)



while lose(gb):
	gb=rand_generator(gb)
	game_board(gb)
	if winner(gb,w):
		print("You Win!!")
		break;
	elif lose(gb)==False:
		print("Sorry You Lose!!")
	m=getchar()
	if (m=="a"):
		gb=left(gb)
	elif (m=="d"):
		gb=right(gb)
	elif (m=="w"):
		gb=up(gb)
	elif (m=="s"):
		gb=down(gb)
	else:
		print("Invalid Move...Try Again")
	clear()







