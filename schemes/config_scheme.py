from typing import TypedDict
from pathlib import Path

class ConfigScheme(TypedDict):
    name: str
    path: str | Path    