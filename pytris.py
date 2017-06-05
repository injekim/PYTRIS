# PYTRIS™ Copyright (c) 2017 Jason Kim All Rights Reserved.

import pygame
from mino import *
from random import *
from pygame.locals import *

# Define
block_size = 17 # Height, width of single block
width = 10 # Board width
height = 20 # Board height
framerate = 30

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((300, 374))
pygame.display.set_caption("PYTRIS™")

class ui_variables:
    # Fonts
    font_path = "./assets/fonts/OpenSans-Light.ttf"
    h1 = pygame.font.Font(font_path, 50)
    h4 = pygame.font.Font(font_path, 20)
    h5 = pygame.font.Font(font_path, 13)
    h6 = pygame.font.Font(font_path, 10)

    #Background colors
    black = (10, 10, 10) #rgb(10, 10, 10)
    white = (255, 255, 255) #rgb(255, 255, 255)
    grey_1 = (26, 26, 26) #rgb(26, 26, 26)
    grey_2 = (35, 35, 35) #rgb(35, 35, 35)

    # Tetrimino colors
    cyan = (69, 206, 204) #rgb(69, 206, 204) # I
    blue = (64, 111, 249) #rgb(64, 111, 249) # J
    orange = (253, 189, 53) #rgb(253, 189, 53) # L
    yellow = (246, 227, 90) #rgb(246, 227, 90) # O
    green = (98, 190, 68) #rgb(98, 190, 68) # S
    pink = (242, 64, 235) #rgb(242, 64, 235) # T
    red = (225, 13, 27) #rgb(225, 13, 27) # Z

    t_color = [grey_2, cyan, blue, orange, yellow, green, pink, red]
    t_list = ['wall', 'I', 'J', 'L', 'O', 'S', 'T', 'Z']

# Draw single block
def draw_block(x, y, color):
    pygame.draw.rect(
        screen,
        color,
        Rect(x, y, block_size, block_size)
    )
    pygame.draw.rect(
        screen,
        ui_variables.grey_1,
        Rect(x, y, block_size, block_size),
        1
    )

# Draw game screen
def draw_board(mino):
    screen.fill(ui_variables.grey_1)

    pygame.draw.rect(
        screen,
        ui_variables.white,
        Rect(204, 0, 96, 374)
    )

    grid = tetrimino.mino_map[mino - 1][0]

    for i in range(4):
        for j in range(4):
            dx = 220 + block_size * j
            dy = 150 + block_size * i
            if grid[i][j] != 0:
                pygame.draw.rect(
                    screen,
                    ui_variables.t_color[grid[i][j]],
                    Rect(dx, dy, block_size, block_size)
                )

    text_hold = ui_variables.h5.render("HOLD", 1, ui_variables.black)
    text_next = ui_variables.h5.render("NEXT", 1, ui_variables.black)
    text_score = ui_variables.h5.render("SCORE", 1, ui_variables.black)

    screen.blit(text_hold, (215, 14))
    screen.blit(text_next, (215, 114))
    screen.blit(text_score, (215, 214))

    for x in range(width):
        for y in range(height):
            dx = 17 + block_size * x
            dy = 17 + block_size * y
            draw_block(dx, dy, ui_variables.t_color[matrix[x][y]])

def draw_mino(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    for i in range(4):
        for j in range(4):
            dx = 17 + block_size * (x + j)
            dy = 17 + block_size * (y + i)
            if grid[i][j] != 0:
                matrix[x + j][y + i] = grid[i][j]

def erase_mino(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    for i in range(4):
        for j in range(4):
            dx = 17 + block_size * (x + j)
            dy = 17 + block_size * (y + i)
            if grid[i][j] != 0:
                matrix[x + j][y + i] = 0

def is_bottom(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    for i in range(4):
        for j in range(4):
            dx = 17 + block_size * (x + j)
            dy = 17 + block_size * (y + i)
            if grid[i][j] != 0:
                if (y + i + 1) > 19:
                    return True
                elif matrix[x + j][y + i + 1] != 0:
                    return True

    return False

def is_leftedge(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    for i in range(4):
        for j in range(4):
            dx = 17 + block_size * (x + j)
            dy = 17 + block_size * (y + i)
            if grid[i][j] != 0:
                if (x + j - 1) < 0:
                    return True
                elif matrix[x + j - 1][y + i] != 0:
                    return True

    return False

def is_rightedge(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    for i in range(4):
        for j in range(4):
            dx = 17 + block_size * (x + j)
            dy = 17 + block_size * (y + i)
            if grid[i][j] != 0:
                if (x + j + 1) > 9:
                    return True
                elif matrix[x + j + 1][y + i] != 0:
                    return True

    return False

# Initial values
blink = True
start = False
done = False
dx, dy = 3, 0
rotation = 0

mino = randint(1, 7)
next_mino = randint(1, 7)

matrix = [[0 for y in range(height)] for x in range(width)]

###########################################################
# Loop Start
###########################################################

while not done:
    # Game screen
    if start:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN:
                erase_mino(dx, dy, mino, rotation)
                if event.key == K_SPACE:
                    while not is_bottom(dx, dy, mino, rotation):
                        dy += 1
                        """
                elif event.key == K_LSHIFT:
                """
                elif event.key == K_UP:
                    rotation += 1
                    if rotation == 4:
                        rotation = 0
                elif event.key == K_DOWN:
                    if not is_bottom(dx, dy, mino, rotation):
                        dy += 1
                elif event.key == K_LEFT:
                    if not is_leftedge(dx, dy, mino, rotation):
                        dx -= 1
                elif event.key == K_RIGHT:
                    if not is_rightedge(dx, dy, mino, rotation):
                        dx += 1
                draw_mino(dx, dy, mino, rotation)
                draw_board(next_mino)

        # Draw a mino
        draw_mino(dx, dy, mino, rotation)
        draw_board(next_mino)
        erase_mino(dx, dy, mino, rotation)

        # Move mino down
        if not is_bottom(dx, dy, mino, rotation):
            dy += 1
        # Create new mino
        else:
            draw_mino(dx, dy, mino, rotation)
            draw_board(next_mino)
            mino = next_mino
            next_mino = randint(1, 7)
            dx, dy = 3, 0
            rotation = 0

        pygame.display.update()
        clock.tick(framerate / 10)

    # Start screen
    else:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    start = True

        screen.fill(ui_variables.white)
        pygame.draw.rect(
            screen,
            ui_variables.grey_1,
            Rect(0, 187, 300, 187)
        )

        title = ui_variables.h1.render("PYTRIS™", 1, ui_variables.grey_1)
        title_start = ui_variables.h5.render("Press space to start", 1, ui_variables.white)
        title_info = ui_variables.h6.render("Copyright (c) 2017 Jason Kim All Rights Reserved.", 1, ui_variables.white)

        if blink:
            screen.blit(title_start, (92, 195))
            blink = False
        else:
            blink = True
        screen.blit(title, (65, 120))
        screen.blit(title_info, (40, 335))

        if not start:
            clock.tick(3)
            pygame.display.update()

pygame.quit()
