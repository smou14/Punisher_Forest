import pygame
pygame.init()
class CollisionHandler:
    def __init__(self):
        pass

    def Is_player_collided(self, player_rect, object_rects):
        if player_rect.collidelist(object_rects) != -1:
            return True
        else:
            return False