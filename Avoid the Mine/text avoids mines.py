import sys, pygame
import numpy as np
from pygame.locals import *

pygame.init()

width1 = 50
height1 = 20
x = 20
y = 20

# Text Character.
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render('s_mario',True,(0,255,0))
mb = text.get_rect()

# For Creating random places for mines.
a = np.random.randint(700,size = 20)
b = np.random.randint(700, size = 20)

# Destination Point
text3 = font.render('peach',True,(0,255,0))
fin = text3.get_rect()

win = pygame.display.set_mode((720,720))

fin.bottom=720
fin.right=720

while 1:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    boo=0
    if keys[pygame.K_w] and mb.top>0:
    # Cases where Main Character falls into trap
        for i in range(len(a)):
            if (mb.top == b[i]+height and mb.left<=a[i]+width and mb.left>=a[i]) or (mb.top == b[i]+height and mb.right<=a[i]+width and mb.right>=a[i]):
                print("over")
                boo=1
                break
        if boo==1:
            break
        mb.top -=1
    if keys[pygame.K_a] and mb.left>0:
        for i in range(len(a)):
            if (mb.left == a[i]+width and mb.top<=b[i]+height and mb.top>=b[i]) or (mb.left == a[i]+width and mb.bottom<=b[i]+height and mb.bottom>=b[i]):
                print("over")
                boo=1
                break
        if(boo==1):
            break
        mb.left-=1   
    if keys[pygame.K_s] and mb.bottom<720:
        for i in range(len(a)):
            if (mb.bottom == b[i] and mb.left<=a[i]+width and mb.left>=a[i]) or (mb.bottom == b[i] and mb.right<=a[i]+width and mb.right>=a[i]):
                print("over")
                boo=1
                break
        if(boo==1):
            break
        mb.bottom+=1
    if keys[pygame.K_d] and mb.right<720:
        for i in range(len(a)):
            if (mb.right == a[i] and mb.top<=b[i]+height and mb.top>=b[i]) or (mb.right == a[i] and mb.bottom<=b[i]+height and mb.bottom>=b[i]):
                print("over")
                boo=1
                break
        if(boo==1):
            break
        mb.right+=1
    width = abs(mb.left-mb.right)
    height = abs(mb.top-mb.bottom)
    
    # Character reasches destination
    if (mb.bottom == fin.top and mb.right== fin.left) or (mb.bottom==fin.top and mb.right>fin.left):
        print("they met")
        break
    if(mb.right==fin.left and mb.bottom>=fin.top):
        print("they met")
        break


    win.fill([0,0,0])
    for i in range(len(a)):
        pygame.draw.rect(win, (255,0,00), (a[i],b[i],width,height))
        text1 = font.render('bowser',True,(0,0,0))
        trap = text1.get_rect()
        trap.top=b[i]+3
        trap.left=a[i]+2
        win.blit(text1,trap)

    pygame.display.update()
    win.blit(text,mb)
    win.blit(text3,fin)
    pygame.display.flip()
    
if boo==1:
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('s_mario died',True,(0,255,0))
    mb = text.get_rect()
    while 1:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
        mb.top=700/2
        mb.left=250
        win.fill([0,0,0])
        win.blit(text,mb)
        pygame.display.flip()
else:
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('s_mario saved peach',True,(0,255,0))
    text1 = font.render('and lived happily ever after',True,(0,255,0))
    mb = text.get_rect()
    db = text1.get_rect()
    while 1:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
        mb.top=700/2
        mb.left=250
        db.top=750/2
        db.left=270
        win.fill([0,0,0])
        win.blit(text,mb)
        win.blit(text1,db)
        pygame.display.flip()
