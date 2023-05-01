"""
Модуль Presenter описывает функциональность посредника
"""

import repository as rep
from Vocab import Vocab
from Literature import Literature


def get_words():
    repository = rep.vocab_factory()
    words = repository.get_all()
    return words


def add_word(word: str, translation: str):
    repository = rep.vocab_factory()
    return repository.add(Vocab(word=word, translation=translation))


def clear_words():
    repository = rep.vocab_factory()
    repository.delete_all()


def get_literatures():
    repository = rep.literature_factory()
    literatures = repository.get_all()
    return literatures


def add_literature(name: str, autor: str, link: str):
    repository = rep.literature_factory()
    return repository.add(Literature(name=name, autor=autor, link=link))


def clear_literatures():
    repository = rep.literature_factory()
    repository.delete_all()
