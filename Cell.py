from dataclasses import dataclass
from enum import Enum, unique
from pprint import pprint


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
    def set_state(cls, _cell: CellShape, _state: Cell):
        _cell.state = _state

    @classmethod
    def has_state(cls, _cell: CellShape, _state: Cell) -> bool:
        return cls.get_state(_cell) == _state

    @classmethod
    def add_cell(cls, _cell: CellShape):
        cls.m_cell_list.append(_cell)

    @staticmethod
    def remove_cell(cls, _cell: CellShape):
        cls.m_cell_list.remove(_cell)

    @classmethod
    def get_state(cls, _cell: CellShape) -> Cell:
        if not (cls.m_cell_list.__contains__(_cell)): print(f"La cellule ({_cell.x, _cell.y}) n'existe pas")
        return _cell.state

    @classmethod
    def display_affected(cls):
        pprint(cls.m_cell_list)
