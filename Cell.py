from dataclasses import dataclass
from enum import Enum, unique
from pprint import pprint
import time
import sys


@unique
class Cell(Enum):
    IS_DEAD = 1,
    IS_ALIVE = 2


@dataclass
class CellShape:
    x: int
    y: int
    state: Cell

    def __init__(self, _x: int, _y: int, _state=Cell.IS_DEAD):
        self.x, self.y, self.state = _x, _y, _state


class CellClass:
    m_cell_list = []

    @classmethod
    def set_state(cls, x: int, y: int, _state: Cell):
        cls.get_cell(x, y).state = _state

    @classmethod
    def has_state(cls, x: int, y: int, _state: Cell) -> bool:
        if not (cls.m_cell_list.__contains__(cls.get_cell(x, y))): print(f"La cellule ({x, y}) n'existe pas")
        return cls.get_state(cls.get_cell(x, y).x, cls.get_cell(x, y).y) == _state

    @classmethod
    def add_cell(cls, x: int, y: int):
        cls.m_cell_list.append(CellShape(x, y))

    @staticmethod
    def remove_cell(cls, _cell: CellShape):
        cls.m_cell_list.remove(_cell)

    @classmethod
    def get_state(cls, x: int, y: int) -> Cell:
        if not cls.get_cell(x, y) is None:
            return cls.get_cell(x, y).state

    @classmethod
    def get_cell(cls, x: int, y: int) -> CellShape:
        for cell in cls.m_cell_list:
            if cell.x == x and cell.y == y:
                return cell
        print('\033[1;31;48m' + "Erreur » La cellule ({}, {}) n'est pas un élément de la liste.".format(x, y))

    @classmethod
    def display_affected(cls):
        for obj in cls.m_cell_list:
            pprint(f"[{type(obj)}]: {obj}")
