import pygame as pg
import sys
from grid import Grid
from Cell import CellClass
import os

ratio = WIDTH, HEIGHT = 800, 600
os.environ['SDL_VIDEO_CENTERED'] = str(1)


def main():
    pg.init()
    clock = pg.time.Clock()
    win = pg.display.set_mode(ratio)
    pg.display.set_caption("The game's life | {} FPS".format(round(clock.get_fps())))
    win.fill((25, 25, 25))
    grid = Grid(win)
    cellClass = CellClass()
    [grid.generate_life(win) for _ in range(100)]
    while True:
        for _ in pg.event.get():
            key = pg.key.get_pressed()
            if key[pg.K_ESCAPE] or _.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif _.type == pg.MOUSEBUTTONDOWN:
                grid.select_cell(win)
        grid.check_life()
        pg.display.update()


if __name__ == '__main__': main()
