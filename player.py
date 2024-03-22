import pygame
from collision_handler import CollisionHandler
collisionhandler = CollisionHandler()
pygame.init()
player_img = pygame.image.load("player_simple.png")
class Player:
    def __init__(self,x ,y ,health ,screen):
        self.x = x
        self.y = y
        self.health = health
        self.hp_rect = pygame.Rect(self.x, self.y - 15, self.health/2, 10)
        self.width = 40
        self.height = 40
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.player_surface = player_img.convert()
        self.xp = 0
        self.level = 0

    def move_to(self,new_x,new_y):
        self.x = new_x
        self.y = new_y


    def FilterList(self, object_rects, player_rect, max_distance):
        filtered_list = []

        for rect in object_rects:
            dx = player_rect.centerx - rect.centerx
            dy = player_rect.centery - rect.centery
            squared_distance = dx ** 2 + dy ** 2

            if squared_distance < max_distance ** 2:
                filtered_list.append(rect)

        return filtered_list

    def CheckForColliding(self, object_rects, direction):
        # Define the test_rect based on the given direction
        if direction == "up":
            test_rect = pygame.Rect(self.x, self.y - 10, self.width, self.height)
        elif direction == "down":
            test_rect = pygame.Rect(self.x, self.y + 10, self.width, self.height)
        elif direction == "right":
            test_rect = pygame.Rect(self.x + 10, self.y, self.width, self.height)
        elif direction == "left":
            test_rect = pygame.Rect(self.x - 10, self.y, self.width, self.height)

        filtered_list = self.FilterList(object_rects, self.rect, 100)
        return collisionhandler.Is_player_collided(test_rect, filtered_list)

    def update(self, object_rects):

        speed = 10
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and not self.CheckForColliding(object_rects, "up"):
            self.y -= speed
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and not self.CheckForColliding(object_rects, "down"):
            self.y += speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not self.CheckForColliding(object_rects, "right"):
            self.x += speed
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not self.CheckForColliding(object_rects, "left"):
            self.x -= speed


        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.update_hp()
        self.draw_hp_bar()
        self.ShouldLevelUp(self.xp)


    def update_hp(self):
        self.hp_rect = pygame.Rect(self.x, self.y - 15, self.health/2, 10)


    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), self.rect)
        self.screen.blit(self.player_surface, (self.x, self.y))

    def draw_hp_bar(self):
        green_health = self.health * 2.55
        red_health = 255 - green_health
        pygame.draw.rect(self.screen, (red_health,green_health,0), self.hp_rect)


    def ShouldLevelUp(self, xp):
        if xp > 200:
            self.level += 1
            self.xp = 0