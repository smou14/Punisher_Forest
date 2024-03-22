import pygame
from player import Player
from grid_handler import GridHandler
from ui_elements import XP_bar
from ui_elements import Level_count
from enemy_handler import EnemyHandler


pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
done = False
player = Player(480, 400, 100, screen)
gridhandler = GridHandler(48,27,screen)
enemyhandler = EnemyHandler(screen)
xp_bar = XP_bar(1700,10, screen)
level_count = Level_count(1700, 30, screen)
grid = gridhandler.create_new_grid(48, 27)
enemies = enemyhandler.Create_enemy_list("wolves", 10)

def update():
    screen.fill((7, 20, 5))
    gridhandler.draw(grid)
    object_rects = gridhandler.object_rects
    player.update(object_rects)
    player.draw()
    xp_bar.draw(player.xp)
    level_count.draw(player.level)
    enemyhandler.update_list(player.x, player.y)
    player.xp += 1
    pygame.display.flip()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    update()
    clock.tick(30)

pygame.quit()