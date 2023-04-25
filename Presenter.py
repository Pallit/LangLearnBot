"""
Модуль Presenter описывает функциональность посредника
"""

import repository as rep
from Vocab import Vocab


def get_words():
    repository = rep.vocab_factory()
    words = repository.get_all()
    return words


def add_word(word: str, translation: str):
    repository = rep.vocab_factory()
    return repository.add(Vocab(word=word, translation=translation))


def clear():
    repository = rep.vocab_factory()
    repository.delete_all()
