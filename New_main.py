import pygame as pg
from pygame import mixer
from random import randint
from Sprites import *








class game():
    def __init__(self): 
        pg.init()
        mixer.init()

        mixer.music.load("happy.mp3")
        mixer.music.set_volume(1)
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)

        self.width = 800
        self.height = 600

        self.text_font = pg.font.SysFont("Arial", 30)

        self.screen = pg.display.set_mode((self.width,self.height))
        self.bg = pg.image.load("tenor.gif")
        self.bg = pg.transform.scale (self.bg , (801,601))

        self.FPS = 160
        self.clock = pg.time.Clock()
        self.new()




    def new(self): # ny runde
        mixer.music.play(loops= -1)
        self.all_sprites = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.food_items = pg.sprite.Group()

        self.mr_pump = player(self)
        self.slimey = slime()
        self.eat = Food()

        self.all_sprites.add(self.slimey)
        self.enemy_group.add(self.slimey)
        self.food_items.add(self.eat)

        self.text_player_hp = self.text_font.render(str(self.mr_pump.life) + " Health", False, (self.RED))
        self.text_energy = self.text_font.render(str(self.mr_pump.energy) + " Energy", False, (self.RED))
        self.run()

    def run(self):
        playing = True
        while playing: # game loop
            self.clock.tick(self.FPS)
            #print("frame game loop")
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    playing=False
            self.screen.blit(self.bg, (-1,-1))


        
            hits = pg.sprite.spritecollide(self.mr_pump, self.enemy_group, True)
            

            food_hit = pg.sprite.spritecollide(self.mr_pump, self.food_items, True)
            if food_hit:
                self.mr_pump.life += 10



            if hits:
                self.mr_pump.life -= 10
                self.mr_pump.image = player_damage
            
            if self.mr_pump.life < 1:
                self.mr_pump.life = 100
                playing = False

            self.text_player_hp = self.text_font.render(str(self.mr_pump.life) + " Health", False, (self.RED))
            self.screen.blit(self.text_player_hp, (10, 10))
            self.text_energy = self.text_font.render(str(self.mr_pump.energy) + " Energy", False, (self.RED))
            self.screen.blit(self.text_energy, (10, 40))

                # lag nye fiender
            if len(self.enemy_group) < 5:
                slimey = slime()
                self.all_sprites.add(slimey)
                self.enemy_group.add(slimey)

            if len(self.food_items) < 1:
                foods = Food()
                self.all_sprites.add(foods)
                self.food_items.add(foods)

            self.all_sprites.update() # kjører update til alle sprites i all_sprites.

            self.all_sprites.draw(self.screen)
            pg.display.update()

g = game() # her lages game classen, also starter spill.



