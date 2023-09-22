from plataform import Plataform
from player import Player
from constantes import *
from enemies import Enemy
from background import Background
from gui_form import Form
from bullets import Bullet
from coin import Coin
from auxiliar import *

class LevelGame2(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.player_1 = Player(x= 1, y = 500, speed_walk= 10, gravity=8, jump=18, animation_rate_ms=30, move_rate_ms=30, jump_height=100, interval_time_jump = 200)
        
        self.enemies_list = []
        self.enemies_list.append(Enemy("flowergun",x= 540, y = 480,hitbox_h=140, hitbox_w=95, speed_walk= 8, gravity=8,frame_animation_ms=35, move_rate_ms=30))
        self.enemies_list.append(Enemy("flowergun",x= -20, y = 270,hitbox_h=140, hitbox_w=95, speed_walk= 8, gravity=8,frame_animation_ms=35, move_rate_ms=30))
        self.enemies_list.append(Enemy("flowergun",x= -20, y = 90,hitbox_h=140, hitbox_w=95, speed_walk= 8, gravity=8,frame_animation_ms=35, move_rate_ms=30))
        self.enemies_list.append(Enemy("mushroom",x= 1180, y = 55,hitbox_h=80, hitbox_w=50, speed_walk= 1, gravity=8,frame_animation_ms=35, move_rate_ms=30, direction= DIRECTION_L, count_cd= 30))
        self.enemies_list.append(Enemy("mushroom",x= 1180, y = 206,hitbox_h=80, hitbox_w=50, speed_walk= 1, gravity=8,frame_animation_ms=35, move_rate_ms=30, direction= DIRECTION_L, count_cd= 70))
        self.enemies_list.append(Enemy("mushroom",x= 1180, y = 375,hitbox_h=80, hitbox_w=50, speed_walk= 1, gravity=8,frame_animation_ms=35, move_rate_ms=30, direction= DIRECTION_L, count_cd= 50))

        self.plataform_list = []
        self.plataform_list.append(Plataform(x = -10, y= 215,path="assets\plataform\lvl02\plataform_lvl02_03.png", width= 868/2, height = 408/2, type=1))
        self.plataform_list.append(Plataform(x = -10, y= 400,path="assets\plataform\lvl02\plataform_lvl02_03.png", width= 868/2, height = 408/2, type=1))
        self.plataform_list.append(Plataform(x = 75, y= 500,path="assets\plataform\lvl02\plataform_lvl02_02.png", width= 568/2, height = 387/2, type=1))
        self.plataform_list.append(Plataform(x = 980, y= 110,path="assets\plataform\lvl02\plataform_lvl02_01.png", width= 559/2, height = 357/2, type=1))
        self.plataform_list.append(Plataform(x = 980, y= 270,path="assets\plataform\lvl02\plataform_lvl02_01.png", width= 559/2, height = 357/2, type=1))
        self.plataform_list.append(Plataform(x = 980, y= 430,path="assets\plataform\lvl02\plataform_lvl02_01.png", width= 559/2, height = 357/2, type=1))
        self.plataform_list.append(Plataform(x = 630, y= 70,path="assets\plataform\lvl02\plataform_lvl02_01.png", width= 559/2, height = 357/2, type=1))
        self.plataform_list.append(Plataform(x = 630, y= 220,path="assets\plataform\lvl02\plataform_lvl02_01.png", width= 559/2, height = 357/2, type=1))
        self.plataform_list.append(Plataform(x = 630, y= 370,path="assets\plataform\lvl02\plataform_lvl02_01.png", width= 559/2, height = 357/2, type=1))
        self.plataform_list.append(Plataform(x = 630, y= 520,path="assets\plataform\lvl02\plataform_lvl02_01.png", width= 559/2, height = 357/2, type=1))
        
        self.plataform_list.append(Plataform(x = 0, y= 605,path="assets\plataform\lvl02\\background_floor_lvl02.png", width= 1280, height = 160, type=1))
        
        self.static_background = Background(x= 0, y=0, widht=w, height=h, path="assets\maps\\background_02.png")

        self.bullets_player = []
        self.bullets_enemy = []

        self.coin_list = []
        self.coin_list.append(Coin(x= 140, y= 260, frame_animation_ms= 30, move_rate_ms= 30))
        self.coin_list.append(Coin(x= 140, y= 100, frame_animation_ms= 30, move_rate_ms= 30))
        self.coin_list.append(Coin(x= 720, y= 250, frame_animation_ms= 30, move_rate_ms= 30))
        self.coin_list.append(Coin(x= 475, y= 290, frame_animation_ms= 30, move_rate_ms= 30))
        self.coin_list.append(Coin(x= 1060, y= 5, frame_animation_ms= 30, move_rate_ms= 30))

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