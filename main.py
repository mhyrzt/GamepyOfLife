import pygame
from playground import PlayGround
from consts import *

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

pg = PlayGround(SCREEN_SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    for row in pg.getCells():
        for cell in row:
            data  = cell.printData()
            color = data[0]
            rect  = data[1]
            pygame.draw.rect(screen, color, rect)
    pg.nextGen()
    pygame.display.update()
    pygame.time.delay(DELAY)
                