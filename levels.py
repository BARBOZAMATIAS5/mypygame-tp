from funciones import *
from constantes import *
from gui_form import Form
from bullets import Bullet
from auxiliar import Auxiliar

class LevelGame(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active, level):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        
        self.player_1 = player_level(lista_dict(select_level(level), "player"))

        self.enemies_list = list_enemies(lista_dict(select_level(level), "enemies"))
        self.plataform_list = list_plataform(lista_dict(select_level(level), "plataform"))
        self.coin_list = list_coins(lista_dict(select_level(level), "coins"))

        self.static_background = background_level(lista_dict(select_level(level), "background"), w=w, h=h)

        self.bullets_player = []
        self.bullets_enemy = []

    def update(self, keys, delta_ms):

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
            coin.update(delta_ms)

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