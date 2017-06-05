# PYTRIS™ Copyright (c) 2017 Jason Kim All Rights Reserved.

import random
import pygame
from mino import tetrimino
from pygame.locals import *

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

    #Colors
    black = (10, 10, 10) #rgb(10, 10, 10)
    white = (255, 255, 255) #rgb(255, 255, 255)
    grey_1 = (26, 26, 26) #rgb(26, 26, 26)
    grey_2 = (35, 35, 35) #rgb(35, 35, 35)
    navy_1 = (32, 46, 55) #rgb(32, 46, 55)
    skyblue = (131, 189, 221) #rgb(131, 189, 221)

    cyan = (69, 206, 204) #rgb(69, 206, 204)
    yellow = (246, 227, 90) #rgb(246, 227, 90)
    pink = (242, 64, 235) #rgb(242, 64, 235)
    blue = (64, 111, 249) #rgb(64, 111, 249)
    green = (98, 190, 68) #rgb(98, 190, 68)
    red = (225, 13, 27) #rgb(225, 13, 27)
    orange = (253, 189, 53) #rgb(253, 189, 53)

# Initial values
is_legal = False
is_bottom = False
t_list = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
mino = t_list[random.randint(0, 6)]
next_mino = t_list[random.randint(0, 6)]
start = False
done = False
blink = True
dx, dy = 3, 0
width, height = 10, 20 # Board width, height
block_size = 17 # height / width of single block
matrix = [[0 for x in range(height)] for y in range(width)]

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

def draw_board():
    pygame.draw.rect(
        screen,
        ui_variables.white,
        Rect(204, 0, 96, 374)
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
            if matrix[x][y] == 0:
                draw_block(dx, dy, ui_variables.grey_2)
            elif matrix[x][y] == 1:
                draw_block(dx, dy, ui_variables.cyan)
            elif matrix[x][y] == 2:
                draw_block(dx, dy, ui_variables.blue)
            elif matrix[x][y] == 3:
                draw_block(dx, dy, ui_variables.orange)
            elif matrix[x][y] == 4:
                draw_block(dx, dy, ui_variables.yellow)
            elif matrix[x][y] == 5:
                draw_block(dx, dy, ui_variables.green)
            elif matrix[x][y] == 6:
                draw_block(dx, dy, ui_variables.pink)
            elif matrix[x][y] == 7:
                draw_block(dx, dy, ui_variables.red)

def draw_mino(x, y, mino, r):
    if mino == 'I':
        color = ui_variables.cyan
        grid = tetrimino.I[r]
    elif mino == 'J':
        color = ui_variables.blue
        grid = tetrimino.J[r]
    elif mino == 'L':
        color = ui_variables.orange
        grid = tetrimino.L[r]
    elif mino == 'O':
        color = ui_variables.yellow
        grid = tetrimino.O[r]
    elif mino == 'S':
        color = ui_variables.green
        grid = tetrimino.S[r]
    elif mino == 'T':
        color = ui_variables.pink
        grid = tetrimino.T[r]
    elif mino == 'Z':
        color = ui_variables.red
        grid = tetrimino.Z[r]

    for i in range(4):
        for j in range(4):
            if x + j > 9 or y + i > 19:
                if grid[i][j] != 0:
                    return False

    for i in range(4):
        for j in range(4):
            dx = 17 + block_size * (x + j)
            dy = 17 + block_size * (y + i)
            if grid[i][j] != 0:
                draw_block(dx, dy, color)
                matrix[x + j][y + i] = grid[i][j]

    return True

def erase_mino(x, y, mino, r):
    if mino == 'I':
        grid = tetrimino.I[r]
    elif mino == 'J':
        grid = tetrimino.J[r]
    elif mino == 'L':
        grid = tetrimino.L[r]
    elif mino == 'O':
        grid = tetrimino.O[r]
    elif mino == 'S':
        grid = tetrimino.S[r]
    elif mino == 'T':
        grid = tetrimino.T[r]
    elif mino == 'Z':
        grid = tetrimino.Z[r]

    for i in range(4):
        for j in range(4):
            dx = 17 + block_size * (x + j)
            dy = 17 + block_size * (y + i)
            if grid[i][j] != 0:
                draw_block(dx, dy, ui_variables.grey_2)
                matrix[x + j][y + i] = 0

def fall_down(x, y, mino, r):
    if is_legal == True and is_bottom == False:
        return x, y + 1

def is_at_bottom(x, y, mino, r):
    if mino == 'I':
        grid = tetrimino.I[r]
    elif mino == 'J':
        grid = tetrimino.J[r]
    elif mino == 'L':
        grid = tetrimino.L[r]
    elif mino == 'O':
        grid = tetrimino.O[r]
    elif mino == 'S':
        grid = tetrimino.S[r]
    elif mino == 'T':
        grid = tetrimino.T[r]
    elif mino == 'Z':
        grid = tetrimino.Z[r]

    for i in range(4):
        for j in range(4):
            dx = 17 + block_size * (x + j)
            dy = 17 + block_size * (y + i)
            if grid[i][j] != 0:
                if y + i + 1 > 18:
                    return True
                elif matrix[x + j][y + i + 1] != 0:
                    return True
        return False

# Set background color
screen.fill(ui_variables.white)
pygame.display.update()

while not done:
    if start:
        screen.fill(ui_variables.grey_1)
        draw_board()
        is_bottom = is_at_bottom(dx, dy, 'I', 0)
        is_legal = draw_mino(dx, dy, 'I', 0)
        pygame.display.update()
        print(is_bottom)
        if not is_bottom:
            erase_mino(dx, dy, 'I', 0)
            dx, dy = fall_down(dx, dy, 'I', 0)
        clock.tick(3)




        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
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
