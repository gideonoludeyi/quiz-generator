import abc
from typing import Sequence

from .question import Question


class QuestionSource(abc.ABC):
    @abc.abstractmethod
    def get(self) -> Sequence[Question]:
        pass
