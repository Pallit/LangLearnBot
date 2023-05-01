"""
Модель информации о литературе
"""

from dataclasses import dataclass


@dataclass
class Literature:
    name: str
    autor: str
    link: str
    pk: int = 0

    def get_text(self):
        return "Название: " + '*'+self.name+'*' + ", Авторы: " + '_'+self.autor+'_', \
            self.link
