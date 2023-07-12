# def jump(self, on_off = True) -> None:
    #     '''
        
        
        
    #     '''
    #     if on_off and not self.__is_jumping and not self.__falling:
    #         self.__y_start_jump = self.__rect.y
    #         self.__move_x = int(self.__move_x / 2)
    #         if self.__direction == DIRECTION_R:
    #             self.__move_y = self.__power_jumping
    #             self.__actual_animation = "self.__jump_r"
    #         else:
    #             self.__move_y = -self.__power_jumping
    #             self.__actual_animation = "self.__jump_l"
    #         self.__frame = 0
    #         self.__is_jumping = True

    #     if not on_off:
    #         self.__is_jumping = on_off
    #         self.__stay()

# def movement_random(self) -> None:
    #     '''
        
        
        
    #     '''
    #     if self.__direction == DIRECTION_R:
    #         self.walk(self.__direction)
    #         if self.__rect.x >= (ANCHO_VENTANA) - 20:
    #             self.attack(self.__direction)

    #     elif(self.__direction == DIRECTION_L):
    #         self.walk(self.__direction)
    #         if self.__rect.x == 40:
    #             self.attack(self.__direction)

# def movement_to_player(self, list_player):
    #     '''
        
        
        
    #     '''
    #     for player in list_player:
    #         if self.__rect_x <= player.rect.x:
    #             self.__orientation = DIRECTION_R
    #             self.__actual_animation = self.__stay_r
    #         if self.__rect_x > player.rect.x:
    #             self.__orientation = DIRECTION_L
    #             self.__actual_animation = self.__stay_l
    