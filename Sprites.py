import pygame as pg
from random import randint
vec = pg.math.Vector2

player_front = pg.image.load ("pumpkinhead-alpha.png")
player_front = pg.transform.scale (player_front , (100,150)) # endrer størrelse på bilde.
player_right = pg.image.load ("pump-right.png")
player_right = pg.transform.scale (player_right , (100,150)) # endrer størrelse på bilde.
player_left = pg.image.load ("pump-left.png")
player_left = pg.transform.scale (player_left , (100,150)) # endrer størrelse på bilde.
player_back = pg.image.load ("pump-back.png")
player_back = pg.transform.scale (player_back , (100,150)) # endrer størrelse på bilde.


Slime_img = pg.image.load ("slime.g.png")

class player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_front
        self.rect = self.image.get_rect() # henter self.image sin størrelse og lager en hitbox.
        self.pos = vec(400 , 300)
        self.rect.center = self.pos
        self.speed = 3
        self.life = 100
        self.energy = 100


    def update(self):
        self.rect.center = self.pos # flytter rect til player til ny posisjon hver frame.

        
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= self.speed
            self.image = player_back

        if keys[pg.K_s]:
            self.pos.y += self.speed
            self.image = player_front

        if keys[pg.K_a]:
            self.pos.x -= self.speed
            self.image = player_left

        if keys[pg.K_d]:
            self.pos.x += self.speed
            self.image = player_right
        
        if keys[pg.K_LSHIFT] is True:
            self.speed = 5
            self.energy -= 1

        
        if keys[pg.K_LSHIFT] is False:
            self.speed = 3
            self.energy += 1
        
        if self.energy < 1:
            self.speed = 3

        if self.energy > 100:
            self.energy = 100
        
        if self.energy < 0:
            self.energy = 0
            
        
        print (self.energy)
            




class slime(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = Slime_img
        self.rect = self.image.get_rect() # henter self.image sin størrelse og lager en hitbox.
        self.pos = vec(randint (0,800) , 0)
        self.rect.center = self.pos
        self.speed = 6

    def update(self):
        self.rect.center = self.pos
        self.pos.y += self.speed


        if self.pos.y > 700:
            
            self.pos.y = -100
            
            self.pos.x = randint (0,800)

