import pygame
xp_icon_img = pygame.image.load("xp_icon.png")
class XP_bar:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(self.x, self.y, 200, 20)
        self.screen = screen
        self.font = pygame.font.Font(None, 30)
        self.xp_icon_surface = xp_icon_img.convert()

    def draw(self, xp_level):
        #impliment xp bar, similar to health_bar
        self.rect = pygame.rect.Rect(self.x, self.y, 5 + xp_level, 20)
        xp_text = self.font.render(str(xp_level), True, (0,100,20))
        xp_rect = xp_text.get_rect()
        xp_rect.center = self.rect.center
        pygame.draw.rect(self.screen, (0,255,0), self.rect)
        self.screen.blit(xp_text, xp_rect)
        self.screen.blit(self.xp_icon_surface, (self.x - 50, self. y))



class Level_count:
    def __init__(self, x,y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.font = pygame.font.Font(None, 30)
        self.rect = pygame.rect.Rect(self.x, self.y, 48,48)

    def draw(self, level):
        level_text = self.font.render(f"Level: {str(level)}", True, (255,255,255))
        self.screen.blit(level_text, self.rect)