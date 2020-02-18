import pygame, sys
import random
from pygame.locals import *
import os
import time

pygame.init()
pygame.mixer.init()
width = 2000
height = 1000
# window set up
infoObject = pygame.display.Info()
DISPLAYSURF = pygame.display.set_mode((infoObject.current_w-100, infoObject.current_h-50))
pygame.display.set_caption('River crossing')
#font
font = pygame.font.Font('freesansbold.ttf', 32)
t0= time.time()
t1= time.time()
t2= time.time()
dt1=0
dt2=0
FPS = 60
fpsClock = pygame.time.Clock()
# color
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,150,255)
yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)
brown = (160,82,45)
boat1Img = pygame.image.load('slow1.png')
boat1x = 10
boat1y = 75
direction1 = 'right'
stone1Img = pygame.image.load('stone.png')
stone1y = random.randrange(40,130)
stone1x = random.randrange(10,1760)
# stonedir1 = 'right'
# line 2
boat2Img = pygame.image.load('fast1.png')
boat2x = 160
boat2y = 260
direction2 = 'right'
# line 3
boat3Img = pygame.image.load('boat12.png')
boat3x = 1780
boat3y = 455
direction3 = 'left'
stone2Img = pygame.image.load('stone.png')
stone2y = random.randrange(430,550)
stone2x = random.randrange(10,1760)
# stonedir2 = 'right'
# line 4
boat4Img = pygame.image.load('slow11.png')
boat4x = 1380
boat4y = 660
direction4 = 'left'
# line 5
boat5Img = pygame.image.load('smol.png')
boat5x = 880
boat5y = 860
direction5 = 'left'
stone3Img = pygame.image.load('stone.png')
stone3y = random.randrange(820,940)
stone3x = random.randrange(10,1760)
# stonedir3 = 'right'
# player
playerImg = pygame.image.load('human1.png')
playerx = 700
playery = height - 10
xchange = 0
ychange = 0
score1 = 0
score2 = 0
flag = 1
jadd1 = 30
jadd2 = 30
level1=0
level2=0
count=0
# game loop ig idk
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(blue)
    pygame.draw.line(DISPLAYSURF,  brown, (0,0), (2000, 0), 50)
    pygame.draw.line(DISPLAYSURF,  brown, (0,200), (2000, 200), 50)
    pygame.draw.line(DISPLAYSURF,  brown, (0,400), (2000, 400), 50)
    pygame.draw.line(DISPLAYSURF,  brown, (0,600), (2000, 600), 50)
    pygame.draw.line(DISPLAYSURF,  brown, (0,800), (2000, 800), 50)
    pygame.draw.line(DISPLAYSURF,  brown, (0,1000), (2000, 1000), 50)
    t1 = time.time()
    dt = t1-t0
    textx = font.render('TIME: ' + str(dt),True, black , yellow)
    textrectx = textx.get_rect()
    textrectx.center = (899,30)
    DISPLAYSURF.blit(textx, textrectx)
# line 1
    if direction1 == 'right':
        if flag==1:
            boat1x += 1 + level1
        if flag==2:
            boat1x += 1 + level2
        if boat1x >= 1780:
            direction1 = 'left'
    elif direction1 == 'left':
        if flag==1:
            boat1x -= (1 + level1)
        if flag==2:
            boat1x -= (1 + level2)
        if boat1x <= 3:
            direction1 = 'right'
    #
    DISPLAYSURF.blit(stone1Img, (stone1x, stone1y))

# line 2
    DISPLAYSURF.blit(boat1Img, (boat1x, boat1y))
    if direction2 == 'right':
        if flag==1:
            boat2x += 1.5 + level1
        if flag==2:
            boat2x += 1.5 + level2
        if boat2x >= 1780:
            direction2 = 'left'
    elif direction2 == 'left':
        if flag==1:
            boat2x -= (1.5 + level1)
        if flag==2:
            boat2x -= (1.5 + level2)

        if boat2x <= 3:
            direction2 = 'right'
