import pygame as pg
vec = pg.math.Vector2

player_img = pg.image.load ("pumpkinhead-alpha.png")
player_img = pg.transform.scale (player_img , (100,150)) # endrer størrelse på player.

class player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect() # henter self.image sin størrelse og lager en hitbox.
        self.pos = vec(100 , 100)
        self.rect.center = self.pos
        self.speed = 3


    


    def update(self):
        self.rect = self.pos # flytter rect til player til ny posisjon hver frame.

        
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= 1
        
        if keys[pg.K_s]:
            self.pos.y += 1

        if keys[pg.K_a]:
            self.pos.x -= 1

        if keys[pg.K_d]:
            self.pos.x += 1
