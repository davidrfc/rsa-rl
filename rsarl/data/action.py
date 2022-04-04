
from typing import NamedTuple

class Action(NamedTuple):
    path: list
    slot_idx: list
    n_slot: int
    duration: float
