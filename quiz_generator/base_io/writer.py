import abc
from pathlib import Path
from typing import Sequence

from ..core.handout import Handout
from ..core.question import Question


class IOWriter(abc.ABC):
    def __init__(self, path: Path | str) -> None:
        self.path = path

    @abc.abstractmethod
    def write(self, questions: Sequence[Question]) -> None:
        pass

    def write_all(self, question_sets: Sequence[Sequence[Question]]) -> None:
        for questions in question_sets:
            self.write(questions)
