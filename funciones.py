import json
from constantes import *
from enemies import Enemy
from plataform import Plataform
from coin import Coin
from player import Player
from background import Background


def leer_archivo(path_completo: str, level: str) -> json:
    '''
    Lee el archivo .json por ruta

    Parametros: ruta en str

    Retorna la lectura del json
    '''

    with open(path_completo, "r") as archivo:
        return list[dict](json.load(archivo)[level])

def lista_dict(game_list: list[dict], key: str):
    '''
    Lee una lista con diccionarios y retorna los valores de la clave pasada por parametro, correspondi-
    ente a: enemigos, plataformas, monedas, background, jugador.
    
    Paramentros: list[dict] (una lista con diccionario dentro), str (es el nombre de la clave a leer)
    
    Retorna los valores de clave deseada
    '''
    copy_list = game_list[:]

    for elements in copy_list:
        for clave, valor in elements.items():
            if clave == key:
                return valor

def list_enemies(game_list: list[dict]):
    '''
    Lee la lista que contiene diccionarios correspondientes a los enemigos con su respectiva informacion,
    almacenandolas en una lista usando la clase Enemy y asignando a los parametros de la misma los valo-
    res pertinentes
    
    Parametro: list[dictionary] (informacion del .json que corresponde a los enemigos)
    
    Retorna una lista guardando la clase de enemigos, con su informacion pertinente
    '''
    copy_list = game_list
    direction_enemy = None
    enemy_list = []
    for enemies in copy_list:
        if enemies["direction"] == "DIRECTION_L":
            direction_enemy = DIRECTION_L
        elif enemies["direction"] == "DIRECTION_R":
            direction_enemy = DIRECTION_R
        else:
            direction_enemy = None
        enemy_list.append(Enemy(owner=enemies["type"],
                                x=enemies["x"],
                                y=enemies["y"],
                                hitbox_h=enemies["hitbox_h"],
                                hitbox_w=enemies["hitbox_w"],
                                speed_walk=enemies["speed_walk"],
                                gravity=enemies["gravity"],
                                frame_animation_ms=enemies["frame_animation_ms"],
                                move_rate_ms=enemies["move_rate_ms"],
                                direction=direction_enemy,
                                count_cd=enemies["count_cd"]))

    return enemy_list

def list_plataform(game_list: list[dict]):
    '''
    Lee la lista que contiene diccionarios correspondientes a las plataformas con su respectiva informa-
    cion, almacenandolas en una lista usando la clase Plataform y asignando a los parametros de la misma
    los valores pertinentes
    
    Parametro: list[dictionary] (informacion del .json que corresponde a las monedas)
    
    Retorna una lista que guarda la clase de plataformas, con su informacion pertinente
    '''
    copy_list = game_list
    plataform_list = []
    for plataforms in copy_list:
        plataform_list.append(Plataform(x=plataforms["x"],
                                        y= plataforms["y"],
                                        path=plataforms["path"],
                                        width=plataforms["width"],
                                        height= plataforms["height"],
                                        type=plataforms["type"]))
    return plataform_list

def list_coins(game_list: list[dict]):
    '''
    Lee la lista que contiene diccionarios correspondientes a las monedas con su respectiva informacion,
    almacenandolas en una lista usando la clase Coin y asignando a los parametros de la misma los valores
    pertinentes

    Parametro: list[dictionary] (informacion del .json que corresponde a las plataformas)
    
    Retorna una lista que guarda la clase de las monedas con su informacion pertinente
    '''
    copy_list = game_list
    coins_list = []
    for coins in copy_list:
        coins_list.append(Coin(x=coins["x"],
                               y=coins["y"],
                               frame_animation_ms=coins["frame_animation_ms"],
                               move_rate_ms=coins["move_rate_ms"]))

    return coins_list

def player_level(game_list: list[dict]):
    '''
    Lee la lista que contiene diccionarios correspondientes al jugador con su respectiva informacion,
    almacenandola en una lista usando la clase Player y asignando a los parametros de la misma los valo-
    res pertinente
    
    Parametro: list[dictionary] (informacion del .json que corresponde a las plataformas)
    
    Retorna una variable que guarda la clase del jugador con la informacion pertinente
    '''
    copy_list = game_list
    player_coor = None
    for coor in copy_list:
        player_coor = Player(x=coor["x"],
                             y=coor["y"],
                             speed_walk=coor["speed_walk"],
                             gravity=coor["gravity"], jump=coor["jump"],
                             animation_rate_ms=coor["animation_rate_ms"],
                             move_rate_ms=coor["move_rate_ms"],
                             jump_height=coor["jump_height"],
                             interval_time_jump=coor["interval_time_jump"])

    return player_coor

def background_level(game_list: list[dict], w, h):
    '''
    Lee la lista que contiene diccionarios correspondientes al background con su respectiva informacion,
    almacenandola en una lista usando la clase Background y asignando a los parametros de la misma los 
    valores pertinentes
    
    Parametro: list[dictionary] (informacion del .json que corresponde al background)
    
    Retorna una variable que guarda la informacion del background
    '''
    copy_list = game_list
    background = None
    for coor in copy_list:
        background = Background(x=coor["x"],
                                y=coor["y"],
                                widht=w,
                                height=h,
                                path=coor["path"])
    
    return background

def select_level(level_select: str):
    '''
    Lee la lista que contiene diccionarios correspondientes al nivel con su respectiva informacion,
    usando la funcion leer_archivo, retornandolo.
    
    Parametro: str (nivel que queremos ejecutar)
    
    Retorna la lista con diccionarios correspondientes al nivel
    '''
    return leer_archivo("levels.json", level_select)
    
