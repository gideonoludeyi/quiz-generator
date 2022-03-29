import json
from typing import Sequence

from ..base_io import IOWriter
from ..core.question import Question


class JSONWriter(IOWriter):
    def write(self, questions: Sequence[Question]) -> None:
        data = [dict(prompt=question.prompt,
                     choices=question.choices,
                     answer_index=question.answer_index)
                for question in questions]

        with open(self.path, 'w') as f:
            json.dump(data, fp=f)

    def write_all(self, question_sets: Sequence[Sequence[Question]]) -> None:
        return self.write([question
                           for questions in question_sets
                           for question in questions])
