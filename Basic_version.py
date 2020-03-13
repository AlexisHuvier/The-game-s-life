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
            print(row, column)
            # cells_table[row][column] = False


def generate_life(_win, _line_wth, _square_wth):
    random_cell_r, random_cell_c = randint(0, 49), randint(0, 66)
    pg.draw.rect(_win, (42, 204, 113), (
        pg.Rect(random_cell_c * _square_wth + _line_wth * (random_cell_c + 1),
                random_cell_r * _square_wth + _line_wth * (random_cell_r + 1), _square_wth,
                _square_wth)))



def select_cells():
    pass


pg.init()
win = pg.display.set_mode((800, 600))
cells_table = [[], []]
line_wth = 2
square_wth = 10
draw(line_wth, square_wth)
[generate_life(win, 2, 10) for _ in range(100)]
continuer = True
while continuer:
    pg.display.update()
    for _ in pg.event.get():
        key = pg.key.get_pressed()
        if key[pg.K_ESCAPE] or _.type == pg.QUIT:
            pg.quit()
            os.sys.exit(0)
