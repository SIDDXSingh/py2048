import random

n = int(input("Enter the size of the game_board n: "))
print(n)
w = int(input("Enter the number required for winning the game: "))
gb = [[0 for i in range(n)] for j in range(n)]


def game_board(a):
    for i in a:
        for j in i:
            print(j, end=" ")
        print("\n")


def winner(Game_Board, winnum):
    win = False


	for i in Game_Board:
		for j in i:
			if j == winnum
				print("Winner")
			win = True

	for i in Game_Board:
		for j in i:
			if j == 0
				win = False
	return win


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


def Movement(a, Move):
    if Move == "l":
        for i in range(len(a)):
            count = 0
            for j in range(len(a)):
                for k in range(1, len(a)):
                    if (a[i][k - 1] == 0):
                        temp = a[i][k]
                        a[i][k] = a[i][k - 1]
                        a[i][k - 1] = temp
                    if (a[i][k - 1] == a[i][k] and count < 1):
                        a[i][k - 1] = 2 * a[i][k - 1]
                        a[i][k] = 0
                        count = count + 1

    elif Move == "w":
        for k in range(len(a)):
            count = 0
            for j in range(len(a)):
                for i in range(1, len(a)):
                    if (a[i - 1][k] == 0):
                        temp = a[i][k]
                        a[i][k] = a[i - 1][k]
                        a[i - 1][k] = temp
                    if (a[i - 1][k] == a[i][k] and count <= 1):
                        a[i - 1][k] = 2 * a[i - 1][k]
                        a[i][k] = 0
                        count = count + 1
                    game_board(a)
                    print("\n \n")

    return a


'''def Movement(a,Move):
	if Move == "l":
		for i in range (len(a)):
			count=0
			for j in range(len(a)):
				for k in range(1,len(a)):
					if (a[i][k-1] == 0 ):
						temp=a[i][k]
						a[i][k]=a[i][k-1]
						a[i][k-1]=temp
		print(a,"modi \n")				
		for i in range (len(a)):
		  for k in range(len(a)-1):
		    if a[i][k]==a[i][k+1]:
		      a[i][k]=2*a[i][k]
		      a[i][k+1]=0
		  x2=a[i].count(0)

		      print (a)
		for i in range (len(a)):
			count=0
			for j in range(len(a)):
				for k in range(1,len(a)):
					if (a[i][k-1] == 0 ):
						temp=a[i][k]
						a[i][k]=a[i][k-1]
						a[i][k-1]=temp		      
	return a


print(Movement(gb,"l"))						        
'''