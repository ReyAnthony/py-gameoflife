import random
import os
import time

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
XMAX = 120
YMAX = 30

def initGrid():
	"""Initialize a random grid"""
	grid = []
	for i in range(YMAX):
		grid.append([])
		for j in range(XMAX):
			if random.randint(0,1) < 1:
				grid[i].append(True)
			else:
				grid[i].append(False)
	return grid

def initEmptyGrid():
	"""Initialize a new empty grid"""
	grid = []
	for i in range(YMAX):
		grid.append([])
		for j in range(XMAX):
				grid[i].append(False)
	return grid

def checkNeigh(grid, posx, posy):
	"""This function check the neighbors to a cell and returns the count"""
	count = 0

	XMAXloc = XMAX - 1
	YMAXloc = YMAX - 1

	#check NORTH
	if posy > 0 and (grid[posy - 1][posx] == True):
		count+=1
	#check SOUTH
	if posy < YMAXloc and (grid[posy + 1][posx] == True):
		count+=1
	#check WEST
	if posx > 0 and (grid[posy][posx-1] == True):
		count+=1
	#check EAST
	if posx < XMAXloc and (grid[posy][posx +1] == True):
		count+=1

	#check N-E
	if posy > 0 and posx < XMAXloc and (grid[posy - 1][posx +1] == True):
		count+=1
	#check N-W
	if posy > 0 and posx > 0 and (grid[posy - 1][posx -1] == True):
		count+=1
	#check S-E
	if posy < YMAXloc and posx < XMAXloc and (grid[posy +1][posx +1] == True):
		count+=1
	#check S-W
	if posy < YMAXloc and posx > 0 and (grid[posy +1][posx -1] == True):
		count+=1

	return count

def newGeneration(oldGen):
	newGen = initEmptyGrid()
	for i in range(YMAX):
		for j in range(XMAX):
			currentCell = oldGen[i][j]
			neighs = checkNeigh(oldGen, j, i)
			if currentCell == True:
				if neighs == 3 or neighs == 2:
					newGen[i][j] = True
			else:
				if neighs == 3:
					newGen[i][j] = True
	return newGen

def printGen(gen):
	for i in range(YMAX):
		for j in range(XMAX):
			currentCell = gen[i][j]
			if currentCell == True:
				print("░" , end="")
			else:
				print(" ", end="")
		print()

	time.sleep(0.1)
	clear()

def main():
	grid = initGrid()
	while True:
		printGen(grid)
		grid = newGeneration(grid)


if __name__ == "__main__":
    main()
