import pygame
import math
pygame.init()
class Wolves:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 20,20)
        self.health = 10
        self.x_dist_to_player = 0
        self.y_dist_to_player = 0
        self.screen = screen

    def update(self, player_x, player_y):
        self.x_dist_to_player = player_x - self.x
        self.y_dist_to_player = player_y - self.y
        distance_to_player = math.sqrt(self.x_dist_to_player**2 + self.y_dist_to_player**2)

        if distance_to_player > 0:
            normalized_x_dist = self.x_dist_to_player / distance_to_player
            normalized_y_dist = self.y_dist_to_player / distance_to_player
            speed = 2  # Adjust this value to set the desired speed

            self.x += normalized_x_dist * speed
            self.y += normalized_y_dist * speed
            self.rect = pygame.Rect(self.x, self.y, 20,20)

    def draw(self):
        pygame.draw.rect(self.screen, (255,0,0), self.rect)