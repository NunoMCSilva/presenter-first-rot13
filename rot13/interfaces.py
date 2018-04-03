"""Rot13 interfaces module"""

from abc import ABCMeta, abstractmethod


class ApplicationModelInterface(metaclass=ABCMeta):

    @abstractmethod
    def rot13(self, text: str) -> str:
        raise NotImplementedError


# useful in case I want to add a new view (Kivy, etc.)
class ApplicationViewInterface(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_view() -> 'ApplicationViewInterface':
        raise NotImplementedError

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def update_ciphertext(self, text: str) -> None:
        raise NotImplementedError
