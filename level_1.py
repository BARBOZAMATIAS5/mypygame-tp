from plataform import Plataform
from player import Player
from constantes import *
from enemies import Enemy
from background import Background
from gui_form import Form
from bullets import Bullet
from coin import Coin
from auxiliar import *

class LevelGame1(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.player_1 = Player(x= 1, y = 500, speed_walk= 10, gravity=8, jump=20, animation_rate_ms=30, move_rate_ms=30, jump_height=100, interval_time_jump = 200)
        
        self.enemies_list = []
        self.enemies_list.append(Enemy("flowergun",x= 640, y = 500,hitbox_h=150, hitbox_w=110, speed_walk= 8, gravity=8,frame_animation_ms=35, move_rate_ms=30))
        self.enemies_list.append(Enemy("flowergun",x= 790, y = 290,hitbox_h=150, hitbox_w=110, speed_walk= 8, gravity=8,frame_animation_ms=35, move_rate_ms=30))
        self.enemies_list.append(Enemy("mushroom",x= -5, y = 355,hitbox_h=90, hitbox_w=50, speed_walk= 1, gravity=8,frame_animation_ms=35, move_rate_ms=30, direction= DIRECTION_R, count_cd=30))
        self.enemies_list.append(Enemy("mushroom",x= 10, y = 60,hitbox_h=90, hitbox_w=50, speed_walk= 1, gravity=8,frame_animation_ms=35, move_rate_ms=30, direction= DIRECTION_R, count_cd=45))

        self.plataform_list = []
        self.plataform_list.append(Plataform(x = -70, y= 110,path="assets\plataform\plataform_rock_04.png", width= 402/2, height = 669/2, type=1))
        self.plataform_list.append(Plataform(x = 1000, y= 120,path="assets\plataform\plataform_risco_01.png", width= 843/2, height = 944/2, type=1))
        self.plataform_list.append(Plataform(x = -75, y= 325,path="assets\plataform\plataform_rocks_small_01.png", width= 544.5, height = 321, type=1))
        self.plataform_list.append(Plataform(x = -15, y= 265,path="assets\plataform\plataform_floor_01.png", width= 427/2, height = 190/2, type=1))
        self.plataform_list.append(Plataform(x = 250, y= 450,path="assets\plataform\plataform_wood_01.png", width= 175, height = 63, type=1))
        self.plataform_list.append(Plataform(x = 550, y= 260,path="assets\plataform\plataform_wood_01.png", width= 175, height = 63, type=1))
        self.plataform_list.append(Plataform(x = 550, y= 460,path="assets\plataform\plataform_wood_01.png", width= 175, height = 63, type=1))
        self.plataform_list.append(Plataform(x = 825, y= 220,path="assets\plataform\plataform_wood_01.png", width= 175, height = 63, type=1))
        self.plataform_list.append(Plataform(x = 800, y= 400,path="assets\plataform\plataform_rocks_larg_01.png", width= 1023, height = 316, type=1))
        self.plataform_list.append(Plataform(x = 1000, y= 510,path="assets\plataform\plataform_wood_01.png", width= 175, height = 63, type=1))
        self.plataform_list.append(Plataform(x = -120, y= 410,path="assets\plataform\plataform_float_01.png", width= 429/2, height = 132/2, type=1))
        self.plataform_list.append(Plataform(x = 0, y= 610,path="assets\plataform\\background_floor.png", width= 1280, height = 108, type=1))
        
        self.static_background = Background(x= 0, y=0, widht=w, height=h, path="assets\maps\\background.png")

        self.bullets_player = []
        self.bullets_enemy = []

        self.coin_list = []
        self.coin_list.append(Coin(x= 300, y= 340, frame_animation_ms= 30, move_rate_ms= 30))
        self.coin_list.append(Coin(x= 50, y= 165, frame_animation_ms= 30, move_rate_ms= 30))
        self.coin_list.append(Coin(x= 1150, y= 330, frame_animation_ms= 30, move_rate_ms= 30))
        self.coin_list.append(Coin(x= 595, y= 305, frame_animation_ms= 30, move_rate_ms= 30))
        self.coin_list.append(Coin(x= 1150, y= 50, frame_animation_ms= 30, move_rate_ms= 30))

    def update(self, list_events, keys, delta_ms):

        Auxiliar.kill_sprites(bullets_list_player=self.bullets_player,
                      bullets_list_enemy=self.bullets_enemy,
                      enemies_list=self.enemies_list,
                      coin_list=self.coin_list,
                      player= self.player_1)
        
        for bullet in self.bullets_player:
            bullet.update(delta_ms)
        
        for bullet in self.bullets_enemy:
            bullet.update(delta_ms)

        Auxiliar.bullets(character= 'player',
                        owner = self.player_1, 
                        bullet_list = self.bullets_player, 
                        bullet = Bullet)

        for enemy in self.enemies_list:
            Auxiliar.bullets(character= 'enemy',
                            owner = enemy,
                            bullet_list = self.bullets_enemy,
                            bullet = Bullet)
            enemy.update(delta_ms, self.plataform_list)

        for coin in self.coin_list:
            coin.update(delta_ms, self.player_1)

        self.player_1.update(delta_ms, self.plataform_list)
        self.player_1.events(delta_ms, keys)

    def draw(self):
        super().draw()
        
        self.static_background.draw(self.surface)
        for plataform in self.plataform_list:
            plataform.draw(self.surface)

        for bullet in self.bullets_player:
            bullet.draw(self.surface)
        for bullet in self.bullets_enemy:
            bullet.draw(self.surface)

        for coin in self.coin_list:
            coin.draw(self.surface)

        for enemy in self.enemies_list:
            enemy.draw(self.surface)
        
        self.player_1.draw(self.surface)