import pygame as pg
from pygame.locals import *

pg.init()
screen = pg.display.set_mode((1000,500))
pg.display.set_caption('Breakout')
clock = pg.time.Clock()
pg.key.set_repeat(50)

barra_pos = (450,470,150,10)
ball_pos = (400,450,10,10)

UP_R = 1
UP_L = 2 
UP = 3
DOWN = 4 
DOWN_R = 5
DOWN_L = 6
ball_direction = UP_L

while True:
    clock.tick(10)
    screen.fill((0,0,0))
    barra = pg.draw.rect(screen, (255,255,255), barra_pos)
    ball = pg.draw.rect(screen, (255,255,255), ball_pos)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                barra_pos = (barra_pos[0] - 10,470,150,10)
            if event.key == K_RIGHT:
                barra_pos = (barra_pos[0] + 10,470,150,10)

    if ball_direction == UP_R:
        ball_pos = (ball_pos[0] + 10, ball_pos[1] - 10,10,10)
    if ball_direction == UP_L:
        ball_pos = (ball_pos[0] - 10, ball_pos[1] - 10,10,10)
    if ball_direction == UP:
        ball_pos = (ball_pos[0], ball_pos[1] - 10,10,10)
    if ball_direction == DOWN_R:
        ball_pos = (ball_pos[0] + 10, ball_pos[1] + 10,10,10)
    if ball_direction == DOWN_L:
        ball_pos = (ball_pos[0] - 10, ball_pos[1] + 10,10,10)
    if ball_direction == DOWN:
        ball_pos = (ball_pos[0], ball_pos[1] + 10,10,10)
        
    if ball_pos[0] > 980 and ball_direction == UP_R:
        ball_direction = UP_L
    elif ball_pos[0] < 10 and ball_direction == UP_L:
        ball_direction = UP_R
    elif ball_pos[0] < 10 and ball_direction == DOWN_L:
        ball_direction = DOWN_R
    elif ball_pos[0] > 980 and ball_direction == DOWN_R:
        ball_direction = DOWN_L
    elif ball_pos[1] < 10 and ball_direction == UP_L:
        ball_direction = DOWN_L
    elif ball_pos[1] < 10 and ball_direction == UP_R:
        ball_direction = DOWN_R
    elif ball_pos[1] < 10 and ball_direction == UP:
        ball_direction = DOWN

    if pg.Rect.colliderect(ball,barra) and ball_direction == DOWN_L:
        ball_direction = UP_L
    if pg.Rect.colliderect(ball,barra) and ball_direction == DOWN_R:
        ball_direction = UP_R
        


    pg.display.update()