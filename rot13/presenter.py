"""ROT13 presenter module"""

from pubsub import pub

from .interfaces import ApplicationModelInterface, ApplicationViewInterface


class ApplicationPresenter:

    def __init__(self, model: ApplicationModelInterface, view: ApplicationViewInterface) -> None:
        self.model = model
        self.view = view

        self._add_listeners()

    def _add_listeners(self) -> None:
        # TODO: put topicnames as Enum, Constants? like ON_APP_START, ON_PT_CHANGE = range(2) ?

        # from model
        pub.subscribe(self._on_app_start, 'app start')

        # from view
        pub.subscribe(self._on_plaintext_change, 'plaintext change')

    # listeners - TODO: check how to set listeners with typing hints
    def _on_app_start(self):
        self.view.run()

    def _on_plaintext_change(self, text):
        self.view.update_ciphertext(self.model.rot13(text))
