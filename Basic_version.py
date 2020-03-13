import pygame as pg
import os

def draw (line_wth, square_wth):
    for row in range(50):
        for column in range(67):
            pg.draw.rect(win, (52, 73, 94),
                         [(line_wth + square_wth) * column + line_wth,
                          (line_wth + square_wth) * row + line_wth,
                          square_wth, square_wth])
            print(row, column)
            cells_table[row][column] = False


def select_cells():
    pass

pg.init()
win = pg.display.set_mode((800,600))
cells_table = [[], []]
line_wth = 2
square_wth = 10
draw(line_wth, square_wth)


continuer = True
while continuer :
    pg.display.update()
    for _ in pg.event.get():
        key = pg.key.get_pressed()
        if key[pg.K_ESCAPE] or _.type == pg.QUIT:
            pg.quit()
            os.sys.exit(0)
