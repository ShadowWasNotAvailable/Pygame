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
player_damage = pg.image.load ("pump-damage.png")
player_damage = pg.transform.scale (player_damage , (100,150)) # endrer størrelse på bilde.
pew_img = pg.image.load("Pew.png")
pew_img = pg.transform.scale (pew_img , (50,50)) # endrer størrelse på bilde.


Slime_img = pg.image.load ("slime.g.png")

class player(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = player_front
        self.rect = self.image.get_rect() # henter self.image sin størrelse og lager en hitbox.
        self.pos = vec(400 , 300)
        self.rect.center = self.pos
        self.speed = 3
        self.life = 100
        self.energy = 100
        self.range_direction_x = 1
        self.range_direction_y = 1
        self.pew_speed = 4
        self.last_healing = 0
        self.healing_timer = 500
        self.healing_count = 500
        self.score = 0


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

        if keys[pg.K_h]:
            self.healing()
        
        if self.energy < 1:
            self.speed = 3

        if self.energy > 100:
            self.energy = 100
        
        if self.energy < 0:
            self.energy = 0

        if self.pos.x > 750:
            self.pos.x = 750
        if self.pos.y > 550:
            self.pos.y = 550

        if self.pos.x < 50:
            self.pos.x = 50
        if self.pos.y < 50:
            self.pos.y = 50

        

        
      
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.attack() # starter attack funksjon hvis vi klikker SPACE knapp
            if keys[pg.K_UP]:
                self.attack_direction_y -= self.pew_speed
            if keys[pg.K_DOWN]:
                self.attack_direction_y = self.pew_speed
            if keys[pg.K_LEFT]:
                self.attack_direction_x -= self.pew_speed            
            if keys[pg.K_RIGHT]:
                self.attack_direction_x = self.pew_speed
        
        now = pg.time.get_ticks()
        self.healing_count = now - self.last_healing
        if self.healing_count > 500:
            self.healing_count = ("Healing is ready")



    def attack(self):
        Ranged_attack(self.game, self.pos.x, self.pos.y)


    def healing(self):
        now = pg.time.get_ticks()
        if now - self.last_healing > self.healing_timer:
            self.life += 10
            self.healing_count = 0
            print ("HEAL!")
            self.last_healing = pg.time.get_ticks()

        else:
            print(now - self.last_healing)
            print ("NOT READY YET!")
         


        
       




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
        
        if self.pos.y > 800:
            self.pos.y = -5
            self.pos.x = randint (0,800)


class Ranged_attack(pg.sprite.Sprite):
    def __init__(self, game, x ,y):
        self.groups = game.all_sprites, game.projectiles_group # legger til i sprite gruppe
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pew_img
        self.rect = self.image.get_rect()
        self.pos = vec(x+22, y+27) # start posisjon
        self.rect.center = self.pos
        self.pew_speed = 10
        
        self.move_to = vec(pg.mouse.get_pos())
        self.move_vector = self.move_to - self.pos  # finner "forskjellen" mellom self.pos og posisjon til musepeker
        self.rect.center = self.pos


    def update(self):
        self.rect.center = self.pos

        self.pos += self.move_vector.normalize() * self.pew_speed  # flytter self.pos litt mot musepeker

        if self.pos.x > 800:
            self.kill
        if self.pos.y > 600:
            self.kill
        if self.pos.x < 0:
            self.kill
        if self.pos.y < 0:
            self.kill

    






