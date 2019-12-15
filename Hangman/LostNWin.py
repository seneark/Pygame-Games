import pygame as pg
import sys


bg = pg.image.load("pics/background.jpg")

def lost():
    # When player loses
    win = pg.display.set_mode((640, 480))

    font = pg.font.SysFont('FreeMono', 50, bold = 10)
    text = font.render('You Lost',True,(255,255,0))
    mb = text.get_rect()
    # Loosing Note
    while 1:
        for events in pg.event.get():
            if events.type == pg.QUIT:
                sys.exit()
        mb.top=200
        mb.left=220
        win.blit(bg,(0,0))
        win.blit(text,mb)
        pg.display.flip()

def win():
    # when the player wins.
    win = pg.display.set_mode((640, 480))

    font = pg.font.SysFont('FreeMono', 50, bold = 10)
    text = font.render('You Win',True,(255,255,0))
    mb = text.get_rect()
    text_ = font.render('Congratulations',True,(255,255,0))
    mb_ = text_.get_rect()

    # Display Winning note
    while 1:
        for events in pg.event.get():
            if events.type == pg.QUIT:
                sys.exit()
        mb.top=200
        mb.left=220

        mb_.top = 230
        mb_.left = 120

        win.blit(bg,(0,0))
        win.blit(text,mb)
        win.blit(text_,mb_)
        pg.display.flip()

