import pygame

 

class Fighter():
    def __init__ (self, x ,y):                    # x and y are coordinates (location)
        self.rect = pygame.Rect((x , y, 120, 300))           # 120 = width , 220 = height.
        self.vel_y = 0                                  # for jumping.
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100       #player health
        self.flip = False
        
    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10                       # players speed.
        GRAVITY = 2.5
        dx = 0                           # delta variables.
        dy = 0

        # keypress
        key = pygame.key.get_pressed()

        # can only perform other functions if not currently attcking.
        if self.attacking == False:

            # movement.
            if key[pygame.K_a]:
                dx = -SPEED
            if key[pygame.K_d]:
                dx = SPEED           
            #jump
            if key[pygame.K_SPACE] and self.jump == False:
                self.vel_y = -30                         # height of jump.
                self.jump = True        
            #attack.
            if key[pygame.K_r] or key[pygame.K_t]:
                self.attack(surface, target)
                # determine which attack was used.
                if key[pygame.K_r]:
                    self.attack_type = 1
                if key[pygame.K_t]:
                    self.attack_type = 2
        
        
        # applying gravity.
        self.vel_y += GRAVITY
        dy += self.vel_y

        #ensure player stays on screen.
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 100:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 100 - self.rect.bottom

        # update player position.
        self.rect.x += dx
        self.rect.y += dy

        #Flipping player facing side
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        # print(self.flip)


    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 *self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -=  10
            
#
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
        

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)           # creating rectangle on game window.

 
