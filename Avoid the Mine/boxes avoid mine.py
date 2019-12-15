import sys, pygame
import numpy as np
from pygame.locals import *

pygame.init()

width = 20
height = 20
x = 20
y = 20

# For creating radom spots for mines.
a = np.random.randint(700,size = 30)    
b = np.random.randint(700, size = 30)

win = pygame.display.set_mode((720,720))

while 1:
    pygame.time.delay(10)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
    
    # Key press events
    keys = pygame.key.get_pressed()
    if (pygame.mouse.get_pressed()[0]) == 1:
        x,y = (pygame.mouse.get_pos())
    boo = 0
    if keys[pygame.K_w]:
        for i in range(len(a)):
            if (x >=a[i] and x <= a[i]+width and y > b[i] and y<b[i] + height) or(  x +width>a[i] and x+width < a[i]+width and y > b[i] and y<b[i] + height):
                print("over")
                boo=1
                break
        if boo ==1:
            break
        y-=1
    if keys[pygame.K_a]:
        for i in range(len(a)):
            if (x == a[i]+width and y >= b[i] and y <= b[i]+height) or (x == a[i] +width and y+height >= b[i] and y+height <=b[i]+height):
                print("over")
                boo=1
                break
        if boo ==1:
            break
        x-=1    
    if keys[pygame.K_s]:
        for i in range(len(a)):
            if(y+height==b[i] and x >=a[i] and x <= a[i]+width) or (y +height==b[i] and x +width>a[i] and x+width < a[i]+width):
                print("over")
                boo=1
                break
        if boo ==1:
            break
        y+=1
    if keys[pygame.K_d]:
        for i in range(len(a)):
            if(x+width==a[i] and y >= b[i] and y <= b[i]+height) or (x+width==a[i] and y+height >= b[i] and y+height <= b[i]+height):
                print("over")
                boo=1
                break
        if boo ==1:
            break
        x+=1
    win.fill([0,0,0])
    for i in range(len(a)):
        pygame.draw.rect(win, (255,0,00), (a[i],b[i],width,height))
    
    pygame.draw.rect(win, (50,20,100), (x,y,width,height))
    pygame.display.update()
