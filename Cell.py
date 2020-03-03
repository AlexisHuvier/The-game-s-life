from enum import Enum, unique


@unique
class Cell(Enum):
    IS_DEAD = 1 << 1,
    IS_ALIVE = 1 << 2


class CellClass:
    m_cell_list = []
    m_cell = 0

    @classmethod
    def set_state(cls, _state):
        cls.m_cell |= _state

    @classmethod
    def un_state(cls, _state):
        cls.m_cell &= ~_state

    @classmethod
    def has_state(cls, _state):
        return (cls.m_cell & _state) != 0
