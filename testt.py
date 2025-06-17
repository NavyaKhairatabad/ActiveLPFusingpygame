import pygame
import sys

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode ((WIDTH, HEIGHT))
pygame.display.set_caption ("Low Pass Filter Game")
clock = pygame. time. Clock ()

# Filter parameters
alpha = 0.1 # smoothing factor
filtered_x,filtered_y = WIDTH // 2, HEIGHT // 2 # Initial position

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            pygame.quit()
            sys. exit ()

    # Get raw input from mouse
    mouse_x,mouse_y = pygame.mouse.get_pos ()

    # Apply low pass filter
    filtered_x = alpha * mouse_x + (1 - alpha) * filtered_x
    filtered_y = alpha * mouse_y + (1 - alpha) * filtered_y

    # Draw background and smoothed circle
    screen.fill((30, 30, 30))
    pygame.draw.circle(screen, (100, 255, 100), (int(filtered_x), int(filtered_y)), 20)

    # Draw actual mouse position (for comparison)
    pygame.draw.circle(screen, (255, 50, 50), (mouse_x, mouse_y), 5)

    # Update display
    pygame.display.flip ()
    clock.tick(60)
