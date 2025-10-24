import pygame
from constantes import *


class Auxiliar:

    @staticmethod
    
    def getSurfaceFromSeparateFiles(path_format,from_index,quantity,flip=False, scale=1,w=0,h=0,repeat_frame=1):
        '''
        Obtiene la superficie de las imagenes separadas creando copias de las mismas, almacenando la cantidad de imagenes 
        solicitadas por parametro en una lista.

        Parámetros: str (ruta imagen), int (numero de la imagen), int (cantidad total de las imagenes), bool (orientacion de la imagen),
        int (escalado de la imagen), int (ancho de la imagen), int (alto de la imagen), int (nu)

        Retorna una lista con las imagenes.
        '''
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
        '''
        Remueve los elementos de la lista (sean proyectiles o monedas) cuando colisionan contra un jugador (proyectiles 
        y monedas) o enemigo (proyectiles).
        
        Parametros: list (proyectiles del jugador), list (proyectiles del enemigo), list (lista de enemigos), list (lista
        de monedas), any (atributo que almacena la informacion del jugador)
        
        No retorna nada
        '''
        
        for bullet in bullets_list_player:
            if bullet.check_collition("enemy", enemies_list, player):
                for enemy in enemies_list:
                    if enemy.getSelfHit() == 3:
                        player.score += 10
                        enemies_list.remove(enemy)
                bullets_list_player.remove(bullet)

        for coin in coin_list:
            if coin.check_take(player):
                player.score += 25
                player.have_coins += 1
                coin_list.remove(coin)

        for bullet in bullets_list_enemy:
            if bullet.check_collition("player", enemies_list, player):
                player.hit(bullets_list_enemy, enemies_list)
                bullets_list_enemy.remove(bullet)
    
    @staticmethod
    def bullets(character: str, owner, bullet, bullet_list: list):
        '''
        Agrega a una lista los proyectiles cada vez que el jugador o enemigo dispare.

        Parametros: str (si es jugador o enemigo), any (atributo que almacena informacion del jugador o enemigo),
        any (corresponde a la clase del proyectil), list (lista donde se almacenarán los proyectiles)
        
        Retorna una lista que contiene los proyectiles cada vez disparados por el jugador o enemigo.
        '''
        from enemies import Enemy
        from player import Player
        if owner.is_shoot:
            if type(owner) == Player:
                if((owner.tiempo_transcurrido - owner.cooldown_shoot) > owner.interval_shoot):
                    owner.cooldown_shoot = owner.tiempo_transcurrido
                    bullet_list.append(bullet(owner= character,
                        x_init=owner.rect.centerx +
                        (0.8 * owner.rect.size[0] * owner.direction),
                        y_init=owner.rect.centery,
                        frame_rate_ms=30, move_rate_ms=60,
                        velocity_x=26, p_scale=0.5,
                        direction=owner.direction))
            elif type(owner) == Enemy:
                if owner.contador == owner.count_cd:
                    bullet_list.append(bullet(owner= character,
                        x_init=owner.rect.centerx +
                        (0.8 * owner.rect.size[0] * owner.direction),
                        y_init=owner.rect.centery,
                        frame_rate_ms=30, move_rate_ms=60,
                        velocity_x=16, p_scale=0.4,
                        direction=owner.direction))
            return bullet_list