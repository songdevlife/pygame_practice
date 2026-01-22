import pygame

pygame.init()

#Screen Size

screen_width = 480
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))

# Background
background = pygame.image.load("C:\\Users\\User\\Downloads\\game_project\\pygame_basic\\background.png")

# Game title
pygame.display.set_caption("Gonie's Game")


# Event Loop while game running

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))
    pygame.display.update()

# End Game
pygame.quit()