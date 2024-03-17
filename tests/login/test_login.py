from contextlib import nullcontext as does_not_raise

import pytest

import framework.conf.constants as c
import framework.conf.logger

logger = framework.conf.logger.get_logger(__name__)


class TestLogin:
    @pytest.mark.parametrize(
        "num_test, email_str, password_str, result, expected",
        [
            (1, c.CORRECT_EMAIL, c.CORRECT_PASSWORD, True, does_not_raise()),
            (2, c.CORRECT_EMAIL, c.INCORRECT_PASSWORD, False, does_not_raise()),
            # (3, c.INCORRECT_EMAIL, c.CORRECT_EMAIL, False, does_not_raise()),
            # (4, c.INCORRECT_EMAIL, c.INCORRECT_PASSWORD, False, does_not_raise()),
            # (5, c.INVALID_EMAIL_FORMAT, c.INCORRECT_PASSWORD, False, does_not_raise()),
            # (6, c.EMPTY_EMAIL_STRING, c.CORRECT_PASSWORD, False, does_not_raise()),
            # (7, c.CORRECT_EMAIL, c.EMPTY_PASSWORD_STRING, False, does_not_raise()),
            # (8, c.EMPTY_EMAIL_STRING, c.EMPTY_PASSWORD_STRING, False, does_not_raise()),
        ])
    def test_login_page(self, login_page_fixture, num_test, email_str, password_str, result, expected):
        logger.info(f"\nSTART TEST USER LOGIN # {num_test}")
        login_page = login_page_fixture
        v_result = login_page.user_login_emulation(email_str, password_str)
        if v_result == result:
            logger.info(f"\nTest user login has been successfully completed.")
        else:
            logger.error(f"\nOps, something went wrong... :-(")
        assert v_result == result
