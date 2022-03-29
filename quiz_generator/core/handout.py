from typing import Sequence

from .question import Question


class Handout(tuple[Question]):
    def __new__(cls: type['Handout'], seq: Sequence[Question]) -> 'Handout':
        return tuple.__new__(Handout, seq)
