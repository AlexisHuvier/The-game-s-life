import pygame as pg
import sys
from grid import Grid
import os

ratio = WIDTH, HEIGHT = 800, 600
os.environ['SDL_VIDEO_CENTERED'] = str(1)


def main():
    line_wth = 2
    square_wth = 10
    square_hght = 10
    table_li_grid = [[], []]
    pg.init()
    clock = pg.time.Clock()
    win = pg.display.set_mode(ratio)
    pg.display.set_caption("The game's life | {} FPS".format(round(clock.get_fps())))
    grid = Grid()
    grid.__init__()
    win.fill((255, 255, 255))
    for row in range(50):
        table_li_grid.append([])
        for column in range(67):
            table_li_grid[row].append(0)
    for row in range(50):
        for column in range(67):
            color = (0, 0, 0)
            if table_li_grid[row][column] == 1:
                color = (255, 255, 255)
            pg.draw.rect(win, (0, 0, 0),
                         [(line_wth + square_wth) * column + line_wth, (line_wth + square_hght) * row + line_wth,
                          square_wth, square_hght])

    while True:
        for _ in pg.event.get():
            key = pg.key.get_pressed()
            if key[pg.K_ESCAPE] or _.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif _.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()

                column = pos[0] // (square_wth + line_wth)
                row = pos[1] // (square_hght + line_wth)

                table_li_grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)

        grid.display()
        pg.display.update()


if __name__ == '__main__': main()
