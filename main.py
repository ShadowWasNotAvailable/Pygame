import pygame as pg
from pygame import mixer
from random import randint
from Sprites import *
pg.init()
mixer.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

bg = pg.image.load("tenor.gif")
bg = pg.transform.scale (bg , (801,601))

mixer.music.load("happy.mp3")
mixer.music.set_volume(1)
mixer.music.play(loops= -1)


all_sprites = pg.sprite.Group()
enemy_group = pg.sprite.Group()

mr_pump = player()
slimey = slime()
all_sprites.add(mr_pump , slimey)
enemy_group.add(slimey)


colours = (randint(0,255) , randint(0,255) , randint(0,255))

x = 0
y = 0

speed = 5

deathcount = 0

direction_x = 1
direction_y = 1


comic_sans30 = pg.font.SysFont("Ferrara-Osf", 30)
print(mr_pump.life)


FPS = 160
clock = pg.time.Clock()

screen = pg.display.set_mode((800,600))

playing = True
while playing: # game loop
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing=False


    screen.blit(bg, (-1,-1))

    all_sprites.update() # kjører update til alle sprites i all_sprites.

    hits = pg.sprite.spritecollide(mr_pump, enemy_group, True)
    if hits:
        mr_pump.life -= 10

    if mr_pump.life < 1:
        mr_pump.kill
        mr_pump.life = 100
        deathcount += 1

    
    
    text_deathcount = comic_sans30.render(str(deathcount) + " Deaths", False, (RED))
    screen.blit(text_deathcount, (10, 30))

    text_player_hp = comic_sans30.render(str(mr_pump.life) + " Health", False, (RED))
    screen.blit(text_player_hp, (10, 10))

    # lag nye fiender
    if len(enemy_group) < 5:
        slimey = slime()
        all_sprites.add(slimey)
        enemy_group.add(slimey)


    all_sprites.draw(screen)



    pg.display.update()