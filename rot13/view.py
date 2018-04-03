"""ROT13 View module"""

import tkinter as tk

from pubsub import pub

from .interfaces import ApplicationViewInterface


class ApplicationView(ApplicationViewInterface, tk.Frame):

    def __init__(self, master) -> None:
        self._master = master
        super().__init__(self._master)

        self._configure_gui()
        self._create_widgets()

    def _configure_gui(self) -> None:
        self._master.title('ROT 13')
        # TODO: start at center of screen

    def _create_widgets(self) -> None:
        self._plaintext = tk.Text()
        self._plaintext.bind('<Key>', self._send_plaintext_change_event)
        self._plaintext.pack(side=tk.LEFT)

        self._ciphertext = tk.Text(state=tk.DISABLED)
        self._ciphertext.pack(side=tk.RIGHT)

    # TODO: put this one public? to make clear communication between the V and P? see about rest of code
    def _send_plaintext_change_event(self, event) -> None:
        text = self._plaintext.get(1.0, tk.END)
        text = text[:-1] + event.char + text[-1]
        pub.sendMessage('plaintext change', text=text)

    # TODO: add to interface -- separate interface from presenter (or...)
    @staticmethod
    def get_view() -> 'ApplicationView':
        root = tk.Tk()
        return ApplicationView(root)

    def run(self) -> None:
        self.master.mainloop()

    def update_ciphertext(self, text: str) -> None:
        self._ciphertext.config(state=tk.NORMAL)
        self._ciphertext.delete(1.0, tk.END)
        self._ciphertext.insert(tk.END, text)
        self._ciphertext.config(state=tk.DISABLED)
