import pygame

pygame.init() #initialised (must be set before doing something)

# Screen size

screen_width = 480 # width
screen_height = 640 # height

screen = pygame.display.set_mode((screen_width, screen_height))

# Screen title
pygame.display.set_caption("Gonie's Game")


# Event Loop

running = True # Does game run?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# End pygame
pygame.quit()
