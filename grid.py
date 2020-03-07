from random import randint
import Cell
import pygame as pg
from pprint import pprint


class Grid:
    m_line_wth = 2
    m_square_wth = 10
    m_square_hght = 10
    m_grid = [[0 for column in range(67)] for row in range(50)]

    def __init__(self, _win):
        for row in range(50):
            for column in range(67):
                pg.draw.rect(_win, (52, 73, 94),
                             [(self.getLine_wth() + self.getSquare_wth()) * column + self.getLine_wth(),
                              (self.getLine_wth() + self.getSquare_hght()) * row + self.getLine_wth(),
                              self.getSquare_wth(), self.getSquare_hght()])
                Cell.CellClass.add_cell(row, column)
                Cell.CellClass.set_state(row, column, Cell.Cell.IS_DEAD)

    @classmethod
    def select_cell(cls, _win):
        pos = pg.mouse.get_pos()
        column = pos[0] // (Grid.m_square_wth + Grid.m_line_wth)
        row = pos[1] // (Grid.m_square_hght + Grid.m_line_wth)
        cls.m_grid[row][column] = 1
        print(f"La cellule est {Cell.CellClass.get_state(row, column)}")  # true : vivante, false : morte

    @classmethod
    def generate_life(cls, _win):
        random_cell_r, random_cell_c = randint(0, 49), randint(0, 66)
        pg.draw.rect(_win, (42, 204, 113), (
            pg.Rect(random_cell_c * cls.getSquare_wth() + cls.getLine_wth() * (random_cell_c + 1),
                    random_cell_r * cls.getSquare_hght() + cls.getLine_wth() * (random_cell_r + 1), cls.getSquare_wth(),
                    cls.getSquare_hght())))
        Cell.CellClass.set_state(random_cell_r, random_cell_c, Cell.Cell.IS_ALIVE)

    @classmethod
    def getLine_wth(cls):
        return cls.m_line_wth

    @classmethod
    def getSquare_wth(cls):
        return cls.m_square_wth

    @classmethod
    def getSquare_hght(cls):
        return cls.m_square_hght

    @classmethod
    def setLine_wth(cls, value):
        cls.m_line_wth = value

    @classmethod
    def setSquare_wth(cls, value):
        cls.m_square_wth = value

    @classmethod
    def setSquare_hght(cls, value):
        cls.m_square_hght = value

    @classmethod
    def check_life(cls, _win):
        for row in range(1, 49):
            for column in range(1, 66):
                neighbours_count = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if Cell.CellClass.get_state(row + x, column + y) == Cell.Cell.IS_ALIVE:
                            neighbours_count += 1
                        print(neighbours_count)
                if Cell.CellClass.get_state(row, column) == Cell.Cell.IS_ALIVE and (neighbours_count < 2 or neighbours_count > 3):
                    Cell.CellClass.set_state(row, column, Cell.Cell.IS_DEAD)
                elif Cell.CellClass.get_state(row, column) == Cell.Cell.IS_ALIVE and (neighbours_count == 2 or neighbours_count == 3):
                    Cell.CellClass.set_state(row, column, Cell.Cell.IS_ALIVE)
                elif Cell.CellClass.get_state(row, column) == Cell.Cell.IS_DEAD and neighbours_count == 3:
                    Cell.CellClass.set_state(row, column, Cell.Cell.IS_ALIVE)
                if Cell.CellClass.get_state(row, column) == Cell.Cell.IS_ALIVE:
                    pg.draw.rect(_win, (42, 204, 113), (pg.Rect(column * cls.getSquare_wth() + cls.getLine_wth() * (column + 1),row * cls.getSquare_hght() + cls.getLine_wth() * (row + 1),cls.getSquare_wth(), cls.getSquare_hght())))
                if Cell.CellClass.get_state(row, column) == Cell.Cell.IS_DEAD:
                    pg.draw.rect(_win, (52, 73, 94), (pg.Rect(column * cls.getSquare_wth() + cls.getLine_wth() * (column + 1),row * cls.getSquare_hght() + cls.getLine_wth() * (row + 1),cls.getSquare_wth(), cls.getSquare_hght())))
