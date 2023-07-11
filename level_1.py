from plataform import Plataform
from player import Player
from constantes import *
from enemies import Enemy
from background import Background
from gui_form import Form
from bullets import Bullet

class LevelGame1(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.static_background = Background(x= 0, y=0, widht=w, height=h, path="assets_2\locations\set_bg_01\\forest\\all.png")

        self.player_1 = Player(x= 0, y = 500, speed_walk= 8, gravity=10, jump=30, animation_rate_ms=35, move_rate_ms=100, jump_height=150, interval_time_jump = 300)
        
        self.enemy_1= Enemy(x= 0, y = 500,hitbox_h=170, hitbox_w=110, speed_walk= 8, gravity=10,frame_animation_ms=25, move_rate_ms=70)
        
        self.plataform_list = []
        self.plataform_list.append(Plataform(x = 0, y= 520, width= 600, height = 69, type=1))

        self.bullet_list = []
    
    def bullets_shoot(self):
        if self.player_1.is_shoot == True:
            self.bullet_list.append(Bullet(x_init=self.player_1.rect.centerx, y_init=self.player_1.rect.centery, frame_rate_ms=40, move_rate_ms=80, velocity_x=1, p_scale=0.5, direction=self.player_1.direction))

    def update(self, list_events, keys, delta_ms):

        for bullet in self.bullet_list:
                bullet.update(delta_ms)

        self.bullets_shoot()

        self.player_1.events(delta_ms, keys)
        self.player_1.update(delta_ms, self.plataform_list)

        self.enemy_1.update(delta_ms)

    def draw(self):
        super().draw()
        self.static_background.draw(self.surface)

        for plataform in self.plataform_list:
            plataform.draw(self.surface)

        for bullet in self.bullet_list:
            bullet.draw(self.surface)

        self.player_1.draw(self.surface)

        self.enemy_1.draw(self.surface)

        