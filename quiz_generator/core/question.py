from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    prompt: str
    choices: tuple[str, ...]
    answer_index: int
    ''' index of the correct answer in `choices` '''
