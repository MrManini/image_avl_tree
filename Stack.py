import os
from typing import Any, List, Optional, Tuple
from pathlib import Path
PATH = Path(__file__).parent / 'data'


class Stack:

    def __init__(self) -> None:
        self.stack: List[Any] = []

    def add(self, elem: Any) -> None:
        self.stack.append(elem)

    def remove(self) -> Any:
        return self.stack.pop()

    def is_empty(self) -> bool:
        return len(self.stack) == 0
