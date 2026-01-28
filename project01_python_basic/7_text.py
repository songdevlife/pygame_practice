import pygame

pygame.init()

#Screen Size
screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width,screen_height))

# Title
pygame.display.set_caption("Gonie's game")

#FPS
clock = pygame.time.Clock()


#load background 
background = pygame.image.load("C:\\Users\\User\\Downloads\\game_project\\pygame_basic\\background.png")

# load character image
character = pygame.image.load("C:\\Users\\User\\Downloads\\game_project\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_height / 2)
character_y_pos = screen_height - character_height

# Character movement
to_x = 0
to_y = 0

# Movement speed
character_speed = 0.7


# Enermy character
enermy = pygame.image.load("C:\\Users\\User\\Downloads\\game_project\\pygame_basic\\enermy.png")
enermy_size = enermy.get_rect().size
enermy_width = enermy_size[0]
enermy_height = enermy_size[1]
enermy_x_pos = (screen_width / 2) - (enermy_width / 2)
enermy_y_pos = (screen_height / 2)- (enermy_height / 2)

# Defintion Font
game_font = pygame.font.Font(None, 40)

# Total Time
total_time = 10

# Calculate Game time
start_ticks = pygame.time.get_ticks()


#Running while loop

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
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
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

    # Collision for rect information update
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enermy_rect = enermy.get_rect()
    enermy_rect.left = enermy_x_pos
    enermy_rect.top = enermy_y_pos


    # Checking collision
    if character_rect.colliderect(enermy_rect):
        print("Collision!!")
        running = False

    screen.blit(background, (0,0))

    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enermy, (enermy_x_pos,enermy_y_pos))

    # Timer
    # Play time
    elapsed_time  = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10,10))

    if total_time - elapsed_time <= 0:
        print("Time out!!")
        running = False


    pygame.display.update()

# Delay before End
pygame.time.delay(2000)


#End game
pygame.quit()