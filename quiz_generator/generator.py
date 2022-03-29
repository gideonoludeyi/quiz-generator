from typing import Sequence

from .core.handout import Handout
from .core.pool import QuestionPool


class QuizGenerator:
    def __init__(self, pool: QuestionPool, question_count: int) -> None:
        self.pool = pool
        self.question_count = question_count

    def generate_handouts(self, size: int) -> Sequence[Handout]:
        count = self.question_count
        handouts = [self.pool.select(count) for _ in range(size)]
        return handouts
