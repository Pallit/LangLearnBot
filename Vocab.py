"""
Модель словаря
"""

from dataclasses import dataclass


@dataclass
class Vocab:
    word: str
    translation: str
    pk: int = 0

    def get_text(self):
        return self.word+" | "+self.translation
