import pygame as pg


class Grid:
    m_line_wth = 2
    m_square_wth = 10
    m_square_hght = 10
    m_grid = [[0 for column in range(67)] for row in range(50)]

    def __init__(self, _win):
        for row in range(50):
            for column in range(67):
                pg.draw.rect(_win, (255, 255, 255),
                             [(self.getLine_wth() + self.getSquare_wth()) * column + self.getLine_wth(), (self.getLine_wth() + self.getSquare_hght()) * row + self.getLine_wth(),
                              self.getSquare_wth(), self.getSquare_hght()])

    @classmethod
    def selectACell(cls):
        pos = pg.mouse.get_pos()
        column = pos[0] // (Grid.m_square_wth + Grid.m_line_wth)
        row = pos[1] // (Grid.m_square_hght + Grid.m_line_wth)
        cls.m_grid[row][column] = 1
        print("Click ", pos, "Grid coordinates: ", row, column)

    def getLine_wth(self): return self.m_line_wth
    def getSquare_wth(self): return self.m_square_wth
    def getSquare_hght(self): return self.m_square_hght
    def setLine_wth(self, value): self.m_line_wth = value
    def setSquare_wth(self, value): self.m_square_wth = value
    def setSquare_hght(self, value): self.m_square_hght = value

