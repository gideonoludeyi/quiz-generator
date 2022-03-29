import json

from ..core.handout import Handout
from ..io import IOWriter


class JSONWriter(IOWriter):
    def write(self, handout: Handout) -> None:
        data = [dict(prompt=question.prompt,
                     choices=question.choices,
                     answer_index=question.answer_index)
                for question in handout]

        with open(self.path, 'w') as f:
            json.dump(data, fp=f)
