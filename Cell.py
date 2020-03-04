from dataclasses import dataclass
from enum import Enum, unique
from typing import overload


@unique
class Cell(Enum):
    IS_DEAD = 1 << 1,
    IS_ALIVE = 1 << 2


@dataclass
class CellShape:
    x: int
    y: int

    def __init__(self, _x: int, _y: int):
        self.x, self.y = _x, _y


class CellClass:
    m_cell_list = []
    m_cell = 0

    @staticmethod
    def set_state(cls, _state):
        cls.m_cell |= _state

    @staticmethod
    def un_state(cls, _state):
        cls.m_cell &= ~_state

    @staticmethod
    def has_state(cls, _state) -> bool:
        return (cls.m_cell & _state) != 0

    @classmethod
    def add_cell(cls, _cell: CellShape):
        cls.m_cell_list.append(_cell)

    @classmethod
    def add_cell_xy(cls, _cell_x: int, _cell_y: int):
        cls.m_cell_list.append(CellShape(_cell_x, _cell_y))

    @staticmethod
    def remove_cell(cls, _cell: CellShape):
        cls.m_cell_list.remove(_cell)

    @classmethod
    def display_affected(cls):
        print(cls.m_cell_list)
