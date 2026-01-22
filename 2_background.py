import pygame

pygame.init()

# Screen size
screen_width = 480
screen_hegith = 680
screen = pygame.display.set_mode((screen_width, screen_hegith))

# Load background images
background = pygame.image.load("C:\\Users\\User\\Downloads\\game_project\\pygame_basic\\background.png")


# Game Title

pygame.display.set_caption("Gonie's Game")

# Event Loop

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0,0))
    pygame.display.update()
# End game
pygame.quit()