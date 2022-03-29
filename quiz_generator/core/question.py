from dataclasses import dataclass


@dataclass
class Question:
    prompt: str
    choices: tuple[str, ...]
    answer_index: int
    ''' index of the correct answer in `choices` '''
