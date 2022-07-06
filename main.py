import pygame
from fighter import Fighter

pygame.init()          # initializing pygame.

# create game  window
Screen_width = 1200                        # 1000,1200
Screen_height = 800                        # 600, 800

screen = pygame.display.set_mode((Screen_width,Screen_height))
pygame.display.set_caption("Street Fighter")                                    # title for game window 


# set framerate.
clock = pygame.time.Clock()
FPS = 60


# define fighter variables.
warrior_size = 162
warrior_scale = 5
warrior_offset = [72, 46]
warrior_data = [warrior_size, warrior_scale, warrior_offset]
wizard_size = 250
wizard_scale = 4
wizard_offset = [112, 97]
wizard_data = [wizard_size, wizard_scale, wizard_offset]


# load background image.
background_image = pygame.image.load("background/background2.jpg").convert_alpha()

#load spritesheets.
warrior_sheet = pygame.image.load("Spritesheet/Warrior/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("Spritesheet/Wizard/wizard.png").convert_alpha()

# define number of steps in each animation.
warrior_animation_steps = [10, 8, 1, 7, 7, 3, 7]
wizard_animation_steps = [8, 8, 1, 8, 8, 3, 7]

# function for drawing background image.
def draw_background():
    scaled_background = pygame.transform.scale(background_image, (Screen_width, Screen_height))            # scaling background image.
    screen.blit(scaled_background, (0,0))         #image will blitted on top left corner so coordinates are (0,0)


# function for health bar

def health_bar(health, x, y):
    health_drop = health /100
    pygame.draw.rect(screen,(0,0,0),(x-1.5, y-1.5 , 554 ,54))
    pygame.draw.rect(screen,(255,0,0),(x, y , 550 ,50))
    pygame.draw.rect(screen,(0,255,0),(x, y , 550 * health_drop,50))


# creating two fighters.
fighter_1 = Fighter(1, 150, 400, False, warrior_data, warrior_sheet, warrior_animation_steps)          # (x, y)
fighter_2 = Fighter(2, 950, 400,  True, wizard_data, wizard_sheet, wizard_animation_steps)

# game loop
run = True  
while run:

    clock.tick(FPS)

    #draw background
    draw_background()

    #players health
    health_bar(fighter_1.health,20,25)
    health_bar(fighter_2.health,630,25)


        # move fighters
    fighter_1.move(Screen_width, Screen_height, screen, fighter_2)
    fighter_2.move(Screen_width, Screen_height, screen, fighter_1)


    #update fighters
    fighter_1.update()
    fighter_2.update()
 

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
