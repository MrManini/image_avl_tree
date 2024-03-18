import os
from typing import Any, List, Optional, Tuple
from pathlib import Path


class Queue:

    def __init__(self) -> None:
        self.queue: List[Any] = []

    def add(self, elem: Any) -> None:
        self.queue.append(elem)

    def remove(self) -> Any:
        return self.queue.pop(0)

    def is_empty(self) -> bool:
        return len(self.queue) == 0