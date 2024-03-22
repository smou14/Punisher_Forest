import pygame
from enemies import *
import random
pygame.init()
class EnemyHandler:
    def __init__(self, screen):
        self.Enemy_list = []
        self.screen = screen

    def Create_enemy_list(self, type_of_enemy, number):
        for i in range(0,number):
            if type_of_enemy == "wolves":
                self.Enemy_list.append(Wolves(random.randint(0,1920), random.randint(0,1080), self.screen))
        return self.Enemy_list

    def update_list(self, px, py):
        for enemy in self.Enemy_list:
            enemy.update(px, py)
            enemy.draw()