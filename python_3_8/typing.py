from typing import Dict
from typing_extensions import Literal, Final, final




# f = open(r'C:\file.txt', 'v')  # v- неправильно



def open_file(file, mode: Literal['r', 'w']):
    pass


open_file(r'C:\file.txt', 'v')

pi: Final = 3.14  # объявление констант


# запретить наследование классов
@final
class Dog:
    def __init__(self):
        self.paws = 4
        self.health = 100


class SuperDog(Dog):
    def __init__(self):
        super().__init__()
        self.health = 200


dog = SuperDog()
print(dog.health)


# ===
person: Dict[str, str] = {'name': 'john', 'last_name': 'conrad', 'sex': 'm'}

from typing import TypedDict

class WordStat(TypedDict):
    word: str
    count: int
    comment: str

dict_result: WordStat = {'word': 'hello'}