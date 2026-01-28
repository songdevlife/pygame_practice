import pygame
import random

pygame.init()


# Screen Size
screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width,screen_height))

#FPS
clock = pygame.time.Clock()

# Title
pygame.display.set_caption("Gonie's Game")

# Load background
background = pygame.image.load("C:\\Users\\User\\Downloads\\game_project\\pygame_basic\\background.jpg")

# Load Character
character = pygame.image.load("C:\\Users\\User\\Downloads\\game_project\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_height / 2)
character_y_pos = screen_height - character_height

# Character movement
to_x = 0

# Movement speed
movement_speed = 10


# enermy
enermy = pygame.image.load("C:\\Users\\User\\Downloads\\game_project\\pygame_basic\\ddong.png")
enermy_size = enermy.get_rect().size
enermy_width = enermy_size[0]
enermy_height = enermy_size[1]
enermy_x_pos = random.randint(0,screen_width - enermy_width)
enermy_y_pos = 0
enermy_speed = 10

# Running while loop

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= movement_speed
            elif event.key == pygame.K_RIGHT:
                to_x += movement_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enermy_y_pos += enermy_speed

    if enermy_y_pos > screen_height:
        enermy_y_pos = 0
        enermy_x_pos = random.randint(0,screen_width - enermy_width)


    # Collision for rect information update
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enermy_rect = enermy.get_rect()
    enermy_rect.left = enermy_x_pos
    enermy_rect.top = enermy_y_pos

    # Checking collision
    if character_rect.colliderect(enermy_rect):
        print("Collision !!")
        running = False


    screen.blit(background , (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enermy, (enermy_x_pos,enermy_y_pos))


    pygame.display.update()


#End game
pygame.quit()