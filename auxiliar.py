import pygame

class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path,columnas,filas,flip=False, step = 1,scale=1):
        lista = []
        surface_imagen = pygame.image.load(path)
        fotograma_ancho = int(surface_imagen.get_width()/columnas)
        fotograma_alto = int(surface_imagen.get_height()/filas)
        fotograma_ancho_scaled = int(fotograma_ancho*scale)
        fotograma_alto_scaled = int(fotograma_alto*scale)
        x = 0
        
        for fila in range(filas):
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                if(scale != 1):
                    surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
                lista.append(surface_fotograma)
        return lista

    @staticmethod
    def getSurfaceFromSeparateFiles(path_format,from_index,quantity,flip=False,step = 1,scale=1,w=0,h=0,repeat_frame=1):
        lista = []
        for i in range(from_index,quantity+from_index):
            path = path_format.format(i)
            surface_fotograma = pygame.image.load(path)
            fotograma_ancho_scaled = int(surface_fotograma.get_rect().w * scale)
            fotograma_alto_scaled = int(surface_fotograma.get_rect().h * scale)
            if(scale == 1 and w != 0 and h != 0):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(w, h)).convert_alpha()
            if(scale != 1):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
            if(flip):
                surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
            
            for i in range(repeat_frame):
                lista.append(surface_fotograma)
        return lista
    
    @staticmethod
    def kill_sprites(bullets_list_player: list, bullets_list_enemy: list, enemies_list: list, coin_list: list, player):

        for bullet in bullets_list_player:
            if bullet.check_collision("enemy", enemies_list, player):
                for enemy in enemies_list:
                    if enemy.hit(bullets_list_player) == 3:
                        player.score += 10
                        enemies_list.remove(enemy)
                bullets_list_player.remove(bullet)

        for coin in coin_list:
            if coin.check_take(player):
                player.score += 25
                coin_list.remove(coin)

        for bullet in bullets_list_enemy:
            if bullet.check_collision("player", enemies_list, player):
                player.hit(bullets_list_enemy, enemies_list)
                bullets_list_enemy.remove(bullet)
       
    @staticmethod
    def bullets(character: str, owner, bullet, bullet_list = list):
        if owner.is_shoot:
            if((owner.tiempo_transcurrido - owner.cooldown_shoot) > owner.interval_shoot):
                owner.cooldown_shoot = owner.tiempo_transcurrido
                if character == "player":
                    bullet_list.append(bullet(owner= character,
                        x_init=owner.rect.centerx +
                        (0.8 * owner.rect.size[0] * owner.direction),
                        y_init=owner.rect.centery,
                        frame_rate_ms=30, move_rate_ms=60,
                        velocity_x=26, p_scale=0.5,
                        direction=owner.direction))
                elif character == "enemy":
                    bullet_list.append(bullet(owner= character,
                        x_init=owner.rect.centerx +
                        (0.8 * owner.rect.size[0] * owner.direction),
                        y_init=owner.rect.centery,
                        frame_rate_ms=30, move_rate_ms=60,
                        velocity_x=16, p_scale=0.4,
                        direction=owner.direction))