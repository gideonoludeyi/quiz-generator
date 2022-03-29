import abc
from pathlib import Path
from typing import Sequence

from ..core.handout import Handout


class IOWriter(abc.ABC):
    def __init__(self, path: Path | str) -> None:
        self.path = path

    @abc.abstractmethod
    def write(self, handout: Handout) -> None:
        pass

    def write_all(self, handouts: Sequence[Handout]) -> None:
        for handout in handouts:
            self.write(handout)
