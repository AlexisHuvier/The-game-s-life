import time
from random import randint

import pygame as pg
import os


def draw(_line_wth, _square_wth):
    for row in range(50):
        for column in range(67):
            pg.draw.rect(win, (52, 73, 94),
                         [(_line_wth + _square_wth) * column + _line_wth,
                          (_line_wth + _square_wth) * row + _line_wth,
                          _square_wth, _square_wth])
            cells_table[row, column] = False


def select_cells():
    pos = pg.mouse.get_pos()
    column = pos[0] // (square_wth + line_wth)
    row = pos[1] // (square_wth + line_wth)
    cells_table[row, column] = True

    if cells_table[row, column]:
        pg.draw.rect(win, (42, 204, 113), (
            pg.Rect(column * square_wth + line_wth * (column + 1),
                    row * square_wth + line_wth * (row + 1), square_wth,
                    square_wth)))
    if not cells_table[row, column]:
        pg.draw.rect(win, (52, 73, 94), (
            pg.Rect(column * square_wth + line_wth * (column + 1),
                    row * square_wth + line_wth * (row + 1), square_wth,
                    square_wth)))


def life():
    for row in range(1, 49):
        for column in range(1, 66):
            neighbours_count = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if cells_table[row + x, column + y]:
                        neighbours_count += 1
            if cells_table[row, column] and (neighbours_count < 2 or neighbours_count > 3):
                cells_table[row, column] = False
            elif cells_table[row, column] and (neighbours_count == 2 or neighbours_count == 3):
                cells_table[row, column] = True
            elif not cells_table[row, column] and neighbours_count == 3:
                cells_table[row, column] = True
            if cells_table[row, column]:
                pg.draw.rect(win, (42, 204, 113), (
                    pg.Rect(column * square_wth + line_wth * (column + 1),
                            row * square_wth + line_wth * (row + 1), square_wth,
                            square_wth)))
            if not cells_table[row, column]:
                pg.draw.rect(win, (52, 73, 94), (
                    pg.Rect(column * square_wth + line_wth * (column + 1),
                            row * square_wth + line_wth * (row + 1), square_wth,
                            square_wth)))
    time.sleep(0.5)


pg.init()
win = pg.display.set_mode((800, 600))
cells_table = {}
line_wth = 2
square_wth = 10
draw(line_wth, square_wth)

while True:
    pg.display.update()
    for _ in pg.event.get():
        key = pg.key.get_pressed()
        if key[pg.K_ESCAPE] or _.type == pg.QUIT:
            pg.quit()
            os.sys.exit(0)
        if key[pg.K_p]:
            while 1:
                life()
                pg.display.update()

        elif _.type == pg.MOUSEBUTTONDOWN:
            select_cells()
            print(cells_table)
