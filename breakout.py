import pygame as pg
from pygame.locals import *

pg.init()
screen = pg.display.set_mode((1000,500))
pg.display.set_caption('Breakout')
clock = pg.time.Clock()
pg.key.set_repeat(50)

barra_pos = (450,470,150,10)
ball_pos = (500,400,10,10)


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

    # primeira fileira de blocos

    bloco1 = pg.draw.rect(screen, (255,255,255), (10, 40, 100,20))
    bloco2 = pg.draw.rect(screen, (255,255,255), (115, 40, 40,20))
    bloco3 = pg.draw.rect(screen, (255,255,255), (160, 40, 150,20))
    bloco4 = pg.draw.rect(screen, (255,255,255), (315, 40, 100,20))
    bloco5 = pg.draw.rect(screen, (255,255,255), (420, 40, 110,20))
    bloco6 = pg.draw.rect(screen, (255,255,255), (535, 40, 90,20))
    bloco7 = pg.draw.rect(screen, (255,255,255), (630, 40, 120,20))
    bloco8 = pg.draw.rect(screen, (255,255,255), (755, 40, 70,20))
    bloco9 = pg.draw.rect(screen, (255,255,255), (830, 40, 160,20))
    # segunda fileira de blocos
    bloco10 = pg.draw.rect(screen, (255,255,255), (20, 65, 160,20))
    bloco11 = pg.draw.rect(screen, (255,255,255), (185, 65, 80,20))
    bloco12 = pg.draw.rect(screen, (255,255,255), (270, 65, 200,20))
    bloco13 = pg.draw.rect(screen, (255,255,255), (475, 65, 130,20))
    bloco14 = pg.draw.rect(screen, (255,255,255), (610, 65, 90,20))
    bloco15 = pg.draw.rect(screen, (255,255,255), (705, 65, 190,20))
    bloco16 = pg.draw.rect(screen, (255,255,255), (900, 65, 80,20))
    # terceira fileira de blocos
    bloco17 = pg.draw.rect(screen, (255,255,255), (10, 90, 130,20))
    bloco18 = pg.draw.rect(screen, (255,255,255), (145, 90, 80,20))
    bloco19 = pg.draw.rect(screen, (255,255,255), (230, 90, 110,20))
    bloco20 = pg.draw.rect(screen, (255,255,255), (345, 90, 100,20))
    bloco21 = pg.draw.rect(screen, (255,255,255), (450, 90, 180,20))
    bloco22 = pg.draw.rect(screen, (255,255,255), (635, 90, 90,20))
    bloco23 = pg.draw.rect(screen, (255,255,255), (730, 90, 100,20))
    bloco24 = pg.draw.rect(screen, (255,255,255), (835, 90, 70,20))
    bloco25 = pg.draw.rect(screen, (255,255,255), (910, 90, 80,20))
    # quarta fileira de blocos
    bloco26 = pg.draw.rect(screen, (255,255,255), (30, 115, 50,20))
    bloco27 = pg.draw.rect(screen, (255,255,255), (85, 115, 70,20))
    bloco28 = pg.draw.rect(screen, (255,255,255), (160, 115, 120,20))
    bloco29 = pg.draw.rect(screen, (255,255,255), (285, 115, 180,20))
    bloco30 = pg.draw.rect(screen, (255,255,255), (470, 115, 110,20))
    bloco31 = pg.draw.rect(screen, (255,255,255), (585, 115, 60,20))
    bloco32 = pg.draw.rect(screen, (255,255,255), (650, 115, 130,20))
    bloco33 = pg.draw.rect(screen, (255,255,255), (785, 115, 50,20))
    bloco34 = pg.draw.rect(screen, (255,255,255), (840, 115, 130,20))
    # quinta fileira de blocos
    bloco35 = pg.draw.rect(screen, (255,255,255), (10, 140, 120,20))
    bloco36 = pg.draw.rect(screen, (255,255,255), (135, 140, 80,20))
    bloco37 = pg.draw.rect(screen, (255,255,255), (220, 140, 150,20))
    bloco38 = pg.draw.rect(screen, (255,255,255), (375, 140, 50,20))
    bloco39 = pg.draw.rect(screen, (255,255,255), (430, 140, 70,20))
    bloco40 = pg.draw.rect(screen, (255,255,255), (505, 140, 180,20))
    bloco41 = pg.draw.rect(screen, (255,255,255), (690, 140, 50,20))
    bloco42 = pg.draw.rect(screen, (255,255,255), (745, 140, 120,20))
    bloco43 = pg.draw.rect(screen, (255,255,255), (870, 140, 120,20))
    # sexta fileira de blocos
    bloco44 = pg.draw.rect(screen, (255,255,255), (20, 165, 50,20))
    bloco46 = pg.draw.rect(screen, (255,255,255), (75, 165, 80,20))
    bloco47 = pg.draw.rect(screen, (255,255,255), (160, 165, 120,20))
    bloco48 = pg.draw.rect(screen, (255,255,255), (285, 165, 180,20))
    bloco49 = pg.draw.rect(screen, (255,255,255), (470, 165, 80,20))
    bloco50 = pg.draw.rect(screen, (255,255,255), (555, 165, 50,20))
    bloco51 = pg.draw.rect(screen, (255,255,255), (610, 165, 150,20))
    bloco52 = pg.draw.rect(screen, (255,255,255), (765, 165, 120,20))
    bloco53 = pg.draw.rect(screen, (255,255,255), (890, 165, 90,20))
    # setima fileira de blocos
    bloco54 = pg.draw.rect(screen, (255,255,255), (10, 190, 110,20))
    bloco55 = pg.draw.rect(screen, (255,255,255), (125, 190, 70,20))
    bloco56 = pg.draw.rect(screen, (255,255,255), (200, 190, 150,20))
    bloco57 = pg.draw.rect(screen, (255,255,255), (355, 190, 50,20))
    bloco58 = pg.draw.rect(screen, (255,255,255), (410, 190, 130,20))
    bloco59 = pg.draw.rect(screen, (255,255,255), (545, 190, 90,20))
    bloco60 = pg.draw.rect(screen, (255,255,255), (640, 190, 180,20))
    bloco61 = pg.draw.rect(screen, (255,255,255), (825, 190, 90,20))
    bloco62 = pg.draw.rect(screen, (255,255,255), (920, 190, 70,20))

    lista = [bloco1,bloco2,bloco3,bloco4,bloco5,bloco6,bloco7,bloco8,bloco9,bloco10,
            bloco11,bloco12,bloco13,bloco14,bloco15,bloco16,bloco17,bloco18,bloco19,
            bloco20,bloco21,bloco22,bloco23,bloco24,bloco25,bloco27,bloco28,bloco28,bloco29,
            bloco30,bloco31,bloco32,bloco33,bloco34,bloco35,bloco36,bloco37,bloco38,bloco39,
            bloco40,bloco41,bloco42,bloco43,bloco44,bloco46,bloco47,bloco48,bloco49,
            bloco50,bloco51,bloco52,bloco53,bloco54,bloco55,bloco56,bloco57,bloco58,bloco59,
            bloco60,bloco61,bloco62]

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

    if pg.Rect.collidepoint(barra, ball_pos[0], ball_pos[1] + 10) and ball_direction == DOWN_R:
        ball_direction = UP_R
    if pg.Rect.collidepoint(barra, ball_pos[0], ball_pos[1] + 10) and ball_direction == DOWN_L:
        ball_direction = UP_L

    for block in lista:
        if pg.Rect.collidepoint(block, ball_pos[0], ball_pos[1]):
            print(block)
            block = 0
            print(block)
            
        


    pg.display.update()