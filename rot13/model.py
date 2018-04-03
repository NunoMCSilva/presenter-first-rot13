"""ROT 13 model module"""

from pubsub import pub

from .interfaces import ApplicationModelInterface


class ApplicationModel(ApplicationModelInterface):

    def __init__(self) -> None:
        # TODO: kludgy, replace with simpler letter generation (check how)
        self._translation_table = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                                'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM')

    def rot13(self, text: str) -> str:
        return text.translate(self._translation_table)

    def run(self) -> None:
        pub.sendMessage('app start')
