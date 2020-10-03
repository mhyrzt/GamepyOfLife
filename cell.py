from consts import *

class Cell:
    def __init__(self, pos, pg):
        self.live = False # False -> Dead , True -> Alive
        self.pos  = pos
        self.playGround = pg
        self.color      = COLOR_BLACK
        
    def setPos(self, pos):
        self.pos = pos
    
    def getPos(self):
        return self.pos

    def getLive(self):
        return self.live
    
    def toggleLive(self):
        self.live = not self.live
        self.color = [abs(x - 255) for x in self.color]
    
    def getColor(self):
        return self.color

    def rectData(self):
        data  = [x for x in self.pos]
        data += [self.playGround.getLen()]
        data += [self.playGround.getLen()]
        return data

    def printData(self):
        return [self.color, self.rectData()]
