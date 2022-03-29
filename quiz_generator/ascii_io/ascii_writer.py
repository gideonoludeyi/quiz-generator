import os
from pathlib import Path

from ..core.handout import Handout
from ..core.question import Question
from ..base_io import IOWriter


class ASCIIWriter(IOWriter):
    def __init__(self, dir: Path | str) -> None:
        super().__init__(path=dir)
        self.next_id = 1

    def _question_to_text(self, question: Question) -> str:
        prompt = question.prompt
        question_choices = question.choices
        answer_index = question.answer_index

        choices = '\n'.join(f'- {choice}' for choice in question_choices)
        answer = f'Answer: {question_choices[answer_index]}'
        return f'{prompt}\n{choices}\n{answer}'

    def write(self, handout: Handout) -> None:
        directory = self.path
        if not os.path.isdir(directory):
            os.mkdir(directory)

        filepath = f'{directory}/handout{self.next_id}.txt'
        with open(filepath, 'w', encoding='utf-8') as f:
            for num, question in enumerate(handout, 1):
                text = self._question_to_text(question)
                print(f'{num}.', text, file=f, end='\n\n')

        self.next_id += 1
