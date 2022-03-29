from typing import Iterable, Sequence

from ..core.question import Question
from ..io import IOReader


class ASCIIReader(IOReader):
    def _slice_range_of_choices(self, lines: Iterable[str]) -> tuple[int, int]:
        start = 0
        for idx, line in enumerate(lines):
            if line.startswith('-'):
                start = idx
                break
        else:
            raise ValueError('lines do not contain any choices')

        end = start
        for idx, line in enumerate(lines):
            if line.startswith('-'):
                end = idx

        return (start, end)

    def _text_to_question(self, text: str) -> Question:
        lines = text.split('\n')
        start, end = self._slice_range_of_choices(lines)

        prompt = ' '.join(line.strip() for line in lines[:start])

        choices = tuple(line.removeprefix('-').strip()
                        for line in lines[start:end+1])

        answer = (' '.join(line.strip() for line in lines[end+1:])
                  .removeprefix('Answer:')
                  .strip())

        return Question(prompt, choices, answer_index=choices.index(answer))

    def read(self) -> Sequence[Question]:
        with open(self.path, 'r', encoding='utf-8') as f:
            sections = f.read().split('\n\n')
            questions = [self._text_to_question(text) for text in sections]
        return questions
