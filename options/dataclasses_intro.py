from dataclasses import dataclass

class Question:
    def __init__(self, text, is_true, explanation):
        self.explanation = explanation
        self.is_true = is_true
        self.text = text

@dataclass
class Question2:
    text: str = ""
    is_true: bool = False
    explanation: str = ""


q = Question2("test", True, "because")
q.text = 'hi'
print(q.text)


@dataclass(frozen=True)  # неизменяемый класс
class Question3:
    text: str = ""
    is_true: bool = False
    explanation: str = ""
        

