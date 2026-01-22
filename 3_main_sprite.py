import pygame

pygame.init()

#Screen Size

screen_width = 480
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))

# Background
background = pygame.image.load("C:\\Users\\User\\Downloads\\game_project\\pygame_basic\\background.png")


# Load Character 
character = pygame.image.load("C:\\Users\\User\\Downloads\\game_project\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height


# Game title
pygame.display.set_caption("Gonie's Game")


# Event Loop while game running

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))
    
    screen.blit(character,(character_x_pos,character_y_pos))
    
    pygame.display.update()
# End Game
pygame.quit()