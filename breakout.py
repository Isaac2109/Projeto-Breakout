import pygame as pg, random
from pygame.locals import *

pg.init()
pg.font.init()
screen = pg.display.set_mode((1000,500))
pg.display.set_caption('Breakout')
clock = pg.time.Clock()
pg.key.set_repeat(25)
font_text = pg.font.SysFont('arial', 30)

text_ganhou = font_text.render("VOCÊ GANHOU", 1, (100,20,200))
text_perdeu = font_text.render("VOCÊ PERDEU", 1, (100,20,200))
text_reiniciar = font_text.render("PARA REINICIAR PRESSIONE ESPAÇO", 1, (100,20,200))

running = True
tela_restart = False
tela_win = False

cor_bloco = (250, 243, 30)
ball_y = random.randint(280,450)
ball_x = random.randint(10,980)
barra_pos = (450,470,150,10)
ball_pos = (ball_x,ball_y,10,10)
pontuação = 0

lista_rects = [(10, 40, 100,20),(115, 40, 40,20),(160, 40, 150,20),(315, 40, 100,20),(420, 40, 110,20),(535, 40, 90,20),(630, 40, 120,20),
(755, 40, 70,20),(830, 40, 160,20),(20, 65, 160,20),(185, 65, 80,20),(270, 65, 200,20),(475, 65, 130,20),(610, 65, 90,20),(705, 65, 190,20),
(900, 65, 80,20),(10, 90, 130,20),(145, 90, 80,20),(230, 90, 110,20),(345, 90, 100,20),(450, 90, 180,20),(635, 90, 90,20),(730, 90, 100,20),
(835, 90, 70,20),(910, 90, 80,20),(30, 115, 50,20),(85, 115, 70,20),(160, 115, 120,20),(285, 115, 180,20),(470, 115, 110,20),(585, 115, 60,20),(650, 115, 130,20),
(785, 115, 50,20),(840, 115, 130,20),(10, 140, 120,20),(135, 140, 80,20),(220, 140, 150,20),(375, 140, 50,20),(430, 140, 70,20),(505, 140, 180,20),
(690, 140, 50,20),(745, 140, 120,20),(870, 140, 120,20),(20, 165, 50,20),(75, 165, 80,20),(160, 165, 120,20),(285, 165, 180,20),(470, 165, 80,20),(555, 165, 50,20),
(610, 165, 150,20),(765, 165, 120,20),(890, 165, 90,20),(10, 190, 110,20),(125, 190, 70,20),(200, 190, 150,20),(355, 190, 50,20),(410, 190, 130,20),
(545, 190, 90,20),(640, 190, 180,20),(825, 190, 90,20),(920, 190, 70,20)]
UP_R = 1
UP_L = 2
DOWN_R = 5
DOWN_L = 6

directions = [UP_R,UP_L]
ball_direction = random.choice(directions)

