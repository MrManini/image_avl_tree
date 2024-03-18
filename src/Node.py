import os
from typing import Any, List, Optional, Tuple
from pathlib import Path
PATH = Path(__file__).parent / 'data'

class Node:

    def __init__(self, data: str) -> None:
        self.data = data
        self.type = self.get_type()
        self.size = self.get_size()
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None

    def get_type(self) -> str:
        data = self.data
        if data[:4] == "bike":
            return "bike"
        elif data[:3] == "car":
            return "cars"
        elif data[:3] == "cat":
            return "cats"
        elif data[:3] == "dog":
            return "dogs"
        elif data[0] == "0":
            return "flowers"
        elif data[0] == "h":
            return "horses"
        else:
            return "human"

    def get_size(self):
        file_name = PATH/self.type/self.data
        file_stats = os.stat(file_name)
        return file_stats.st_size