import pygame as pg
from pygame.locals import *

pg.init()
screen = pg.display.set_mode((1000,500))
pg.display.set_caption('Breakout')
clock = pg.time.Clock()
pg.key.set_repeat(50)

barra = pg.Surface((150,10))
barra.fill((255,255,255))
barra_pos = [450,470]

ball = pg.Surface((10,10))
ball.fill((255,255,255))
ball_pos = [200,200]

while True:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                barra_pos[0] -= 10 
            if event.key == K_RIGHT:
                barra_pos[0] += 10

    screen.fill((0,0,0))
    screen.blit(barra,barra_pos)
    screen.blit(ball,(200,200))
    pg.display.update()