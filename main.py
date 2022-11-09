import pygame as pg
from random import randint
from Sprites import *
pg.init()


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

all_sprites = pg.sprite.Group()

mr_pump = player()
all_sprites.add(mr_pump)


colours = (randint(0,255) , randint(0,255) , randint(0,255))

x = 0
y = 0

speed = 5

direction_x = 1
direction_y = 1

FPS = 160
clock = pg.time.Clock()

screen = pg.display.set_mode((800,600))

playing = True
while playing: # game loop
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing=False


    screen.fill(WHITE)

    all_sprites.update() # kjører update til alle sprites i all_sprites.
    all_sprites.draw(screen)

    pg.display.update()