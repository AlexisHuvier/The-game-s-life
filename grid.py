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
                             [(self.m_line_wth + self.m_square_wth) * column + self.m_line_wth, (self.m_line_wth + self.m_square_hght) * row + self.m_line_wth,
                              self.m_square_wth, self.m_square_hght])

    def selectACell(self):
        pos = pg.mouse.get_pos()
        column = pos[0] // (self.m_square_wth + self.m_line_wth)
        row = pos[1] // (self.m_square_hght + self.m_line_wth)

        self.m_grid[row][column] = 1
        print("Click ", pos, "Grid coordinates: ", row, column)
