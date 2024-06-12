from typing import Iterable, Iterator, Sequence

from quiz_generator.core.question import Question
from quiz_generator.core.source import QuestionSource


class TextFileQuestionSource(QuestionSource):
    def __init__(self, lines: Iterator[str]) -> None:
        self.lines = lines

    def _slice_range_of_choices(self, lines: Iterable[str]) -> tuple[int, int]:
        start = 0
        for idx, line in enumerate(lines):
            if line.startswith('-'):
                start = idx
                break
        else:  # if the for loop does not break
            raise ValueError('lines do not contain any choices')

        end = start
        for idx, line in enumerate(lines):
            if line.startswith('-'):
                end = idx

        return (start, end)

    def _text_to_question(self, lines: list[str]) -> Question:
        start, end = self._slice_range_of_choices(lines)

        prompt = ' '.join(line.strip() for line in lines[:start])

        choices = tuple(line.removeprefix('-').strip()
                        for line in lines[start:end+1])

        answer = (' '.join(line.strip() for line in lines[end+1:])
                  .removeprefix('Answer:')
                  .strip())

        return Question(prompt, choices, answer_index=choices.index(answer))

    def _chunk(self, it: Iterator[str], sep: str) -> Iterator[list[str]]:
        bucket = []
        for value in it:
            if value != sep:
                bucket.append(value)
            else:
                yield bucket
                bucket = []
        yield bucket

    def get(self) -> Sequence[Question]:
        sections = self._chunk(self.lines, '')
        questions = [self._text_to_question(section) for section in sections]
        return questions
