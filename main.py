import pygame, random, time, sys

pygame.init()

#screen info
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

#game variables
clock = pygame.time.Clock()
grid_size = 50
food_spawn = True
food_pos = [random.randrange(1, (screen_width//grid_size)) * grid_size, random.randrange(1, (screen_height//grid_size)) * grid_size]
score = 0

# show score at top of screen
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (screen_width/2, 10)
    else:
        score_rect.midtop = (screen_width/2, screen_height/1.25)
    screen.blit(score_surface, score_rect)

class food:
    def __init__(self):
        self.color = red
        
    def draw(self, screen):
        return pygame.draw.rect(screen, self.color, pygame.Rect(food_pos[0], food_pos[1], grid_size, grid_size))

class snake:
    def __init__(self):
        self.color = white
        self.body = [[grid_size * 5, grid_size * 5]]
        self.direction = 'RIGHT'
    
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, pygame.Rect(segment[0], segment[1], grid_size, grid_size))

    def move(self, key_pressed):
        if key_pressed == pygame.K_w or key_pressed == pygame.K_UP:
            if self.direction != 'DOWN':
                self.direction = 'UP'
        elif key_pressed == pygame.K_s or key_pressed == pygame.K_DOWN:
            if self.direction != 'UP':
                self.direction = 'DOWN'
        elif key_pressed == pygame.K_a or key_pressed == pygame.K_LEFT:
            if self.direction != 'RIGHT':
                self.direction = 'LEFT'
        elif key_pressed == pygame.K_d or key_pressed == pygame.K_RIGHT:
            if self.direction != 'LEFT':
                self.direction = 'RIGHT'
    
    def grow(self, food_pos):
        global food_spawn, score
        
        # calculate new head position based on current direction
        new_head = [self.body[0][0], self.body[0][1]]
        
        if self.direction == 'UP':
            new_head[1] -= grid_size
        elif self.direction == 'DOWN':
            new_head[1] += grid_size
        elif self.direction == 'LEFT':
            new_head[0] -= grid_size
        elif self.direction == 'RIGHT':
            new_head[0] += grid_size
        
        # add new head to front of body
        self.body.insert(0, new_head)
        
        # check if new head hit food
        if new_head[0] == food_pos[0] and new_head[1] == food_pos[1]:
            # food eaten - don't remove tail (snake grows)
            score += 1
            food_spawn = False
        else:
            # no food eaten - remove tail (snake stays same length)
            self.body.pop()
            

    def check_collisions(self):
        head_x, head_y = self.body[0]
        # checking to see if the head x, y exceed screen
        if (head_x < 0 or head_x >= screen_width or
            head_y < 0 or head_y >= screen_height):
            self.game_over()
    
    def check_collisions_with_self(self):
        head = self.body[0]
        # loop through each 'body part' and check if the (head x, y) are = to (body x, y) 
        for segment in self.body[1:]:
            if head[0] == segment[0] and head[1] == segment[1]:
                self.game_over()
            
    
    def game_over(self):
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render('YOU DIED', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (screen_width/2, screen_height/4)
        screen.fill(black)
        screen.blit(game_over_surface, game_over_rect)
        show_score(0, red, 'times', 20)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

player = snake()
food = food()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            player.move(event.key)
    
    #init black background for the game
    screen.fill(black)
    
    #draw the snake
    player.draw(screen)
    
    # show score
    show_score(1, white, 'consolas', 50)
    
    #draw food
    food.draw(screen)
        
    #collisions
    player.check_collisions()
    player.check_collisions_with_self()
    
    #grow
    player.grow(food_pos)
    
    if food_spawn == False:
        food_pos = [random.randrange(1, (screen_width//grid_size)) * grid_size, random.randrange(1, (screen_height//grid_size)) * grid_size]
        food_spawn = True
    
    clock.tick(7) / 1000.0 #framerate, convert milliseconds to seconds
    
    # had to look this one up but any changes that are made to the drawing surface(like screen or other Surface objects) visible to the user
    pygame.display.flip()

pygame.quit()