# line 3

    DISPLAYSURF.blit(boat2Img, (boat2x, boat2y))
    if direction3 == 'right':
        if flag==1:
            boat3x += 3.5 + level1
        if flag==2:
            boat3x += 3.5 + level2
        if boat3x >= 1780:
            direction3 = 'left'
    elif direction3 == 'left':
        if flag==1:
            boat3x -= (3.5 + level1)
        if flag==2:
            boat3x -= (3.5 + level2)

        if boat3x <= 7:
            direction3 = 'right'
    DISPLAYSURF.blit(stone2Img, (stone2x, stone2y))

# line 4
    DISPLAYSURF.blit(boat3Img, (boat3x, boat3y))
    if direction4 == 'right':
        if flag==1:
            boat4x += 1.75 + level1
        if flag==2:
            boat4x += 1.75 + level2
        if boat4x >= 1780:
            direction4 = 'left'
    elif direction4 == 'left':
        if flag==1:
            boat4x -= (1.75 + level1)
        if flag==2:
            boat4x -= (1.75 + level2)
        if boat4x <= 5:
            direction4 = 'right'
# line 5
    DISPLAYSURF.blit(boat4Img, (boat4x, boat4y))
    if direction5 == 'right':
        if flag==1:
            boat5x += 2 + level1
        if flag==2:
            boat5x += 2 + level2
        if boat5x >= 1780:
            direction5 = 'left'
    elif direction5 == 'left':
        if flag==1:
            boat5x -= (2 + level1)
        if flag==2:
            boat5x -= (2 + level2)
        if boat5x <= 4:
            direction5 = 'right'

    DISPLAYSURF.blit(boat5Img, (boat5x, boat5y))

    DISPLAYSURF.blit(stone3Img, (stone3x, stone3y))
    # player moves
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xchange = -50
            elif event.key == pygame.K_RIGHT:
                xchange = 50
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xchange = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ychange = -20
            elif event.key == pygame.K_DOWN:
                ychange = 20
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ychange = 0
        playerx += xchange
        playery += ychange
        if playerx>=2000:
            playerx = 2000
        if playerx <= 10:
            playerx = 10
        if playery >= 1000:
            playery = 1000
        if playery <= 10:
            playery = 10
    DISPLAYSURF.blit(playerImg, (playerx, playery))
# collisions
    if flag==1:
        t1 = time.time()
        dt1 = t1-t0
        textx = font.render('TIME: ' + str(dt1),True, black , yellow)
        textrectx = textx.get_rect()
        textrectx.center = (899,30)
        DISPLAYSURF.blit(textx, textrectx)

        if playerx >= boat1x-70 and playerx <= boat1x+70:
            if playery >= (boat1y-30) and playery <= (boat1y+140):
                flag = 3
        if playerx >= boat2x-70 and playerx <= boat2x+70:
            if playery >= (boat2y-30) and playery <= (boat2y+50):
                flag = 3
        if playerx >= boat3x-70 and playerx <= boat3x+70:
            if playery >= (boat3y-30) and playery <= (boat3y+40):
                flag = 3
        if playerx >= boat4x-70 and playerx <= boat4x+70:
            if playery >= (boat4y-30) and playery <= (boat4y+100):
                flag = 3
        if playerx >= boat5x-70 and playerx <= boat5x+70:
            if playery >= (boat5y-30) and playery <= (boat5y+40):
                flag = 3
        if playerx >= stone1x-10 and playerx <= stone1x+10:
            if playery >= (stone1y-30) and playery <= (stone1y+40):
                flag = 3
        if playerx >= stone2x-10 and playerx <= stone2x+10:
            if playery >= (stone2y-30) and playery <= (stone2y+40):
                flag = 3
        if playerx >= stone3x-10 and playerx <= stone3x+10:
            if playery >= (stone3y-30) and playery <= (stone3y+40):
                flag = 3

    if flag==2:
        t2 = time.time()
        dt2 = t2-t0-dt1
        textx = font.render('TIME: ' + str(dt2),True, black , yellow)
        textrectx = textx.get_rect()
        textrectx.center = (899,30)
        DISPLAYSURF.blit(textx, textrectx)

        if playerx >= boat1x-70 and playerx <= boat1x+70:
            if playery >= (boat1y-30) and playery <= (boat1y+140):
                count = count + 1
                flag = 4
        if playerx >= boat2x-70 and playerx <= boat2x+70:
            if playery >= (boat2y-30) and playery <= (boat2y+50):
                count = count + 1
                flag = 4
        if playerx >= boat3x-70 and playerx <= boat3x+70:
            if playery >= (boat3y-30) and playery <= (boat3y+100):
                count = count + 1
                flag = 4
        if playerx >= boat4x-70 and playerx <= boat4x+70:
            if playery >= (boat4y-30) and playery <= (boat4y+100):
                count = count + 1
                flag = 4
        if playerx >= boat5x-70 and playerx <= boat5x+70:
            if playery >= (boat5y-30) and playery <= (boat5y+40):
                count = count + 1
                flag = 4
        if playerx >= stone1x-10 and playerx <= stone1x+10:
            if playery >= (stone1y-30) and playery <= (stone1y+40):
                count = count + 1
                flag = 4
        if playerx >= stone2x-10 and playerx <= stone2x+10:
            if playery >= (stone2y-30) and playery <= (stone2y+40):
                count = count + 1
                flag = 4
        if playerx >= stone3x-10 and playerx <= stone3x+10:
            if playery >= (stone3y-30) and playery <= (stone3y+40):
                count = count + 1
                flag = 4

    if flag== 3:
            playerx = width/2 + 500
            playery = 10
            flag = 2
    if flag== 4:
            playerx = 700
            playery = height - 10
            flag = 1

