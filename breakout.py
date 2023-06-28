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
ball_pos = (800,450)
UP_R = 1
UP_L = 2 
UP = 3
DOWN = 4 
DOWN_R = 5
DOWN_L = 6
ball_direction = UP_R

while True:
    clock.tick(10)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                barra_pos[0] -= 10 
            if event.key == K_RIGHT:
                barra_pos[0] += 10

    if ball_direction == UP_R:
        ball_pos = (ball_pos[0] + 10, ball_pos[1] - 10)
    if ball_direction == UP_L:
        ball_pos = (ball_pos[0] - 10, ball_pos[1] - 10)
    if ball_direction == UP:
        ball_pos = (ball_pos[0], ball_pos[1] - 10)
    if ball_direction == DOWN_R:
        ball_pos = (ball_pos[0] + 10, ball_pos[1] + 10)
    if ball_direction == DOWN_L:
        ball_pos = (ball_pos[0] - 10, ball_pos[1] + 10)
    if ball_direction == DOWN:
        ball_pos = (ball_pos[0], ball_pos[1] + 10)
        
    if ball_pos[0] > 1000 and ball_direction == UP_R:
        ball_direction == UP_L
        
    print(ball_pos)
    screen.fill((0,0,0))
    screen.blit(barra,barra_pos)
    screen.blit(ball,ball_pos)
    pg.display.update()