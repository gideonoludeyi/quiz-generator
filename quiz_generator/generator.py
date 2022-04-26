from typing import Sequence

from .core.handout import Handout
from .core.pool import QuestionPool


class QuizGenerator:
    def __init__(self, pool: QuestionPool) -> None:
        self.pool = pool

    def generate_handouts(self, *, num_questions_per_handout: int, num_handouts: int) -> Sequence[Handout]:
        return [self.pool.select(num_questions_per_handout) for _ in range(num_handouts)]
