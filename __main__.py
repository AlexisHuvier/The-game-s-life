import pygame as pg
import sys
from grid import Grid
from Cell import CellClass, Cell
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
            elif key[pg.K_p] :
                print("launching the game")
                while 1 :
                    for row in range(1,49):
                        for column in range(1,66):
                            neighbours_count = 0
                            for x in range (-1,2):
                                for y in range(-1, 2):
                                    if CellClass.get_state(row + x, column + y) == Cell.IS_ALIVE:
                                        neighbours_count += 1
                            print(neighbours_count)
                            if CellClass.get_state(row, column) == Cell.IS_ALIVE and (neighbours_count < 2 or neighbours_count > 3) :
                                CellClass.set_state(row, column, Cell.IS_DEAD)
                            elif CellClass.get_state(row, column) == Cell.IS_ALIVE and (neighbours_count == 2 or neighbours_count == 3):
                                CellClass.set_state(row, column, Cell.IS_ALIVE)
                            elif CellClass.get_state(row, column) == Cell.IS_DEAD and neighbours_count == 3 :
                                CellClass.set_state(row, column, Cell.IS_ALIVE)
                            if CellClass.get_state(row, column) == Cell.IS_ALIVE:
                                pg.draw.rect(win, (42, 204, 113), (pg.Rect(column * grid.getSquare_wth() + grid.getLine_wth() * (column + 1),row * grid.getSquare_hght() + grid.getLine_wth() * (row + 1),grid.getSquare_wth(),grid.getSquare_hght())))
                            if CellClass.get_state(row, column) == Cell.IS_DEAD:
                                pg.draw.rect(win, (52, 73, 94), (pg.Rect(column * grid.getSquare_wth() + grid.getLine_wth() * (column + 1),row * grid.getSquare_hght() + grid.getLine_wth() * (row + 1),grid.getSquare_wth(),grid.getSquare_hght())))
                    pg.display.update()





        pg.display.update()


if __name__ == '__main__': main()
