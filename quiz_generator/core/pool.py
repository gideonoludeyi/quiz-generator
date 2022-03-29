from random import sample
from typing import Callable, Sequence

from .handout import Handout
from .question import Question
from .source import QuestionSource

SelectionStrategy = Callable[[Sequence[Question], int], Sequence[Question]]

random_selection = sample


class QuestionPool:
    def __init__(self, source: QuestionSource, strategy: SelectionStrategy = random_selection) -> None:
        self.questions = source.get()
        self.strategy = strategy

    def select(self, n: int = 1) -> Handout:
        questions = self.strategy(self.questions, n)
        return Handout(questions)
