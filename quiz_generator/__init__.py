import os
from dataclasses import dataclass
from random import sample
from typing import Iterable


@dataclass
class Question:
    prompt: str
    choices: tuple[str]
    answer_index: int
    ''' index of the correct answer in the `choices` list '''

    def as_text(self) -> str:
        choices = '\n'.join(f'- {choice}' for choice in self.choices)
        answer = f'Answer: {self.choices[self.answer_index]}'
        return f'{self.prompt}\n{choices}\n{answer}'


class QuestionPool:
    def __init__(self, questions: Iterable[Question] = []) -> None:
        self.questions = questions

    def choose(self, n: int = 2) -> Iterable[Question]:
        return sample(self.questions, n)


class QuestionReader:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

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

    def read(self) -> Iterable[Question]:
        with open(self.filepath, 'r', encoding='utf-8') as f:
            sections = f.read().split('\n\n')
            questions = [self._text_to_question(text) for text in sections]
        return questions


class QuizWriter:
    def __init__(self, directory: str) -> None:
        self.dir = directory
        self.next_id = 1

    def write(self, handout: Iterable[Question]):
        if not os.path.isdir(self.dir):
            os.mkdir(self.dir)

        filepath = f'{self.dir}/handout{self.next_id}.txt'
        with open(filepath, 'w', encoding='utf-8') as f:
            for num, question in enumerate(handout, 1):
                print(f'{num}.', question.as_text(), file=f, end='\n\n')
        self.next_id += 1


if __name__ == '__main__':
    questions_filepath = input('Questions filepath: ')
    quiz_output_dir = input('Directory to generate handouts into: ')

    question_reader = QuestionReader(questions_filepath)
    quiz_writer = QuizWriter(quiz_output_dir)

    pool = QuestionPool(question_reader.read())

    handout_count = int(input('Handouts: '))
    question_size = int(input('Questions per handout: '))

    for _ in range(handout_count):
        quiz_writer.write(pool.choose(question_size))
