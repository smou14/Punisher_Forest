import random
import pygame
pygame.init()
# Load the images and create Surface objects
grass_img = pygame.image.load("grass.png")
power_flower_img = pygame.image.load("power_flower.png")
tree_img = pygame.image.load("tree.png")

# Create Surface objects for each image

class GridHandler:
    def __init__(self,width,height,screen):
        self.width = width
        self.height = height
        self.square_size = 40
        self.screen = screen
        self.grass_surface = grass_img.convert()
        self.power_flower_surface = power_flower_img.convert()
        self.tree_surface = tree_img.convert()
        self.object_rects = []


    def create_new_grid(self,width, height):
        tiles = ["grass","tree","power_flower"]
        rows = width
        columns = height
        grid = []
        for i in range(columns):
            row = []
            for j in range(rows):
                num = random.randint(0,1000)
                value = random.choice(tiles)
                if num > 30 and value == "power_flower":
                    value = "grass"
                row.append(value)
            grid.append(row)
        return grid


    def draw(self, grid):
        self.object_rects = []
        for row in range(self.height):
            for col in range(self.width):
                current_tile = grid[row][col]

            # Compute the position of the square on the screen
                x = col * self.square_size
                y = row * self.square_size

            # Draw the square
                if current_tile == "grass":
                    self.screen.blit(self.grass_surface, (x, y))
                elif current_tile == "power_flower":
                    self.screen.blit(self.power_flower_surface, (x, y))
                elif current_tile == "tree":
                    self.object_rects.append(pygame.Rect(x ,y ,40 ,40))
                    self.screen.blit(self.tree_surface, (x, y))



#pygame.draw.rect(self.screen, color, (x, y, self.square_size, self.square_size))