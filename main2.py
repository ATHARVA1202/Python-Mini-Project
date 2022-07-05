import pygame
from fighter import Fighter

pygame.init()          # initializing pygame.

# create game  window
Screen_width = 1200                        # 1000,1200
Screen_height = 800                        # 600, 800

screen = pygame.display.set_mode((Screen_width, Screen_height))
# title for game window
pygame.display.set_caption("")


# set framerate.
clock = pygame.time.Clock()
FPS = 60

# load background image.
background_image = pygame.image.load("background/background2.jpg").convert_alpha()


#Size
warrior_size = 162 
warrior_data = [warrior_size]
wizard_size =200
wizard_data = [wizard_size]

# load Spritesheets
warrior_sheet = pygame.image.load('Spritesheet/Warrior/warrior.png').convert_alpha()
wizard_sheet = pygame.image.load('Spritesheet/Wizard/wizard.png').convert_alpha()

#steps in animation
warrior_steps = [10, 8, 1, 7, 7, 3, 7]
wizard_steps = [8, 8, 1, 8, 8, 3, 7]

# function for drawing background image.
def draw_background():
    # scaling background image.
    scaled_background = pygame.transform.scale(
        background_image, (Screen_width, Screen_height))
    # image will blitted on top left corner so coordinates are (0,0)
    screen.blit(scaled_background, (0, 0))


# func for healthbar
def health_bar(health, x, y):
    health_drop = health / 100
    pygame.draw.rect(screen, (0, 0, 0), (x-2, y-2, 554, 54))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 550, 50))
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 550 * health_drop, 50))


# creating two fighters.
fighter_1 = Fighter(150, 400,warrior_data,warrior_sheet , warrior_steps)          # (x, y)
fighter_2 = Fighter(950, 400, wizard_data, wizard_sheet,wizard_steps)

# game loop
run = True
while run:

    clock.tick(FPS)

    # draw background
    draw_background()

    # players health
    health_bar(fighter_1.health, 20, 25)
    health_bar(fighter_2.health, 630, 25)

    # move fighters.
    fighter_1.move(Screen_width, Screen_height, screen, fighter_2)
    # fighter_2.move()

    # draw fighter.
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # event handler
    for event in pygame.event.get():
        # to close the game window.
        if event.type == pygame.QUIT:
            run = False

    # update display       (for updating image)
    pygame.display.update()

# exit pygame
pygame.quit()
