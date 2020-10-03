from cell import Cell
from consts import *
from random import randint

class PlayGround:
    def __init__(self, size):
        self.size   = size
        self.len    = RECT_LEN
        self.cells  = [[Cell([x, y], self) for y in range(0, size[0], self.len)] for x in range(0 ,size[1], self.len)]
        self.setCells()
    
    def nextGen(self):
        newGen = self.cells.copy()
        
        x = self.size[0]
        y = self.size[1]
        
        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                aliveNeighbors = 0
                for r in range(-1, 2):
                    for c in range(-1, 2):
                        Nx = i + r
                        Ny = j + c
                        if Nx < 0 or Nx >= len(self.cells) or Ny < 0 or Ny >= len(self.cells[0]):
                            pass
                        else:
                            aliveNeighbors += int(self.cells[Nx][Ny].getLive())
                            
                aliveNeighbors -= int(self.cells[i][j].getLive())
                
                kill = self.cells[i][j].getLive() and (aliveNeighbors < 2 or aliveNeighbors > 3)
                born = not self.cells[i][j].getLive() and aliveNeighbors == 3
                if kill or born:
                    newGen[i][j].toggleLive()
        
        self.cells = newGen

    def setCells(self):
        for i in range(0, len(self.cells)):
            for j in range(0, len(self.cells[0])):
                SHAPE = SHAPES[randint(1, 100) % SHAPE_COUNT]
                Xshape = len(SHAPE)
                Yshape = len(SHAPE[0])
                if randint(1, 200) % CONST_SET == 0:
                    if Xshape + i < len(self.cells) and Yshape + j < len(self.cells[0]):
                        for x in range(0, Xshape):
                            for y in range(0, Yshape):
                                if SHAPE[x][y]:
                                    try:
                                        self.cells[x + i][y + j].toggleLive()
                                    except:
                                        print(x + i, y + j)
    
    def getCells(self):
        return self.cells
    
    def getLen(self):
        return self.len