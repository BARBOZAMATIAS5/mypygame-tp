from plataform import Plataform
from player import Player
from constantes import *
from enemies import Enemy
from background import Background
from gui_form import Form
from bullets import Bullet
from coin import Coin
from auxiliar import *

class LevelGame3(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.player_1 = Player(x= 1, y = 30, speed_walk= 10, gravity=8, jump=18, animation_rate_ms=30, move_rate_ms=30, jump_height=100, interval_time_jump = 200)
        
        self.enemies_list = []
        self.enemies_list.append(Enemy("flowergun",x= 25, y = 440,hitbox_h=140, hitbox_w=95, speed_walk= 2, gravity=8,frame_animation_ms=35, move_rate_ms=30, count_cd= 50))
        self.enemies_list.append(Enemy("flapy_bird",x= 850, y = 360,hitbox_h=140, hitbox_w=95, speed_walk= 5, gravity=8,frame_animation_ms=35, move_rate_ms=30, direction= DIRECTION_L, count_cd= 50))
        self.enemies_list.append(Enemy("flapy_bird",x= 65, y = 220,hitbox_h=80, hitbox_w=50, speed_walk= 3, gravity=8,frame_animation_ms=35, move_rate_ms=30, direction= DIRECTION_R, count_cd= 30))
        self.enemies_list.append(Enemy("flapy_bird",x= 635, y = 10,hitbox_h=80, hitbox_w=50, speed_walk= 4, gravity=8,frame_animation_ms=35, move_rate_ms=30, direction= DIRECTION_L, count_cd= 60))

        self.plataform_list = []
        self.plataform_list.append(Plataform(x = 0, y= 120,path="assets\plataform\lvl03\plataform_cloud_01.png", width= 208, height = 79, type=1))
        self.plataform_list.append(Plataform(x = 208, y= 120,path="assets\plataform\lvl03\plataform_cloud_01.png", width= 208, height = 79, type=1))
        self.plataform_list.append(Plataform(x = 416, y= 215,path="assets\plataform\lvl03\plataform_cloud_01.png", width= 208, height = 79, type=1))
        self.plataform_list.append(Plataform(x = 40, y= 540,path="assets\plataform\lvl03\plataform_cloud_02.png", width= 176, height = 70, type=1))
        self.plataform_list.append(Plataform(x = 308, y= 620,path="assets\plataform\lvl03\plataform_cloud_02.png", width= 176, height = 70, type=1))
        self.plataform_list.append(Plataform(x = 576, y= 540,path="assets\plataform\lvl03\plataform_cloud_02.png", width= 176, height = 70, type=1))
        self.plataform_list.append(Plataform(x = 630, y= 350,path="assets\plataform\lvl03\plataform_cloud_03.png", width= 208, height = 64, type=1))
        self.plataform_list.append(Plataform(x = 1072, y= 650,path="assets\plataform\lvl03\plataform_cloud_03.png", width= 208, height = 64, type=1))
        self.plataform_list.append(Plataform(x = 214, y= 350,path="assets\plataform\lvl03\plataform_cloud_03.png", width= 208, height = 64, type=1))
        self.plataform_list.append(Plataform(x = 764, y= 155,path="assets\plataform\lvl03\plataform_cloud_03.png", width= 208, height = 64, type=1))
        self.plataform_list.append(Plataform(x = 1002, y= 135,path="assets\plataform\lvl03\plataform_cloud_01.png", width= 208, height = 79, type=1))

        self.static_background = Background(x= 0, y=0, widht=w, height=h, path="assets\maps\\background_03.png")

        self.bullets_player = []
        self.bullets_enemy = []

        self.coin_list = []
        self.coin_list.append(Coin(x= 85, y= 360, frame_animation_ms= 30, move_rate_ms= 30))
        self.coin_list.append(Coin(x= 350, y= 540, frame_animation_ms= 30, move_rate_ms= 30))
        self.coin_list.append(Coin(x= 855, y= 460, frame_animation_ms= 30, move_rate_ms= 30))
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