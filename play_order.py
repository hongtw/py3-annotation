from typing import Sequence, Optional, TypeVar

import random

Choosable = TypeVar("Choosable", str, float)


def choose(items: Sequence[Choosable]) -> Choosable:
    return random.choice(items)

def player_order(
    names: Sequence[str], start: Optional[str] = None
) -> Sequence[str]:
    """Rotate player order so that start goes first"""
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]

def player_order2(
    names: Sequence[str], start: str=None
) -> Sequence[str]:
    """Rotate player order so that start goes first"""
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]

print(player_order(['apple','bird', 'dog'], 'bird'))