# scoring
    if flag == 1:
        if playery <=800:
            if score1 <=jadd1:
                score1+=30
        if playery <= 600:
            if score1 <=jadd1+30:
                score1+=30
        if playery <= 400:
            if score1 <=jadd1+60:
                score1+=30
        if playery <= 200:
            if score1 <=jadd1+90:
                score1+=30
        if playery <= 50:
            if score1 <= jadd1+120:
                score1 += 100
                level1 = 1
                playerx = width/2
                playery = 0
                flag = 2
    text1 = font.render('Player 1 score: ' + str(score1), True, black, yellow)
    DISPLAYSURF.blit(text1, (1480, 970))
    if flag == 2:
        if playery >=200:
            if score2 <=jadd2:
                score2+=30
        if playery >= 400:
            if score2 <=jadd2+30:
                score2+=30
        if playery >= 600:
            if score2 <jadd2+60:
                score2+=30
        if playery >= 800:
            if score2 <jadd2+90:
                score2+=30
        if playery >= 950:
            if score2 >= jadd2+120:
                score2 += 100
                level2 = 1
                playerx= 700
                playery= height - 10
                flag = 1
                count = count + 1

    text2 = font.render('Player 2 score: ' + str(score2), True, black, yellow)
    DISPLAYSURF.blit(text2, (280, 970))
    if score1 == 220:
        flag = 2
    if count == 2:
        running = False
    if level1 == 1:
        if flag==1:
            jadd1=320
    if level1 == 2:
        if flag==1:
            jadd1 =640
    if level2 == 1:
        if flag==2:
            jadd2=320
    if level2 == 2:
        if flag==2:
            jadd2 =640

    pygame.display.update()
while not running:
    DISPLAYSURF.fill(yellow)

    if score1 > score2:
        text = font.render('Player 1 wins with a score of ' + str(score1) + '!!', True, black, yellow)
        DISPLAYSURF.blit(text, (500, 500))
    if score2 > score1:
        text = font.render('Player 2 wins with a score of ' + str(score2) + '!!', True, black, yellow)
        DISPLAYSURF.blit(text, (500, 500))
    if score1 == score2:
        if dt1>dt2:
            text = font.render('Player 2 wins with a score of ' + str(score2) + ' in ' + str(dt2) + ' seconds!!', True, black, yellow)
            DISPLAYSURF.blit(text, (500, 500))
        if dt1<dt2:
            text = font.render('Player 1 wins with a score of ' + str(score1) + ' in ' + str(dt1) + ' seconds!!', True, black, yellow)
            DISPLAYSURF.blit(text, (500, 500))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
