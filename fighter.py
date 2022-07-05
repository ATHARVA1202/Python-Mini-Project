import pygame

 

class Fighter():
    def __init__ (self, x ,y, flip, data, sprite_sheet, animation_steps):                    # x and y are coordinates (location)
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip     
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0    # 0 : run 2:jump 3:attack1 4:attack2 5:hit 6:death
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect((x , y, 120, 300))           # 120 = width , 220 = height.
        self.vel_y = 0                                  # for jumping.
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100       #player health
        self.update_time = pygame.time.get_ticks()
        self.run = False
        self.attack_cooldown = 0
        self.hit = False
        self.alive = True




    def load_images(self, sprite_sheet, animation_steps):
        #extract images from spritesheet.
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                 temp_img = sprite_sheet.subsurface(x*self.size, y*self.size, self.size, self.size)
                 temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.image_scale,self.size * self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list 
            
        
        
        
    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10                       # players speed.
        GRAVITY = 2.5
        dx = 0                           # delta variables.
        dy = 0
        self.run = False
        self.attack_type = 0
        # keypress
        key = pygame.key.get_pressed()

        # can only perform other functions if not currently attcking.
        if self.attacking == False:

            # movement.
            if key[pygame.K_a]:
                dx = -SPEED
                self.run = True
            if key[pygame.K_d]:
                dx = SPEED           
                self.run = True
            #jump
            if key[pygame.K_SPACE] and self.jump == False:
                self.vel_y = -30                         # height of jump.
                self.jump = True        
            #attack.
            if key[pygame.K_c] or key[pygame.K_v]:
                self.attack(surface, target)
                # determine which attack was used.
                if key[pygame.K_c]:
                    self.attack_type = 1
                if key[pygame.K_v]:
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

        if self.attack_cooldown > 0:
            self.attack_cooldown-=1

    def attack(self, surface, target):
        if self.attack_cooldown == 0:
            self.attacking = True
            attacking_rect = pygame.Rect(self.rect.centerx - (2 *self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
            if attacking_rect.colliderect(target.rect):
                target.health -=  10
                target.hit = True
            
        

    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        # pygame.draw.rect(surface, (255, 0, 0), self.rect)           # creating rectangle on game window.
        surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))

    #update fighter
    def update(self):
        #player's current movement
        if self.health <=0:
            self.alive = False
            self.update_action(6)
        elif self.hit == True:
            self.update_action(5)
        elif self.attacking == True:
            if self.attack_type == 1:
                self.update_action(3)
            elif self.attack_type == 2:
                self.update_action(4)
        elif self.jump == True:
            self.update_action(2)
        elif self.run == True:
            self.update_action(1)
        else:
            self.update_action(0)


        animation_cooldown = 50 
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index +=1
            self.update_time = pygame.time.get_ticks()
        #if animation has finished
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
            #if attack has finished
                if self.action == 3 or self.action == 4:
                    self.attacking = False
                    self.attack_cooldown = 25
                if self.action == 5:
                    self.hit = False
                    self.attacking = False
                    self.attack_cooldown = 20



    def update_action(self, curr_action):
        if curr_action != self.action:
            self.action = curr_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
