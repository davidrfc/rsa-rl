
from typing import NamedTuple

class Action(NamedTuple):
    path1: list
    path2: list
    path3: list
    slot_idx: int
    n_slot: int
    duration: float
