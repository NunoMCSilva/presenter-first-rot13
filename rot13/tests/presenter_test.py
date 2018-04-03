"""ROT13 presenter tests module"""

from pubsub import pub
import pytest

from ..presenter import *


@pytest.fixture
def presenter(mocker):
    model = mocker.Mock(spec_set=ApplicationModelInterface)
    view = mocker.Mock(spec_set=ApplicationViewInterface)

    return ApplicationPresenter(model, view)


def test__on_app_start__should_call_view_run(presenter):
    pub.sendMessage('app start')

    presenter.view.run.assert_called_once()


def test__on_plaintext_change__with_string__should_encrypt_string_and_update_view(presenter):
    # arrange
    plaintext, ciphertext = 'abcde 12', 'nopqr 12'
    presenter.model.rot13.return_value = ciphertext

    # act
    pub.sendMessage('plaintext change', text=plaintext)

    # assert
    presenter.model.rot13.assert_called_once_with(plaintext)
    presenter.view.update_ciphertext.assert_called_once_with(ciphertext)
