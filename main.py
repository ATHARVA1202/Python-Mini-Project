import pygame
from fighter import Fighter

pygame.init()          # initializing pygame.

# create game  window
Screen_width = 1200                        # 1000,1200
Screen_height = 800                        # 600, 800

screen = pygame.display.set_mode((Screen_width,Screen_height))
pygame.display.set_caption("")                                    # title for game window 


# set framerate.
clock = pygame.time.Clock()
FPS = 60

# load background image.
background_image = pygame.image.load("mini_project/images/background/background2.jpg").convert_alpha()

# function for drawing background image.
def draw_background():
    scaled_background = pygame.transform.scale(background_image, (Screen_width, Screen_height))            # scaling background image.
    screen.blit(scaled_background, (0,0))         #image will blitted on top left corner so coordinates are (0,0)

# creating two fighters.
fighter_1 = Fighter(150, 400)          # (x, y)
fighter_2 = Fighter(950, 400)

# game loop
run = True  
while run:

    clock.tick(FPS)

    #draw background
    draw_background()

    # move fighters.
    fighter_1.move(Screen_width, Screen_height, screen, fighter_2)
    #fighter_2.move()

    # draw fighter.
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                            # to close the game window.
            run = False

    # update display       (for updating image)
    pygame.display.update()          

# exit pygame
pygame.quit()
