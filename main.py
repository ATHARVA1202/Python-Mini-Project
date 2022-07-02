import pygame

pygame.init()          # initializing pygame.

# create game  window
Screen_width = 1200                        
Screen_height = 800                        

screen = pygame.display.set_mode((Screen_width,Screen_height))
pygame.display.set_caption("Street Fighter")                                    # title for game window 

# game loop
run = True  
while run:

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                            # to close the game window.
            run = False

    # update display       (for updating image)
    pygame.display.update()          

# exit pygame
pygame.quit()