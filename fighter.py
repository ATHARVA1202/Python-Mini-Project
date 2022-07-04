from turtle import Screen
import pygame

#from mini_project.main import Screen_width 

class Fighter():
    def __init__ (self, x ,y):                    # x and y are coordinates (location)
        self.rect = pygame.Rect((x , y, 120, 300))           # 120 = width , 220 = height.
        
    def move(self, screen_width):
        SPEED = 10                       # players speed.
        dx = 0                           # delta variables.
        dy = 0

        # keypress
        key = pygame.key.get_pressed()

        # movement.
        if key[pygame.K_a]:                # a is used to go left
            dx = -SPEED                    # since 'a' goes left speed decreases  ' - '
        if key[pygame.K_d]:                # d is used to go right
            dx = SPEED

        #ensure player stays on screen.
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right



        # update player position.
        self.rect.x += dx
        self.rect.y += dy
        

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)           # creating rectangle on game window.
