# Type Hints добавляет статическую типизацию
from random import random
from typing import Optional, Any, Union, List, Tuple, Dict, Iterable


class Character:

    def __init__(self, armor: int, power: int):
        self.armor = armor
        self.power = power
        self.health = 100

    def hit(self, damage: int):
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0


c1 = Character(12, 20)


amount: int
amount: None  # должна ругаться

price: Optional[int]
price = 10
price = None  # все нормально

attack: Any = 1
attack = 'hi'

# объединение типов
length: Union[int, float]
length = 1
length = "abcd"

quotes: list

quotes: List[int]  # Set, FrozenSet
quotes.append(1)

player: Tuple[str, int] = ("Kramnik", 2750)

changes_in_rating: Tuple[int, ...]
changes_in_rating = (1, 2, 3, 4, 5)

chess_players: Dict[str, int] = {"Kramnik": 2750}


def random_stream(min_val: int, max_val: int) -> Iterable[int]:
    while True:
        yield random.randint(min_val, max_val)