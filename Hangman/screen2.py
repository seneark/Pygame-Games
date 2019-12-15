import pygame as pg
import sys
import screen1
import LostNWin

dead = 0

def screen2():
    screen = pg.display.set_mode((640, 480))

    bg = pg.image.load("pics/bg12.jpg")   #loads background image.

    Hints_there = screen1.screne1()

    font = pg.font.Font(None, 32)
    input_box = pg.Rect(220, 240, 50, 32) # for inputting letter
    color_inactive = pg.Color(0,0,0)
    color_active = pg.Color(255,0,0)
    color = color_inactive
    text = ''
    active = False

    # for hangman box
    hang_box = pg.Rect(245,300,50,90)

    # for game title.
    font_title = pg.font.SysFont("Manjari", 40, bold=5)
    text_title = font_title.render('Hangman',True,(255,255,100))
    Name_title = text_title.get_rect()
    Name_title.left = 100
    Name_title.top = 50

    font_in = pg.font.SysFont("Chilanka", 20, bold=5)
    text_in = font_in.render('Input Here',True,(25,0,100))
    Name_in = text_in.get_rect()
    Name_in.left = 80
    Name_in.top = 245

    # for displaying hint.
    font_H = pg.font.SysFont(None, 28)     ## for windows use comicsansms in place of Chilanka.
    text_H = font_H.render('Hints:',True,(0,0,0))
    Name_H = text_H.get_rect()
    Name_H.left = 100
    Name_H.top = 120
 
    font_hints = pg.font.SysFont("Chilanka", 20)     ## for windows use comicsansms in place of Chilanka.
    text_hints = font_hints.render(str(Hints_there[1]),True,(0,0,0))
    Name_hints = text_hints.get_rect()
    Name_hints.left = 100
    Name_hints.top = 150

    a =""
    Hints_there[0] = Hints_there[0].lower()
    Count = len(Hints_there[0])
    # for Displaying movie name as asterisk
    for i in Hints_there[0]:
        if i.isalnum():
            a += '*'
        elif i == ' ':
            a += ' '
            Count -= 1
        else:
            a += '*'
    Max = max(0,len(Hints_there[0])-10)
    #for disaplaying movie name as *
    font_Movie = pg.font.SysFont(None, 50)     ## for windows use comicsansms in place of Chilanka.
    text_Movie = font_Movie.render(a,True,(0,0,0))
    Name_Movie = text_Movie.get_rect()
    Name_Movie.left = 150-Max
    Name_Movie.top = 200

    # attempts.
    attemp = "total attempt: 7"
    font_att = pg.font.SysFont(None, 18)
    text_att = font_att.render(attemp,True,(0,0,0))
    Name_att = text_att.get_rect()
    Name_att.left = 500
    Name_att.top = 50

    # attempt used.
    at = "attempt used = 0"
    font_at = pg.font.SysFont(None, 18)
    text_at = font_at.render(at,True,(0,0,0))
    Name_at = text_at.get_rect()
    Name_at.left = 500
    Name_at.top = 90
    

    boo = False      # word has not been found.
    penalty = 0     # for finding no of wrong attempt.

    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT :
                sys.exit() 

            if event.type == pg.MOUSEBUTTONDOWN:
                   # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                   # Toggle the active variable.
                    active = not active
                else:
                    active = False
               # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                            text = text.lower()
                            for i in range(len(Hints_there[0])):
                                if text == Hints_there[0][i]:
                                    a = list(a)
                                    a[i] = text
                                    a = "".join(a)
                                    Count -=1
                                    boo = True      # alphabet is there in movie name.
                            if not boo:
                                penalty +=1
                                at = list(at)
                                at[-1] = str(penalty)
                                at = "".join(at)
                            else:
                                boo = False
                            font_Movie = pg.font.SysFont(None, 50)     ## for windows use comicsansms in place of Chilanka.
                            text_Movie = font_Movie.render(a,True,(0,0,0))
                            Name_Movie = text_Movie.get_rect()
                            Name_Movie.left = 150-Max
                            Name_Movie.top = 200-Max

                            text_at = font_at.render(at,True,(0,0,0))
                            Name_at = text_at.get_rect()
                            Name_at.left = 500
                            Name_at.top = 90

                            text = ""
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode 

        screen.blit(bg,(0,0))

        if penalty >= 1:
            pg.draw.circle(screen, (100,100,0), (270,320), 10,1)
        if penalty >= 2:
            pg.draw.line(screen,(100,100,0),(270,330),(270,355),3)
        if penalty >=3:
            pg.draw.line(screen,(100,100,0),(270,355),(260,375),3)
        if penalty >= 4:
            pg.draw.line(screen,(100,100,0),(270,355),(280,375),3)
        if penalty >= 5:
            pg.draw.line(screen,(100,100,0),(270,340),(260,360),3)
        if penalty >= 6:
            pg.draw.line(screen,(100,100,0),(270,340),(280,360),3)
        if penalty >=7:
            dead = 1
            print('dead')
            LostNWin.lost()
            break
        elif Count == 0:
            print("Correct")
            LostNWin.win()
            break

        txt_surface = font.render(text, True, color)
        
        width = max(200, txt_surface.get_width()+10)    # Resize the input box if the text is too long.
        input_box.w = width

        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        
        
        screen.blit(text_title,Name_title)
        screen.blit(text_H,Name_H)
        screen.blit(text_hints,Name_hints)
        screen.blit(text_Movie,Name_Movie)
        screen.blit(text_in,Name_in)
        screen.blit(text_att,Name_att)
        screen.blit(text_at,Name_at)

        pg.draw.rect(screen, color, input_box, 2)   #for input box.
        pg.draw.rect(screen,(0,255,0), hang_box,2 )

        pg.display.update()
        pg.display.flip()