while True:
    if running:
        if pontuação > 1000 and pontuação < 4000:
            clock.tick(25)
            cor_bloco = (250, 70, 5)
        elif pontuação > 4000:
            clock.tick(30)
            cor_bloco = (252, 3, 3)
        else:
            clock.tick(20)
        if pontuação == 6510:
            running = False
            tela_restart = False
            tela_win = True
        screen.fill((0,0,0))
        barra = pg.draw.rect(screen, (40,50,255), barra_pos)
        ball = pg.draw.rect(screen, (40,200,0), ball_pos)

        for i,block in enumerate(lista_rects):
            bloco = pg.draw.rect(screen,cor_bloco,block)
            if pg.Rect.collidepoint(bloco, ball_pos[0] + 10, ball_pos[1] - 5) and ball_direction == UP_R:
                pontuação += lista_rects[i][2]
                lista_rects[i] = (0,0,0,0)
                ball_direction = DOWN_R
                print(pontuação)
            if pg.Rect.collidepoint(bloco, ball_pos[0] + 10, ball_pos[1] - 5) and ball_direction == UP_L:
                pontuação += lista_rects[i][2]
                lista_rects[i] = (0,0,0,0)
                ball_direction = DOWN_L 
                print(pontuação)  
            if pg.Rect.collidepoint(bloco, ball_pos[0], ball_pos[1] - 5) and ball_direction == UP_R:
                pontuação += lista_rects[i][2]
                lista_rects[i] = (0,0,0,0)
                ball_direction = DOWN_R
                print(pontuação)
            if pg.Rect.collidepoint(bloco, ball_pos[0], ball_pos[1] - 5) and ball_direction == UP_L:
                pontuação += lista_rects[i][2]
                lista_rects[i] = (0,0,0,0)
                ball_direction = DOWN_L 
                print(pontuação) 
            if pg.Rect.collidepoint(bloco, ball_pos[0] , ball_pos[1] + 15) and ball_direction == DOWN_L:
                pontuação += lista_rects[i][2]
                lista_rects[i] = (0,0,0,0)
                ball_direction = UP_L
                print(pontuação)  
            if pg.Rect.collidepoint(bloco, ball_pos[0], ball_pos[1] + 15) and ball_direction == DOWN_R:
                pontuação += lista_rects[i][2]
                lista_rects[i] = (0,0,0,0)
                ball_direction = UP_R  
                print(pontuação)  
            if pg.Rect.collidepoint(bloco, ball_pos[0] + 10, ball_pos[1] + 15) and ball_direction == DOWN_L:
                pontuação += lista_rects[i][2]
                lista_rects[i] = (0,0,0,0)
                ball_direction = UP_L
                print(pontuação)  
            if pg.Rect.collidepoint(bloco, ball_pos[0] + 10, ball_pos[1] + 15) and ball_direction == DOWN_R:
                pontuação += lista_rects[i][2]
                lista_rects[i] = (0,0,0,0)
                ball_direction = UP_R  
                print(pontuação)  

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_LEFT and barra_pos[0] > 0:
                    barra_pos = (barra_pos[0] - 10,470,150,10)
                if event.key == K_RIGHT and barra_pos[0] < 850:
                    barra_pos = (barra_pos[0] + 10,470,150,10)

        if ball_direction == UP_R:
            ball_pos = (ball_pos[0] + 10, ball_pos[1] - 10,10,10)
        if ball_direction == UP_L:
            ball_pos = (ball_pos[0] - 10, ball_pos[1] - 10,10,10)
        if ball_direction == DOWN_R:
            ball_pos = (ball_pos[0] + 10, ball_pos[1] + 10,10,10)
        if ball_direction == DOWN_L:
            ball_pos = (ball_pos[0] - 10, ball_pos[1] + 10,10,10)

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

        if ball_pos[1] > 510:
            running = False
            tela_restart = True

        if pg.Rect.collidepoint(barra, ball_pos[0] + 10, ball_pos[1] + 15) and ball_direction == DOWN_R:
            ball_direction = UP_R
        if pg.Rect.collidepoint(barra, ball_pos[0], ball_pos[1] + 15) and ball_direction == DOWN_R:
            ball_direction = UP_R
        if pg.Rect.collidepoint(barra, ball_pos[0], ball_pos[1] + 15) and ball_direction == DOWN_L:
            ball_direction = UP_L
        if pg.Rect.collidepoint(barra, ball_pos[0] + 10, ball_pos[1] + 15) and ball_direction == DOWN_L:
            ball_direction = UP_L
        
        pg.display.update()

    if tela_restart:
        lista_rects = [(10, 40, 100,20),(115, 40, 40,20),(160, 40, 150,20),(315, 40, 100,20),(420, 40, 110,20),(535, 40, 90,20),(630, 40, 120,20),
(755, 40, 70,20),(830, 40, 160,20),(20, 65, 160,20),(185, 65, 80,20),(270, 65, 200,20),(475, 65, 130,20),(610, 65, 90,20),(705, 65, 190,20),
(900, 65, 80,20),(10, 90, 130,20),(145, 90, 80,20),(230, 90, 110,20),(345, 90, 100,20),(450, 90, 180,20),(635, 90, 90,20),(730, 90, 100,20),
(835, 90, 70,20),(910, 90, 80,20),(30, 115, 50,20),(85, 115, 70,20),(160, 115, 120,20),(285, 115, 180,20),(470, 115, 110,20),(585, 115, 60,20),(650, 115, 130,20),
(785, 115, 50,20),(840, 115, 130,20),(10, 140, 120,20),(135, 140, 80,20),(220, 140, 150,20),(375, 140, 50,20),(430, 140, 70,20),(505, 140, 180,20),
(690, 140, 50,20),(745, 140, 120,20),(870, 140, 120,20),(20, 165, 50,20),(75, 165, 80,20),(160, 165, 120,20),(285, 165, 180,20),(470, 165, 80,20),(555, 165, 50,20),
(610, 165, 150,20),(765, 165, 120,20),(890, 165, 90,20),(10, 190, 110,20),(125, 190, 70,20),(200, 190, 150,20),(355, 190, 50,20),(410, 190, 130,20),
(545, 190, 90,20),(640, 190, 180,20),(825, 190, 90,20),(920, 190, 70,20)]
        ball_y = random.randint(280,450)
        ball_x = random.randint(10,980)
        ball_pos = (ball_x,ball_y,10,10)
        ball = pg.draw.rect(screen, (40,200,0), ball_pos)
        ball_direction = random.choice(directions)
        pontuação = 0
        cor_bloco = (250, 243, 30)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    tela_restart = False
                    running = True
        
        screen.fill((0,0,0))
        screen.blit(text_perdeu,(380,180))
        screen.blit(text_reiniciar,(220,220))
        pg.display.update()

    if tela_win:
        lista_rects = [(10, 40, 100,20),(115, 40, 40,20),(160, 40, 150,20),(315, 40, 100,20),(420, 40, 110,20),(535, 40, 90,20),(630, 40, 120,20),
(755, 40, 70,20),(830, 40, 160,20),(20, 65, 160,20),(185, 65, 80,20),(270, 65, 200,20),(475, 65, 130,20),(610, 65, 90,20),(705, 65, 190,20),
(900, 65, 80,20),(10, 90, 130,20),(145, 90, 80,20),(230, 90, 110,20),(345, 90, 100,20),(450, 90, 180,20),(635, 90, 90,20),(730, 90, 100,20),
(835, 90, 70,20),(910, 90, 80,20),(30, 115, 50,20),(85, 115, 70,20),(160, 115, 120,20),(285, 115, 180,20),(470, 115, 110,20),(585, 115, 60,20),(650, 115, 130,20),
(785, 115, 50,20),(840, 115, 130,20),(10, 140, 120,20),(135, 140, 80,20),(220, 140, 150,20),(375, 140, 50,20),(430, 140, 70,20),(505, 140, 180,20),
(690, 140, 50,20),(745, 140, 120,20),(870, 140, 120,20),(20, 165, 50,20),(75, 165, 80,20),(160, 165, 120,20),(285, 165, 180,20),(470, 165, 80,20),(555, 165, 50,20),
(610, 165, 150,20),(765, 165, 120,20),(890, 165, 90,20),(10, 190, 110,20),(125, 190, 70,20),(200, 190, 150,20),(355, 190, 50,20),(410, 190, 130,20),
(545, 190, 90,20),(640, 190, 180,20),(825, 190, 90,20),(920, 190, 70,20)]
        ball_y = random.randint(280,450)
        ball_x = random.randint(10,980)
        ball_pos = (ball_x,ball_y,10,10)
        ball = pg.draw.rect(screen, (40,200,0), ball_pos)
        ball_direction = random.choice(directions)
        pontuação = 0
        cor_bloco = (250, 243, 30)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    tela_win = False
                    tela_restart = False
                    running = True
        
        screen.fill((0,0,0))
        screen.blit(text_ganhou,(380,180))
        screen.blit(text_reiniciar,(220,220))
        pg.display.update()