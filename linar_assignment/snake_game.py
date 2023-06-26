import pygame
import time

pygame.init()

# Define window dimensions
width = 800
height = 600

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the game window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define snake and food dimensions
snake_block = 10
snake_speed = 15

# Define fonts
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])


def game_over():
    message("Game Over!", red)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()


def game_loop():
    game_over = False
    game_close = False

    # Initialize snake's starting position
    x1 = width / 2
    y1 = height / 2

    # Initialize the change in position
    x1_change = 0
    y1_change = 0

    # Create an empty list to keep track of the snake's body
    snake_list = []
    snake_length = 1

    # Generate the position of the food
    food_x = round((round(width / 10) * 10) / 10)
    food_y = round((round(height / 10) * 10) / 10)

    while not game_over:
        while game_close:
            window.fill(white)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            # Check for player's input after losing
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Listen for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check for boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Update snake's position
        x1 += x1_change
        y1 += y1_change
        window.fill(white)
        pygame.draw.rect(window, red, [food_x, food_y, snake_block, snake_block])

        # Store the snake's position
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Remove extra
