from contextlib import nullcontext as does_not_raise

import pytest

import conf.constants as c


class TestLogin:
    @pytest.mark.parametrize(
        "email_str, password_str, result, expected",
        [
            (c.CORRECT_EMAIL, c.CORRECT_PASSWORD, True, does_not_raise()),
            (c.CORRECT_EMAIL, c.INCORRECT_PASSWORD, False, does_not_raise()),
            (c.INCORRECT_EMAIL, c.CORRECT_EMAIL, False, does_not_raise()),
            (c.INCORRECT_EMAIL, c.INCORRECT_PASSWORD, False, does_not_raise()),
            (c.INVALID_EMAIL_FORMAT, c.INCORRECT_PASSWORD, False, does_not_raise()),
            (c.EMPTY_EMAIL_STRING, c.CORRECT_PASSWORD, False, does_not_raise()),
            (c.CORRECT_EMAIL, c.EMPTY_PASSWORD_STRING, False, does_not_raise()),
            (c.EMPTY_EMAIL_STRING, c.EMPTY_PASSWORD_STRING, False, does_not_raise()),
        ])
    def test_login_page(self, login_page_fixture, email_str, password_str, result, expected):
        login_page = login_page_fixture
        assert login_page.user_login_emulation(email_str, password_str) == result
