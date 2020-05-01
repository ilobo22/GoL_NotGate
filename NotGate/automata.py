from random import randint
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mplc


class Cell:

    def __init__(self):
        self.status = 'Dead'

    def setDead(self):
        self.status = 'Dead'

    def setAlive(self):
        self.status = 'Alive'

    def isAlive(self):

        if self.status == 'Alive':
            return True

        return False

    def get_print_char(self):

        if self.isAlive():
            return '0'

        return '.'


class Board:
    def __init__(self, rows, columns, lists):
        self.rows = rows
        self.columns = columns

        self.grid = [[Cell() for colc in range(self.columns)]
                     for rowc in range(self.rows)]

        if len(lists) != 0:
            self.dead()
            for cell in lists:
                self.grid[cell[0]][cell[1]].setAlive()
        else:
            self.generate()

    def dead(self):
        for row in self.grid:
            for col in row:

                col.setDead()

    def printBoard(self):
        # print('\n'*10)
        for row in self.grid:
            for col in row:
                print(col.get_print_char(), end='')
            print()

    def generate(self):
        for row in self.grid:
            for col in row:

                num = randint(0, 2)
                if num == 1:
                    col.setAlive()

    def update(self):
        alive = []
        dead = []

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):

                checkNeighbor = self.checkNeighbor(row, col)

                livingNeighbor = []

                for neighbors in checkNeighbor:

                    if neighbors.isAlive():
                        livingNeighbor.append(neighbors)

                tempObject = self.grid[row][col]
                tempStat = tempObject.isAlive()

                if tempStat == True:
                    if len(livingNeighbor) < 2 or len(livingNeighbor) > 3:
                        dead.append(tempObject)
                    if len(livingNeighbor) == 3 or len(livingNeighbor) == 2:
                        alive.append(tempObject)
                else:
                    if len(livingNeighbor) == 3:
                        alive.append(tempObject)

        for cell in alive:
            cell.setAlive()

        for cell in dead:
            cell.setDead()

    def checkNeighbor(self, theRow, theColumn):
        min = -1
        max = 2

        neighsList = []

        for row in range(min, max):
            for col in range(min, max):

                neighRow = row + theRow
                neighCol = col + theColumn

                valNeigh = True

                if (neighRow) == theRow and (neighCol) == theColumn:
                    valNeigh = False

                if (neighRow) < 0 or (neighRow) >= self.rows:
                    valNeigh = False

                if (neighCol) < 0 or (neighCol) >= self.columns:
                    valNeigh = False

                if valNeigh:
                    neighsList.append(
                        self.grid[neighRow][neighCol])

        return neighsList


def main():

    ggg = [ 
            # input stream using a gosper glider gun
            (53-33,101+0), (54-33,101+0), (53-33,102+0), (54-33,102+0), (51-33,112+0), (52-33,112+0), (56-33,112+0), (57-33,112+0), (52-33,114+0), (56-33,114+0), (53-33,115+0),(54-33,115+0),(55-33,115+0), (53-33,116+0),(54-33,116+0),(55-33,116+0), (56-33,119+0), (55-33,120+0),(56-33,120+0),(57-33,120+0),(54-33,121+0),(58-33,121+0),(56-33,122+0),(53-33,123+0),(59-33,123+0),(53-33,124+0),(59-33,124+0),(54-33,125+0),(58-33,125+0),(55-33,126+0),(56-33,126+0),(57-33,126+0), (55-33,136+0),(56-33,136+0),(55-33,135+0),(56-33,135+0),

            # not gate using a gosper glider gun
            (5+0, 1+0), (5+0, 2+0), (6+0, 1+0), (6+0, 2+0), (5+0, 11+0), (6+0, 11+0), (7+0, 11+0), (4+0, 12+0), (3+0, 13+0), (3+0,14+0), (8+0, 12+0), (9+0, 13+0), (9+0, 14+0), (6+0, 15+0), (4+0, 16+0), (5+0, 17+0), (6+0, 17+0), (7+0, 17+0),
            (6+0, 18+0), (8+0, 16+0), (3+0, 21+0), (4+0, 21+0), (5+0, 21+0), (3+0, 22+0), (4+0, 22+0), (5+0, 22+0), (2+0, 23+0), (6+0, 23+0), (1+0, 25+0), (2+0, 25+0), (6+0, 25+0), (7+0, 25+0), (3+0, 35+0), (4+0, 35+0), (3+0, 36+0), (4+0, 36+0)
           ]
    
    board = Board(150, 150, ggg)

    A = np.arange(22500).reshape(150, 150)

    rows = 0

    for row in board.grid:

        cells = 0
        for cell in row:

            if(cell.isAlive()):
                A[rows][cells] = 255
            else:
                A[rows][cells] = 0

            cells += 1

        rows += 1

    fig, ax = plt.subplots()

    img = ax.imshow(A, interpolation='nearest')

    img1 = []

    for i in range(3000):
        board.update()

        rows = 0

        for row in board.grid:

            cells = 0
            for cell in row:

                if(cell.isAlive()):
                    A[rows][cells] = 255
                else:
                    A[rows][cells] = 0

                cells += 1

            rows += 1

        img1.append([plt.imshow(A, cmap='OrRd')])

    ani = animation.ArtistAnimation(
        fig, img1, interval=5, blit=True, repeat_delay=0)

    plt.show()


main()
