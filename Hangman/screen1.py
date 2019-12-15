import sys
import numpy as np
import pygame as pg

def screne1():
    Answer = []     # The array to be return containing name of movie and hints.
    
    bg = pg.image.load("pics/bg12.jpg")   #loads background image.

    screen = pg.display.set_mode((640, 480))    # set the length of x and y axis of display screen.
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 150, 140, 32)  # created the movie input box.
    hint_box = pg.Rect(100, 230, 140, 32)   #created the hinf input box.


    color_inactive = pg.Color(100,0,0)
    color_active = pg.Color(0,0,0)

    #for game title.
    font_title = pg.font.SysFont("Manjari", 40, bold=5)
    text_title = font_title.render('Hangman',True,(255,255,100))
    Name_title = text_title.get_rect()
    Name_title.left = 100
    Name_title.top = 50


    # for movie box.
    color = color_inactive
    active = False
    text = ''
    done = False

    # for Text above movie box.
    font_ = pg.font.SysFont("Chilanka", 28)     ## for windows use comicsansms in place of Chilanka.
    text_ = font_.render('Name of Movie:',True,(0,0,0))
    Name = text_.get_rect()
    Name.left = 100
    Name.top = 120

    #for hint box.
    color_h = color_inactive
    active_h = False
    text_h = ''
    done_h = False

    # for Text above hint box.
    font__h = pg.font.SysFont("Chilanka", 28)   ## for windows use comicsansms in place of Chilanka.
    text__h = font__h.render('Hint goes in below Box:',True,(0,0,0))
    Name_h = text__h.get_rect()
    Name_h.left = 100
    Name_h.top = 200

    #for submit portion
    font_S = pg.font.SysFont("Comfortaa", 40)
    text_S = font_S.render('Submit',True,(255,255,50))
    Name_S = text_S.get_rect()
    Name_S.left = 100
    Name_S.top = 290

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT :
                done = True      

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
                    if event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            
            if event.type == pg.MOUSEBUTTONDOWN:
                if hint_box.collidepoint(event.pos):
                    active_h = not active_h
                else:
                    active_h = False
                # Change the current color of the hint box.
                color_h = color_active if active_h else color_inactive

            if event.type == pg.KEYDOWN:
                if active_h:
                    if event.key == pg.K_BACKSPACE:
                        text_h = text_h[:-1]
                    else:
                        text_h += event.unicode
            
            # Submit button.
            if event.type == pg.MOUSEBUTTONDOWN:
                if Name_S.collidepoint(event.pos):
                    Answer.append(text)
                    Answer.append(text_h)
                    done = True
                    return Answer
                    break

 
        screen.blit(bg,(0,0))

        screen.blit(text_title,Name_title)

        screen.blit(text_,Name)     # for movie Text.
        txt_surface = font.render(text, True, color)    #for movie box.

        screen.blit(text__h,Name_h)     #for hint Text
        txt_surface_h = font.render(text_h, True, color)    #for hint box.
        
        screen.blit(text_S,Name_S)

        width = max(200, txt_surface.get_width()+10)    # Resize the input box if the text is too long.
        input_box.w = width

        width_h = max(200, txt_surface_h.get_width()+10)    # Resize the hint box.
        hint_box.w = width_h

        # Blit the texts.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        screen.blit(txt_surface_h, (hint_box.x+5, hint_box.y+5))

        # Blit the input_box rect and hint_box.
        pg.draw.rect(screen, color, input_box, 2)
        pg.draw.rect(screen, color, hint_box, 2)
 
        pg.display.flip()
        clock.tick(30)



