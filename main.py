import pygame as pg
from grid import Grid
import os

ratio = WIDTH, HEIGHT = 800, 600
os.environ['SDL_VIDEO_CENTERED'] = str(1)


def main():
    pg.init()
    clock = pg.time.Clock()
    win = pg.display.set_mode(ratio)
    pg.display.set_caption(f"The game's life | {round(clock.get_fps())} FPS")
    grid = Grid()
    grid.__init__()
    win.fill((255, 255, 255))
    while True:
        for _ in pg.event.get():
            if _.type == pg.QUIT: return
        grid.display()
        pg.display.update()


if __name__ == '__main__': main()
