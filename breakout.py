import pygame as pg
from pygame.locals import *

pg.init()
screen = pg.display.set_mode((1000,500))
pg.display.set_caption('Dino')

barra = pg.Surface((150,10))
barra.fill((255,255,255))
barra_pos_x = 450


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            rodando = False
            pg.quit()
            quit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                barra_pos_x = barra_pos_x - 10
            if event.key == K_RIGHT:
                barra_pos_x = barra_pos_x + 10
              

    screen.blit(barra,(barra_pos_x, 470))

    pg.display.update()