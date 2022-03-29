import abc
from pathlib import Path
from typing import Sequence

from ..core.question import Question
from ..core.source import QuestionSource


class IOReader(QuestionSource, abc.ABC):
    def __init__(self, path: Path | str) -> None:
        self.path = path

    @abc.abstractmethod
    def read(self) -> Sequence[Question]:
        pass

    def get(self) -> Sequence[Question]:
        return self.read()
