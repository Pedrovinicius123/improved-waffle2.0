from dataclasses import dataclass
import os, pickle
from translator.conversor import find_value

@dataclass
class File:
    name: str
    size: str
    extension: str


