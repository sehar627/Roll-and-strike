import pygame
import pymunk
import pymunk.pygame_util

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
score = 0
attempts = 3
game_over = False

#create bowling ball



#create pin



# Vertically arranged pins
pins = []
rows = [ 4, 3, 2, 1]  # Number of pins per row
start_x = 600
start_y = 520
dx = 30  # horizontal spacing between pins
dy = 70  # vertical spacing between rows

for row_index, num_pins in enumerate(rows):
    row_y = start_y - row_index * dy
    row_start_x = start_x - ((num_pins - 1) * dx) / 2
    for i in range(num_pins):
        x = row_start_x + i * dx
        y = row_y
        pins.append(create_pin(x, y))
# Draw
def draw_game():
    
    # Draw Ball
    
   
    
# Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
