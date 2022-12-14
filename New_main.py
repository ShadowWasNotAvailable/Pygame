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
        self.CRIMSON = (153,0,0)

        self.width = 800
        self.height = 600

        self.text_font = pg.font.SysFont("Arial", 30)

        self.screen = pg.display.set_mode((self.width,self.height))
        self.bg = pg.image.load("Grass.png")
        self.bg = pg.transform.scale (self.bg , (801,601))
        self.skull = pg.image.load ("Skull.png")
        self.skull = pg.transform.scale (self.skull , (500,500))
        self.FPS = 160
        self.clock = pg.time.Clock()
        self.new()




    def new(self): # ny runde
        mixer.music.play(loops= -1)
        self.all_sprites = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.projectiles_group = pg.sprite.Group()
   

        self.mr_pump = player(self)
        self.slimey = slime()
       
  

        self.all_sprites.add(self.slimey)
        self.enemy_group.add(self.slimey)
        
   

        self.text_player_hp = self.text_font.render(str(self.mr_pump.life) + " Health", False, (self.RED))
        self.text_energy = self.text_font.render(str(self.mr_pump.energy) + " Energy", False, (self.RED))
        self.text_healing_timer = self.text_font.render(str(self.mr_pump.healing_timer) + " Healing timer", False, (self.RED))
        self.run()

    def run(self):
        playing = True
        while playing: # game loop
            self.clock.tick(self.FPS)
          
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    playing=False
            self.screen.blit(self.bg, (-1,-1))


        
            hits = pg.sprite.spritecollide(self.mr_pump, self.enemy_group, True)
            self.perojectiles_hit = pg.sprite.groupcollide(self.enemy_group,self.projectiles_group , True , True)
        



            if hits:
                self.mr_pump.life -= 10
                self.mr_pump.image = player_damage
                          
            if self.perojectiles_hit:
                self.mr_pump.score += 1

            if self.mr_pump.life < 1:
                self.mr_pump.life = 100
                self.game_over()
                playing = False

            if self.mr_pump.life > 100:
                self.mr_pump.life = 100

            self.text_player_hp = self.text_font.render(str(self.mr_pump.life) + " Health", False, (self.RED))
            self.screen.blit(self.text_player_hp, (10, 10))
            self.text_energy = self.text_font.render(str(self.mr_pump.energy) + " Energy", False, (self.RED))
            self.screen.blit(self.text_energy, (10, 40))
            self.text_score = self.text_font.render(str(self.mr_pump.score) + " Score",  False, (self.RED))
            self.screen.blit(self.text_score, (10, 70))
            self.text_healing_timer = self.text_font.render(str(self.mr_pump.healing_count), False, (self.RED))
            self.screen.blit(self.text_healing_timer, (10, 100))

                # lag nye fiender
            if len(self.enemy_group) < 15:
                slimey = slime()
                self.all_sprites.add(slimey)
                self.enemy_group.add(slimey)


            self.all_sprites.update() # kjører update til alle sprites i all_sprites.

            self.all_sprites.draw(self.screen)
            pg.display.update()

    def game_over(self):
 
        self.game_over = True
        while self.game_over:
            self.clock.tick(self.FPS)
            self.game_over_text = self.text_font.render("Game over, click R to restart", False, (self.CRIMSON))
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_over = False
                    pg.quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:  # om vi clicker på R, avslutter vi game over loop, og går derett til self.new() som ligger etter game_over loop
                        self.game_over = False  

            self.screen.fill(self.BLACK)
            self.screen.blit(self.game_over_text,(250,500))  # tegner tekst på skjerm. 
            self.screen.blit(self.skull, (170,30))

            pg.display.update()
        
        self.new()
 

g = game() # her lages game classen, also starter spill.



