"""ROT13 model tests module"""

from hypothesis import given, strategies as st
import pytest

from ..model import *


@pytest.fixture
def model():
    return ApplicationModel()


@given(plaintext=st.from_regex(r'\A[^A-Za-z]*\Z'))   # strings without characters in the AZaz range (includes '' str)
def test_rot13__with_only_unaffected_characters_in_text__should_return_ciphertext_eq_to_plaintext(model, plaintext):
    assert model.rot13(plaintext) == plaintext


@given(plaintext=st.from_regex(r'\A[A-Za-z]+\Z'))   # strings with chars only in the AZaz range (doesn't include '')
def test_rot13__with_only_affected_characters_in_text__should_return_ciphertext_diff_from_plaintext(model, plaintext):
    assert model.rot13(plaintext) != plaintext


@given(plaintext=st.text())     # any string
def test_rot13__with_double_encrypt__should_return_equal_to_starting_plaintext(model, plaintext):
    assert model.rot13(model.rot13(plaintext)) == plaintext


@pytest.mark.parametrize('plaintext, ciphertext', [
    ('abcde', 'nopqr'),                         # lowercase
    ('AZ', 'NM'),                               # lowercase and wrap-around
    ('This is a Test', 'Guvf vf n Grfg'),       # lowercase, uppercase and space
])
def test_encrypt__string_as_param__should_return_ciphertext(model, plaintext, ciphertext):
    assert model.rot13(plaintext) == ciphertext


def test_run__should_send_app_start_event(mocker, model):
    # arrange
    send_msg_mocker = mocker.Mock(spec_set=pub.sendMessage)
    mocker.patch('pubsub.pub.sendMessage', send_msg_mocker)

    # act
    model.run()

    # assert
    send_msg_mocker.assert_called_with('app start')
