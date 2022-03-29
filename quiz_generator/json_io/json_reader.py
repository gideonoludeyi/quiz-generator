import json
from typing import Sequence

from ..core.question import Question
from ..base_io.reader import IOReader


class JSONReader(IOReader):
    def read(self) -> Sequence[Question]:
        with open(self.path, 'r') as f:
            data = json.load(f)

        questions = [
            Question(question['prompt'],
                     question['choices'],
                     question['answer_index'])
            for question in data
        ]

        return questions
