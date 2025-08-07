import copy
import time

class cell():
    def __init__(self, matrix):
        self.matrix = matrix

    def printmatrix(self, n):
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j] == 1:
                    print("◼︎", end=" ")
                else:
                    print("◻︎", end=" ")
            print()
        print()

    def checkNeighbor(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                nx = x + i
                ny = y + j
                if 0 <= nx < len(self.matrix) and 0 <= ny < len(self.matrix[nx]):
                    if self.matrix[nx][ny] == 1:
                        count += 1
        return count

    def generation(self):
        neighbors = 0
        replicate = copy.deepcopy(self.matrix)
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                neighbors = self.checkNeighbor(x, y)
                if self.matrix[x][y] == 1:
                    if neighbors > 3 or neighbors < 2:
                        replicate[x][y] = 0
                else:
                    if neighbors == 3:
                        replicate[x][y] = 1
        self.matrix = replicate

grid = []
for i in range(10):
    tmp = []
    for j in range(10):
        tmp.append(0)
    grid.append(tmp)

x = int(input('enter x '))
y = int(input('enter y '))
grid[x][y] = 1
while input('would you like to start ') != 'y':
    x = int(input('enter x '))
    y = int(input('enter y '))
    grid[x][y] = 1

print('\n\n\n\n')
c = cell(grid)
while True:
    c.printmatrix(10)
    c.generation()
    time.sleep(0.2)
