from typing import Iterator

import pytest

from app.text_file_source import TextFileQuestionSource
from quiz_generator.core.question import Question


@pytest.fixture
def lines() -> Iterator[str]:
    return iter([
        'My favorite superhero',
        '- Superman',
        '- Iron Man',
        '- Winter Soldier',
        'Answer: Superman',
        '',

        'My favorite programming language',
        '- Java',
        '- JavaScript',
        '- Python',
        'Answer: Python',
    ])


def test_should_transform_lines_of_str_to_questions(lines: Iterator[str]) -> None:
    source = TextFileQuestionSource(lines)
    assert source.get() == [
        Question(
            prompt='My favorite superhero',
            choices=('Superman', 'Iron Man', 'Winter Soldier'),
            answer_index=0
        ),
        Question(
            prompt='My favorite programming language',
            choices=('Java', 'JavaScript', 'Python'),
            answer_index=2
        ),
    ]
