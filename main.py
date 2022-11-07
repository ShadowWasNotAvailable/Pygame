import pygame as pg
from random import randint
pg.init()


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

colours = (randint(0,255) , randint(0,255) , randint(0,255))

x = 0
y = 0

speed = 5

direction_x = 1
direction_y = 1

FPS = 160
clock = pg.time.Clock()

screen = pg.display.set_mode((800,600))
player_img = pg.image.load ("pumpkinhead-alpha.png")
player_img = pg.transform.scale (player_img , (100,150))

playing = True
while playing: # game loop
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing=False


    screen.fill(WHITE)
    


    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        y += -speed

    if keys[pg.K_s]:
        y += speed

    if keys[pg.K_d]:
        x += speed
    
    if keys[pg.K_a]:
        x += -speed
    

    


 
    if x > 700:
        x = 700
    if y > 450:
        y = 450
    
    if x < 0:
        x = 0
    if y < 0:
        y = 0

    colours = (randint(0,255) , randint(0,255) , randint(0,255))

    screen.blit(player_img , (x,y))

    pg.display.update()