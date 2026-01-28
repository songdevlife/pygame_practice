import random
import pygame

pygame.init()

# Screen size

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# Title
pygame.display.set_caption("Gonie's Game")


# FPS
clock = pygame.time.Clock()


# load background imamge

background = pygame.image.load("C:\\Users\\User\\Downloads\\game_project\\pygame_basic\\background.png")

# load character iammge

character = pygame.image.load("C:\\Users\\User\\Downloads\\game_project\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_height / 2)
character_y_pos = screen_height - character_height

# Character movement
to_x = 0
to_y = 0

# movement speed
character_speed = 0.7


# Enermy character

enermy = pygame.image.load("C:\\Users\\User\\Downloads\\game_project\\pygame_basic\\enermy.png")
enermy_size = enermy.get_rect().size
enermy_width = enermy_size[0]
enermy_height = enermy_size[1]
enermy_x_pos = random.randint(0, screen_width - enermy_width)
enermy_y_pos = 0

enermy_speed = 10

# Running with while loop

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
        

    enermy_y_pos += enermy_speed

    if enermy_y_pos > screen_height:
        enermy_y_pos = 0
        enermy_x_pos = random.randint(0, screen_width - enermy_width)

    # collision for rect information update
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enermy_rect = enermy.get_rect()
    enermy_rect.left = enermy_x_pos
    enermy_rect.top = enermy_y_pos

    # Chcking Collision
    if character_rect.colliderect(enermy_rect):
        print("Collision!")
        running = False

    screen.blit(background, (0,0))

    screen.blit(character, (character_x_pos, character_y_pos))

    screen.blit(enermy, (enermy_x_pos , enermy_y_pos))

    pygame.display.update()

# End game
pygame.quit()

    